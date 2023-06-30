import sys
import timeit
from collections import namedtuple

# ==================================================================================================================== #
# helper functions to get better data on memory consumption

SizeInfo = namedtuple("SizeInfo", ["basic_size", "sys_size", "true_size"])


def get_size_info(obj):
    def get_true_size(obj):
        # Note: This is still not really the full size.
        # For the actual memory footprint of a Python object, use pympler.asizeof(obj).
        # Pympler is a third party library
        result = sys.getsizeof(obj)
        if hasattr(obj, "__dict__"):
            for attribute in vars(obj).values():
                result += get_true_size(attribute)
        return result

    cls = type(obj)
    basic_size = cls.__basicsize__
    sys_size = sys.getsizeof(obj)
    true_size = get_true_size(obj)

    return SizeInfo(basic_size, sys_size, true_size)


def get_size_string(size_info):
    return f"basic size: {size_info.basic_size}; sys.getsizeof: {size_info.sys_size}; true size: {size_info.true_size}"


# ==================================================================================================================== #
# Exploring classic and slotted classes ...

# A helper class, providing means to automatically set up and print instances
class AutoInitAndStr:
    # remember: slots are inherited, but child classes have a __dict__ by default.
    # making this a slotted class only makes sure that the child classes don't inherit a __dict__ if they're slotted.
    __slots__ = tuple()

    def has_slots(self):
        cls = type(self)
        return "__slots__" in dir(cls)

    def has_dict(self):
        return "__dict__" in dir(self)

    def get_attributes(self):
        attributes = []

        if self.has_slots():
            attributes.extend(self.__slots__)
        if self.has_dict():
            attributes.extend(self.__dict__)
        return attributes

    def __init__(self):
        for i, attribute_name in enumerate(self.get_attributes()):
            # "self.attribute_name = i + 1"
            setattr(self, attribute_name, i + 1)

    def __str__(self):
        lines = []
        for attribute_name in self.get_attributes():
            # "value = self.attribute_name"
            value = getattr(self, attribute_name)
            lines.append(f"{attribute_name:20}: {value}")

        size_info = get_size_info(self)
        lines.append(get_size_string(size_info))
        return "\n".join(lines)


class NormalDict(AutoInitAndStr):
    def __init__(self):
        self.attrib_1 = 0
        self.attrib_2 = 1
        super()


class NormalSlots(AutoInitAndStr):
    __slots__ = ("attrib_1", "attrib_2")


class MutableSlots(AutoInitAndStr):
    __slots__ = ["initially_present"]


# -------------------------------------------------------------------------------------------------------------------- #
# Empty classes, as minimal examples
class NothingDict:
    pass


class NothingSlots:
    __slots__ = tuple()


# -------------------------------------------------------------------------------------------------------------------- #
# classes with 26 attributes in direct comparison

# tuple of strings "a", "b", "c", ...
attributes = tuple(chr(i) for i in range(ord("a"), ord("z") + 1))


class ManyAttributesSlots:
    __slots__ = attributes

    def __init__(self):
        for attribute in attributes:
            setattr(self, attribute, None)

    def __str__(self):
        size_info = get_size_info(self)
        return f"MinimalSlotClass instance with {get_size_string(size_info)}"


class ManyAttributesDict:
    def __init__(self):
        for attribute in attributes:
            setattr(self, attribute, None)

    def __str__(self):
        size_info = get_size_info(self)
        return f"MinimalDictClass instance with {get_size_string(size_info)}"


# ==================================================================================================================== #
def main():
    print("### INSTANCE OF CLASS WITHOUT SLOTS")
    non_slotted_instance = NormalDict()
    print(non_slotted_instance)
    print()

    print("adding attributes is possible. It affects total size, but not descriptor size")
    non_slotted_instance.foo = "bar"
    print(non_slotted_instance)
    print("dict entries:", vars(non_slotted_instance))
    print()

    print("### INSTANCE OF CLASS WITH SLOTS")
    instance_normal_slots = NormalSlots()
    print(instance_normal_slots)
    print()

    print("Access to existing attributes:", "ok" if instance_normal_slots.attrib_1 else None)
    print("Access to non-existing attributes: ", end="")
    try:
        print(instance_normal_slots.attrib1)
    except AttributeError:
        print("denied")
    print("Likewise, vars(...) would raise a TypeError on slotted class instances")
    print()

    print("### INSTANCE OF CLASS WITH *MUTABLE* SLOTS")
    instance_mutable_slots = MutableSlots()

    print("before altering the slots:")
    print(instance_mutable_slots)
    print()

    instance_mutable_slots.__slots__.append("new_attribute")

    print("after altering the slots:")
    try:
        print(instance_mutable_slots)
    except AttributeError:
        print("~~ now you're in trouble, bro")
    print()

    print("### OKAY, LET'S MAKE A SECOND INSTANCE OF THE CLASS")
    try:
        second_instance = MutableSlots()
        print(second_instance)
    except AttributeError as e:
        print("~~ Changing __slots__ does not create any fields")
        print("~~ Error message:", e)
    print()

    print("Reason: The Class itself does not contain a new member. The attributes of the class are:")
    for key, value in vars(MutableSlots).items():
        print(f"  {key:20}: {value}")
    print()

    print("Let's \"fix\" this:")
    MutableSlots.new_attribute = "new data"
    print("The new instance now looks like this:")
    print(instance_mutable_slots)
    print("okay, the first instance seems okay, but...")

    try:
        second_instance = MutableSlots()
    except AttributeError as e:
        print("~~~ ... we still can't instantiate a second variable, because the CTor attempts to change the value")
        print("~~~", e)
    print()

    print("### RESTORE ORIGINAL SLOTS")
    MutableSlots.__slots__ = ["initially_present"]
    second_instance = MutableSlots()
    print(second_instance)
    print("renaming one slot")
    second_instance.__slots__[0] = "renamed"
    try:
        print(second_instance.renamed)
    except AttributeError:
        print("~~~ the lookup still uses the original name, thus we get an error again")

    print("### SIZES OF EMPTY CLASSES")
    print("empty slots:", get_size_string(get_size_info(NothingSlots())))
    print("empty dict :", get_size_string(get_size_info(NothingDict())))
    print()

    print("### COMPARING CLASS INSTANCES WITH MANY ATTRIBUTES")
    print(ManyAttributesSlots())
    print("  Time to initialize:", timeit.timeit("ManyAttributesSlots()", globals=globals()))
    print("  Time for access   :", timeit.timeit("x = instance.x", "instance=ManyAttributesSlots()", globals=globals()))
    print(ManyAttributesDict())
    print("  Time to initialize:", timeit.timeit("ManyAttributesDict()", globals=globals()))
    print("  Time for access   :", timeit.timeit("x = instance.x", "instance=ManyAttributesDict()", globals=globals()))
    print()

    non_slotted_instance.__dict__["foo bar"] = "FOO BAR"
    print(dir(non_slotted_instance))



if __name__ == '__main__':
    main()

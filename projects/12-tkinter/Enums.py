import enum
import collections


class Modes(enum.IntEnum):
    restricted = enum.auto()
    default = enum.auto()
    admin = enum.auto()


class MessageClass(enum.Flag):
    info = enum.auto()
    warning = enum.auto()
    error = enum.auto()
    verbose = enum.auto()
    debug = enum.auto()


Message = collections.namedtuple("Message", ["text", "level"])
# a named tuple is what the name suggests: a special tuple where you can access the members not only by index but by an
# attribute name. Think of it as a C struct.
# First attribute to the CTor ("Message") is a string used when printing instances of the named tuple.
# Second attribute is an iterable of strings that defines the attribute names.
# You can then access them with instance.attribute.
# Note: like a tuple, these instances are immutable.
# Use types.SimpleNamespace if you need a mutable object, or consider using dataclass.


def filter_messages(msg, filter):
    if msg.level in filter:
        print(msg.text)


def main():
    print("Attributes of Enum Modes")
    for attribute in dir(Modes):
        print(f" {attribute:11} = {getattr(Modes, attribute)}")
    print()

    print("All items of Modes:")
    for item in Modes:
        print(f" {item}, with value {item.value} and name {item.name}")
    print()

    print("Using Flags to filter messags")
    defaultMessageFilter = MessageClass.info | MessageClass.warning | MessageClass.error
    message_1 = Message("foo", MessageClass.warning)
    message_2 = Message("bar", MessageClass.verbose)

    filter_messages(message_1, defaultMessageFilter)
    filter_messages(message_2, defaultMessageFilter)

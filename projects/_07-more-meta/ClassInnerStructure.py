class Aggregate:
    instance_counter = 0

    def __init__(self):
        Aggregate.instance_counter += 1
        self.content = "some data"


def main():
    instance = Aggregate()

    print("Inspecting instance directly after creation:")
    print("  via __dict__:", instance.__dict__)
    print("  via vars    :", vars(instance))
    print("  via dir     :", dir(instance))

    print("Inspecting the class itself:")
    print(" ", vars(Aggregate))

    look_for_attribute = "instance_counter"
    print("Looking for a specific member in the class attributes... ")
    if look_for_attribute in vars(Aggregate):
        print(f"  Found '{look_for_attribute}' with value", vars(Aggregate)[look_for_attribute])
    else:
        print(f"  Attribute '{look_for_attribute}' is not in the class attributes.")

    second = Aggregate()
    instance.specification = "more data"
    look_for_attribute = "specification"
    print(f"Looking for '{look_for_attribute}' in ...")
    print("  instance :", "found" if look_for_attribute in vars(instance) else "not found")
    print("  second   :", "found" if look_for_attribute in vars(second) else "not found")
    print("  Aggregate:", "found" if look_for_attribute in vars(Aggregate) else "not found")

    instance.__dict__["the_spice"] = "must flow"
    print("the_spice:", instance.the_spice)
    print("all variables in current scope:", vars())


if __name__ == "__main__":
    main()

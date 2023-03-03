from dataclasses import dataclass


@dataclass(order=True)
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0


def main():
    foo = InventoryItem("Foo", 2)
    bar = InventoryItem("Bar", 5)

    print(foo)
    print(foo < bar)


if __name__ == "__main__":
    main()

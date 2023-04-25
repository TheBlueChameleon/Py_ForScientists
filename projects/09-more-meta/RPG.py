import random


class Item:
    def __init__(self, name, category, boost):
        self.name = name
        self.category = category
        self.boost = boost

    def __str__(self):
        return f"{self.name} ({self.category}: {self.boost:+2})"


class Person:
    categories = ["strength", "charisma", "intelligence", "dexterity"]

    def __init__(self, name):
        self.name = name
        self.backpack = []

        # note: this is arguably an example of how NOT to do it...
        for category in Person.categories:
            self.__dict__[category] = random.randint(5, 10)

    def get_basevalue(self, category):
        return self.__dict__[category]

    def get_property(self, category):
        value = self.__dict__[category]
        for item in self.backpack:
            if item.category == category:
                value += item.boost
        return value

    def __str__(self):
        result = f"PERSON:\n"
        result += f" {'name':20}: {self.name}"
        for category in Person.categories:
            result += f"\n {category:20}: {self.get_property(category):2} (base value = {self.get_basevalue(category):2})"
        result += "\n items in backpack:"
        for item in self.backpack:
            result += "\n  * " + str(item)
        return result


def main():
    sword = Item("Berret", "charisma", 3)
    cursed = Item("Chard", "strength", -1)

    petra = Person("Petra")
    petra.backpack.append(sword)

    jacques = Person("Jacques")
    jacques.backpack.append(cursed)

    print(petra)
    print(jacques)

"""
Описать сказку про Колобка (не обязательно про колобка) классами.
Ссылка на текст сказки  - https://nukadeti.ru/skazki/kolobok
Нужно создать классы деда, бабки, колобка, лисы (по желанию можно добавить героев) с методами, которые будут имитировать
реплики героев в сказке. Описывать реплики можно не полностью, вызывать методы нужно в очередности сценария
"""


class Hero:

    def __init__(self, name):
        self.name = name
        self.is_alive = True
        print(self)

    def move(self):
        print(f"{self.name} is moving")

    def meet(self, person):
        print(f"{self.name} meets {person.name}")

    def die(self):
        self.is_alive = False
        print(f"{self.name} is dead now.")


class Kolobok(Hero):

    def __init__(self, name="Kolobok"):
        super().__init__(name)

    def move(self):
        print(f"{self.name} is rolling away")

    def meet(self, person):
        print(f"{self.name} meets {person.name}")
        self.charm(person)

    def charm(self, person):
        print(f"{self.name} is trying to charm {person.name}")
        if person.name == "Fox":
            print(f"Charming has been failed. {person.name} is eating {self.name}.")
            person.eat(self)
        else:
            print(f"{self.name} eluded {person.name}")
            self.move()


class Grandma(Hero):

    def __init__(self, name="Grandma"):
        super().__init__(name)
        self.flour_amount = 0

    def bake(self):
        if self.flour_amount == 2:
            kolobok = Kolobok()
            print(f"{kolobok.name} has been baked.")
            return kolobok
        else:
            print(f"{self.name} need more flour.") if self.flour_amount == 1 else print("Some flour is required.")
            raise ValueError

    def gather_flour(self):
        print(f"{self.name} is gathering flour.")
        self.flour_amount += 1


class Animal(Hero):

    def __init__(self, name):
        super().__init__(name)

    def eat(self, food: Hero):
        food.die()


def tale():
    grandma = Grandma()
    kolobok = None

    while kolobok is None:
        try:
            kolobok = grandma.bake()
        except ValueError:
            grandma.gather_flour()
        else:
            kolobok.move()

    animal_names = ["Hare", "Wolf", "Bear", "Fox", "Dinosaur"]
    for name in animal_names:
        animal = Animal(name)
        kolobok.meet(animal)
        if not kolobok.is_alive:
            break


if __name__ == "__main__":
    tale()

# Мусулезный Максим 02.08.2023
# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.


#Задание №6
# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

# Вариант № 1
class Animal:
    def __init__(self, type, age):
        self.__name, self.__age = type, age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Fish(Animal):

    def __init__(self, type, age, color):
        super().__init__(type, age)
        self.__name, self.__age = type, age
        self.__color = color

    def get_specific(self):
        return self.__color


class Mammal(Animal):

    def __init__(self, type, age, wool):
        super().__init__(type, age)
        self.__name, self.__age = type, age
        self.__wool = wool

    def get_specific(self):
        return self.__wool


class Bird(Animal):

    def __init__(self, type, age, feather):
        super().__init__(type, age)
        self.__name, self.__age = type, age
        self.__feather = feather

    def get_specific(self):
        return self.__feather

if __name__ == '__main__':
    bird = Bird("Ворон", 2, "черные")
    print(f'имя птицы: {bird.get_name()}, возраст {bird.get_age()}, оперенье {bird.get_specific()}')


# Вариант № 2

class Animal:
    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f"{self.name} {self.weight} {self.age}"


class Bird(Animal):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self._sound = sound

    def move(self):
        return "Fly"

    def say(self):
        return self._sound

    def __str__(self):
        return f"{super().__str__()} {self.bird_type}"


class Dog(Animal):
    def __init__(self, name: str, weight: int, age: int, dog_type: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type

    def move(self):
        return "Run"

    def say(self):
        return "Gov"

    def __str__(self):
        return f"{super().__str__()} {self.dog_type}"


class Fish(Animal):
    def __init__(self, name: str, weight: int, age: int, fish_type: str):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self):
        return "Swim"

    def say(self):
        return ""

    def __str__(self):
        return f"{super().__str__()} {self.fish_type}"


if __name__ == '__main__':
    dog = Dog("Чарлик ", 2, 6, "Кокер")
    bird = Bird("Яша ", 10, 22, "Попугай", "Чирик")
    fish = Fish("Сом ", 100, 7, "Речной")

    print(dog)
    print(bird)
    print(fish)

# 3 Вариант
class Cat:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        return "Mяу"


class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        return "Гав"


class AnimalFactory:
    def create_animal(self, animal_type, name, breed, age):
        if animal_type.lower() == "cat":
            return Cat(name, breed, age)
        elif animal_type.lower() == "dog":
            return Dog(name, breed, age)
        else:
            raise ValueError("Invalid animal type")


factory = AnimalFactory()

cat = factory.create_animal("cat", "Fluffy", "Persian", 8)
dog = factory.create_animal("dog", "Buddy", "Golden Retriever", 20)

print(cat.speak())  # Выводит: "Мяу"
print(dog.speak())  # Выводит: "Гав"
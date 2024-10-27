
class Animals:
    wool_color = 'White'
    min_age_animal = 1
    max_age_animal = 30

    def __init__(self, name='None_name', age=0):
        self.name = name
        if Animals.check_age(age) == 1:
            self.age = age
        else:
            print(f'Вашему животному {self.name} много лет, вероятно оно сдохло')
            self.age = 'RIP'

    @classmethod
    def check_age(cls, value: int) -> bool:
        return cls.min_age_animal <= value <= cls.max_age_animal

    def voice(self, value='ГРРРРР'):
        print(f'Животное которому {self.age} лет издало звук {value}!')


list_animals = list()

def reg_animal(name, age):
    global list_animals
    new_animal = Animals(name, age)
    list_animals.append(new_animal)
    return new_animal

dog = reg_animal('Бобик', 15)
cat = reg_animal('Барсик', 35)
# dog.voice('ГААААВ')
# print(list_animals)
print(list_animals[0].voice('Гав'))


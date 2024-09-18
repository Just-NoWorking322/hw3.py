class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu 
        self.__memory = memory 
    
    def __make_computations(self):
        sum_result = self.__cpu + self.__memory
        del_result = self.__cpu - self.__memory
        mul_result = self.__cpu * self.__memory
        div_result = self.__cpu / self.__memory 
        
        print(f'Сложение: {sum_result}')
        print(f'Вычитание: {del_result}')
        print(f'Умножение: {mul_result}')
        print(f'Деление: {div_result}')
    
    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def info(self):
        print(f'Компьютер с процесором: {self.__cpu}, память: {self.__memory}')
        self.__make_computations()

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card 

    def get_memory_card(self):
        return self.__memory_card

    def info(self):
        print(f'Ноутбук с процесором: {self.get_cpu()}, память: {self.get_memory()}, карта памяти: {self.__memory_card}')
   

comp = Computer(4, 8)
comp.info()

laptop = Laptop(4, 16, 256)
laptop.info()

print(f'CPU ноутбука: {laptop.get_cpu()}')
print(f'Память ноутбука: {laptop.get_memory()}')
print(f'Карта памяти ноутбука: {laptop.get_memory_card()}')


'''Домашняя работа №3

1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
2. Добавить в класс Computer приватный метод make_computations, в котором бы выполнялись арифметические вычисления(‘+’,  ‘-’,  ‘*’,  ‘/’ ) с атрибутами объекта cpu и memory результат вывести красиво с помощью ‘ f ’ .
3. Добавить геттеры к существующим атрибутам.
4. Создать класс Laptop - который наследуется от класса Computer с приватным полем memory_card(карта памяти)
5. Добавить геттеры к существующему атрибуту.
6. Распечатать информацию о созданных объектах с помощью метода info
7. Опробовать все возможные методы каждого объекта
'''
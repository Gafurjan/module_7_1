import string
from pprint import pprint
# создание класса Product
class Product:
    #начальные свойства создоваемый объектов данного класса
    def __init__(self, name: string, weight: float, category: string ):
        self.name = name
        self.weight = weight
        self.category = category
    # метод для получение атрибутов объекта класса
    def __str__(self):
       return f'{self.name}, {self.weight}, {self.category} '

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        str = file.read()
        file.close()
        return str

    def add(self, *products):
        str1 = self.get_products()
        if len(str1) == 0:
            file = open(self.__file_name, 'a')
            for i in products:
                file.write(i.__str__()+'\n')
            file.close()
        else:
            file = open(self.__file_name, 'r')
            str2 = file.readlines()
            list1 = []
            for i in str2:
                list1.append(i.split(',')[0])

            for i in products:
                if i.name in list1:
                    print(f'Продукт {i.name} уже есть в магазине')
                else:
                    file = open(self.__file_name, 'a')
                    for i in products:
                        file.write(i.__str__() + '\n')
                    file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


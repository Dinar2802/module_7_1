import os


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        if os.path.exists(self.__file_name):
            with open(self.__file_name, 'r') as file:
                products = file.read()
            return products
        else:
            return ""

    def add(self, *products):
        try:
            with open(self.__file_name, 'r') as file:
                current_products = {line.split(", ")[0] for line in file}
        except FileNotFoundError:
            current_products = set()

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in current_products:
                    file.write(f'{product}\n')
                    current_products.add(product.name)
                else:
                    print(f'Продукт {product.name} уже есть в магазине')


# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# 1. Створити клас-конструктор, який прийматиме кілька аргументів і формуватиме обʼєкт та виводитиме методом речення з цими аргументами;

class Car:
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price

    def present_car(self):
        print(f"This is {self.name} of model {self.model}")

    def car_price(self):
        print(f"The chosen {self.name} costs {self.price}")

choosing_car = Car("Tesla", "Model 3", "15000$")

choosing_car.present_car() # This is Tesla of model Model 3
choosing_car.car_price() # The chosen Tesla costs 15000$

# 2. Створити 2 класи, які прийматимуть інші класи; передати в них аргументи та викликати методи переданих класів для змінних, через які передавали аргументи

class Carshop(Car):
    def present_car(self):
        desired_price = self.price + 5000
        print(f"Today this {self.name} {self.model} costs around {desired_price}")

    def selling_car(self):
        if(self.price):
            if(self.price > 10000):
                print(f"The price is {self.price}")
            else:
                desired_price = self.price + 5000
                print(f"The price of {self.price} is too low for today's production requirements. The current price is {desired_price}")
        else:
            print(f"Apologiez, this {self.name} {self.model} is already being sold")

purchasing_car = Carshop("Merceddez", "Benz", 9000)

purchasing_car.present_car()
purchasing_car.selling_car()

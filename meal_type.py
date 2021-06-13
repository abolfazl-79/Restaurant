
from meal import Meal
from persian_typer import type_persian

class Cafe:
    def __init__(self) -> None:
        pass
    def get_all_cafes():
        return [Meal(type_persian('نوتلا'), 18000), 
                Meal(type_persian('سیب زمینی'), 19000), 
                Meal(type_persian('قهوه'), 12000), 
                Meal(type_persian('بستنی'), 11000),
                Meal(type_persian(' '), 0)]

    def get_cafe_property(meal):
        for cafe in Cafe.get_all_cafes():
            name, price = cafe.name, cafe.price
            if type_persian(name) == type_persian(meal):
                return[name, price]

class Food:
    def __init__(self) -> None:
        pass
    def get_all_food():
        return [Meal(type_persian('مرغ'), 40000), 
                Meal(type_persian('ماهی'), 65000), 
                Meal(type_persian('بختیاری'), 70000), 
                Meal(type_persian('جوجه'), 45000),
                Meal(type_persian('کباب'), 50000)]
    def get_food_property(meal):
        for food in Food.get_all_food():
            name, price = food.name, food.price
            if type_persian(name) == type_persian(meal):
                return[name, price] 


class Beverage:
    def __init__(self) -> None:
        pass
    def get_all_beverages():
        return [Meal(type_persian('موهیتو'), 8000), 
                Meal(type_persian('آب معدنی'), 2000), 
                Meal(type_persian('دلستر'), 6000), 
                Meal(type_persian('نوشابه'), 5000),
                Meal(type_persian(''), 0)]
    def get_beverage_property(meal):
        for beverage in Beverage.get_all_beverages():
            name, price = beverage.name, beverage.price
            if type_persian(name) == type_persian(meal):
                return[name, price]

def get_all_meals():
    return Cafe.get_all_cafes() + Food.get_all_food() + Beverage.get_all_beverages()

def is_empty(order):
    if order == '':
        return True
    return False




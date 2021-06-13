from meal_type import *
from persian_typer import type_persian


class Waiter:

    def show_menu():
        print(18*' ' + '*'*33 + ' ' + type_persian(' منو ') + ' ' + '*'*33, end=' ')
        print('\n',21*' '+ type_persian('کافی شاپ') + 20*' ' + type_persian('غذا') +20*' '+ type_persian('نوشیدنی') )
        print(22*' '+ 8*'-' + 17*' ' + 8*'-' +17*' '+ 8*'-' )
        for food, cafe, beverage in zip(Food.get_all_food(), Cafe.get_all_cafes() , Beverage.get_all_beverages()):
            print(((28 - len(cafe.name))* ' ' + cafe.name)+ ((25 - len(food.name))* ' ' + food.name)+((26 - len(beverage.name))* ' ' + beverage.name))
    
        print(17*' ' + '*'*68, end=' ')

    def welcoming(self):
        print('\n' + type_persian('*** به رستوران ما خوش آمدید ***').rjust(70) +  '\n')
    def asking_order(self):
        return input(type_persian('درخواست شما چیست ؟').rjust(100) + '\n')

    def calculate(orders):
        print('\n' + type_persian('** سفارشات **').rjust(100) + '\n')
        if len(orders) == 0:
            print(type_persian('سفارشی ثبت نشده است').rjust(100))
            return
        final_price = 0
        set_orders = set(orders)
        for order in set_orders:

            cafe_properties = Cafe.get_cafe_property(order)
            food_properties = Food.get_food_property(order)
            beverage_properties = Beverage.get_beverage_property(order)

            if cafe_properties != None:
                your_order_name = type_persian(cafe_properties[0])[::-1] 
                
                count = orders.count(your_order_name)
                your_order_price = count * cafe_properties[1]
                final_price = your_order_price + final_price
                your_order_name =  your_order_name + ' X{}'.format(count)
                print( your_order_name.rjust(100)  , str(your_order_price).rjust(100))
            
            elif food_properties != None:
                your_order_name = type_persian(Food.get_food_property(order)[0])[::-1]
                count = orders.count(your_order_name)
                your_order_price = count * food_properties[1]
                final_price = your_order_price + final_price
                your_order_name =  your_order_name + ' X{}'.format(count)
                print( your_order_name.rjust(100), str(your_order_price).rjust(100))
            else:
                your_order_name = type_persian(beverage_properties[0])[::-1]
                count = orders.count(your_order_name)
                your_order_price = count * beverage_properties[1]
                final_price = your_order_price + final_price
                your_order_name =  your_order_name + ' X{}'.format(count)
                print( your_order_name.rjust(100) , str(your_order_price).rjust(100))
        print('**************'.rjust(100))
        print('\n' + type_persian('جمع کل').rjust(100)+ str(final_price).rjust(100))   
    

    def command_list(self):
        print('\n')
        print(type_persian('1-منو').rjust(100))
        print(type_persian('2-سفارش').rjust(100))
        print(type_persian('3-صورت حساب').rjust(100))
        print(type_persian('4-خروج').rjust(100))
        print()
    
        

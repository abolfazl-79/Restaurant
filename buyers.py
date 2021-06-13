from servants import Waiter
from persian_typer import type_persian
from meal_type import *

class Customer:
    __is_leaving = False
    customer_orders = []
    def __init__(self) -> None:
        self.customer_orders = []


    # set_customer_orders()  
    
    def __is_done(order):
        if order == type_persian('تمام'):
            return True
        return False
    
    def get_menu(self):
        Waiter.show_menu()

    def ordering(self):
        print(type_persian('سفارش خود را بفرمایید') + '\n')
        while True:
            order = type_persian(input()) 
            if is_empty(order):continue

            elif Customer.__is_done(order):break

            else:Customer.get_order(order)
    
    def get_chek_list(self):
        Waiter.calculate(Customer.customer_orders)
    def exit(self):
        Customer.is_leaving = True
        return Customer.is_leaving

    def get_order(order):
        is_exist = False
        for meal in get_all_meals():          
            meal = type_persian(meal.name)[::-1]
            if meal == order:      
               Customer.customer_orders.append(order)
               is_exist = True
               break
        if is_exist == False:
            print(type_persian(' {} موجود نیست .'.format(order[::-1])))
    
    
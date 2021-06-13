from servants import Waiter
from meal_type import *
from buyers import Customer
from persian_typer import type_persian

leaving = False
waiter = Waiter()
waiter.welcoming()
new_customer = Customer()  
while not leaving:
     waiter.command_list()
     command = waiter.asking_order()
     if command == '1': new_customer.get_menu()
     if command == '2': new_customer.ordering()
     if command == '3': new_customer.get_chek_list()
     if command == '4': 
          print('\n' + type_persian('*** ممنون از انتخابتون ***').rjust(70))
          leaving = new_customer.exit()
     




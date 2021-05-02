print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
""")
print("""***********************************
** What would you like to order? **
***********************************
""")

def resturant():
    menu=["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]
    order = []
    orders= input(' ')
      
    while orders != 'quit':
        if orders in menu:
            order.append(orders)
            if len(order)==1: #to solve the s in order string  
                print(f'** {order.count(orders)} order of {orders} have been added to your meal **')
            elif len(order)>1:
                print(f'** {order.count(orders)} orders of {orders} have been added to your meal **')       
        else: # Stretch Goal
            print('please order one of the items on the menu!!')
        orders = input(' ')
        
if __name__ == '__main__':
    resturant()



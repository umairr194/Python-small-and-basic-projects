menu={
    'pizza':50,
    'pasta':60,
    'burger':70,
    'coffe':80,
    'drink':90,
}
print("----------------welcome to python resturant---------------")
print("pizza:RS 50\npasta:RS 60\nburger:RS 70\ncoffe:RS 80\ndrink:RS 90 ")
order_total= 0


item_1=input("select item that you will order:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your order {item_1} add successfully:")
else:
    print(f"order {item_1} you will add not found:")

#second item process
another_item= input("do yo order another item? (yes/no):")

if another_item.lower() == 'yes':
    item_2=input("enter your next item that you will add:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your order {item_2} add succesfully:")
    else:
        print(f"{item_2} not found:")

    print("total sum of all item is:",order_total)


       
     
     
   
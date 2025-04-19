menu ={
'Pizza':100,
'Pasta':80,
'Hot chocolate':70,
'Fries':50,
'Cold coffee':70
}
print("welcome to PYTHON cafe")
print("Pizza:100\nPasta:80\nHot chocolate:70\nFries:50\nCold coffee:70")
order_total =0
item_1=input("Enter the item you want to oder = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order ")
else:
    print(f"ordered item {item_1} is not available for the moment")

another_order = input("would you like to add something else to your order? (yes/no)")
if another_order == "yes":
   item_2 = input("Enter the item you want to add to your order = ")
   if item_2 in menu:
      order_total += menu[item_2]
      print(f"item {item_2} is added to your order")
   else:
      print(f"item {item_2} is not available in the menu")
      
      
print(f"the total amount of your order to pay rs{order_total}")

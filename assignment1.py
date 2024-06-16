#Step 1
class ItemToPurchase:
  def __init__(self, item_name='none', item_price= 0.00, item_quantity = 0 ):
    self.item_name = item_name
    self.item_price = item_price 
    self.item_quantity = item_quantity
  
  def print_item_cost(self):
    print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_quantity * self.item_price:.2f}\n".center(50))

#Step 2
item1_name = input("Enter the item name: ")
item1_price = float(input("Enter the item price: "))
item1_quantity = int(input("Enter the item quantity: ")) 
item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

item2_name = input("Enter the item name: ")
item2_price = float(input("Enter the item price: "))
item2_quantity = int(input("Enter the item quantity: ")) 
item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

#Step 3
print('\n')
print("TOTAL COST\n".center(50))
item1.print_item_cost()
item2.print_item_cost()
print(f"Total: $ {item1.item_quantity * item1.item_price + item2.item_quantity * item2.item_price:.2f}\n".center(50))
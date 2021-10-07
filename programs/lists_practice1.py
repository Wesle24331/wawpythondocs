#Wesley Welch
#Lists Practice 1

#A variable that holds more than one value is a list
groceries = ['bread', 'milk', 'eggs', 'cheese']
#You can get items from a list by their index
print(groceries[0])

#Start an empty list
cart = []

#For every item in my grocery list:
#Add that item to the cart
for item in groceries:
    cart.append(item)
print(cart)
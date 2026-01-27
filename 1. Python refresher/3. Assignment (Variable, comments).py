"""
- You have $50
- You buy an item that is $15
- with a tax of 3%
- print how much money you have left
"""

x = 50
item_cost = 15
tax = 0.03
taxedItem = item_cost + (item_cost * tax)
moneyLeft = x - taxedItem

print("Money left is ", moneyLeft)
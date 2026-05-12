"""
IS 303 - A03
Jeremy Eldredge
Expense Tracker

Description: Tracks expenses by category and produces a spending summary
Loop logic: Accumulate totals per category, find the biggest expense, filter expenses above a limit

Inputs:
- number of purchases (int)
- for each purchase: description (str), price (int), category (str)

Processes:
- collect purchases into a list of dictionaries
- accumulator: calculate total spending per category, average transaction price
- min/max: find biggest expense across all categories
- filter: build a list of expenses above average

Outputs:
- print each purchase with its description, price, and category
- print total per category, average transaction price, biggest expense, list of above average purchases

"""

num_purchases = int(input("How many purchases? "))
purchases = []

for i in range(num_purchases):
    description = input(f"Purchase {i + 1} description: ")
    category = input(f"Purchase {i + 1} category (dining, entertainment, car, other): ")
    price = int(input(f"Purchase {i + 1} price: "))
    purchases.append({"description": description, "category": category, "price": price})

# accumulator: total per category and average transaction price
total_dining = 0
total_ent = 0
total_car = 0
total_other = 0


for purchase in purchases:
    if purchase["category"].lower() == "dining":
        total_dining += purchase["price"]
    elif purchase["category"].lower() == "entertainment":
        total_ent += purchase["price"]
    elif purchase["category"].lower() == "car":
        total_car += purchase["price"]
    elif purchase["category"].lower() == "other":
        total_other += purchase["price"]

total_price = 0
for purchase in purchases:
    total_price += purchases["price"]


average_price = total_price / len(purchases)

# output

print("---")
print(f"Total purchases: {len(purchases)}")
print("---")
for purchase in purchases:
    print(f"{purchase['description']} ({purchase['category']}): ${purchase['price']}:.2f")

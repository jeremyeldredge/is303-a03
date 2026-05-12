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
# collect purchases
num_purchases = int(input("How many purchases? "))
if num_purchases <= 0:
    print("Error: must enter at least 1 purchase.")
    exit()

purchases = []
valid_categories = ["dining", "school", "car", "other"]

for i in range(num_purchases):
    description = input(f"Purchase {i + 1} description: ")

    category = input(f"Purchase {i + 1} category (dining, school, car, other): ").lower()
    if category not in valid_categories:
        print(f"Error: '{category}' is not a valid category.")
        exit()

    price = float(input(f"Purchase {i + 1} price: "))
    if price < 0:
        print("Error: price cannot be negative.")
        exit()

    purchases.append({"description": description, "category": category, "price": price})


# accumulator: total per category and average transaction price
total_dining = 0
total_school = 0
total_car = 0
total_other = 0


for purchase in purchases:
    if purchase["category"].lower() == "dining":
        total_dining += purchase['price']
    elif purchase["category"].lower() == "school":
        total_school += purchase['price']
    elif purchase["category"].lower() == "car":
        total_car += purchase['price']
    elif purchase["category"].lower() == "other":
        total_other += purchase['price']

total_price = 0
for purchase in purchases:
    total_price += purchase['price']

average_price = total_price / len(purchases)

# min/max: find largest purchase
big_purchase = purchases[0]
for purchase in purchases:
    if purchase['price'] > big_purchase['price']:
        big_purchase = purchase

# filter: purchases above average purchase price
high_prices = []
for purchase in purchases:
    if purchase['price'] > average_price:
        high_prices.append(purchase['description'])

# output message

print("---")
print("Spending Report")
print("---")
print(f"Total purchases: {len(purchases)}")
print("---")
for purchase in purchases:
    print(f"{purchase['description'].title()} ({purchase['category'].title()}): ${purchase['price']:.2f}")

print("---")
print("Total spent per category:")
print(f"Dining: ${total_dining:.2f}")
print(f"School: ${total_school:.2f}")
print(f"Car: ${total_car:.2f}")
print(f"Other: ${total_other:.2f}")

print("---")
print(f"Average purchase price: ${average_price:.2f}")

print("---")
print(f"Largest purchase: {big_purchase['description'].title()} ({big_purchase['category'].title()}): ${big_purchase['price']:.2f}")
print("---")

print(f"Purchases above average price: {', '.join(high_prices)}")
print("---")


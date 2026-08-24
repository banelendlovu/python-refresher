# PART 1: DEFINE & CALL A FUNCTION

def display_order(order_id, customer, product):
    print(f'Order {order_id} belongs to {customer} and contains a {product}')

display_order('0RD-1001', 'Sarah', 'Laptop')
display_order('ORD-1107', 'John', 'Monitor')

# PART 2: FUNCTION ARGUMENTS

def calculate_order_total(price, quantity):
    order_total = price * quantity
    return order_total

order_total_1 = calculate_order_total(49.99, 3)
print(order_total_1)

order_total_2 = calculate_order_total(65.50, 4)
print(order_total_2)

# PART 3: RETURNING MULTIPLE RESULTS

sales = [125, 200, 75, 350, 90, 500, 180]

def analyze_sales(sales):
    total = 0

    for sale in sales:
        total = total+sale

    average = total / len(sales)

    return total, average

sales = [125, 200, 75, 350, 90, 500, 180]

total_sales, average_sales = analyze_sales(sales)

print("Total sales: ",total_sales)
print("Average sales: ", average_sales)

# PART 4: ASSIGN A FUNCTION TO A VARIABLE

def calculate_discount(total, discount_rate):
    return total - (total * discount_rate)

discount_function = calculate_discount
print(discount_function(100, 0.10))

# PART 5: LAMBDA FUNCTIONS

calculate_tax = lambda x: x + (x * 0.08) 

print(calculate_tax(45.90))
print(calculate_tax(30.99))
print(calculate_tax(16.00))

order_status = lambda num: 'Delayed' if num > 5 else 'On Time'
print(order_status(10))
print(order_status(2))

# PART 6: LIST COMPREHENSION WITH A FUNCTION

prices = [15, 25, 40, 60, 85, 120]

def add_tax(price):
    return price + (price * 0.08)


prices_with_tax = [add_tax(price) for price in prices]
print(prices_with_tax)


# PART 7: MAP()

customers = ["sarah", "david", "james", "lisa"]

upper = map(lambda x: x.upper(), customers)
print(list(upper))

# PART 8: FILTER()

order_amounts = [25, 150, 75, 300, 45, 500, 120]

check = filter(lambda x: x >= 100, order_amounts)
print(list(check))

comp_amounts = [x for x in order_amounts if x >= 100]
print(comp_amounts)


















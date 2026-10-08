# COMPREHENSIVE PRACTICE
# Variables → Data Types → Strings → Lists → Tuples → Sets → Dictionaries → Functions → Loops


orders = [
    {
        "order_id": "ORD-1001",
        "customer": " Sarah ",
        "product": "Laptop",
        "category": "Electronics",
        "quantity": 2,
        "price": 899.99,
        "status": "shipped"
    },
    {
        "order_id": "ORD-1002",
        "customer": "James",
        "product": "Keyboard",
        "category": "Accessories",
        "quantity": 1,
        "price": 75.50,
        "status": "processing"
    },
    {
        "order_id": "ORD-1003",
        "customer": " Lisa ",
        "product": "Monitor",
        "category": "Electronics",
        "quantity": 2,
        "price": 249.99,
        "status": "delayed"
    },
    {
        "order_id": "ORD-1004",
        "customer": "David",
        "product": "Mouse",
        "category": "Accessories",
        "quantity": 3,
        "price": 35.00,
        "status": "shipped"
    }
]

# PART 1 - Inspect Data
# Orders table in a list. List items are stored as dictionaries

num_orders = len(orders)
print(f'Total orders: {num_orders}')

print(type(orders))

print(isinstance(orders, list))
print(isinstance(orders[0], dict))
print(isinstance(orders[0]['quantity'], int))
print(isinstance(orders[0]['price'], float))

# PART 2 - Work With Strings

for order in orders:
    name = order['customer'].strip().upper()
    print(name)

products = [order['product'] for order in orders]
print('Laptop' in products)

for order in orders:
    print(f'Order {order['order_id']}: {order['customer']} purchased {order['quantity']} {order['product']}(s)')
    


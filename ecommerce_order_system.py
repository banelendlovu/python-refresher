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

# PART 3 - Lists

product_list = []

for order in orders:
    item = order["product"]
    product_list.append(item)
print(product_list)

product_list.append("Webcam")
print(product_list)

product_list.remove("Webcam")
print(product_list)

sec_list = ["Speakers", "Headphones"]
updated_list = [item for item in product_list + sec_list]
print(updated_list)

# PART 4 - List Comprehension Challenge

# total = price x quanitity

order_totals = [order["price"] * order["quantity"] for order in orders]
print(order_totals)

totals_greater_than_500 = [total for total in order_totals if total > 500]
print(totals_greater_than_500)

# PART 5 - Tuples

o_id = orders[0]["order_id"]
o_cust = orders[0]["customer"]
o_prod = orders[0]["product"]
o_quant = orders[0]["quantity"]

first_tuple = (o_id, o_cust, o_prod, o_quant)

first = first_tuple[0]
print(first)

last = first_tuple[-1]
print(last)

cust_prod = first_tuple[1:3]
print(cust_prod)

o_id, o_cust, o_prod, o_quant = first_tuple

sec_tuple = ("Warehouse A", "Electronics", "Section 4")
third_tuple = ("Section 7", "Loading Dock")

final_tuple = sec_tuple + third_tuple
print(final_tuple)

# PART 6 - Sets & Data Quality

system_a = {"ORD-1001", "ORD-1002", "ORD-1003", "ORD-1005"}
system_b = {"ORD-1002", "ORD-1003", "ORD-1004", "ORD-1006"}

sys_ab = system_a.union(system_b)
print(sys_ab)

i = system_a.intersection(system_b)
print(i)

only_a = system_a.difference(system_b)
print(only_a)

only_b = system_b.difference(system_a)
print(only_b)

customer_ids = [101, 102, 102, 103, 104, 104, 105]
customer_ids = set(customer_ids)
print(customer_ids)

# PART 7 - Dictionaries

total_orders = len(orders)

total_products = 0
for order in orders:
    value = order["quantity"]
    total_products = value + total_products
print(total_products)

customers = []
for order in orders:
    name = order["customer"]
    customers.append(name)
print(customers)

unique_customers = set(customers)
print(unique_customers)

store_summary = {
    "total_orders": len(orders),
    "total_products": total_products,
    "unique_customers": len(unique_customers)
}
print(store_summary)

store_summary['store_status'] = "Active"
store_summary['store_status'] = "Processing Orders"

for item in store_summary:
    print(f'total_orders: {len(orders)}\n\ntotal_products: {total_products}' )

# PART 8 - Functions

def calculate_order_total(price, quantity):
    return price * quantity

calculate_order_total(899.99, 2)

def clean(customer):
    return customer.strip().upper()

clean(' Sarah')

status = lambda order: "Needs Attention" if order == "delayed" else "On Track"
print(status)


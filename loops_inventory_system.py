# PART 1: FOR LOOPS

products = ['Laptop', 'Keyboard', 'Monitor', 'Mouse', 'Webcam']

for product in products:
    print(product)

for p in products:
    print(f'Processing product: {p}')

print(f'Total products: {len(products)}')

# PART 2: RANGE()

for i in range(1, 11):
    print(i)

for e in range(2, 21):
    if e % 2 == 0:
        print(e)

for r in range(10, 1, -2):
    print(r)

# PART 3: ENUMERATE()

products = ['Laptop', 'Keyboard', 'Monitor', 'Mouse', 'Webcam']

for i, j in enumerate(products):
    print(f'{i}: {j}')


for n, prod in enumerate(products):
    n = 100 + n
    print(f'{n}: {prod}')

# PART 4: WHILE LOOPS

order_number = 1

while order_number <= 5:
    print(f'Processing order {order_number}')
    order_number += 1
    

# PART 5: CONTINUE

order_ids = ['ORD-101', 'ORD-102', 'TEST-103', 'ORD-104', 'TEST-105', 'ORD-106']

for order in order_ids:
    if order.startswith('TEST'):
        continue
    print(f'Processing {order}')
    

# PART 6: BREAK

inventory = ['Laptop', 'Keyboard', 'Monitor', 'Mouse', 'Webcam']

for item in inventory:
    if item == 'Monitor':
        print(f'Found: {item}')
        break 
    print(item)

# PART 7: PASS

products_to_review = ['Laptop', 'Keyboard', 'Monitor']

for prod in products_to_review:
    if prod == 'Keyboard':
        pass
    print(f'Reviewing: {prod}')


# PART 8: LOOP ELSE

inventory = ['Laptop', 'Keyboard', 'Monitor', 'Mouse', 'Webcam']

search_product = 'Printer'

for p in inventory:
    if p == search_product:
        print('Product found!')
        break
else:
    print('Product not found.')


# PART 9: NESTED LOOPS

warehouses = {
    "Atlanta": ["Laptop", "Monitor"],
    "Toronto": ["Keyboard", "Mouse"],
    "Vancouver": ["Webcam", "Speakers"]
}

for location, products in warehouses.items():
    print(location)

    for item in products:
        print(f'- {item}')

    



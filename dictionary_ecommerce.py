# PART 1: CREATE & ACCESS A DICTIONARY 

order = {'order_id': 'ORD-1048',
         'customer': 'Sarah',
         'product': 'Wireless Headphones',
         'quantity': 2,
         'price': 89.99,
         'status': 'processing'}
print(order)
print(order['order_id'])
print(order['customer'])
print(order['product'])
print(order['quantity'])
print(order['status'])
print(order['time'])
# KeyError: 'time' --- error because key 'time' does not exist in the dictonary, thus no value can be returned 

# PART 2: ADD & UPDATE ITEMS

order['shipping_method'] = 'Express'
order['discount'] = 10
order['quantity'] = 3
order['status'] = 'shipped'
order['price'] = 134.98
print(order)
print(order['quantity'])
print(order['price'])
print(order['status'])

# PART 3: REMOVE ITEMS

del order['discount']

removed_shipping = order.pop('shipping_method')
print(removed_shipping)

order['gift_message'] = 'Happy Birthday!'
order['internal_note'] = 'Call customer before delivery'

print(order.popitem())
print(order)

temporary_order = {'name': 'Lisa',
                   'color': 'Red',
                   'batch': 'T4',
                   'cost': 25}
print(temporary_order)

# PART 4: ITERATE THROUGH KEYS

for key in order.keys():
    print(key)

for key in order:
    print(f'Field: {key}')

# PART 5: ITERATE THROUGH VALUES

for value in order.values():
    print(value)

for value in order.values():
    print(f'Order information: {value}')

# PART 6: ITERATE THROUGH KEY-VALUE PAIRS

for k, v in order.items():
    print(f'{k}: {v}')

# PART 7: DATA QUALITY CHECK

order_check = {
"order_id": "ORD-2050",
"customer": "David",
"product": "Laptop Stand",
"quantity": 1,
"status": "Pending"
}

order_check['price'] = 5.99

for k, v in order_check.items():
    print(k, v)

order_check['status'] = 'Processing'
order_check['payment_method'] = 'Credit Card'
print(order_check)
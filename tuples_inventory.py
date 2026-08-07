# PART 1: CREATING TUPLES

products = ('Laptop', 'Keyboard', 'Monitor', 'Mouse', 'Webcam')
print(products)
print(type(products))

prices = (1200, 75, 350, 40, 95)
print(prices)
print(type(prices))

featured_product = ('Product Name', 'Category', 'Price', 'Customer rating')
print(featured_product)
print(type(featured_product))

# PART 2: ACCESS TUPLE ELEMENTS

first_product = products[0]
print(first_product)

last_product = products[-1]
print(last_product)

third_product = products[2]
print(third_product)

total_products = len(products)
print(total_products)

is_monitor_present = ('Monitor' in products)
print(is_monitor_present)

is_printer_present = ('Printer' in products)
print(is_printer_present)

# PART 3: SLICE A TUPLE

first_3_prod = products[:3]
print(first_3_prod)

last_2_prod = products[-2:]
print(last_2_prod)

except_first = products[1:]
print(except_first)

except_last = products[:-1]
print(except_last)

complete_tuple = products[:]
print(complete_tuple)

# PART 4: UNPACK A PRODUCT

prod_name, category, price, cust_rating = featured_product
print(prod_name)
print(category)
print(price)
print(cust_rating)

# PART 5: UNPACK USING AN ASTERISK

warehouse_sections = ('Receieving', 'Storage', 'Packing', 'Quality Check', 'Shipping', 'Returns')

first_section, * middle_sections, last_section = warehouse_sections
print(first_section)
print(middle_sections)
print(last_section)

# PART 6: CONCATENATE TUPLES

warehouse_a = ('Laptop', 'Monitor', 'Mouse')
warehouse_b = ('Keyboard', 'Webcam', 'Speakers')

inventory = warehouse_a + warehouse_b
print(inventory)
print(len(inventory))

# PART 7: DELETE A TUPLE

archived_orders = ('001', '002', '003', '004')
print(archived_orders)

del archived_orders
print(archived_orders)

# NameError - del removes the variable, so archived_orders no longer exists
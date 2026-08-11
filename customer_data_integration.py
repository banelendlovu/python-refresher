# PART 1: CREATE & INSPECT SETS

system_a_customers = {101, 102, 103, 104, 105}
print(system_a_customers)
print(type(system_a_customers))
num_a_customers = len(system_a_customers)
print(f'Number of customers: {num_a_customers}')

system_b_customers = {103, 104, 105, 106, 107}
print(system_b_customers)
print(type(system_b_customers))
num_b_customers = len(system_b_customers)
print(f'Number of customers: {num_b_customers}')

system_a_customers.add(108)
print(system_a_customers)

# PART 2: TYPE CASTING

customer_list = [101, 102, 102, 103, 104, 104, 105, 105]

new_cust = set(customer_list)
print(new_cust)

length_cust_list = len(customer_list)
print(length_cust_list)

length_new_list = len(new_cust)
print(length_new_list)

# lengths are different because new_cust is a set and sets have unique elements. Duplicate elements are automatically removed 

back_list = list(new_cust)
print(back_list)

# PART 3: HETEROGENEOUS SETS

mixed_data = {3, 9.6, 'orders', True, (8, 4)}
print(mixed_data)
print(type(mixed_data))
mixed_data.add('delivery')
mixed_data.add(['package', 'amount'])

# TypeError: unhashable type: 'list'
# Does not allow a list because a list is unhashable -- lists are mutable, thus cannot be hashed 

# PART 4: UNION - COMBINE DATA

system_a_customers = {101, 102, 103, 104, 105}
system_b_customers = {103, 104, 105, 106, 107}

all_customers = system_a_customers.union(system_b_customers)
print(all_customers)
print(f'Unique Customers: {len(all_customers)}')
all_customers.add(109)
print(all_customers)

# PART 5: INTERSECTION - FIND OVERLAPPING DATA

duplicate_customers = system_a_customers.intersection(system_b_customers)
print(duplicate_customers)
print(f'Number of duplicate customers: {len(duplicate_customers)}')

# Intersection identifies the values that two sets have in common.

# PART 6: DIFFERENCE - FIND UNIQUE DATA

system_a_only = system_a_customers.difference(system_b_customers)
print(system_a_only)

system_b_only = system_b_customers.difference(system_a_customers)
print(system_b_only)

# system a only represents elements found only in set a and not in set b
# system b only represents elements found only in set b and not in set a

# PART 7: FROZEN SET 

required_fields = frozenset({'customer_id', 'email', 'first_name', 'last_name'})
print(required_fields)
print(type(required_fields))
required_fields.add('phone_number')

# Attribute Error due the fact that .add() doesn't exist as a method for these onjects that are in a frozen set.
# Frozen set cannot be modified after its creation

# PART 8: CLEARING DATA

temporary_customers = {201, 202, 203, 204}
print(temporary_customers)
temporary_customers.clear()
print(temporary_customers)
print(len(temporary_customers))

# clear () removes all the elements in a set, whereas del removes the variable itself/ object reference








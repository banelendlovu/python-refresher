# VARIABLES & DATA TYPES

# Exercise 3: Data Type Detective

square_sides = 4
print(square_sides)
print(type(square_sides))
print('Is this an integer?', isinstance(square_sides, int))


length = 12.3
print(length)
print(type(length))
print('Is this a float?', isinstance(length, float))


name_of_shape = 'square'
print(name_of_shape)
print(type(name_of_shape))
print('Is this a string?', isinstance(name_of_shape, str))


is_shape = True
print(is_shape)
print(type(is_shape))
print('Is this a bool?', isinstance(is_shape, bool))


two_d = ['circle', 'square', 'triangle']
print(two_d)
print(type(two_d))
print('Is this a list?', isinstance(two_d, list))


objects = ('1D', '2D', '3D')
print(objects)
print(type(objects))
print('Is this a tuple?', isinstance(objects, tuple))


colors = {'red', 'blue', 'green'}
print(colors)
print(type(colors))
print('Is this a set?', isinstance(colors, set))


data = {'name': 'rectangle',
       'color': 'green',
       'sides': 4}
print(data)
print(type(data))
print('Is this a dictonary?', isinstance(data, dict))


values = range(5)
print(values)
print(type(values))
print('Is this a range?', isinstance(values, range))


line_sides = None
print(line_sides)
print(type(line_sides))
print('Is this a None value?', isinstance(line_sides, type(None)))

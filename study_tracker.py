# VARIABLES & DATA TYPES

# Exercise 2: Build a simple study tracker

name = 'Jane'
study_hrs = 2
num_days = 7
completed_hrs = 2
today_complete = True


total_planned_hrs = study_hrs * num_days


print('Weekly Study Summary')


print('Planned hours: ', total_planned_hrs)
print('Completed hours: ', completed_hrs)
print("Completed today's session: ", today_complete)


print(type(total_planned_hrs))
print(type(completed_hrs))
print(type(today_complete))


print('Is total planned time an integer?', isinstance(total_planned_hrs, int))
print('Is the completion value a Boolean?', isinstance(today_complete, bool))
print('Is my name a string?', isinstance(name, str))

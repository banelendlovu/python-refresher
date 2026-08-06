# PART 1: CREATE LISTS

programming_languages = ['Python', 'SQL', 'R', 'Java']
print(programming_languages)
print(type(programming_languages))

study_days = list(('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'))
print(study_days)
print(type(study_days))

weekly_scores = [0] * 5
print(weekly_scores)
print(type(weekly_scores))

# PART 2: ACCESS & UPDATE LIST ELEMENTS

first_pro = programming_languages[0]
print(first_pro)

last_pro = programming_languages[-1]
print(last_pro)

sec_third_item = programming_languages[1:3]
print(sec_third_item)

programming_languages[3] = 'Javascript'
print(programming_languages)

len_prog = len(programming_languages)
print(len_prog)

# PART 3: ADD ELEMENTS TO A LIST

programming_languages.append('Tableau')

programming_languages.insert(1, 'Excel')

data_tools = ['PowerBI', 'Git', 'Docker']

programming_languages.extend(data_tools)
print(programming_languages)
print(f'Total number of items: {len(programming_languages)}')

# PART 4: REMOVE ELEMENTS

tasks = ['study Python', 'practice SQL', 'apply for jobs', 'update resume', 'exercise']

tasks.remove('update resume')

completed_task = tasks.pop()
print(completed_task)

del tasks[0]
print(tasks)

backup_tasks = list(tasks)
print(backup_tasks)

# PART 5: ITERATE THROUGH A LIST

skills = ['Python', 'SQL', 'Git', 'Excel', 'PowerBI']

for item in skills:
    print(item)

    for item in skills:
        print(f'I am learning {item}')

# Use a for loop and range() to print the index and the corresponding skill. 
#   Example:
#   Index 0: Python

for i in range(len(skills)):
    skill = skills[i]
    print(f'Index {i}: {skill}')

# PART 6: NESTED LISTS

weekly_study_plan = [['Monday', 'Python', 2], ['Tuesday', 'SQL', 2], ['Wednesday', 'Python', 2], ['Thursday', 'SQL', 2]]
print(weekly_study_plan)

first_list = weekly_study_plan[0]
print(first_list)

sql_from_tues = weekly_study_plan[1][1]
print(sql_from_tues)

# Update Wednesday's study hours from 2 to 3.

weekly_study_plan[2][2] = 3
print(weekly_study_plan)


for item in weekly_study_plan:
    for i in range(len(item)):
        print(item[i])

# PART 7: LIST COMPREHENSIONS

digits = [num for num in range(10)]
print(digits)

squares = [num ** 2 for num in range(10)]
print(squares)

even = [num for num in range(21) if num % 2 == 0]
print(even)

odd = [num for num in range(21) if num % 2 != 0]
print(odd)

numbers = [4, 7, 10, 13, 16, 19]
new_list = [num for num in numbers if num > 10]
print(new_list)

scores = [8, 12, 6, 15, 10]
final = ['Pass' if grade >= 10 else 'Needs Improvement' for grade in scores]
print(final)
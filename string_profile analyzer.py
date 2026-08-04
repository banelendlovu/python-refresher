# PART 1: CREATE & CLEAN A STRING

original = ' Jane is learning Python and preparing for a Data Engineering career. '
print(original)

clean_profile = original.strip()
print(clean_profile)

len_clean_profile = len(clean_profile)
print(len_clean_profile)

# PART 2: ACCESS & SLICE THE STRING

first = clean_profile[0]
print(first)

last = clean_profile[-1]
print(last)

fsix_char = clean_profile[:6]
print(fsix_char)

name = clean_profile[:4]
print(name)

last_10 = clean_profile[-10:]
print(last_10)

# PART 3: CHANGE THE TEXT

print(clean_profile.upper())

print(clean_profile.lower())

sql_profile = clean_profile.replace('Python', 'SQL')
print(sql_profile)

# PART 4: TEST STRING MEMBERSHIP

test1 = 'Python' in clean_profile
print(f'Is Python in the profile? {test1}')

test2 = 'Data' in clean_profile
print(f'Is Data in the profile? {test2}')

test3 = 'Java' in clean_profile
print(f'Is Java in the profile? {test3}')

test4 = 'Engineering' in clean_profile
print(f'Is Engineering in the profile? {test4}')

# PART 5: LOOP THROUGH A STRING

word = 'Python'

for char in word:
    print(char)


for letter in word:
    print(letter.upper())

# PART 6: FORMAT A STUDY MESSAGE

name ='Jane'
language = 'Python'
career = 'Data Engineer'
study_hours = 2

# Jane is studying Python for 2 hours to prepare for a Data Engineer career.

concat_msg = name + ' is studying ' + language + ' for ' + str(study_hours) + ' hours to prepare for a ' + career + ' career.'
print(concat_msg)

f_string = f'{name} is studying {language} for {study_hours} hours to prepare for a {career} career.'
print(f_string)

format_msg = '{} is studying {} for {} hours to prepare for a {} career.'.format(name,language, study_hours, career)
print(format_msg)
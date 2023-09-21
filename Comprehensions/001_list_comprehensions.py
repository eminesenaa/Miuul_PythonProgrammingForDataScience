def new_salary(x):
    return x * 20 / 100 + x

salaries = [1000, 2000, 3000, 4000, 5000]

null_list = []


for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

print(null_list)           


# this line does same calculation


[new_salary(salary ) if salary > 3000 else new_salary(salary * 2) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000] # if is written on right if there is no else keyword.

[salary * 2 if salary < 3000 else salary for salary in salaries]




students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John",  "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]
[student.upper() if student not in students_no else student.lower() for student in students]


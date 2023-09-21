
# ? goal: add the square of even numbers into a dict
# ? keys are original, values are changed 


numbers = range(10)
new_dict = {}


for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

new_dict.items()

{n: n ** 2  for n in numbers if n  % 2 == 0}
new_dict.items()

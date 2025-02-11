
# number = 7

# while True:
#   user_input = input('daj n ak nechces hrat: ')
#   if user_input == 'n':
#     break

#   user_number = int(input('hadaj cislo: '))
#   if user_number == number: 
#     print('spravne pixi boa')
#     break
#   elif abs(number - user_number) == 1:
#     print('tesnotka uuuu')
#   else: 
#     print('HAHAHA debilko')


# ludia = ['rado', 'pato', 'ludek', 'stanka']

# for lud in ludia:
#   print(f"{lud} je clovek")

class Student:
  pes = 'pes'
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades

  def __str__(self):
    return f'toto je {self.name}'

  def average(self):
    return sum(self.grades) / len(self.grades)

  def piseme(self, text: str):
    self.pes = text

student = Student('Manko', (90,90,93,78,70))
print(student.pes)
print(student.piseme('haudy'))
print(student.pes)
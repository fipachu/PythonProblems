from collections import namedtuple

Student = namedtuple('Student', 'name, age, department')

alina = Student('Alina', '22', 'linguistics')
alex = Student('Alex', '25', 'programming')
kate = Student('Kate', '19', 'art')

print(alina, alex, kate, sep='\n')

students = ("manasa", "pranathi", "shrestha", "likitha")
sorted(students) #(students, reverse = True)

for i in students:
    print(i)

print("_________________")

students_1 = [("manasa", "D", 22),
             ("pranathi", "A", 23),
             ("shrestha", "C", 21),
             ("likitha", "B", 24)]

students_1.sort() #sorted according to first element of tuple

for i in students_1:
    print(i)

print("_________________")

students_1.sort(key = lambda age: age[2]) #sorted according to third element of tuple

for i in students_1:
    print(i)

print("_________________")

students_1.sort(key = lambda grade: grade[1]) #sorted according to second element of tuple

for i in students_1:
    print(i)

print("_________________")

students_2 = (("manasa", "D", 22),
                ("pranathi", "A", 23),
                ("shrestha", "C", 21),
                ("likitha", "B", 24))

students_2 = sorted(students_2, key = lambda grade: grade[1]) #sorted according to second element of tuple

for i in students_2:
    print(i)
fruits=['apple', 'ananas', 'kiwi']
print(len(fruits))

numbers=[]
for i in range(5):
    num=int(input('Enter number'))
    numbers.append(num)
print(numbers)

colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop()
print(colors)

animals = ["dog", "cat", "elephant", "lion"]
animals.insert(1,"monkey")
print(animals)

students=[]
for i in range(3):
    student=input('Enter student name')
    students.append(student)
students.insert(0,'teacher')
students.pop(3)
print(students)
print(len(students))

    

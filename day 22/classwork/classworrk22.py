students = ['Alex' , 'Jane' , 'Lucas' , 'Kate']
print(students)
#ვქმნით ცვლადს სიით რომელსაც შემდეგ ვპრინტავთ
students.append('Mary')
students.append('Pitt')
print(students)
students.insert(0,'Embreigh')
students.insert(3,'Nikolozi')
print(students)

data = [15, 40.2, 15, 5, 7, 10, 23, 15]
print(data)
N = data.count(15)
print(N)
data.sort()
print(data)
print(data[::-1])
#ეს ფორმულა (slicing გამოყენებით) ატრიალებს სიას და ეს ხდება იმიტომ რომ start stop მეშვეობით მთლიან სიას ვნიშნავთ და ნაბიჯებში კი -1ით ვაუკუთველვინებთ
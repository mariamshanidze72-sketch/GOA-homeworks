numbers_step = [5, 10, 15, 20, 25, 30, 35, 40]
print(numbers_step[0:8:2])

fruits = ["ვაშლი", "მსხალი", "ატამი", "ბალი", "ყურძენი", "ბანანი", "ფორთოხალი"]
print(fruits[2:5:1])

mixed_nums= [12,45,8,33,91,24,10,77]
for i in mixed_nums:
    if i%2 == 0 :
        print(i)

#ფუნქცია ჩვენს მიერ დაკისრებულ სამუშაოს ასრულებს და კოდს გვიმარტივებს
#ფუნქციის არგუმენტები არის მნიშვნელობები რომლებსაც პარამეტრებს ვანიჭებთ მაგალითად def greet(greeting).....  greet('Hello!)


print('HelLo'.lower())
print('gOodbye'.upper())
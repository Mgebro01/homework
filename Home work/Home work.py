# Homework 1

# print(9-3, 8*2.5, 9/2, 9/-2, 9%2, 9**2)
# print(4-2**3+5*2-3/2)
# print((3+245)*4-3**4)
# print((42+3*3)/(2+4))



# # Homework 2
#
# # 1-What's up, Tim
#
# message = "What's up, Tim?"
# print(message)
#
# # 2-A and B reverse
#
# a = 1
# b = 4
# a, b = b, a
# print('a', a, 'b', b)
#
# # 3- Name and last name
#
# Name = input("What's your name?:")
# lastname = input("What's your last name?:")
#
# print('you are', Name, lastname)
#
# # 4- Salary per month
#
# Salaryperhour = input('How much do you earn per hour?:')
# Workingtime = input('How long do you work a month?:')
# Answer = int(Salaryperhour) * int(Workingtime)
#
# print('You earn', Answer, '$ per month')
#
#
# # 5- საშუალო არითმეტიკული
#
# a = input("write any number:")
# b = input("write any number:")
# c = input("write any number:")
#
# Answer = ((int(a)+int(b)+int(c))/3)
# print(Answer)
#
# # 6- How many years to 100 years
#
# Name, Age = (input("What's your name?:")), (input("How old are you?:"))
# Year = (100 - int(Age))
#
# print("You will be 100 years old in", Year, "years")
#
# # C to F
#
# C = (input("Write any C degrees:"))
# F = (int(C)*9/5)+32
#
# print('Your input in Celsius degrees Fahrenheit', F)


# homework-3

# 1: Positive and Negative numbers

# Number = input('Write any negative or positive number:')
#
# if (int(Number)) > 0:
#     print("Number is positive")
#
# if (int(Number)) < 0:
#     print("Number is negative")
#
# if (int(Number)) == 0:
#     print("Number is equal to zero")
#
#
# # 2: 10-is jeradi
#
# Number = input('Write any number:')
#
# Finalresult = (int(Number)) % 10
#
# if Finalresult == 0:
#     print("რიცხვი ბოლოვდება 0-ით")
# else:
#     print("რიცხვი არ ბოლოვდება 0-ით")
#
# # 3: >10 or <10
#
# Number = input('Write any number:')
#
# Number2 = input('Write any number:')
#
# if (int(Number)) > 10 and (int(Number2)) > 10:
#     print(((int(Number)) + (int(Number2))) / 2, 'არის პირველი და მეორე რიცხვის საშუალო არითმეტიკული')
# else:
#     print((int(Number)) * (int(Number2)), 'არის პირველი და მეორე რიცხვის ნამრავლი')
#
#
# # 4: 3 number programm
#
# Number = input('Write any number:')
#
# Number2 = input('Write any number:')
#
# Number3 = input('Write any number:')
#
# if (int(Number)) < (int(Number2)) and (int(Number)) < (int(Number3)):
#     print('Number 1 is lowest number')
#
# else:
#     if (int(Number2)) < (int(Number)) and (int(Number2)) < (int(Number3)):
#         print('Number 2 is lowest number')
#     else:
#         if (int(Number3)) < (int(Number)) and (int(Number3)) < (int(Number2)):
#             print('Number 3 is lowest number')
#
#
# # 5: Last digit of number
#
# Number = int(input('Write any number:'))
#
# print(Number % 10, "is last digit of number")

# Homework 4

#  ნაკიანი წლები
#
# Year = int(input('write any year:'))
#
# if not Year % 4 == 0 and not Year % 400 == 0 and not Year % 100 == 0:
#     print(Year, 'არ არის, ნაკიანი წელი')
# elif Year % 4 == 0 and not Year % 100 == 0 and not Year % 400 == 0:
#     print(Year, 'არის, ნაკიანი წელი')
# elif Year % 100 == 0 and Year % 4 == 0 and not Year % 400 == 0:
#     print(Year, 'არ არის, ნაკიანი წელი')
# elif Year % 100 == 0 and Year % 4 == 0 and Year % 400 == 0:
#     print(Year, 'არის, ნაკიანი წელი')


# Homework 5

# 1) 5 ის ჯერადები 20 - 125

# print('5 ის ჯერადები 20 - 125')
# print()
# Number = 20
#
# while Number <= 125:
#
#     if Number % 5 == 0:
#         print(Number)
#
#     Number += 1
#
# input()
#
# # 2) 8 ის ჯერადები 200 - 25
#
# print()
# print('8 ის ჯერადები 200 - 25')
# print()
#
# for i in range(200, 25, -1):
#
#     if i % 8 == 0:
#         print(i)
#
# input()
#
# # 3) 1500 - 2100 5 ის და 7 ის ჯერადები
#
# print()
# print('1500 - 2100 5 ის და 7 ის ჯერადები')
# print()
#
# for i in range(1500, 2101, 1):
#
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
#
# input()
#
# # 4) 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად.
#
# print()
# print('1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად.')
# print()
#
# Number = 0
#
# for i in range(1500, 2101, 1):
#
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
#         Number += i
#
# print('ამ რიცხვების ჯამი არის', Number)
#
# input()
#
# # 5) 1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად. როგორც კი რიცხვების ჯამი გადააჭარბებს 20 000-ს, შეწყვიტეთ ციკლი. დაბეჭდეთ მიღებული ჯამი ეკრანზე.
#
# print()
# print('1500-დან 2100-ის ჩათვლით რიცხვების ჯამი რომლებიც არიან 7-ის და 5-ის ჯერადი ერთდროულად. როგორც კი რიცხვების ჯამი გადააჭარბებს 20 000-ს, შეწყვიტეთ ციკლი. დაბეჭდეთ მიღებული ჯამი ეკრანზე.')
# print()
#
# Number = 0
#
# for i in range(1500, 2101, 1):
#
#     if i % 7 == 0 and i % 5 == 0:
#         print(i)
#         Number += i
#
#     if Number > 20000:
#         break
#
# print('ამ რიცხვების ჯამი არის', Number)
#
# input()
#
# # 6) დაითვალეთ 1500-დან 2100-ის ჩათვლით 5-ის ჯერადი რიცხვების რაოდენობა. დაბეჭდეთ შედეგი.
#
# print()
# print('დაითვალეთ 1500-დან 2100-ის ჩათვლით 5-ის ჯერადი რიცხვების რაოდენობა. დაბეჭდეთ შედეგი.')
# print()
#
# Number = 0
#
# for i in range(1500, 2101, 1):
#
#     if i % 5 == 0:
#         print(i)
#         Number += 1
#
# print('ამ რიცხვების რაოდენობა არის', Number)
#
# input()
#
# # 7) შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო არითმეტიკული.
#
# print()
# print('შეიყვანეთ 10 რიცხვი კლავიატურიდან ციკლის გამოყენებით. დაითვალეთ შეყვანილი რიცხვების საშუალო არითმეტიკული.')
# print()
#
# Number = 0
#
# for i in range(0, 10):
#     Number += int(input('input number:'))
# print(Number/10)
#
# input()
#
# # 8) დაითვალეთ 1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი და დაბეჭდეთ შედეგი.
#
# print()
# print('დაითვალეთ 1-დან 100-ის ჩათვლით ლუწი რიცხვების ჯამი და დაბეჭდეთ შედეგი.')
# print()
#
# Number = 0
#
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)
#         Number += i
#
# print(Number)
#
# input()
#
# # 9) დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის, 75, 80-ისა. გამოიყენეთ continue ოპერატორი.
#
# print()
# print('დაბეჭდეთ ეკრანზე 15-დან 150-მდე 5-ის ჯერადი რიცხვები გარდა 50-ის, 75, 80-ისა. გამოიყენეთ continue ოპერატორი.')
# print()
#
# for i in range(14, 150, 1):
#
#     if i % 5 == 0 and i == 50 or i == 75 or i == 80:
#         continue
#     elif i % 5 == 0:
#         print(i)
#
# input()
#
# 10) შეიყვანეთ რიცხვი. დაითვალეთ ამ რიცხვის ფაქტორიალი და დაბეჭდეთ. მაგალითად 5-ის ფაქტორიალი იგივია რაც 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5
#
# print()
# print('შეიყვანეთ რიცხვი. დაითვალეთ ამ რიცხვის ფაქტორიალი და დაბეჭდეთ. მაგალითად 5-ის ფაქტორიალი იგივია რაც 1 ∗ 2 ∗ 3 ∗ 4 ∗ 5')
# print()
#
# # ვარიანტი 1
#
# end = int(input('input number:'))
# N = 1
# Number = 1
#
# for i in range(0, end):
#
#     Number *= N
#     N += 1
#
# print(Number)
#
# # ვარიანტი 2
#
# for i in range(0, end):
#
#     Number *= i
#
# print(Number)
#

# Homework 6

# 1.შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უდიდესი საერთო გამყოფი.
#
# print()
# print("1.შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უდიდესი საერთო გამყოფი.")
# print()
#
# Number = int(input('input number:'))
#
# Number2 = int(input('input number:'))
# Low = Number2
#
#
# if Number < Number2:
#
#     Low = Number
#
# for i in range(Low, 0, -1):
#
#     if Number < 0 or Number2 < 0:
#         print('ეს რიცხვი 0-ზე ნაკლებია')
#         break
#
#     elif Number % i == 0 and Number2 % i == 0:
#         print(i)
#         break
#
#
# # შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.
#
# print()
# print('შეიყვანეთ 2 დადებითი მთელი რიცხვი. იპოვეთ ამ ორი რიცხვის უმცირესი საერთო ჯერადი.')
# print()
#
# Number = int(input('input number:'))
#
# Number2 = int(input('input number:'))
#
# i = 0
#
# while True:
#     i += 1
#
#     if Number < 0 or Number2 < 0:
#         print('ეს რიცხვი 0-ზე ნაკლებია')
#         break
#
#     if i % Number == 0 and i % Number2 == 0:
#         print(i)
#         break
#
#
# # 3. შეიყვანეთ 10 რიცხვი ციკლის გამოყენებით.
# # იპოვეთ რიცხვებს შორის უდიდესი კენტი რიცხვი და დაბეჭდეთ.
# # თუ კენტი რიცხვი არ შეგხვდათ, გამოიტანეთ შესაბამისი შეტყობინება.
#
# print()
# print('3. შეიყვანეთ 10 რიცხვი ციკლის გამოყენებით. იპოვეთ რიცხვებს შორის უდიდესი კენტი რიცხვი და დაბეჭდეთ.თუ კენტი რიცხვი არ შეგხვდათ, გამოიტანეთ შესაბამისი შეტყობინება.')
# print()
#
# Number = 0
#
# N = 0
#
# for i in range(0, 10):
#
#     Number = int(input('input number:'))
#
#     if Number % 2 != 0 and Number > N:
#         N = Number
#
#
# if N == 0:
#     print('ამ რიცხვებში არ არის კენტი რიცხვი')
# else:
#     print(i)
#
#

#  Homework 7

# 1. შეიყვანეთ ნებისმიერი რიცხვი. დაადგინეთ არის
# თუ არა შეტანილი რიცხვი პალინდრომი. (მითითება: პალინდრომია რიცხვი, რომელიც მარჯვნიდან და მარცხნიდან ერთნაირად იკითხება)
# . მაგ. 12521 არის პალინდრომი
#
# print()
# print('1. შეიყვანეთ ნებისმიერი რიცხვი. დაადგინეთ არის თუ არა შეტანილი რიცხვი პალინდრომი. (მითითება: პალინდრომია რიცხვი, რომელიც მარჯვნიდან და მარცხნიდან ერთნაირად იკითხება). მაგ. 12521 არის პალინდრომი')
# print()
#
# number = int(input('input number:'))
#
# temp_number = number
# result = 0
#
# while temp_number >= 1:
#
#     result *= 10
#     result += temp_number % 10
#
#     temp_number //= 10
#
# if result == number:
#     print('შეტანილი რიცხვი პალინდრომია.')
# else:
#     print('შეტანილი რიცხვი არ არის პალინდრომი.')
#
#
# # 2 შეიყვანეთ ორი რიცხვი.
# # დაბეჭდეთ ამ ორ რიცხვს შორის არსებული ყველა „სარკისებური მარტივი“ რიცხვები (Mirror Prime Numbers).
# # რიცხვი „სარკისებურად მარტივია“ თუ იგი არის მარტივი და მისი შებრუნებული მნიშვნელობაც მარტივია.
# # დაბეჭდეთ ამ ორ რიცხვს შორის არსებული ყველა „სარკისებური მარტივი“ რიცხვები (Mirror Prime Numbers).
# # რიცხვი „სარკისებურად მარტივია“ თუ იგი არის მარტივი და მისი შებრუნებული მნიშვნელობაც მარტივია.
#
# print()
# print('2. შეიყვანეთ ორი რიცხვი. დაბეჭდეთ ამ ორ რიცხვს შორის არსებული ყველა „სარკისებური მარტივი“ რიცხვები (Mirror Prime Numbers). რიცხვი „სარკისებურად მარტივია“ თუ იგი არის მარტივი და მისი შებრუნებული მნიშვნელობაც მარტივია. ')
# print()
#
# number = int(input('input number:'))
# number2 = int(input('input number:'))
#
# if number > number2:
#     high = number
#     low = number2
# else:
#     high = number2
#     low = number
#
# temp_number = 0
# result = 0
#
# for n in range(low, high):
#      h = 0
#      temp_number = n
#      for i in range(2, n):
#          if n % i == 0:
#              h = 1
#
#      if h == 0:
#          temp_number = n
#          result = 0
#          while temp_number >= 1:
#              result *= 10
#              result += temp_number % 10
#
#              temp_number //= 10
#          if result == n:
#              print(n)


# homework 8
# 1. შეიტანეთ ათწილადი რიცხვი, დაამრგვალეთ ათწილად ნაწილში მეათედის სიზუსტით (1 ციფრი ათწილად ნაწილში) და დაბეჭდეთ შედეგი.
# გამოიყენეთ round, ceil, floor, trunc ფუნქციები სათითაოდ და შეამოწმეთ შედეგი თითოეულის გამოყენებით.
#
# print('1. შეიტანეთ ათწილადი რიცხვი, '
#       'დაამრგვალეთ ათწილად ნაწილში მეათედის სიზუსტით (1 ციფრი ათწილად ნაწილში) და დაბეჭდეთ შედეგი.'
#       ' გამოიყენეთ round, ceil, floor, trunc ფუნქციები სათითაოდ და შეამოწმეთ შედეგი თითოეულის გამოყენებით.')
#
# from math import ceil, floor, trunc
#
# print(ceil(float(input('შეიყვანე ათწილადი:'))))
# print(floor(float(input('შეიყვანე ათწილადი:'))))
# print(trunc(float(input('შეიყვანე ათწილადი:'))))
# print(round(float(input('შეიყვანე ათწილადი:'))))
#
# # 2. შეიტანეთ სამი რიცხვი, იპოვეთ მათ შორის მაქსიმუმი და დაბეჭდეთ შედეგი. გამოიყენეთ max ფუნქცია.
#
# print()
# print('2. შეიტანეთ სამი რიცხვი, იპოვეთ მათ შორის მაქსიმუმი და დაბეჭდეთ შედეგი. გამოიყენეთ max ფუნქცია.')
# print()
#
# print(max(input('input number'), input('input number'), input('input number')))
#
# # 3. გამოთვალეთ 38 ფუნქციის გამოყენებით და დაბეჭდეთ შედეგი. ასევე გამოთვალეთ 29, 46 და დაბეჭდეთ მიღებული შედეგი.
#
# print()
# print("გამოთვალეთ 38 ფუნქციის გამოყენებით და დაბეჭდეთ შედეგი. ასევე გამოთვალეთ 29, 46 და დაბეჭდეთ მიღებული შედეგი.")
# print()
#
# from math import pow
#
# print(pow(3, 8), ',', pow(2, 9), ',', pow(4, 6))
#
#
# # 4. გამოთვალეთ მათემატიკური ფუნქციის გამოყენებით: ა) კვადრატული ფესვი 225625-დან ბ) კვადრატული ფესვი 4225-დან
#
# print()
# print('4. გამოთვალეთ მათემატიკური ფუნქციის გამოყენებით: ა) კვადრატული ფესვი 225625-დან ბ) კვადრატული ფესვი 4225-დან')
# print()
#
# from math import sqrt
#
# print(sqrt(225625))
# print(sqrt(4225))
#
# # 5. დააგენერირეთ ნებისმიერი შემთხვევითი ათწილადი რიცხვი დიაპაზონიდან 0-დან 1-ის ჩათვლით.
# # დაამრგვალეთ რიცხვი (3 ციფრი ათწილად ნაწილში) და დაბეჭდეთ.
#
# print()
# print('5. დააგენერირეთ ნებისმიერი შემთხვევითი ათწილადი რიცხვი დიაპაზონიდან 0-დან 1-ის ჩათვლით.'
#       ' დაამრგვალეთ რიცხვი (3 ციფრი ათწილად ნაწილში) და დაბეჭდეთ.')
# print()
#
# from random import uniform
#
# print(uniform(0, 1), 3)
#
#
# # 6. დააგენერირეთ ნებისმიერი შემთხვევითი ათწილადი რიცხვი 100-დან 120-მდე.
# # დაამრგვალეთ რიცხვი (1 ციფრი ათწილად ნაწილში) და ისე გამოიტანეთ.
#
# print()
# print(". დააგენერირეთ ნებისმიერი შემთხვევითი ათწილადი რიცხვი 100-დან 120-მდე."
#       " დაამრგვალეთ რიცხვი (1 ციფრი ათწილად ნაწილში) და ისე გამოიტანეთ.")
# print()
#
#
# print(round(uniform(100, 120), 1))
#
#
# # 7. დააგენერირეთ 10 შემთხვევითი მთელი რიცხვი და დაბეჭდეთ ეკრანზე. მითითება: გამოიყენეთ ციკლის ოპერატორი.
#
# print()
# print('7. დააგენერირეთ 10 შემთხვევითი მთელი რიცხვი და დაბეჭდეთ ეკრანზე. მითითება: გამოიყენეთ ციკლის ოპერატორი.')
# print()
#
# from random import randint
#
# for i in range(1, 11):
#     print(randint(1, 1000000000))
#



# homework 9

# 1. შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის (დააბრუნებს) მათ საშუალო არითმეტიკულს.
# გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის და დაბეჭდეთ შედეგი.
# print()
# print('1. შექმენით ფუნქცია, '
#       'რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის (დააბრუნებს) მათ საშუალო არითმეტიკულს.'
#       'გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის და დაბეჭდეთ შედეგი.')
# print()
#
# from random import uniform
#
# def task1(x, y):
#     return ((x + y) / 2)
#
# for i in range(0,3):
#     print(task1(uniform(10, 100), uniform(10, 100)))
#
# # 2. დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის მათ საშუალო არითმეტიკულს და დაბეჭდავს შედეგს
# # (გაითვალისწინეთ რომ დაბეჭდვა უნდა მოხდეს ფუნქციის შიგნით - ფუნქცია არ აბრუნებს მნიშვნელობას).
# # გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის.
#
# print()
# print('2. დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი და დაითვლის'
#       ' მათ საშუალო არითმეტიკულს და დაბეჭდავს შედეგს(გაითვალისწინეთ რომ დაბეჭდვა უნდა მოხდეს ფუნქციის'
#       ' შიგნით - ფუნქცია არ აბრუნებს მნიშვნელობას).გამოიძახეთ ფუნქცია 3-ჯერ სხვადასხვა რიცხვებისთვის.')
# print()
#
#
# def task2(x, y):
#     sasualo = (x + y) / 2
#
#     print(sasualo)
#
# for i in range(0,3):
#     task2(uniform(10, 100), uniform(10, 100))
#
#
#
# # 3. შექმენით ფუნქცია, რომელიც დაითვლის (დააბრუნებს) არგუმენტად გადაცემული რიცხვის კუბს.
# # გამოიძახეთ ფუნქცია რამდენიმეჯერ და დაბეჭდეთ მიღებული შედეგი.
#
# print()
# print('3. შექმენით ფუნქცია, რომელიც დაითვლის (დააბრუნებს) არგუმენტად გადაცემული რიცხვის კუბს.'
#       ' გამოიძახეთ ფუნქცია რამდენიმეჯერ და დაბეჭდეთ მიღებული შედეგი.')
# print()
#
#
#
# def task3(x):
#
#     return x ** 3
#
# print(task3(34))
#
#
# # 4. შექმენით ფუნქცია, რომელიც დაითვლის (დააბრუნებს) ორ რიცხვს შორის მინიმალურ მნიშვნელობას.
# # გამოიძახეთ ფუნქცია და დაბეჭდეთ შედეგი. (პარამეტრად გადაეცით ნებისმიერი ორი რიცხვი).
#
# print()
# print('4. შექმენით ფუნქცია, რომელიც დაითვლის (დააბრუნებს) ორ რიცხვს შორის მინიმალურ მნიშვნელობას.'
#       ' გამოიძახეთ ფუნქცია და დაბეჭდეთ შედეგი.'
#       ' (პარამეტრად გადაეცით ნებისმიერი ორი რიცხვი).')
# print()
#
#
# def task4(x, y):
#     if x > y:
#         return y
#     else:
#         return x
#
# print(task4(int(input('input number:')), int(input('input number:'))))
#
#
# # 5. დაწერეთ ფუნქცია, რომელიც შეამოწმებს პარამეტრად გადაცემული რიცხვი არის თუ არა კენტი.
# # თუ კენტია, დააბრუნოს მნიშვნელობა True, თუ არადა - False. შეამოწმეთ რამდენიმე რიცხვისთვის და დაბეჭდეთ შედეგი.
#
# print()
# print('5. დაწერეთ ფუნქცია, რომელიც შეამოწმებს პარამეტრად გადაცემული რიცხვი არის თუ არა კენტი.'
#       ' თუ კენტია, დააბრუნოს მნიშვნელობა True, თუ არადა - False.'
#       ' შეამოწმეთ რამდენიმე რიცხვისთვის და დაბეჭდეთ შედეგი.')
# print()
#
# def task5(x):
#     if x % 2 != 0:
#         return True
#     else:
#         return False
#
# print(task5(int(input('input number:'))))
#
# # 6. დაწერეთ ფუნქცია, რომელიც დაითვლის (დააბრუნებს) პარამეტრად გადაცემული რიცხვის ფაქტორიალს და დაბეჭდეთ შედეგი სხვადასხვა რიცხვებისთვის.
#
# print()
# print('6. დაწერეთ ფუნქცია, რომელიც დაითვლის (დააბრუნებს) პარამეტრად გადაცემული რიცხვის ფაქტორიალს და დაბეჭდეთ შედეგი სხვადასხვა რიცხვებისთვის.')
# print()
#
# from math import factorial
#
# def task6(x):
#
#     return factorial(x)
#
# print(task6(int(input("input number:"))))
#
# #7. დაწერეთ უპარამეტრო ფუნქცია რომელიც ეკრანზე ბეჭდავს შემდეგ ტექსტს: “Hello World”.
# # (გაითვალისწინეთ რომ ფუნქცია არ აბრუნებს მნიშვნელობას).
#
# print()
# print("7. დაწერეთ უპარამეტრო ფუნქცია რომელიც ეკრანზე ბეჭდავს შემდეგ ტექსტს: “Hello World”."
#       " (გაითვალისწინეთ რომ ფუნქცია არ აბრუნებს მნიშვნელობას).")
# print()
#
#
# def task7():
#     print("hello world")
#
# task7()
#
# # 8. დაწერეთ ფუნქცია, რომელიც დაადგენს არის თუ არა პარამეტრად გადაცემული რიცხვი მარტივი რიცხვი.
#
# print()
# print('8. დაწერეთ ფუნქცია, რომელიც დაადგენს არის თუ არა პარამეტრად გადაცემული რიცხვი მარტივი რიცხვი.')
# print()
#
# def task8(x):
#
#     is_prine = True
#     for i in range(2, x):
#
#          if x % i == 0:
#              is_prine = False
#              break
#
#     return is_prine
#
#
# print(task8(int(input('input number:'))))
#


# homework 10
# task 1
#
#1. შეიყვანეთ ნებისმიერი სტრიქონი. იპოვეთ ყველაზე ხშირად განმეორებადი სიმბოლო და დაბეჭდეთ.
#
# print()
# print('1. შეიყვანეთ ნებისმიერი სტრიქონი. იპოვეთ ყველაზე ხშირად განმეორებადი სიმბოლო და დაბეჭდეთ.')
# print()
#
# text = input('input text:')
#
# # for i in range(0, len(text)):
# # ??? vergavige pirveli mas
# #
# #
# # task 2
# # 2. დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა სამკუთხედის სამივე გვერდი და აბრუნებს
# # bool მნიშვნელობას არსებობს თუ არა სამკუთხედი.
# # (სამკუთხედი არსებობს თუ ნებისმიერი ორი გვერდის ჯამი მესამე გვერდზე მეტია)
# print()
# print('2. დაწერეთ ფუნქცია, რომელსაც არგუმენტად გადაეცემა სამკუთხედის სამივე გვერდი და აბრუნებს'
#       ' bool მნიშვნელობას არსებობს თუ არა სამკუთხედი.'
#       ' (სამკუთხედი არსებობს თუ ნებისმიერი ორი გვერდის ჯამი მესამე გვერდზე მეტია)')
# print()
#
# def triangle(a, b, c):
#     if (a + b) > c and (a + c) > b and (c + b) > a:
#         return True
#     else:
#         return False
#
# print(triangle(input(">"), input(">"), input(">")))
# #
# #
# #
# #
# #
# # task 3
# # 3. text ცვლადს მიანიჭეთ სტრიქონი "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების".
# # სტრიქონში შეცვალეთ ყველა "ლ" ასო "ნ" ასოდ. და დაბეჭდეთ მიღებული შედეგი
# print()
# print('3. text ცვლადს მიანიჭეთ სტრიქონი "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების".'
#       ' სტრიქონში შეცვალეთ ყველა "ლ" ასო "ნ" ასოდ.'
#       ' და დაბეჭდეთ მიღებული შედეგი')
# print()
#
# Text = 'სწავლის ძირი მწარე არის, კენწეროში გატკბილდების.'
# final_result = ''
#
# for i in range(0, len(Text)):
#     if 'ლ' == Text[i]:
#         final_result += 'ნ'
#     else:
#         final_result += Text[i]
#
# print(final_result)
# #
#
#
#homework 11
# task 1. შეიყვანეთ სტრიქონი. გადაიყვანეთ სტრიქონის ყველა სიმბოლო მაღალ რეგისტრში და დაბეჭდეთ შედეგი.
#
# print()
# print('1. შეიყვანეთ სტრიქონი. გადაიყვანეთ სტრიქონის ყველა სიმბოლო მაღალ რეგისტრში და დაბეჭდეთ შედეგი.')
# print()
#
# text = input('input text:')
#
# print(text.upper())
#
# # task 2. შეიყვანეთ სამი სტრიქონი რომელიც წარმოადგენს სხვადასხვა ხილის დასახელებას (მაგ. Banana, Watermelon, Apple).
# # დაბეჭდეთ ისინი ალფაბეტის ზრდადობის მიხედვით.
#
# print()
# print('2. შეიყვანეთ სამი სტრიქონი რომელიც წარმოადგენს სხვადასხვა ხილის დასახელებას'
#       ' (მაგ. Banana, Watermelon, Apple).'
#       ' დაბეჭდეთ ისინი ალფაბეტის ზრდადობის მიხედვით.')
# print()
#
# alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
#
# text = input('input fruit >')
# text2 = input('input fruit >')
# text3 = input('input fruit >')
#
# #

# homework 12
#1. დაწერეთ პროგრამა, რომლის მეშვეობით შექმნით ფაილს იმავე დირექტორიაში (საქაღალდეში), ჩაწერეთ მასში ნებისმიერი ტექსტი და დახურეთ ფაილი.
#
# print()
# print('1. დაწერეთ პროგრამა, რომლის მეშვეობით შექმნით ფაილს იმავე დირექტორიაში'
#       ' (საქაღალდეში), ჩაწერეთ მასში ნებისმიერი ტექსტი და დახურეთ ფაილი.')
# print()
#
#
# file_object = open('testfile.txt', 'w')
# file_object.write('task done')
# file_object.close()
#
# # 2. დაწერეთ პროგრამა, რომლის მეშვეობით გახსნით ფაილს, წაიკითხავთ კონტენტს და დაბეჭდავთ ეკრანზე. დაითვალეთ სიმბოლოების რაოდენობა ფაილში.
#
# print()
# print('2. დაწერეთ პროგრამა, რომლის მეშვეობით გახსნით ფაილს,'
#       ' წაიკითხავთ კონტენტს და დაბეჭდავთ ეკრანზე.'
#       ' დაითვალეთ სიმბოლოების რაოდენობა ფაილში.')
# print()
#
# file_object2 = open('testfile.txt', 'r')
# i = file_object2.read()
#
# print(i)
# print(len(i))
#
# file_object2.close()
# #
# #
# # 3. დაწერეთ პროგრამა, რომლის მეშვეობით გახსნით უკვე არსებულ ფაილს და ბოლოში დაამატეთ თქვენთვის სასურველი ტექსტი.
# print()
# print('3. დაწერეთ პროგრამა, რომლის მეშვეობით გახსნით უკვე არსებულ ფაილს და ბოლოში დაამატეთ თქვენთვის სასურველი ტექსტი.')
# print()
#
#
# file_object2 = open('testfile.txt', 'a')
# file_object2.write('\nhello world')
#
# file_object2.close()
# #
# #
# #
# #4. დაწერეთ პროგრამა რომელიც წაიკითხავს ინფორმაციას ერთი ფაილიდან და ჩააკოპირებს მეორე (ახალ) ფაილში.
# #
# print()
# print('4. დაწერეთ პროგრამა რომელიც წაიკითხავს ინფორმაციას ერთი ფაილიდან და ჩააკოპირებს მეორე (ახალ) ფაილში.')
# print()
#
#
# file_object2 = open('testfile.txt', 'r')
# i = file_object2.read()
#
# file_object3 = open('test_file_2', 'w')
#
# file_object3.write(i)
#
# file_object3.close()
# file_object2.close()


# Homeowrk done !

#
#
#
#
#
# Homework 13

# 1. დაწერეთ პროგრამა, რომელის გაშვების შემდეგ კლავიატურიდან შეყვანილ ინფორმაციას ჩავწერთ data.txt
# ფაილში ცალ-ცალკე ხაზზე. დავასრულოთ შეტანა 0-ით.
#
# print()
# print('1. დაწერეთ პროგრამა, რომელის გაშვების შემდეგ'
#       ' კლავიატურიდან შეყვანილ ინფორმაციას ჩავწერთ data.txt'
#       ' ფაილში ცალ-ცალკე ხაზზე.'
#       ' დავასრულოთ შეტანა 0-ით.')
# print()
#
# file = open('data.txt', 'a')
#
# text = input('input text: >')
#
# file.write(text + '\n')
#
# file.close()
#
# # 2. დაწერეთ პროგრამა, რომლის მეშვეობით ერთი ფაილიდან წაიკითხავთ კონტენტს. ჩაწერეთ მთლიანი კონტენტი მეორე (ახალ) ფაილში ერთ ხაზზე.
# # მითითება: თუ პირველ ფაილში არის 3 სტრიქონი, ახალ ფაილში ჩაწერეთ ერთ სტრიქონზე და გამოყავით სპეისით.
#
# print()
# print('2. დაწერეთ პროგრამა, რომლის მეშვეობით ერთი ფაილიდან წაიკითხავთ კონტენტს.'
#       ' ჩაწერეთ მთლიანი კონტენტი მეორე (ახალ) ფაილში ერთ ხაზზე. მითითება:'
#       ' თუ პირველ ფაილში არის 3 სტრიქონი, ახალ ფაილში ჩაწერეთ ერთ სტრიქონზე და გამოყავით სპეისით.')
# print()
#
# file = open('data.txt', 'r')
# file2 = open('testfile.txt', 'a')
#
# text = file.read()
#
# file2.write(text)
#
# file.close()
# #
# #
# # 3. დაწერეთ პროგრამა, დაითვლის ფაილში სიტყვების, სიმბოლოების და ხაზების რაოდენობას. დაბეჭდეთ მიღებული შედეგები.
#
# print()
# print('3. დაწერეთ პროგრამა, დაითვლის ფაილში სიტყვების, სიმბოლოების და ხაზების რაოდენობას. დაბეჭდეთ მიღებული შედეგები.')
# print()
# #
# # file = open('data.txt', 'rt')
# # word = file.read()
# # word.split()
# # print(len(word))
#
# file = open("data.txt", "rt")
#
# data = file.read()
# words = data.split()
#
# print('Number of words in text file :', len(words))
# file.close()
#
# file = open("data.txt", "r")
# lines = len(file.readlines())
#
# print(lines)
#
# file.close()
# #
# #
# #
# # 4. შექმენით ტექსტური ფაილი რომელშიც ჩაწერთ რიცხვებს ცალ-ცალკე ხაზზე.
# # დაწერეთ პროგრამა, რომელიც წაიკითხავს მონაცემებს ფაილიდან,
# # აიყვანს რიცხვებს კვადრატში და ჩაწერს შედეგებს
# # ახალ ფაილში.
#
# print()
# print('4. შექმენით ტექსტური ფაილი რომელშიც ჩაწერთ რიცხვებს ცალ-ცალკე ხაზზე.'
#       ' დაწერეთ პროგრამა, რომელიც წაიკითხავს მონაცემებს ფაილიდან,'
#       ' აიყვანს რიცხვებს კვადრატში და ჩაწერს შედეგებს ახალ ფაილში.')
# print()
#
# #
# #
#
#
#1. დაწერეთ ფუნქცია, რომელიც დაადგენს არის თუ არა პარამეტრად გადაცემული რიცხვი რაიმე მთელი რიცხვის კვადრატი.
# ფუნქციამ უნდა დააბრუნოს შესაბამისი მნიშვნელობა. ფუნქციის გარეთ მომხმარებელს შეატანინეთ ნებისმიერი მთელი რიცხვი.
# გამოიძახეთ შექმნილილ ფუნქცია ამ რიცხვისთვის და დაბეჭდეთ შესაბამისი შეტყობინება.
#
#

from math import sqrt

def task_1(x):
    result = sqrt(x)
    print(result)
    if str(result).__contains__('.'):
         return False
    else:
         return True


number = int(input('შეიყვანე ნებისმიერი მთელი რიცხვი:>'))

print(task_1(number))



# task done!


# 2. იხილეთ ატვირთული ფაილი oscars.txt, რომელშიც მოცემულია ოსკაროსანი საუკეთესო ქალის და მამაკაცის
# შემსრულებელი მსახიობების სია.
# ფაილის თითოეულ სტრიქონზე მოცემულია წელი, მსახიობის სქესი, ასაკი (ოსკარის აღების მომენტში),
# მსახიობის სახელი გვარი და ფილმის დასახელება. აღნიშნული ველები ერთმანეთისგან გამოყოფილია მძიმით.
# დაწერეთ პროგრამა, რომელიც იმუშავებს ამ ფაილთან და შეასრულებს შემდეგ დავალებებს:

# • მომხმარებელს შეაყვანინეთ წელი, იპოვეთ შეყვანილ წელს ოსკაროსნების სახელი
# გვარი და დაბეჭდეთ.

# • დაბეჭდეთ იმ მსახიობის სახელი, გვარი და ასაკი, რომელმაც ყველაზე
# ახალგაზრდამ აიღო ოსკარი.
print()
print()
print()

youngest = ''
age = 100

with open('oscars.txt', 'r') as file:
    year = input('input year:')
    for i in file:
        if age > int(i[7:9]):
            youngest = i
            age = int(i[7:9])

        if year == i[:4]:
            N = i.rfind(',')
            print(i[10:N])

    print()
    result = youngest.rfind(',')
    print('Youngest is', youngest[7:result])

#
#
#
# Account registration
#
print()
print('you must input your password and addres and Then a code(Account Key) will be created '
      'in the file which belongs to your account and you can see it only with the code ')
print()

addres = input('input addres:>')

if addres.__contains__('@gmail.com'):
    i = True
else:
    i = False

addres.strip(' ')

if i == False:
    addres += '@gmail.com'

password = input('input password:>')

from random import randint

with open('Account_Key.txt', 'w') as file:
    file.write(str(randint(100000000, 999999999)))

with open('Account_Key.txt', 'r') as file:
    Account_key = input('input your password to see your account key:')
    if Account_key == password:
        print('your account key is', file.read())
        print('your addres is', addres)
        print('your password is', password)
    else:
        print('Wrong password.')
#
# Task done!
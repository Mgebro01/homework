# Number = int(input('შეიყვანე მებისმირეი რიცხვი 0-100 :'))
#
# if Number > 100 and Number < 0:
#     print('wrong number')
# elif Number >= 0 and Number <= 40:
#     print('Failed')
# elif Number >= 41 and Number <= 50:
#     print('Fx')
# elif Number >= 51 and Number <= 60:
#     print('E')
# elif Number >= 61 and Number <= 70:
#     print('D')
# elif Number >=71 and Number <= 80:
#     print('C')
# elif Number >= 81 and Number <= 90:
#     print('B')
# elif Number >= 91 and Number <= 100:
#     print('A')
#
#

# #  ნაკიანი წლები
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

#
#
# string = input('input string:')
#
# print(len(string))
# #
# #
# #
# string = input('input string:')
#
# string2 = input('input string:')
#
# string3 = string + string2
#
# print(string3)
# #
# #
# string = input('input string:')
#
# count = 0
#
# for i in range(0, len(string)):
#     if "a" == string[i]:
#         count += 1
#
# print(count)
#
# #
#
#
# #
# string = "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების"
# string2 = ''
# count = 0
# for i in range(0, 20):
#     if "ს" == string[i]:
#         count += 1
#     string2 += string[i]
#
# print(count)
# print(string2)
# #
# #
# #
# #
# text = 'Hello, this is example of string. Please, write this text and do some exercises'
# count = 0
# for i in range(len(text)):
#     if " " in text[i]:
#         count += 1
# count += 1
# print(count)
# #
# #
# #
# #
# #
# #
# text = 'Have a nice day.'
# i = len(text)
#
# while i > 0:
#     i -= 1
#     print(text[i])
# #
# #
# #
# #
# text = input('input string')
# count = 0
# for i in range(0, len(text)):
#     if text[i] in 'AaEeIiOoUu':
#         count += 1
#
# print(count)
# #
# #
# #
# #
# #
# #
# n = str(input('input number:'))
# print(len(n))
# #
# #
# #
# #
# #
# name = input('input name:')
# surename = input('input surename:')
# email = name + surename + '@gmail.com'
# print(email)
# #
# #
# #
# #
# #
# #
# #
# text = input('input text')
#
#
#
#
#
#
#
#
# def count(letter, text):
#     c_count = 0
#     for c in text:
#         if c == letter:
#             c_count += 1
#     return c_count
#
# my_text = 'სწავლის ძირი მწარე არის, კენწეროში გატკბილდების'
# max_char = ''
# max_count = 0
#
# for i in my_text:
#     char_count = count(i, my_text)
#
#     if char_count > max_count:
#         max_char = i
#         max_count = char_count
#
# print(max_char, max_count)
#
#
# text = 'გამარჯობა'
# ch = 'რ'
#
# for i in range(len(text)):
#     if ch == text[i]:
#         print(i)
#         break
#
# print(text.find(ch))



# text = '4444444444444hello world'
# print(text)
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.title())
# print(text.strip('4'))
# print(text.startswith('4'))

#
# a = 'hello'
# b = 'world'
# c = f'{a} {b}!'
# print(c)
#
# f_name = input('first name: ')
# l_name = input('last name: ')
#
# inp = input('(1) - gmail.com \n(2) - apple.com \n(3) - students.gov.ge\n> ')
#
# if inp == '1':
#     domain = 'gmail.com'
# elif inp == '2':
#     domain = 'apple.com'
# elif inp == '3':
#     domain = 'students.gov.ge'
# else:
#     domain = 'mail.ru'
#
#
# print(f'{f_name}.{l_name}@{domain}')

# lesson 4

# 3. text ცვლადს მიანიჭეთ სტრიქონი "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების".
# სტრიქონიდან წაიკითხეთ პირველი 20 სიმბოლო და დაბეჭდეთ შედეგი
# . დაითვალეთ რამდენჯერ არის ნახსენები სიმბოლო
#
# print()
# print('3. text ცვლადს მიანიჭეთ სტრიქონი "სწავლის ძირი მწარე არის, კენწეროში გატკბილდების". სტრიქონიდან წაიკითხეთ პირველი 20 სიმბოლო და დაბეჭდეთ შედეგი. დაითვალეთ რამდენჯერ არის ნახსენები სიმბოლო ''. ')
# print()
#
# text = 'სწავლის ძირი მწარე არის, კენწეროში გატკბილდების'
#
# print(text[:20], text[:20].count('ს'))
#
# #
# # 4. შეიყვანეთ სტრიქონი. პატარა ლატინური ასოები შეცვალეთ დიდი ლათინური ასოებით, ხოლო დიდი-პატარათი და გამოიტანეთ შედეგი.
# #
# print()
# print('4. შეიყვანეთ სტრიქონი. პატარა ლატინური ასოები შეცვალეთ დიდი ლათინური ასოებით, ხოლო დიდი-პატარათი და გამოიტანეთ შედეგი.')
# print()
# #
# text = input('input text:')
# new_text = ''
# for i in text:
#     if i == i.upper():
#         new_text += i.lower()
#     else:
#         new_text += i.upper()
#
# print(new_text)

#
# text = input('input text:')
# new_text = ''
# for i in text:
#     if i.isupper():
#         new_text += i.lower()
#     else:
#         new_text += i.upper()
#
# print(new_text)

#
#
# 6. დაწერეთ პროგრამა, რომელშიც მომხარებელს შეაყვანინებთ რაიმე სტრიქონს. პროგრამამ უნდა დაითვალოს დიდი ლათინური ასოების, პატარა ლათინური ასოების და ციფრების რაოდენობა ცალ-ცალკე და დაბეჭდეთ მიღებული შედეგები.
# ასევე დაითვალეთ სტრიქონში გამოყენებული სპეციალური სიმბოლოების რაოდენობა როგორიცაა !@#$%^&*()_+
#
# print()
# print('6. დაწერეთ პროგრამა, რომელშიც მომხარებელს'
#       ' შეაყვანინებთ რაიმე სტრიქონს. პროგრამამ '
#       'უნდა დაითვალოს დიდი'
#       ' ლათინური ასოების, პატარა '
#       'ლათინური ასოების და ციფრების რაოდენობა'
#       ' ცალ-ცალკე და დაბეჭდეთ მიღებული შედეგები. ასევე'
#       ' დაითვალეთ სტრიქონში გამოყენებული სპეციალური'
#       ' სიმბოლოების რაოდენობა როგორიცაა !@#$%^&*()_+')
# print()
#
# symbols = '!@#$%^&*()_+'
# text = input('input text:')
# countupper = 0
# countlower = 0
# countnumber = 0
# countsymbol = 0
#
# for i in text:
#     if i.isupper():
#         countupper += 1
#     if i.islower():
#         countlower += 1
#     if i.isdigit():
#         countnumber += 1
#     if i in symbols:
#         countsymbol += 1
#
# print(countupper)
# print(countlower)
# print(countnumber)
# print(countsymbol)
#
# #
# #
# # 8. შეიყვანეთ ნებისმიერი სტრიქონი. იპოვეთ ყველაზე ხშირად განმეორებადი სიმბოლო და დაბეჭდეთ.
# #
# print()
# print('8. შეიყვანეთ ნებისმიერი სტრიქონი. იპოვეთ ყველაზე ხშირად განმეორებადი სიმბოლო და დაბეჭდეთ.')
# print()
#
# text = input('input text:')
#
# for i in text:
#     text.count(i)

























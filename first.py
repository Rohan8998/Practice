print("Hellow world")
'''
N1 = input("Hello Please Enter 1st Number: ")
N2 = input("Hello Please Enter 2nd Number: ")

Addition =int (N1) + int (N2)
Substraction= int (N1) - int (N2)
Multiply= int (N1) * int (N2)
Division= int (N1) / int (N2)

print("Addition : ", Addition )
print("Substraction : ", Substraction )
print("Multiply : ",Multiply )
print("Division : ",Division )


Firstname = input("Please Enetr First name: ")
Lastname = input ("Please Emter Last name:")
Fullname = Firstname + Lastname

print(f"Hello {Firstname} {Lastname} Welcome to my first Program")
print(f"This my Fullname: {Fullname}")
''' 

S1 = "Tree"
s2 = ""

for char in S1:
    if char not in s2:
        s2 += char     

print(s2)


List = [1,2,3,4,5,6,7,8,9,10,10,10]
list2 = []

for i in List:
    if i % 2 == 0:
        list2.append(i)

print(list2)

unique_list = []
for i in List:
    if i not in unique_list:
        unique_list.append(i)

print(f"List without duplicates: {unique_list}")



names_list = ["Visaero", "QA", "Automation", "QA", "Visaero"]
name2 = []

for i in names_list:
    if i not in name2:
        name2.append(i)

print(f"List without duplicates: {name2}")

def revresestring(String):
    return String[::-1]    


Sring = input ("Please NEter sting: ")
reversed_Sting = revresestring(Sring)
print(f"Reversed string:{reversed_Sting}")

def pallindrom(sring):
    if reversed_Sting == sring:
        print("Pallindrom")
    else:
        print("Not a Pallindrom")

pallindrom(Sring)

def count_character_occurrences(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

occurrences = count_character_occurrences(Sring)
print(f"Character occurrences in '{Sring}': {occurrences}")



def fizzbuzz(num):
    fizzbuzz2 = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz2.append("FizzBuzz")
        elif i % 3 == 0:
            fizzbuzz2.append("Fizz")
        elif i % 5 == 0:
            fizzbuzz2.append("Buzz")
        else:
            fizzbuzz2.append(i)
    return fizzbuzz2


num = int(input("Please ENtger Num: "))
fizzbuzz_list = fizzbuzz(num)
print(fizzbuzz_list)



text= "Programming"

freq ={}

for ch in text:
    freq[ch]=freq.get(ch,0) + 1

print(freq)





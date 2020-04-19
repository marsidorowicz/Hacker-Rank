# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phonebook = []
phonebook_dict = {}
for item in range(n):
    phonebook.append(list(map(str, input().rstrip().split())))
for name, number in phonebook:
    #print(name, number)
    phonebook_dict[name] = number
# for item in input():
#     for i in item:
#         phone_book[name] = phone
# print(n)
# print(phonebook)
# print(phonebook_dict)
try:
    while True:
        item = input().rstrip().split()
        number = phonebook_dict.get(item[0])
        if item[0] in phonebook_dict:
            print(str(item[0])+"="+str(number))
        else:
            print("Not found")
except:
    pass
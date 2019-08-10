numbers = [2, 6, 9, 3, 6]
i = 0
for i in range(len(numbers)):
    num = numbers[i]
    print("Number : {} ".format(num))

print("The first number is {} ".format(numbers[0]))
print("The last number is {} ".format(numbers[-1]))
print("The largest number is {} ".format(max(numbers)))
print("The smallest number is {} ".format(min(numbers)))
print("The average of the numbers is {} ".format(sum(numbers)/len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

name = input("Enter your username : ")

if name in usernames:
    print("Access granted!")
else:
    print("Access denied!")
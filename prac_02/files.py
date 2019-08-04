"""1"""
OUTPUT_FILE = 'name.txt'
out_file = open(OUTPUT_FILE, 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

"""2"""

in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close()
print("Your name is {}".format(name))

"""3"""

num_file = open("numbers.txt", 'r')
num1 = int(num_file.readline())
num2 = int(num_file.readline())
in_file.close()
sum = num1 + num2
print(sum)

"""4"""

num_file = open("numbers.txt", 'r')
sum = 0
for i in num_file:
    num = int(i)
    sum += num
in_file.close()

print(sum)

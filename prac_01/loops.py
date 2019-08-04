for i in range(1, 21, 2):
    print(i, end=' ')
print()

"""a"""

for i in range(0, 110, 10):
    print(i, end=' ')
print()

"""b"""

for i in range(20, 0, -1    ):
    print(i, end=' ')
print()

"""c"""

# num = int(input("Enter a number:"))
# for i in range(num):
#     print("*")

"""d"""

num = int(input("Enter a number:"))

for i in range(num+1):
    for j in range(i):
        print("*", end="")
    print()




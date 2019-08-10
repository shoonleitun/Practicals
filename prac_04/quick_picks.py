import random

num_per_line = 6
max = 45
min = 1

no_of_picks = int(input("How many quick picks ?"))
while no_of_picks <= 0:
    print("Invalid!!")
    no_of_picks = int(input("How many quick picks ?"))

for i in range(no_of_picks):
    quick_picks = []
    for j in range(num_per_line):
        number = random.randint(min, max)
        while number in quick_picks:
            number = random.randint(min, max)
        quick_picks.append(number)
    quick_picks.sort()
    print(" ".join("{:2}".format(number) for number in quick_picks))
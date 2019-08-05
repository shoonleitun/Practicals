
def main():
    score = float(input("Enter score: "))
    print(cal_score(score))


def cal_score(score):

    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

main()
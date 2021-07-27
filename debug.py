import random

def generateRandom(upper):
    """
    :param: upper = number >= 0
    :return: int
    """
    r = random.randint(1, upper)
    return r

def main():

    run = True
    numA = generateRandom(10)
    numB = generateRandom(10)
    result = numA * numB

    while run:
        ans = input(f"What is {str(numA)} X {str(numB)} : ")

        if ans.isdigit():
            if int(ans) == result:
                print("Correct !")
                run = False
            else:
                print("Incorrect, try again !")
        else:
            print("Answer must be a positive number, try again !")

main()

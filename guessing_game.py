from random import randint
smallest_num = int(input("what is the smallest number you can use?? \n"))
largest_num = int(input("what is the largest number you can use?? \n"))
target = randint(smallest_num, largest_num)
num_tries = int(input("how many tries would you like? \n"))

enter_num = 999
count = 0
while count < num_tries:
    print("you have" + str(num_tries-count) + "tries left")
    enter_num = int(input("enter a guess: \n"))
    if enter_num < target:
        print("the entered number is smaller than the target")
    elif enter_num > target:
        print("the entered number is larger than the target ")
    else:
        print("correct!")
        break
    count += 1
if count == num_tries:
    # all guesses are used up!
    print("sorry, the target is " + str(target))
    print("Better luck next time")
else:
    print("great job!!")


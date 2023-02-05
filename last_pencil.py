import random


def jacks_turn(pencils_left):
    if pencils_left == 1:
        return 1
    loosing = [i for i in range(1, pencils_left + 1, 4)]
    if pencils_left in loosing:
        return random.randint(1, 3)
    removing = pencils_left
    while removing not in loosing:
        removing -= 1
    return pencils_left - removing


nb_pencils = input("How many pencils would you like to use:\n")
while True:
    try:
        nb_pencils = int(nb_pencils)
    except ValueError:
        print("The number of pencils should be numeric")
        nb_pencils = input()
    else:
        if nb_pencils <= 0:
            print("The number of pencils should be positive")
            nb_pencils = input()
        else:
            break
name = input("Who will be the first (John, Jack):")
while True:
    if name == "John" or name == "Jack":
        break
    else:
        name = input("Choose between 'John' and 'Jack'")
while nb_pencils > 0:
    print("|" * nb_pencils)
    while True:
        print(name + "'s turn!")
        if name == "John":
            pencils_to_remove = input()
        else:
            pencils_to_remove = str(jacks_turn(nb_pencils))
            print(pencils_to_remove)
        if pencils_to_remove in "123":
            if nb_pencils - int(pencils_to_remove) < 0:
                print("Too many pencils were taken")
                break
            nb_pencils -= int(pencils_to_remove)
            name = "Jack" if name == "John" else "John"
            break
        print("Possible values: '1', '2' or '3'")
print(name + " won!", end="")

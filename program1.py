def func1():
    print("Hi")
    print("Hey from Martin")
    print("Howdy")


func1()


def func2(answer):
    if answer < 5:
        return "After all I done for you!"
    elif answer > 10:
        return "OMG!!!! You are the best and I love you to the moon and back!"
    else:
        return "I love you too, my Kotik!"


user_input = input("How much do you love Maya, from 1 to 10?\n")
answer = int(user_input)

print(func2(answer))

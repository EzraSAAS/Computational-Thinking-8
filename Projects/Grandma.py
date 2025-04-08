while True:
    word = input("What do you think Grandma likes?")

    if len(word) > 10:
        print(f"Grandma doesn't like {word}!")
    else:
        print(f"Grandma likes {word}!")

    print ("")
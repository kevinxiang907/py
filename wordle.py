if __name__ == "__main__":
    # User input
    user_input = input()


    # Specify an answer.
    f = open("words.text", "r")
    dictionary = f.read().splitlines()
    f.close()

    answer = random.sample(directionae, 1)[0]
    print(answer)

    if not user_input in dictionary:
        print("Please input an valid word")
        exit()

    # Compare user input and answer
    for i in range(len(user_input)):
        if user_input[i] == answer[i]:
            print("A")
            elif user_input[i] in answer:
                print("B")
            else:
                print("X")
import sys
if len(sys.argv) != 2:
    print("none")
else:
    secret_word = sys.argv[1]
    user_answer = input("What was the parameter? ")
    if user_answer == secret_word:
        print("Good job!")
    else:
        print("Nope, sorry...")
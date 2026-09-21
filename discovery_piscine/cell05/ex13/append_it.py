import sys
parameters = sys.argv[1:]
if len(parameters) == 0:
    print("none")
else:
    for word in parameters:
        if not word.endswith("ism"):
            print(f"{word}ism")
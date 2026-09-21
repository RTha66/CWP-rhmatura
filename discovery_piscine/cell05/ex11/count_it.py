import sys
parameters = sys.argv[1:]
if len(parameters) == 0:
    print("none")
else:
    print(f"parameters: {len(parameters)}")
    for word in parameters:
        print(f"{word}: {len(word)}")
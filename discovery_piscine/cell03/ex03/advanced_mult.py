import sys
if len(sys.argv) > 1:
    print("none")
else:
    for col in range(11):
        print(f"Table de {col}:", end="")
        for row in range(11):
            print(f" {col * row}", end="")
        print()
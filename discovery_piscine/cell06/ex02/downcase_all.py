import sys

def downcase_it(text):
    return text.lower()
parameters = sys.argv[1:]
if len(parameters) == 0:
    print("none")
else:
    for word in parameters:
        print(downcase_it(word))
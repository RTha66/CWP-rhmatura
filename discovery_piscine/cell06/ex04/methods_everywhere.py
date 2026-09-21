import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    while len(text) < 8:
        text += 'Z'
    print(text)

parameters = sys.argv[1:]

if len(parameters) < 1:
    print("none")
else:
    for word in parameters:
        word_length = len(word)
        
        if word_length > 8:
            shrink(word)
        elif word_length < 8:
            enlarge(word)
        else:
            print(word)
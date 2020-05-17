def translate(phrase):
    translation= ""
    for letter in phrase:
        if letter.upper() in "A,E,I,O,U":
            if letter.isupper():
               translation = translation + "Z"
            else :
                translation = translation + "z"
        else :
          translation = translation + letter
    return translation

print(translate(input("Enter a Phrase: ")))


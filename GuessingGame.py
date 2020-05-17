secret_word = "analyst"
guess = ""
guess_count= 0
guess_limit = 5
out_of_guesses = False

print("Hint: A person who analyzes data (7 letters)")
while guess != secret_word and not (out_of_guesses) :
    if guess_count < guess_limit:
        guess = input("Enter the word : ")
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses , You Lose!")
else:
    print("You WIN!!!")
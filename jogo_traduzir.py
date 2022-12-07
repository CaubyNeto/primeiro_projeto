words = "she goes to work by train"

print(words)

translation = "ela vai para o trabalho de trem"

guess = ""
guess_count = 0
out_of_guesses = False
while guess != translation and not(out_of_guesses):
    if guess_count < 5:
        guess = input("translate that phrase in Portuguese: ")
        guess_count += 1
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("You lose!")
else:
    print("You win!")




guess = ""
secret_word = "giraffe"
guess_count = 0
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < 3:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("You lose!")
else:
    print("You win!")


print("\nmade in 12/nov/2022")
print("\ntraduzido em 07/12/2022")

#guess the number game using python
secret_number=8.0
your_guess=""
guess_counter=0
guess_limit= 4
out_of_guesses = False

while your_guess != secret_number and not out_of_guesses:


    if guess_counter < guess_limit:
       your_guess = float(input("Enter your guess: "))
       guess_counter += 1
       if your_guess > secret_number:
           print("Your guess is too high")
       elif your_guess < secret_number:
           print("Your guess is too low")
    else:
         out_of_guesses = True

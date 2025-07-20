import random
while True:
    print("Welcome to Number Guessing Game")
    lower_bound=int(input("Enter your lower_bound number:-"))
    upper_bound=int(input("Enter your upper_bound number:-"))
    print(f"Your guessing range should be {lower_bound} and {upper_bound}")
    
    secret_number=random.randint(lower_bound , upper_bound)
    
    attempts=10
    while attempts>0:
        guess_number=int(input("Try to guess the number in 10 attempts:-"))
        
        if secret_number> guess_number:
            attempts-=1
            print(f"Too Low!!your remaining attempts are:-{attempts}")
        elif secret_number < guess_number:
            attempts-=1
            print(f"Too High!! your remaining attempts are:-{attempts}")
        elif secret_number==guess_number:
            print(f"You won!! you took total {10-attempts+1} attempts to guess")
            break

    else:
        
        print(f"Oops!! your attempts are over the secret number is:-{secret_number}\n Better luck next time ")
    play_again=input("Do you want to play again yes/no:-").lower()
    if play_again!="yes":
        print("Thank you for playing")
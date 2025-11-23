import random

#list of words

words = ["hello", "friend", "stupid", "papaya", "capsule", "initialise", "giraffe", "switch", "variable", "loser", "winner"]
secret = random.choice(words)
# print(secret)

#pic
stages = [
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / \\
       |
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / 
       |
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  
       |
    """,
    """
       -----
       |   |
       |   O
       |  /|
       |  
       |
    """,
    """
       -----
       |   |
       |   O
       |
       |
       |
    """,
    """
       -----
       |   |
       |
       |
       |
       |
    """,
    """
       
       
       
       
       
    """
]



#display

print("Welcome to the game, answer the word or get HANGED!!")
print()
display = ["_"]*len(secret)
print(" ".join(display))


#lives

lives = 6
print("Lives :", lives)

# sets to track guesses
correct_guesses = set()
wrong_guesses = set()

#functionality

while lives>0:
    guess = input("Guess a letter: ").lower()
    
    # already guessed check
    if guess in correct_guesses or guess in wrong_guesses:
        print("You already guessed that letter!")
        print("Wrong guesses so far:", ", ".join(wrong_guesses))
        continue
    
    
    if guess in secret:
        print("Correct!")
        #update the blank
        for i in range(len(secret)):
            if secret[i] == guess:
                display[i] = guess
    else:
        lives-=1
        print("Wrong")
        wrong_guesses.add(guess)
        print("Lives left:", lives)
     
    print(stages[lives]) 
       
    print(" ".join(display))      #current display
    print("Wrong guesses:", ", ".join(wrong_guesses))
    
    #win
    if "_" not in display:
        print("You win! The word was:", secret)
        break
#loss   
if lives==0:
    print("You lost! The word was :", secret)
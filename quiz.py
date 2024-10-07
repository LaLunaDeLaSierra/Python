# welcoming the participant
print("Welcome to the Trivia Quiz!")

# ask if they want to play
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

# Continuing if yes
print("Okay! Let's play, good luck! :) ")

# initialize score tracker
score = 0 

# first question
answer = input("What is 10^3? ")
if answer == "1000":
     # add point to total score
    score += 1

    print("Correct! Your score is", score)

else:
    print("Incorrect, your score is", score)

# second question
answer = input("How many continents are there in the world? ")
if answer == "7":
     # add point to total score
    score += 1

    print("Correct! Your score is", score)

else:
    print("Incorrect, your score is", score)

# third question
answer = input("Which planet is known as the Red Planet? ")
if answer.lower() == "mars":
     # add point to total score
    score += 1

    print("Correct! Your score is", score)

else:
    print("Incorrect, your score is", score)

# fourth question
answer = input("How many bones are in the human body? ")
if answer == "206":
     # add point to total score
    score += 1

    print("Correct! Your score is", score)

else:
    print("Incorrect, your score is", score)

# fifth question
answer = input("What is the hardest natural substance on Earth? ")
if answer.lower() == "diamond":
     # add point to total score
    score += 1

    print("Correct! You got", score, "questions correct.")

else:
    print("Incorrect, You got", score, "questions correct.")

print("Your score is " + str(score/5 * 100) + "% Thanks for playing!")
import random

numberOfPegs=4
numberOfGuesses=12
numberOfColors=6

ch = ""

for i in range(numberOfPegs):
    ch=ch+str(random.randint(1,numberOfColors))

i = 0
while i < numberOfGuesses:
    ip = input("Guess: ")
    if ip == "end":
        i = numberOfGuesses
    else:
        black = 0
        white = 0
        for j in range(numberOfPegs):
            if ip[j]==ch[j]:
               black=black+1
            else:
                con=True
                for c in ch:
                    if ip[j]==c and con:
                        white=white+1
                        con=False
        if black == numberOfPegs:
            print("You Win")
            i = numberOfGuesses
        else:
            print("black: " + str(black) + " white: " + str(white))
    i = i + 1
if i == numberOfGuesses:
    print("You Lose. The answor was " + ch + ".")

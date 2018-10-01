import random

ch = ""

for i in range(0,4):
    ch=ch+str(random.randint(1,6))

i = 0
while i < 12:
    ip = input("Guess: ")
    if ip == "end":
        i = 12
    else:
        black = 0
        white = 0
        for j in range(0,4):
            if ip[j]==ch[j]:
               black=black+1
            else:
                for c in ch:
                    if ip[j]==c:
                        white=white+1
        if black == 4:
            print("You Win")
            i = 12
        else:
            print("black: " + str(black) + " white: " + str(white))
    i = i + 1
if i == 12:
    print("You Lose. The answor was " + ch + ".")

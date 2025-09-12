import random
import math
z=0
spela=True
försök=int(input("Hur många försök tror du det tar för dig att gissa ett slumpessig tal mellan 1.10 skriv ett heltal "))
x=random.randint(1,10)
while spela == True:
    y=int(input("Vilket tal tror du det är, välj ett heltal mellan 1 till 10  "))
    if x==y:
        print("Wow du är så cool för att du vann!!!!!!!")
        z+=1
        print("du gissade ",z," gånger")
        print("Din gissning var" ,abs(försök - z), "ifrån hur många det faktiskt tog")
        spela=False
    elif x<y:
        print("Du är sämst du fick fel haha, nu måste du gissa igen. Du gissade för högt ")
        z+=1
    elif x>y:
        print("Du är sämst du fick fel haha, nu måste du gissa igen. Du gissade för lågt ")
        z+=1

    if spela == False:
        si=input("Vill du spela igen, svara ja eller nej ")
        if si == "ja":
            z=0
            x=random.randint(1,10)
            försök=int(input("Hur många försök tror du det tar för dig att gissa ett slumpessig tal mellan 1.10 skriv ett heltal "))
            spela = True

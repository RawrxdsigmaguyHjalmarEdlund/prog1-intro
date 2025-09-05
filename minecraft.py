import random
name = input("skriv ditt namn ") #Spelarens namn är en string
pl = 100 #Spelarens hälsa är en integer
zl = 100 #Zombiens hälsa är en integer
spela=True 
while spela==True:
    pl -= random.randint(1,10) #Ett slumpmässigt nummer mellen 1,10 som är en integer.
    zl -= random.randint(1,10) #integer
    if zl <= 0:
        print(name," vann") #string
        spela=False
    elif pl <= 0:
        print(name," förlorade")
        spela=False
    print(name," har ",pl," hp kvar och zombie har ",zl, "hp kvar.") #String
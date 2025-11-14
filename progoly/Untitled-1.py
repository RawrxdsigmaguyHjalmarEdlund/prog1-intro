import math
n=int(input("Hur många bilar har Anna, minst 1. "))
m=int(input("Hur många bildäck har Simon, max 100. "))
x=n*4
if (m-x%m)>x:
    print(n)
else:
    y=(m-x%m)/4
    print(y)
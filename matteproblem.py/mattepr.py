
try:
    x=float(input("skriv ett nummer "))
    for y in range (1, 11):
        print(x*y)

except ValueError:
    print("Felaktig information")
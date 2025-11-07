run = True
bag = []
print("Välkommen till påsen 🎒")
max=10
while run:
    print("Visa innehållet i påsen [V]")
    print("Spara i påsen [S]")
    print("Sök efter något i påsen [F]")
    print("Ta bort något ur påsen [R]")
    print("Avsluta programmet [Q]")
    choice = input("Välj: ")
    if choice.lower() == "v":
        items=sorted(bag)
        print(items)
    elif choice.lower() == "s":
        if len(bag) >= max:
            print(f"Påsen är full — max {max} saker (T_T)")
        else:
            bag.append(input("Skriv vad du vill spara (￣▽￣)"))
    elif choice.lower() == "q":
        run = False
    elif choice.lower() == "f":
        query=input("vad vill du söka efter ^3^")
        if query.lower() in bag:
            print(f"Hittade: {query} i påsen")
    elif choice.lower() == "r":
        bag.remove(input("Skriv vad du vill ta bort >_<"))
    else:
        print("Felaktigt kommando, försök igen.🤬🤬🤬🤬🤬🤬")
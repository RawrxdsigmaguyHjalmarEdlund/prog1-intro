run = True
bag = []
print("\033[92mVälkommen till påsen 🎒")
max=10
while run:
    print("\033[92mVisa innehållet i påsen [V]")
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
            print(f"\033[91mPåsen är full — max {max} saker (T_T)")
        else:
            bag.append(input("\033[92mSkriv vad du vill spara (￣▽￣)"))
    elif choice.lower() == "q":
        run = False
    elif choice.lower() == "f":
        query=input("\033[92mvad vill du söka efter ^3^")
        if query.lower() in bag:
            print(f"\033[92mHittade: {query} i påsen")
    elif choice.lower() == "r":
        bag.remove(input("\033[92mSkriv vad du vill ta bort >_<"))
    else:
        print("\033[91mFelaktigt kommando, försök igen.🤬🤬🤬🤬🤬🤬")
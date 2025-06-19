contacts = {}
while True:
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.Display")
    print("4.Exit")
    choice = input("Enter a choice:")
    if choice == "1":
        name = input("enter a name:")
        ph = input("enter a number:")
        contacts[name] = ph
        print("contact added")
    elif choice == "2":
        name = input("enter a name to search:")
        if name in contacts:
            print("number:",contacts[name])
        else:
            print("contact not found")
    elif choice == "3":
        for name, number in contacts.items():
            print(name,":",number)
    elif choice == "4":
            break  
    else:
            print("invalid choice")
              
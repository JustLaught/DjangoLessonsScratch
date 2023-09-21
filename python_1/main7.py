import json

def print_menu():
    print("\n1. Load data","2. Save data", "3. Add value", "4. Delete value", "5. Show data", "0. Exit", sep="\n")

data = []
while True:
    print_menu()
    choice = int(input("\nEnter your option : "))
    print()
    if choice == 1:
        try:
            with open('Data', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open('Data', 'w') as f:
                pass
    
    if choice == 2:
        with open('Data','w')as f:
            json.dump(data,f)

    if choice == 3:
        rangeN = int(input("Enter amount of values: "))
        for i in range(rangeN):
            data.append(int(input("Enter number: ")))

    if choice == 4:
        rangeN = int(input("Enter amount of values: "))
        for i in range(rangeN):
            data.remove(int(input("Enter number to delete:  ")))

    if choice == 5:
        print(data)
        print()

    if choice == 0:
        break
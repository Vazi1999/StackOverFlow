from fetch import *

def main():
    print("Would you like to run test on a script or write an error yourself ?\n")
    print("Please enter 0 for a script and 1 for a write error  ")
    choice = int(input())
    if choice == 0:
        print("Enter locaition of the script to test")
        script = input()
        fetch_stackoverflow(choice,script)
    elif choice == 1:
        print("Please enter the problem")
        problem = input()
        fetch_stackoverflow(choice,problem)
    else:
        print("Wrong input , exiting...")
        exit(1)

if __name__ == "__main__":
    main()






print("Would you like to run test on a script or write an error yourself ?\n")
print("Please enter 0 for a script and 1 for a write error  ")
choice = int(input())
if choice == 0:
    print("Enter locaition of the script to test")
    script = input()
    #call fetch_stackoverflow
elif choice == 1:
    print("Please enter the problem")
    problem = input()
    #call fetch_stackoverflow
else:
    print("Wrong input , exiting...")
    exit(1)





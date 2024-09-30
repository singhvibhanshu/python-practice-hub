while True:
    num = input("Enter the number: ")
    try:
        if float(num) % 2.0 == 0.0:
            print("Even Number")
            break
        else:
            print("Odd Number")
            break
    except:
        print("Invalid Input. Try Again.")
while True:
    temp_c = input("Enter the temperature in Celsius: ")
    try:
        temp_f = (float(temp_c) * (9/5)) + 32.0
        print("Temperature in Fahrenheit: ",  temp_f)
        break
    except:
        print("Invalid Input. Try Again.")
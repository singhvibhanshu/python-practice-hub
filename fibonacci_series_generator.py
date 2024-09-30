def f_series_gen():
    while True:
        num = input("Enter the number of terms you want to see in the Fibonacci Series: ")
        try:
            check = int(num)
            if check <= 0:
                print("Invalid Input! Must be greater than 0")
                break
            elif check == 1:
                print("[0]")
                break
            elif check == 2:
                print("[0, 1]")
                break
            else:
                series = [0, 1]
                for x in range(2, check):
                    next_value = series[-1] + series[-2]
                    series.append(next_value)
                print(series)
                break
        except:
            print("Invalid Input. Try Again.")



f_series_gen()
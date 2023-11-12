def check(s: str) -> None:
    try:
        n = int(s)
    except ValueError:
        print("It is not a number!")
    else:
        if n < 202:
            print("There are less than 202 apples! You cheated me!")
        else:
            print(n)
        

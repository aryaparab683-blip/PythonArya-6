def getNumber():
    return int(input("Enter a number: "))

def checkEvenOdd(num):
    return bool(num % 2 )
#def checkEvenOdd(num):
"""return bool
def """
def pCheck(num):
    if checkEvenOdd(num):
        print(f"{num} - Odd")
    else:
        print(f"{num} - Even")

def main():
    n = getNumber()
    for _ in range(n+1):
        pCheck(_)

if __name__ == "__main__":
    main()
    #find a factorial using modular approach (name of the function is get factorial)
    #count number of digits 
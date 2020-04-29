
def main():
    msg = "This program will take a number and change last 2 digits to zero if is greater than 99."
    msg = msg + "\n Otherwise, the number will be returned without any particular change."
    print(msg)
    strAmount = input("Please type in your amout: ")

    if int(strAmount) > 99:
      print(f"New Number is:  {strAmount[:-2]}00")
    else:
      print(f"The Number remained the same: {strAmount} ")

if __name__ == "__main__":
    main()

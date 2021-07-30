# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


scores_dict = {
    1: "Failed",
    2: "Very Poor",
    3: "Poor",
    4: "Good",
    5: "Very Good",
    6: "Excellent"
}

try:
    grade = int(input("Enter Score: "))
    result = ""

    if grade < 40:
        result = scores_dict[1]
    elif grade >= 40 and grade <= 44:
        result = scores_dict[2]
    elif grade > 44 and grade <= 49:
        result = scores_dict[3]
    elif grade > 49 and grade <= 59:
        result = scores_dict[4]
    elif grade > 59 and grade <= 69:
        result = scores_dict[5]
    elif grade > 69 and grade <= 100:
        result = scores_dict[6]
    elif grade > 100:
        raise ValueTooLargeError
    else:
        print(f"The provided Grade is invalid. Please try again later.")
        quit()

except ValueError:
    print(f"Error! Only integer numbers are allowed. Please try again later.")
    quit()

except ValueTooLargeError:
    print("Invalid Grade. This value is too large, Please try again!")
    quit()

else:
    print(f"Your Final Score for a grade of {grade} is {result.upper()}.")

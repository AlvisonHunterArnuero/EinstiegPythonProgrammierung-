# --------------------------------------------------------------------------------
# Calculate Sales commision for sales received by a salesperson
# Made with ❤️ in Python 3 by Alvison Hunter - October 16th, 2021
# JavaScript, Python and Web Development tips at: https://bit.ly/3p9hpqj
# --------------------------------------------------------------------------------

class CalculateCommission:
    def __init__(self, name, amount_sales, class_type):
        self.name = name
        self.amount_sales = amount_sales
        self.class_type = class_type
        self.commision_received = 0


    def displayCalculations(self):
        print(f"Name: {self.name}")
        print(f"Amount Of Sales: {self.amount_sales}")
        print(f"Class Type: {self.class_type}")
        print(f"Commission Received: {self.commision_received}")


    def calculateCommission(self):
        if(self.class_type==1):
            print("Class 1")
        elif():
            print("Class 2")
        elif():
            print("Class 3")
        else:
            print("No Class")
            
        print(f"\nGood bye for now, {self.name}.")


Employee_01 = CalculateCommission("Declan Hunter",4, 2)


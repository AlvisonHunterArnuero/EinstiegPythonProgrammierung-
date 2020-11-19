# This routine simulates a rustic invoice process in which the user will be prompted
# to enter quantity, description and unit price of a certain product and once all products
# have been entered, the routine will return the total due for this purchase.
# Made with ❤️ in Python 3 by Alvison Hunter - November 17th, 2020
def main():
    # I will store on this list the elements being entered by the user
    lst_details = []
    lst_final = [['Quantity', 'Description','Unit Price','Line Total']]
    #sub total sum of all of the entered elements will be stored here
    sub_total = 0
    # This is an optional charge, however, in this routine I will add it
    value_added_tax = 0.18
    #last but not least, let's add a divider on this code for aesthetic purposes
    title_sep = "══════════════════════════════════════════════════════════════════════"
    table_sep = "______________________________________________________________________"

    # As usual, I add try and catch error handling to make sure I am covered
    try:
        exit_out = 'n'
        # Inform the user what this routine does and how to exit out when needed to
        print(title_sep)
        program_description_lst = ["The Royal Acme Supermarket - Products Invoice", "Please enter quantity, description & unit price for each product.", "When you are ready to check out, please type in [y] when prompted."]
        for s in program_description_lst:
            print(s.center(70, ' '))

        #let's close the main title o'er here, fellows.
        print(title_sep)

        while exit_out != 'y' or exit_out =="":
            # let's capture quantity as float & add it to the list
            quantity = float(input("Enter Quantity: \n"))
            lst_details.append(str(quantity))
            #product can be passed as string, no problemo!
            product_description = input("Product Description: \n")
            lst_details.append(product_description)
            # unit price should be added to the list as float type as well
            unit_price = float(input("Enter Unit Price: \n"))
            lst_details.append(str(unit_price))
            # calculate line total and add it to the list as well
            line_total = round(quantity*unit_price, 2)
            # let's add line total to the sub total var
            lst_details.append(str(line_total))
            # now be will add the value of line total to the sub total
            sub_total = sub_total +line_total
            # let's extend the list of lists to print these elements in a table
            lst_final.append(list(lst_details))
            #clear the details list for further use in another loop
            lst_details.clear()
            # let us ask users if they would like to proceed to pay now
            exit_out = input("Would you like to proceed with the payment (y/n)? \n").lower()

        # now, this is the line in where I handle the errors on this routine
    except:
        print("Uh oh! Something went really wrong!")
        quit
        # if all went well, the time has come to print the results
    finally:
        print(table_sep)
        # Find maximal length of all elements in list
        n = max(len(x) for l in lst_final for x in l)
        # Print the rows
        for row in lst_final:
            print(''.join(x.ljust(n+6) for x in row))

        print(table_sep)
        # don't forget to add the sub total of these elements in the screen
        print("Sub Total: {:.2f}".format(sub_total).rjust(70))
        tax = sub_total * value_added_tax
        total_due = sub_total + tax
        # Now that ugly tax that we all hate, we need to reflect it here as well
        print("Value Added Tax: {:.2f}".format(tax).rjust(70))
        print(table_sep)
        # time to tell the customer how much it has to be paid for this purchase.
        print("Total Due: {:.2f}".format(total_due).rjust(70))

        # Adding tab & joining elements to be ready for printing as table
        print("""
Thank you for your purchase from Royal Acme Supermarket.
Please let us know if we can do anything else to help!'
""")



if __name__== "__main__":
    main()

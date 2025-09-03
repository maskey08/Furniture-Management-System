import read
import write
import datetime

# Initialize 'all_item_data' as an empty dictionary to store product details
all_item_data = {}

# Call fetching_data from read.py
read.fetching_data(all_item_data)

def calculate_widths():
    """Calculate column widths based on item data and returns widths of each column and total width."""
    
    #Initializing column widths with default widths
    default = [1, 12, 12, 9, 5]

    # Determining maximum widths using max function
    for value in all_item_data.values():
        # Calculates maximum length of Manufacturer
        default[1] = max(default[1], len(value[0]))
        
        # Calculates maximum length of Product Name
        default[2] = max(default[2], len(value[1]))
        
        # Calculates maximum length of Quantity
        default[3] = max(default[3], len(str(value[2])))
        
        # Calculates maximum length of Price
        default[4] = max(default[4], len(str(value[3])))

    # Calculates ID column width
    default[0]=max(default[0],len(str(max(all_item_data.keys()))))
    
    # Determining final column widths 
    headers=[
        default[0] + 5,
        default[1] + 8,
        default[2] + 4,
        default[3] + 8,
        default[4] + 12
    ]

    return headers

    
def display_items():
    """Displays all available furniture in a proper tabular format."""
    
    # Printing welcome message
    print("\n-----------------------------------------|Welcome To BRJ Furniture Management System|------------------------------------------\n")
    print("List of Available Furnitures:")

    # Calling calculate_widths function to compute the column widths
    headers = calculate_widths()

    # Initializing 'out_of _stock' to 0 
    out_of_stock = 0
    
    # Constructing a border line of a table dashes based on headers and printing where needed
    bline=(
        '+' + '-' * (headers[0]) +
        '+' + '-' * (headers[1]) +
        '+' + '-' * (headers[2]) +
        '+' + '-' * (headers[3]) +
        '+' + '-' * (headers[4]) +
        '+' + '-' * 20 +
        '+'
    )
    print(bline)
    
    # Constructing and printing the table header with appropriate spacing
    print("| ID" + " " * (headers[0] - 3) +  # Adjusting space for ID
          "| Manufacturer" + " " * (headers[1] - 13) +  # Adjusting space for Manufacturer
          "| Product Name" + " " * (headers[2] - 13) +  # Adjusting space for Product Name
          "|" + " " * (headers[3] - 10) + " Quantity |" +  # Adjusting space for Quantity
          " " * (headers[4] - 7) + " Price |" +  # Adjusting space for Price
          "       Status       |")
    
    # Printing border line
    print(bline)

    # Printing rows whose quantity is greater than 0
    for key, value in all_item_data.items():
        if value[2] > 0:
            print("|", str(key) + " " * (headers[0] - 2 - len(str(key))),
                  "|", value[0] + " " * (headers[1] - 2 - len(value[0])),
                  "|", value[1] + " " * (headers[2] - 2 - len(value[1])),
                  "|", " " * (headers[3] - 2 - len(str(value[2]))) + str(value[2]),
                  "|", " " * (headers[4] - 2 - len(str(value[3]))) + str(value[3]),
                  "|      In Stock      |")
        else:
            print("|", str(key) + " " * (headers[0] - 2 - len(str(key))),
                  "|", value[0] + " " * (headers[1] - 2 - len(value[0])),
                  "|", value[1] + " " * (headers[2] - 2 - len(value[1])),
                  "|", " " * (headers[3] - 2 - len(str(value[2]))) + str(value[2]),
                  "|", " " * (headers[4] - 2 - len(str(value[3]))) + str(value[3]),
                  "|    Out of Stock    |")
            out_of_stock += 1

    # Printing border line
    print(bline)

    # Printing number of products that are out of stock
    print("Out of Stock:", out_of_stock, "product(s)")
    
                
def ordering():
    """
    Facilitates product ordering and invoicing process.
    Updates product quantities in the `all_item_data` dictionary and records orders in a list.
    Displays appropriate error messages for invalid inputs.
    """
    x = True # Flag to control the while loop
    employee_name, number = person_detail()
    orders = [] # Initializing list to store orders
    while x == True:
        try:
            # Prompt for product ID
            product_id = int(input("Enter Product ID:"))

            # Check if the product ID exists in the all_item_data dictionary
            if product_id in all_item_data.keys():
                while True:
                    try:
                        # Prompt for quantity of the selected product
                        print("How many '", all_item_data[product_id][1], "' do you want to order from ", all_item_data[product_id][0], "?")
                        quantity = int(input(">> "))
                        
                        if quantity > 0:
                            # Update the quantity in all_item_data and record the order
                            all_item_data[product_id][2] += quantity
                            orders.append([product_id, quantity])
                            
                            while True:
                                # Prompt for further actions
                                ask = input("Do you want to order another furniture item?[y/n]\n>>").lower()
                                if ask == 'y':
                                    x = True # Continue ordering
                                    break
                                
                                elif ask == 'n':
                                    # Generate invoice, save changes, and finalize order
                                    print(generate_invoice(employee_name, number, orders, 1))
                                    write.save_changes(all_item_data)
                                    input("Press Enter to continue...")
                                    x = False # Exit the ordering loop
                                    break
                                
                                else:
                                    # Calling ask_error to print error message 
                                    ask_error()
                                    
                            break
                        
                        else:
                            # Print error message for invalid quantity 
                            print("\n +------------------------> !PRODUCT QUANTITY ERROR! <--------------------------+")
                            print(" | Not enough quantity! Please choose a larger quantity that is greater than 0. |")
                            print(" +------------------------------------------------------------------------------+")
                            input("Press Enter to continue...")
    
                    except:
                        # Calling value_error to print error message
                        value_error()
                        
            else:
                # Calling id_match_error to print error message
                id_match_error(product_id)
                
        except:
            # Calling value_error to print error message
            value_error()
        

def selling():
    """
    Facilitates the process of selling products to a customer and generating invoices.
    Updates product quantities in the `all_item_data` dictionary and records sales in a list.
    Displays appropriate error messages for invalid inputs.
    """
    x = True  # Flag to control the while loop
    customer_name, number = person_detail()
    orders = []  # List to store orders
    
    while x == True:
        try:
            product_id = int(input("Enter Product ID:"))  # Prompt for product ID
            
            # Check if the product ID exists in the all_item_data dictionary
            if product_id in all_item_data.keys():
                if all_item_data[product_id][2] == 0:
                    # Print error message for product out of stock
                    print("\n +---------------------------------> !PRODUCT OUT OF STOCK! <--------------------------------+")
                    print(" | Unfortunately the product you are selling is Out of Stock. Please choose another product. |")
                    print(" +-------------------------------------------------------------------------------------------+")
                    input("Press Enter to continue...")
                else:
                    while True:
                        try:
                            # Prompt for quantity of the selected product to sell
                            print("How many '" + all_item_data[product_id][1] + "' from " + all_item_data[product_id][0] + " do you want to sell to " + customer_name + "?")
                            quantity = int(input(">> "))    
                            
                            # Validates quantity against available stock and check it's greater than 0
                            if all_item_data[product_id][2] >= quantity and quantity > 0:
                                # Updates the quantity in all_item_data and record the sale
                                all_item_data[product_id][2] -= quantity
                                orders.append([product_id, quantity])
                                
                                while True:
                                    # Prompt for further actions 
                                    ask = input("Do you want to sell another furniture item?[y/n]\n>>").lower()
                                    
                                    if ask == 'y':
                                        x = True  # Continue selling
                                        break
                                    elif ask == 'n':
                                        # Generates invoice, save changes, and finalizes sale
                                        print(generate_invoice(customer_name, number, orders, 2))
                                        write.save_changes(all_item_data)
                                        input("Press Enter to continue...")
                                        x = False  # Exit the selling loop
                                        break
                                    else:
                                        # Calling ask_error function to handle invalid input 
                                        ask_error()
                                
                                break
                                
                            else:
                                # Print error message for invalid quantity or insufficient stock
                                print("\n +-------------------------> !PRODUCT QUANTITY ERROR! <--------------------------+")
                                print(" | Not enough quantity! Please choose a smaller quantity that is greater than 0. |")
                                print(" +-------------------------------------------------------------------------------+")
                                input("Press Enter to continue...")
                                
                        except:
                            # Calling value_error to print error message
                            value_error()

            else:
                # Handles error if product ID does not match any keys in all_item_data
                id_match_error(product_id)
        
        except:
            # Handles exception if input cannot be converted to an integer
            value_error()


def shipping():
    """Asks shipping address and returns shipping details"""
    
    while True:
        # Display shipping location options
        print("\nPlease select your shipping address:")
        print("1. Inside Kathmandu Valley")
        print("2. Outside Kathmandu Valley")
        print("3. No Shipping Required")

        try:
            # Prompt user for input and convert it to an integer
            location = int(input("Enter the corresponding number (1 or 2 or 3) to select your shipping location: "))
            
            # Check shipping address and assign dtype and scost, handles invalid input
            if location == 1:
                dtype = "Inside Kathmandu Valley"
                scost = 100.0
                break 
            elif location == 2:
                dtype = "Outside Kathmandu Valley"
                scost = 250.0
                break
            elif location == 3:
                dtype = "No Shipping Required"
                scost = 0
                break
            else:
                print("\n +--------------------------------------------> !INVALID CHOICE! <-------------------------------------------+")
                print(" | Entered Shipping Address: '", location, "' failed to match! Please select one of the provided options (1, 2, or 3). |")
                print(" +-----------------------------------------------------------------------------------------------------------+")
                input("Press Enter to continue...")     
        except:
            # Calling value_error
            value_error()
    return dtype, scost

def invoice_records(orders):
    """
    Generates formatted invoice records based on the orders provided.
    Accepts orders list as parameter.
    Calculates total width, tmax, invoice rows and total amount
    Returns headers, tmax, row, width, total (as tuple).
    """

    # Calculate the maximum width of the 'Total' column
    tmax = 4
    for rows in orders:
        tmax = max(tmax, len(str(all_item_data[rows[0]][3] * rows[1])))

    # Calling calculate_widths for header lengths
    headers = calculate_widths()

    # Calculate total width
    width = tmax + 11
    for each in headers:
        width += each
    
    # Initialize variables to store ordered products in row format and calculate total amount
    total = 0
    row = ""
    
    # Iterate through each order to format rows and calculate totals
    for rows in orders:
        row += (
            " " + str(rows[0]) + " " * (headers[0] - len(str(rows[0]))) +  # Product ID
            all_item_data[rows[0]][0] + " " * (headers[1] - len(all_item_data[rows[0]][0])) +  # Manufacturer
            all_item_data[rows[0]][1] + " " * (headers[2] - len(all_item_data[rows[0]][1])) +  # Product Name
            " " * (headers[3] - len(str(rows[1]))) + str(rows[1]) +  # Quantity
            " " * (headers[4] - len(str(all_item_data[rows[0]][3]))) + str(all_item_data[rows[0]][3]) +  # Price
            " " * (tmax + 8 - len(str(all_item_data[rows[0]][3] * rows[1]))) + str(all_item_data[rows[0]][3] * rows[1]) + "\n"  # Total
        )
        total += (all_item_data[rows[0]][3] * rows[1])  # Accumulate total amount

    return headers, tmax, row, width, total



def generate_invoice(name,number, orders,transaction_type):
    """
    Generates an invoice for either an order or sale transaction.
    Accepts name of the employee or customer depending on the transaction type.
    Accepts orders, transaction_type(1 or 2)
    Returns invoice content formatted as a string.
    Assignes unique name to store each file.
    Constructs and saves the invoice as a .txt file using `write.save_invoice`.
    """
    
    # Create a unique file name/invoice number using datetime
    date = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(datetime.datetime.now().day)
    time = str(datetime.datetime.now().hour) + ":" +  str(datetime.datetime.now().minute) + ":" + str(datetime.datetime.now().second)

    # Retrieve invoice details
    headers, tmax, invoice_rows, width, total = invoice_records(orders)

    # Calculate VAT amount (13%)
    vat_amount = 0.13 * total

    # Determine file name and labels based on transaction type
    if transaction_type == 1:
        file_name = "Order_" + date.replace("-", "") + "_" + time.replace(":", "") + "_" + name + ".txt"
        name_label = "Employee"
        column2 = " Manufacturer" + " " * (headers[1] - 12)
    else:
        file_name = "Sale_" + date.replace("-", "") + "_" + time.replace(":", "") + "_" + name + ".txt"
        name_label = "Customer"
        column2 = " Brand" + " " * (headers[1] - 5)
    
    # Retrieve shipping details
    dtype, scost = shipping()
    
    # Construct invoice content as a one string using '+' operator
    invoice_content = ("\n" + "*" * width + "\n" + " " * int((width / 2) - 9) +
                        "BRJ Furniture Store\n" + " " * int((width / 2) - 4) +
                        "INVOICE\n\n Invoice No.       : " + date.replace("-", "") + "_" + time.replace(":", "") +
                        "\n Date              : " + date +
                        "\n Time              : " + time +
                        "\n " + name_label + " Name     : " + name +
                        "\n Phone Number      : " + number +
                        "\n Shipping Address  : " + dtype +
                        "\n" + "-" * width + "\n" +
                        " ID" + " " * (headers[0] - 3) +
                        column2 +
                        "Product Name" + " " * (headers[2] + headers[3] - 20) +
                        "Quantity" + " " * (headers[4] - 5) +
                        "Price" + " " * (tmax + 3) +
                        "Total\n\n" +
                        invoice_rows +  
                        "=" * width +
                        "\n Sub Total     : $" + str(total) + "\n" +
                        " VAT(13%)      : $" + str(vat_amount) + "\n" +
                        " Shipping cost : $" + str(scost) + "\n" +
                        " Grand Total   : $" + str(total + vat_amount + scost) + "\n" +
                        "-" * width + "\n" +
                        " " * int((width / 2) - 6) + "-THANK YOU-\n" +
                        "*" * width)
                            
    # Save invoice as a .txt file
    write.save_invoice(file_name, invoice_content)

    print("\n\nGenerating invoice...")
    return invoice_content

def person_detail():
    X = True    # Flag for name while loop
    Y = True    # Flag for number while loop
    
    # List containing a-z and a space 
    checklist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    
    while X:
        name = input("Enter Name of Purchaser: ").lower()   # Prompt for user name
        validity = True # Initializing validity for checking

        # Iterating through every character in the input string and checks if each character is not in the list
        for letter in name:
            if letter not in checklist:
                validity = False
                break  # Terminates for-loop if any letter is not in the list

        # Check if input string is valid or not and displays a suitable message 
        if validity:
            X = False  # Exit while-loop
        else:
            # Prints error message
            print("\n +-----------------------------> !ValueError! <------------------------------+")
            print(" |  WARNING: Invalid Input! Please do not enter a 'number' in given prompt.  |")
            print(" +---------------------------------------------------------------------------+")
            input("Press Enter to continue...")
            
    while Y:
        phone = input("Enter phone number: ")   # Prompt for phone number

        # Check if phone number is 10 digit
        if len(phone) == 10:
            validity = True  # Initializing validity for checking

            # Iterating through every digit of input and checks if digit is in list
            for digit in phone:
                if digit in checklist:
                    validity = False
                    break  # Terminates for-loop

            # Check if input string is valid or not and displays a suitable message 
            if validity:
                Y = False
            else:
                print("\n +-----------------------------> !ValueError! <------------------------------+")
                print(" |  WARNING: Invalid Input! Please do not enter a 'letter' in given prompt.  |")
                print(" +---------------------------------------------------------------------------+")
                input("Press Enter to continue...")
                
        else:
            print("\n +-------------------------------> !ValueError! <--------------------------------+")
            print(" |  WARNING: Invalid Input! Please enter 10 digit phone number in given prompt.  |")
            print(" +-------------------------------------------------------------------------------+")
            input("Press Enter to continue...")
  
    return name, phone

def value_error():
    """Displays a warning message for invalid input and prompts the user to continue."""
    
    print("\n +--------------------------------> !ValueError! <---------------------------------+")
    print(" |  WARNING: Invalid Input! Please enter a 'number' from the options given above.  |")
    print(" +---------------------------------------------------------------------------------+")
    input("Press Enter to continue...")

def ask_error():
    """Displays a warning message for invalid choice and prompts the user to continue."""
    
    print("\n +-------------------------------------------------> !INVALID CHOICE! <-----------------------------------------------------+")
    print(" | WARNING: Input match failed! Please only enter 'y' to add/order another product OR 'n' to checkout and generate invoice. |")
    print(" +--------------------------------------------------------------------------------------------------------------------------+")
    input("Press Enter to continue...")

def id_match_error(product_id):
    """Displays an error message when the entered product ID does not match any product's ID."""
    
    print("\n +--------------------------------------------> !ProductIdMatchError! <-------------------------------------------+")
    print(" |   Entered product Id: '",product_id,"' did not match any products. Please enter a valid product ID from the below table. |")
    print(" +----------------------------------------------------------------------------------------------------------------+")
    input("Press Enter to continue...")

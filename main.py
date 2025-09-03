import operations

'''
Main Code for BRJ Furniture management system that loops continuously until user wants to exit.
Imported operations.py
Takes input from user, and calls function(s) from operation.py.
Handles input errors and ValueError Exception.
'''
while True:
    try:
        # Call display_items function to display available items from operations.py
        operations.display_items()

        # Prompt user for transaction/operation type
        transaction_type=int(input("\nType '1' to Order from Manufacturer\nType '2' to Sell to Customer\nType '0' to Exit Program\n>>"))

        if transaction_type == 1:
            operations.ordering() # Call function for ordering from manufacturer
            
        elif transaction_type == 2:
            operations.selling() # Call function for selling to customer
            
        elif transaction_type == 0:
            print("terminating program...")
            break # Exit loop and terminate program
        
        else:
            # Display error message for invalid transaction type
            print("\n +---------------------------------------------> !INVALID CHOICE! <----------------------------------------------+")
            print(" | Entered transaction type: '",transaction_type,"' failed to match! Please select one of the provided options (0 or 1 or 2). |")
            print(" +---------------------------------------------------------------------------------------------------------------+")
            input("Press Enter to continue...") # Wait for user input to continue after error message
            
    except:
        # Calls value_error to handle ValueError by displaying an error message
        operations.value_error()
 
# Final exit message 
print("PROGRAM HAS BEEN EXITED.")

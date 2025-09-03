def save_changes(all_item_data):
    """
    Save the changes made to all_item_data dictionary back to the .txt file.
    Takes dictionary with IDs as keys and a list with 'manufacturer, product, quantity, price' as values.
    """

    # Open 'main.txt' in write mode
    with open("main.txt", "w") as writing:
        # Iterate through each key-value pair in all_item_data
        for key,value in all_item_data.items():
            # Format the data as string and write to the file
            updated = str(key) + ', ' + value[0] + ', ' + value[1] + ', ' + str(value[2]) + ', ' + str(value[3]) + '\n'
            writing.write(updated)
    print("\n")

def save_invoice(file_name,invoice_content):
    """Creates new file and opens in write mode. Invoice content is written in the .txt file with unique naming."""

    # Open file_name in write mode
    with open(file_name,"w") as file:
        # Write invoice_content into the file
        file.write(invoice_content)
    
        
    

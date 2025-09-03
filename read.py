#reads main.txt file and stores each line in dictionary format which is assigned to a list for easy access
def fetching_data(all_item_data):
    """
    Retrieves data from a file and updates the all_item_data dictionary.
    Takes all_item_data as parameter to store the fetched data.
    """
    try:
        # Open 'main.txt' in read mode
        with open("main.txt","r") as file:
            for item in file:
                # split the line by ', ' and puts it in a list
                item_data = item.split(', ')

                # Assign first element(Id) as key
                key = int(item_data[0])

                # Assign remaining elementa as value in a list
                value = [item_data[1], item_data[2], int(item_data[3]), int(item_data[4])]

                # Add key-value pairs in the dictionary
                all_item_data.update({key : value})
    except:
        print("FileError: There was a problem reading file 'main.txt'. Please check your file exists and values are correct.")



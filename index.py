# File Read & Write Challenge with Error Handling

def modify_content(line):
    """
    Modify the line before writing to the new file.
    Example: convert to uppercase. You can change this logic.
    """
    return line.upper()

def main():
    try:
        filename = input("Enter the name of the file to read: ")
        with open(filename, 'r') as file:
            content = file.readlines()
        
        # Create a new file to write modified content
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            for line in content:
                new_file.write(modify_content(line))
        
        print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' could not be read or written.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
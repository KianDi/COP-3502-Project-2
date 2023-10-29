from console_gfx import ConsoleGfx
# displays the rainbow image and prints welcome message
print("Welcome to the RLE image encoder!\n")
print("Displaying Spectrum Image:")
ConsoleGfx.display_image(ConsoleGfx.test_rainbow)


# function for displaying the menu
def menu_display():
    print("\nRLE MENU")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data\n")


if __name__ == '__main__':
    # variables for user input and image data
    user_input = 0
    image_data = None
    while True:
        # keep displaying menu
        # calling the function to display menu
        menu_display()
        user_input = input("Select a menu option: ")
        if user_input == "1":
            user_file_input = 0
            # prompts user for input and loads the file data
            user_file_input = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(user_file_input)
        elif user_input == "2":
            # loads file data for test image
            image_data = ConsoleGfx.test_image
            print("Test Image Data Loaded")
        elif user_input == "6":
            print("Displaying image...")
            # Displays the image loaded in option 1 or 2
            ConsoleGfx.display_image(image_data)

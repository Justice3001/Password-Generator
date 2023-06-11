
#menu display function
def showMenu():
    print('''How will your password be structured :
        		1. Digits
        		2. Letters
        		3. Special characters + Letters + Digits
        		4. Auto Generate Password (recommended by cybersecurity professionals)
        		5. Exit''')


def main():
    import string
    import random

    characterList = ""


    # Getting character set for password
    while True:

        # user input validation
        while True:
            try:
                length = int(input("Enter password length: "))
                if length < 1 or length < 7:
                    print("Length must be greater than zero (0) and minimum seven (7) digits for security reasons.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        showMenu()
        print('\n')

        # user input validation
        while True:
            try:
                choice = int(input("Enter a number (1-5): "))
                if 1 <= choice <= 5:

                    break
                else:
                    print("Invalid input. Please enter a number from 1 to 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")


        #Digits selection
        if (choice == 1):

            # user input validation
            while True:
                try:
                    num_generations = int(input("How many passwords do you want to generate: "))
                    if num_generations > 0:
                        break
                    else:
                        print("Invalid input. Please enter a number greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # loop for diplaying number of passwords user wants
            for _ in range(num_generations):
                # Adding digits to possible characters
                characterList += string.digits

                password = []

                for i in range(length):
                    # Picking a random character from our
                    # character list
                    randomchar = random.choice(characterList)

                    # appending a random character to password
                    password.append(randomchar)
                # Generate and display the password here
                print("The random password is " + "".join(password) + '\n\n')


        #Letters selection
        elif (choice == 2):

            #user input validation
            while True:
                try:
                    num_generations = int(input("How many passwords do you want to generate: "))
                    if num_generations > 0:
                        break
                    else:
                        print("Invalid input. Please enter a number greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            print('\n')

            # loop for diplaying number of passwords user wants
            for _ in range(num_generations):
                # Adding letters to possible characters
                characterList += string.ascii_letters

                password = []

                for i in range(length):
                    # Picking a random character from our
                    # character list
                    randomchar = random.choice(characterList)

                    # appending a random character to password
                    password.append(randomchar)

                # printing password as a string
                print("The random password is " + "".join(password) + '\n\n')


        #Special characters + Letters + Digits selection
        elif (choice == 3):

            # user input validation
            while True:
                try:
                    num_generations = int(input("How many passwords do you want to generate: "))
                    if num_generations > 0:
                        break
                    else:
                        print("Invalid input. Please enter a number greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # loop for diplaying number of passwords user wants
            for _ in range(num_generations):
                # Adding special characters to possible
                # characters
                characterList += string.punctuation + string.digits + string.ascii_letters

                password = []

                for i in range(length):
                    # Picking a random character from our
                    # character list
                    randomchar = random.choice(characterList)

                    # appending a random character to password
                    password.append(randomchar)

                # printing password as a string
                print("The random password is " + "".join(password) + '\n\n')

        #Auto Generate Password selection
        elif(choice == 4):

            # user input validation
            while True:
                try:
                    num_generations = int(input("How many passwords do you want to generate: "))
                    if num_generations > 0:
                        break
                    else:
                        print("Invalid input. Please enter a number greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            #loop for diplaying number of passwords user wants
            for _ in range(num_generations):
                characterList += string.punctuation + string.digits + string.ascii_letters

                password = []

                for i in range(15):
                    # Picking a random character from our
                    # character list
                    randomchar = random.choice(characterList)

                    # appending a random character to password
                    password.append(randomchar)

                # printing password as a string
                print("The random password is " + "".join(password) + '\n\n')

            # user input validation
            while True:
                try:
                    choiceMenu = input('Want to know why this password was chosen? (y/n): ')
                    if choiceMenu.lower() == 'y' or choiceMenu.lower() == 'n':
                        break
                    else:
                        print("Invalid input. Please enter 'y' for Yes or 'n' for No.")
                except:
                    print("Invalid input. Please try again.")

            if choiceMenu.lower() == 'y':
                print(
                    'The National Institute of Standards and Technology (NIST) states that password length has been found to be a primary factor in characterizing password strength. To strengthen the security of your online information, ensure your passwords are a random mix of at least 14 to 16 characters.\n')
            else:
                print('Okay.\n')

        #exit/end program selection
        elif (choice == 5):
            print('okay bye!\n')
            exit()



if __name__ == '__main__':
 main()

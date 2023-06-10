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

    # Getting password length


    # Continue with the rest of your code

    characterList = ""


    # Getting character set for password
    while True:

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

        while True:
            try:
                choice = int(input("Enter a number (1-5): "))
                if 1 <= choice <= 5:

                    break
                else:
                    print("Invalid input. Please enter a number from 1 to 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")


        if (choice == 1):
            # Adding digits to possible characters
            characterList += string.digits

            password = []

            for i in range(length):
                # Picking a random character from our
                # character list
                randomchar = random.choice(characterList)

                # appending a random character to password
                password.append(randomchar)

            # printing password as a string
            print("The random password is " + "".join(password) +'\n\n')


        elif (choice == 2):
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
            print("The random password is " + "".join(password) +'\n\n')


        elif (choice == 3):

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
            print("The random password is " + "".join(password) +'\n\n')

        elif(choice == 4):
            characterList += string.punctuation + string.digits + string.ascii_letters

            password = []

            for i in range(15):
                # Picking a random character from our
                # character list
                randomchar = random.choice(characterList)

                # appending a random character to password
                password.append(randomchar)

            # printing password as a string
            print("The random password is " + "".join(password) +'\n\n')

            choiceMenu=input('Want to know why this password was chosen this chosen? (y/n):')
            if(choiceMenu=='y'):
                print('the National Institute of Standards and Technology (NIST) states, Password length has been found to be a primary factor in characterizing password strength. To strengthen the security of your online information, ensure your passwords are a random mix of at least 14 to 16 characters\n\n')
            else:
                print('okay.\n\n')


        elif (choice == 5):
            print('okay bye!\n')
            exit()

        else:
            print("Please selection a valid option:")



if __name__ == '__main__':
 main()

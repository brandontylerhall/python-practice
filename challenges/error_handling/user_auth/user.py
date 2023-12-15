import pandas as pd

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = ['!', '#', '$', '%', '&', '*', '+']


def add_user(writer):
    while True:
        username = input("Enter a username\n"
                         "Your username must be between 6 and 15 characters long\n"
                         "> ")
        password = input("Enter you password\n"
                         "You must include:\n"
                         "One number\n"
                         "One capital letter\n"
                         "One lowercase letter\n"
                         "One special character\n"
                         "> ")
        try:
            df = pd.read_csv('users.csv')
            # Check if the username already exists in the DataFrame
            if username in df['username'].values:
                raise ValueError("Username already exists. Please choose a different username.")
        except FileNotFoundError:
            df = pd.DataFrame(columns=['username', 'password'])

        if len(username) < 6 or len(password) > 15:
            print("Username must be between 6 and 15 characters. Please try again.")
            continue

        if (
                not any(char in lower for char in password) or
                not any(char in upper for char in password) or
                not any(char in numbers for char in password) or
                not any(char in special_characters for char in password)
        ):
            print("One or more password requirements were not met. Please try again.")
            continue

        userdata = [username, password]
        writer.writerow(userdata)
        print(f'Successfully added {username} to the file')
        return True

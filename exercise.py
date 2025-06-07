users: dict[str, str] = {}
logged_in_user = None

def menu():
    while True:
        action = input('Enter a command: ').strip().lower()

        if action == 'signup':
            signup()
        elif action == 'login':
            user = input('Enter your username: ').strip()
            password = input('Enter your password: ')

            login(user, password)
        elif action == 'exit':
            break
        else:
            print('Unknown command')

def signup():
    user = input('Enter your username: ').strip()
    password = input('Enter your password: ')

    if user in users:
        print("A user with this username already exists")
        return

    if len(password) < 8:
        print('Your password is too short')
        return

    users[user] = password

def login(user: str, password: str):
    global logged_in_user

    if user not in users:
        print("This user does not exist")
        return

    if users[user] != password:
        print("Wrong password")
        return

    logged_in_user = user

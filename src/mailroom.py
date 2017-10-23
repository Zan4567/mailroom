'''.'''

DONOR_DATA = [
    {'name', [100, 500, 120]}
]

def prompt():
    while True:
        print("""Welcome! Please select:
            Send a (T)hank You
            Create a (R)eport""")

        user_input = raw_input()

        if user_input.startswith(('t', 'T')):
            thankyou()
        elif user_input.startswith(('r', 'R')):
            report()
        elif user_input.startswith(('q', 'Q')):
            break;

def thankyou():
    name = ''
    while(name == ''):
        print('Please enter the name of the recipient:')
        user_input = raw_input()

        if user_input == 'list':
            for donor in DONOR_DATA:
                print(donor)
        elif user_input == 'q' or user_input == 'Q':
            print('Exiting to main menu...')
            return
        elif DONOR_DATA[user_input]:
            name = user_input
        elif user_input != '':
            DONOR_DATA.append({user_input}, [])
            name = user_input

    amount = 0
    while(amount == 0):
        print("Please enter the donation amount:")
        user_input = raw_input()

        try:
            amount = user_input
        except ValueError:
            continue
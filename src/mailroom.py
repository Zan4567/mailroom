'''.'''

DONOR_DATA = {
    'name': [100, 500, 120]
}

def prompt():
    """Prompts a user to make selections"""
    while True:
        user_input = input("""Welcome! Please select:
            Send a (T)hank You
            Create a (R)eport: """)
        if user_input.startswith(('t', 'T')):
            thankyou()
        elif user_input.startswith(('r', 'R')):
            report()
        elif user_input.startswith(('q', 'Q')):
            break;

def thankyou():
    """Prompts user for list of donors"""
    name = ''
    while(name == ''):
        print('Please enter the name of the recipient or type list to see a list of donors - or q to quit')
        user_input = input()
        if user_input == 'list':
            for donor in DONOR_DATA.keys():
                print(donor)
        elif user_input == 'q' or user_input == 'Q':
            print('Exiting to main menu...')
            return
        elif DONOR_DATA.get(user_input, False):
            name = user_input
        elif user_input != '':
            DONOR_DATA.update((user_input, []))
            name = user_input
    amount = 0
    while(amount == 0):
        print("Please enter the donation amount:")
        user_input = input()
        try:
            amount = user_input
        except ValueError:
            continue
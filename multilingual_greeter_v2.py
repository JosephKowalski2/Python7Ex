import multilingual_greeter

def prompt():
    mode_select = input("Please select 1 for admin mode or 2 for user mode\n")
    if mode_select == '1':
        admin()
    elif mode_select == '2':
        user()
    else:
        print('Please select the correct user mode')


def admin():
    admin_options = input('1: Add Language, 2: Change Language\n')
    if admin_options == 1:
        add_language = input('Please enter the language you want to add')
        add_new_language_name = input('Please enter "What is your name?" in the new language')
        add_greeting = input('Enter "Hello" in the new language')




from reporter import Reporter
"""
Main Application Entry Point 🚀
--------------------------------
This module contains the main function to run the Habit Tracker command-line 
application. 

It handles:
1. Instantiating the Reporter (UI) class.
2. Initializing the application (loading data).
3. Running the main application loop, which processes user menu choices until 
   the user chooses to exit (6).
"""
def main():
    """
    The core loop for the Habit Tracker application.
    """
    r = Reporter()
    r.welcome()
    while True:
        number = r.menu()
        if number == 1:
            r.add_user()
        if number == 2:
            r.list_users()
        if number == 3:
            user = r.enter_user()
            if user != "":
                r.user_menu(user)
        if number == 4:
            r.save()
        if number == 5:
            r.u.print_all()
        if number == 6:
            break

if __name__ == "__main__":
    main()
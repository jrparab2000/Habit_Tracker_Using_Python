from user import User
from storage import Storage
from api_client import APIClient

"""
Reporter Module (User Interface) 🖥️
-----------------------------------
This module defines the Reporter class, which acts as the main user interface 
(UI) for the command-line application. 

It handles:
1. Application initialization (loading data and configuration).
2. Displaying all menus (main menu, user menu).
3. Collecting user input and validating choices.
4. Calling appropriate methods on the User, Habit_Tracker, Storage, and APIClient 
   classes to execute user commands.
"""

class Reporter():
    u = User()

    @classmethod
    def welcome(cls):
        """
        Initializes the application upon startup.
        
        This method performs critical startup tasks:
        1. Checks for the required data directory structure.
        2. Loads persistent user and habit data from 'data.json'.
        3. Loads the list of valid habits for validation/suggestion from Storage.
        """
        print("-----------Welcome To Habit Manger-----------")
        print("Checking for current logs...")
        str_path = Storage.data_path()
        data = Storage.load_json(str_path)
        Storage.load_Valid_habits(str_path)
        if data != {}:
            cls.u.load_user(data)
            print("Data loaded successfully...")
        else:
            print("No file found using system for 1st time")


    @staticmethod    
    def menu():
        """
        Displays the main application menu and prompts the user for a choice.
        
        Handles input validation to ensure a number between 1 and 6 is entered.
        
        Returns:
            int: The user's valid menu choice.
        """
        while True:
            print()
            print("---------------Main Menu---------------")
            print("1.\tAdd User")
            print("2.\tList Users")
            print("3.\tEnter Current User")
            print("4.\tSave")
            print("5.\tPrint all")
            print("6.\tExit")
            try:
                number = int(input(f"Enter your choice: "))
            except Exception:
                print("Nice Try, Please enter a valid number...")
                number = 0
                continue
            
            if number in [1, 2, 3, 4, 5, 6]:
                return number
            else:
                print("Please enter a correct option")
        
    @classmethod
    def add_user(cls):
        """
        Handles the logic for creating a new user account.
        
        Prompts for a unique UserID and a display name, and calls the User class 
        method to register the new user.
        """
        while True:
            userId = input(f"Enter UserID (Enter 0 to go back): ")
            if userId == "0":
                break
            else:
                name = input(f"Enter your name: ")
                if cls.u.add_user(userId, name):
                    print("User added successfully time to login...")
                    break

    @classmethod
    def list_users(cls):
        """
        Displays a list of all current UserIDs in the system.
        """
        cls.u.print_users()
    
    @classmethod
    def enter_user(cls):
        """
        Prompts for a UserID and validates its existence before granting access 
        to the user menu.
        
        Returns:
            str: The valid UserID, or an empty string ("") to go back.
        """
        while True:
            userId = input(f"Enter UserID (Enter 0 to go back): ")
            if userId == "0":
                return ""
            else:
                if cls.u.check_user(userId):
                    return userId
                
    @classmethod
    def user_menu(cls,userId):
        """
        Displays the menu specific to the currently logged-in user.
        
        Provides options for managing habits, viewing streaks, and getting 
        motivational quotes.
        
        Args:
            userId (str): The ID of the currently active user.
        """
        # Flag to ensure summary is only printed once on initial entry
        flag = True
        while True:
            print()
            print(f"---------------Welcome {cls.u.get_name(userId)}---------------")
            if flag:
                cls.summary(userId)
                flag = False
                print()
            print("Motivation:-")
            print(str(APIClient.get_quote()))
            print("1.\tView Habits")
            print("2.\tAdd New Habit")
            print("3.\tMark Habit as Done for today")
            print("4.\tDelete a Habit")
            print("5.\tDelete this User")
            print("6.\tGo Back")
            print("7.\tSave")
            try:
                number = int(input(f"Enter your choice: "))
            except Exception:
                print("Nice Try, Please enter a valid number...")
                number = 0

            if number not in [0,1,2,3,4,5,6,7]:
                print("Please choose from the option given...")
                continue

            if number == 1:
                cls.u.print_habits(userId)
            if number == 2:
                cls.add_new_habit(userId)
            if number == 3:
                cls.mark_habit_done(userId)
            if number == 4:
                cls.delete_habit(userId)
            if number == 5:
                cls.u.delete_user(userId)
                print("user deleted successfully...")
                break
            if number == 6:
                break
            if number == 7:
                cls.save()

    @classmethod
    def add_new_habit(cls,userId):
        """
        Prompts the user for a new habit name and attempts to add it to their tracker.
        
        Args:
            userId (str): The ID of the user.
        """
        while True:
            habit = input(f"Enter Habit (Enter 0 to go back): ")
            if habit == "0":
                break
            else:
                if cls.u.users[userId].add_habit(habit):
                    print(f"Habit Successfully added next step mark as done")
                    break 
    
    @classmethod
    def mark_habit_done(cls,userId):
        """
        Prompts the user for a habit name and marks it as done for today.
        
        Args:
            userId (str): The ID of the user.
        """
        while True:
            habit = input(f"Enter Habit (Enter 0 to go back): ")
            if habit == "0":
                break
            else:
                if cls.u.users[userId].mark_as_done(habit):
                    break 

    @classmethod
    def delete_habit(cls,userId):
        """
        Prompts the user for a habit name and deletes it from their tracker.
        
        Args:
            userId (str): The ID of the user.
        """
        while True:
            habit = input(f"Enter Habit (Enter 0 to go back): ")
            if habit == "0":
                break
            else:
                if cls.u.users[userId].delete_habit(habit):
                    print(f"Habit Successfully deleted")
                    break 
    
    @classmethod
    def save(cls):
        """
        Saves all current user and habit data to the persistent JSON file.
        
        This method orchestrates the saving process between the User manager and Storage utility.
        """
        str_path = Storage.data_path()
        data = cls.u.store_user()
        Storage.save_json(str_path, data)

    @classmethod
    def summary(cls,userId):
        """
        Prints the streak status and summary for all habits of the given user.
        
        Args:
            userId (str): The ID of the user whose summary is requested.
        """
        print("Summary:-")
        cls.u.summary(userId)

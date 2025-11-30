from habit_tracker import Habit_Tracker

"""
User Module
-----------
This module defines the User class, which serves as the top-level container 
for the entire application's data. 

It is responsible for:
1. Managing a collection of individual Habit_Tracker instances (one for each user).
2. Handling user-level operations like adding, deleting, and selecting users.
3. Managing the serialization and deserialization of all user data.
"""

class User:
    def __init__(self):
        """
        Constructor to initialize the User manager.
        
        The 'users' dictionary stores all user data, where the key is the 
        lowercase user ID (str) and the value is a Habit_Tracker object.
        """
        self.users = {}

    def add_user(self, userId, name):
        """
        Creates and adds a new user (Habit_Tracker instance) to the collection.
        
        Args:
            userId (str): A unique identifier for the user (used as the dictionary key).
            name (str): The display name of the user.
            
        Returns:
            bool: True if the user was successfully added, False otherwise.
        """
        str_name = Habit_Tracker.check_str(name)
        str_userId = Habit_Tracker.check_str(userId)
        if(str_name != None) and (str_userId != None):
            if str_userId not in self.users.keys():
                h1 = Habit_Tracker(str_name)
                self.users.update({str_userId : h1})
                return True
            print("UserID already present try something else...")
        return False
    
    def check_user(self, userId):
        """
        Checks if a user ID exists in the system.
        
        Args:
            userId (str): The ID to check.
            
        Returns:
            bool: True if the user ID is found, False otherwise.
        """
        str_userId = Habit_Tracker.check_str(userId)
        if str_userId != None:
            if str_userId in self.users.keys():
                return True
            else:
                print("User not found...")
                return False
        else:
            print("not a vaild input...")
            return False
        
    def delete_user(self, userId):
        """
        Removes a user and their associated Habit_Tracker data from the system.
        
        Args:
            userId (str): The ID of the user to delete.
            
        Returns:
            bool: True if the user was successfully deleted, False otherwise.
        """
        str_userId = Habit_Tracker.check_str(userId)
        if(str_userId != None):
            if str_userId in self.users.keys():
                self.users.pop(str_userId)
                return True
        return False
    
    def store_user(self):
        """
        Serializes all user data into a single dictionary for persistent storage (e.g., JSON).
        
        It delegates the serialization of habits to each Habit_Tracker instance.
        
        Returns:
            dict: The top-level dictionary containing all users and their habit data.
                  Format: {user_id: {user_data_from_habit_tracker}, ...}
        """
        dict = {}
        for keys, values in self.users.items():
            dict.update({keys : values.store_habits()})
        return dict
    
    def load_user(self,users):
        """
        Loads user and habit data from a dictionary (e.g., loaded from a JSON file).
        
        Args:
            users_data (dict): The dictionary containing all user data.
        """
        for keys, values in users.items():
            h = Habit_Tracker(values["name"])
            dict = values
            dict.pop("name")
            h.load_habits(dict)
            self.users.update({keys: h})

    def get_name(self, userId):
        """
        Retrieves the display name of a user based on their ID.
        
        Args:
            userId (str): The ID of the user.
            
        Returns:
            str: The user's display name, or None if the ID is invalid.
        """
        str_userId = Habit_Tracker.check_str(userId)
        if str_userId != None:
            return self.users[str_userId].name
        
    def print_users(self):
        """
        Prints a numbered list of all active user IDs in the system.
        """
        count = 1
        for keys in self.users.keys():
            print(f"{count}.\t{keys}")
            count += 1

    def summary(self,userId):
        """
        Prints the streak summary for all habits belonging to a specific user.
        
        Args:
            userId (str): The ID of the user whose summary is needed.
        """
        self.users[userId].summary()

    def print_all(self):
        """
        Debug method to print all details for every user and all their habits 
        in the system.
        """
        for keys, values in self.users.items():
            print()
            print(f"============================ User: {keys} ==============================")
            values.print_all()

    def print_habits(self,userId):
        """
        Prints a list of habits (done/not done indicators) for a specific user.
        
        Args:
            userId (str): The ID of the user whose habits should be printed.
        """
        self.users[userId].print_habits()

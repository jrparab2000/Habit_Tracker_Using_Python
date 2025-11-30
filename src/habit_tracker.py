from habit import Habit
from storage import Storage

"""
Habit_Tracker Module
--------------------
This module defines the Habit_Tracker class, which acts as the main manager for 
a single user's habits. 

It handles:
1. Creating, managing, and storing a collection of Habit objects.
2. Interacting with the Storage class for data validation and persistence.
3. Providing methods for the user interface (e.g., summary, printing habits).
"""

class Habit_Tracker:
    def __init__(self, name, datapath="data/habits.json"):
        """
        Initializes the Habit_Tracker for a specific user.
        
        Args:
            name (str): The name of the user this tracker belongs to.
            datapath (str): The file path where habit data is stored/loaded. (NOTE: note in use for future scope)
        """
        self.name = name
        self.datapath = datapath
        self.habits = {}
        
    def add_habit(self, habit_name):
        """
        Adds a new habit to the user's tracker after validation.
        
        It checks for valid input, suggests corrections (using the validator, 
        which typically involves Difflib logic), and prevents duplicates.
        
        Args:
            habit_name (str): The name/description of the habit to add.
            
        Returns:
            bool: True if the habit was successfully added, False otherwise.
        """
        habit_name_str = self.check_str(habit_name)
        if habit_name_str != None:
            habit_name_str, category = self.habit_validator(habit_name_str)
            if habit_name_str not in self.habits.keys():
                h1 = Habit(self.name,habit_name_str)
                self.habits.update({habit_name_str : h1})
                return True
            else:
                print(f"Cannot add same habit again do you want to mark this habit as done")
                return False
        else:
            print(f"Not a valid input")
            return False
    
    def habit_validator(self, habit_name):
        """
        Handles the habit name validation and correction process.
        
        This method interacts with the external Storage methods (is_valid_habit, 
        suggest_similar) to check for common habits and offer corrections, 
        improving data quality.
        
        Args:
            habit_name (str): The initial user input for the habit name.
            
        Returns:
            tuple: (validated_habit_name_str, category)
        """
        flag, habit_name_str, category = Storage.is_valid_habit(habit_name)
        if not flag:
            if habit_name_str != "":
                while True:
                    ans = input(f"did you mean: {habit_name_str} instead of {habit_name} (y/n): ")
                    if ans.lower() == "y":
                        return habit_name_str, category
                    elif ans.lower() == "n":
                        return habit_name, ""
                    else:
                        continue
            else:
                suggestion = Storage.suggest_similar(habit_name)
                count = 1
                for i in suggestion:
                    print(f"{count}.\t{i}")
                    count += 1
                while True:
                    try:
                        if suggestion == []:
                            print("WARNING: Don't look like a habit are you sure you want to keep it: ")
                            number = 0
                        else:
                            number = int(input(f"Select a suggestion or enter 0 to keep same: "))
                    except Exception:
                        print("Nice Try, Please enter a valid number...")
                        continue
                    if number > 0:
                        if number <= len(suggestion):
                            flag_1, habit_name_str_1, category_1 = Storage.is_valid_habit(suggestion[number-1])
                            return habit_name_str_1, category_1
                        else:
                            continue
                    elif number == 0:
                        return habit_name, ""
        else:
            return habit_name_str, category


    def mark_as_done(self, habit_name):
        """
        Marks a specific habit as completed for the current day.
        
        Args:
            habit_name (str): The name of the habit to mark.
            
        Returns:
            bool: True if the habit was found (regardless of success), False if not found.
        """
        habit_name_str = self.check_str(habit_name)
        if habit_name_str != None:
            for keys in self.habits.keys():
                if(keys == habit_name_str):
                    if self.habits[keys].mark_as_done():
                        print(f"Habit Successfully marked as done")
                    else:
                        print(f"This is already done for today")
                    return True
            print(f"Habit not found...")
            return False
        else:
            return False
    
    def delete_habit(self, habit_name):
        """
        Removes a habit from the tracker's collection.
        
        Args:
            habit_name (str): The name of the habit to delete.
            
        Returns:
            bool: True if the habit was successfully deleted, False otherwise.
        """
        habit_name_str = self.check_str(habit_name)
        if habit_name_str != None:
            for keys in self.habits.keys():
                if(keys == habit_name_str):
                    self.habits.pop(keys)
                    return True
            print(f"Habit not found...")
            return False
        else:
            return False
    
    def load_habits(self, habits):
        """
        Loads habits from a dictionary (e.g., data loaded from a JSON file).
        
        It iterates through the dictionary and reconstructs Habit objects 
        using the from_dict method, including loading the history.
        
        Args:
            habits_dict (dict): A dictionary containing habit data.
        """
        for keys, values in habits.items():
            h = Habit()
            h.from_dict(values)
            self.habits.update({keys : h})

    def store_habits(self):
        """
        Serializes all habits into a dictionary for storage (e.g., saving to JSON).
        
        Returns:
            dict: A dictionary containing the user's name and all serialized habit data.
        """
        dict = {"name" : self.name}
        for keys, values in self.habits.items():
            dict.update({keys : values.to_dict()})
        return dict
    
    def summary(self):
        """
        Prints the streak status summary for all managed habits.
        
        It iterates over all Habit objects and calls their individual summary method.
        """
        for keys, values in self.habits.items():
            print(f"Your Habit of {keys}:")
            values.summary()

    def print_all(self):
        """
        Debug method to print all stored data for the tracker and all habits.
        """
        print(f"Name:\t{self.name}")
        for keys, values in self.habits.items():
            print(f"-------{keys}-------")
            values.print_all()
    
    def print_habits(self):
        """
        Lists all habits with a visual indicator (✅/❌) showing if the habit 
        has been completed today.
        """
        count = 1
        for keys in self.habits.keys():
            if self.habits[keys].check_done():
                print(f"{count}.\t{keys}\t✅")
            else:
                print(f"{count}.\t{keys}\t❌")
            count = count + 1
    
    def print_to_do(self):
        count = 1

    @staticmethod
    def check_str(temp_str):
        """
        A static utility method to ensure all user input is converted to a 
        lowercase string for consistent comparison and key management.
        
        Args:
            temp_str: Any input received from the user.
            
        Returns:
            str or None: The validated lowercase string, or None if casting fails.
        """
        try:
            return str(temp_str).lower()
        except:
            print("string casting failed try entering a string...")
            return None
   
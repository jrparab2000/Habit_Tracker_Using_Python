import json
import difflib
import os

"""
Storage Module
--------------
This module defines the Storage class, which handles all file system and data 
persistence operations for the application. All methods are static or class 
methods, making it a utility class.

It is responsible for:
1. Managing file paths and directory creation (e.g., 'data' folder).
2. Saving and loading the main user data (data.json).
3. Loading the internal list of pre-approved valid habits (valid_habits.json).
4. Providing suggestions and corrections for habit names using difflib.
"""

class Storage:
    valid_habits = {}
    def __init__(self):
        pass
    
    @staticmethod
    def data_path():
        """
        Creates the necessary 'data' directory if it doesn't exist and returns 
        its absolute path.
        
        The method changes the directory temporarily to create the folder and then 
        reverts to the original current working directory (CWD).
        
        Returns:
            str: The absolute path to the newly created or existing 'data' directory.
        """
        cwd = os.getcwd()
        if not os.path.exists("data"):
            os.makedirs("data")
        os.chdir("data")
        new_cwd = os.getcwd()
        os.chdir(cwd)
        return str(new_cwd)
    
    @staticmethod
    def load_json(path):
        """
        Attempts to load data from the main user data JSON file (data.json).
        
        Handles common file errors like FileNotFoundError and JSON decoding errors.
        
        Args:
            path (str): The directory path to the 'data' folder.
            
        Returns:
            dict: The loaded dictionary data, or an empty dictionary on failure.
        """
        try:
            path = path + "\data.json"
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Warning: Data file not found...")
            return {}
        except json.JSONDecodeError:
            print("Error: Corrupted data file!")
            return {}

    @staticmethod
    def save_json(path, data):
        """
        Saves the provided data dictionary to the main user data JSON file (data.json).
        
        Uses indent=4 for human-readable formatting.
        
        Args:
            path (str): The directory path to the 'data' folder.
            data (dict): The dictionary containing all user and habit data.
        """
        path = path + "\data.json"
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_Valid_habits(cls,path):
        """
        Loads the internal list of pre-approved valid habits from 'valid_habits.json' 
        into the class attribute `valid_habits`.
        
        This list is used for suggestions and typo correction.
        
        Args:
            path (str): The directory path where 'valid_habits.json' is located.
        """
        path = path + "\\valid_habits.json"
        with open(path, "r") as f:
            temp = json.load(f).get("habits")
            for i in temp:
                cls.valid_habits.update({i.get("name").lower() : i.get("category").lower()})

    @classmethod
    def is_valid_habit(cls, habit_name):
        """
        Checks if a user's input matches a known valid habit or is a close typo.
        
        Uses difflib with a high cutoff (0.90) for strict typo correction.
        
        Args:
            habit_name (str): The user's input for the habit name.
            
        Returns:
            tuple: (is_valid: bool, corrected_name: str, category: str)
        """
        habit_name = habit_name.lower().strip()

        if habit_name in cls.valid_habits.keys():
            return True, habit_name, cls.valid_habits.get(habit_name,"")

        close_matches = difflib.get_close_matches(habit_name, list(cls.valid_habits.keys()), n=1, cutoff=0.90)
        if len(close_matches) > 0:
            return False, close_matches[0], cls.valid_habits.get(close_matches[0],"")
        else:
            return False, "", ""
    
    @classmethod
    def suggest_similar(cls, habit_name, n=5):
        """
        Suggests multiple similar habits when no close match is found.
        
        Uses difflib with a lower cutoff (0.55) to provide broader suggestions.
        
        Args:
            habit_name (str): The user's input for the habit name.
            n (int): The maximum number of suggestions to return.
            
        Returns:
            list: A list of suggested habit names (strings).
        """
        habit_name = habit_name.lower().strip()

        suggestions = difflib.get_close_matches(
            habit_name,
            list(cls.valid_habits.keys()),
            n=n,
            cutoff=0.55  # allow loose matches for better suggestions
        )

        return suggestions
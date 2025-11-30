from datetime import date

"""
Habit Module
----------------
This module defines the Habit class, which represents a single habit for a user.
It is responsible for:
1. Tracking the name and description of the habit.
2. Managing the streak counter (gamification).
3. Maintaining a history of dates when the habit was completed.
4. Serializing and Deserializing data for JSON storage.
"""

class Habit:
    def __init__(self, name = "", habit = ""):
        """
        Constructor to initialize a new Habit instance.
        
        Args:
            name (str): The name of the user.
            habit (str): A short description or a word (e.g., "morning Run" or "running").
        """
        self.name = name
        self.habit = habit
        self.streak = 0
        self.history = []

    def mark_as_done(self):
        """
        Marks the habit as completed for the current day.
        
        Logic:
        1. Checks if the habit was already done today.
        2. If not, it updates the streak count.
        3. Adds today's date to the history.
        
        Returns:
            bool: True if successfully marked as done, False if already done today.
        """
        today = date.today()
        if today not in self.history:
            self.streak_update(today)
            self.history.append(today)
            return True
        return False
    
    def streak_update(self,today):
        """
        Internal method to calculate and update the streak counter.
        
        This handles the 'Problem' mentioned in the presentation regarding 
        accessing empty lists. It checks if history exists before comparing dates.
        
        Args:
            today (date): The current date being marked.
        """
        if(self.history != []):
            if((today.day - self.history[len(self.history) - 1].day) == 1):
                self.streak += 1
            elif(today.day != self.history[len(self.history) - 1].day):
                self.streak = 1
        else:
            self.streak = 1
    
    def check_done(self):
        """
        Checks if the habit has been completed today.
        
        Returns:
            bool: True if the habit is in today's history, False otherwise.
        """
        today = date.today()
        if today in self.history:
            return True
        else:
            return False
        
    def store_history(self):
        """
        Converts the history list (date objects) into a list of strings (ISO format).
        Required for saving to JSON files, as JSON cannot store Python date objects.
        
        Returns:
            list: A list of date strings (e.g., ['2023-10-01', '2023-10-02']).
        """
        return [d.isoformat() for d in self.history]
    
    def load_history(self, json_history):
        """
        Converts a list of strings (from JSON) back into Python date objects.
        
        Args:
            json_history (list): List of date strings loaded from the file.
        """
        self.history = [date.fromisoformat(s) for s in json_history]
    
    def to_dict(self):
        """
        Serializes the Habit object into a dictionary.
        This is used to prepare the object for saving to the JSON file.
        
        Returns:
            dict: Key-value pairs of the habit's data.
        """
        return {
            "name" : self.name,
            "habit" : self.habit,
            "history" : self.store_history(),
            "streak" : self.streak  
        }
    
    def from_dict(self, dict):
        """
        Updates the current Habit object using data from a dictionary.
        This is used when loading data from the JSON file.
        
        Args:
            dict (dict): The dictionary containing habit data.
        """
        self.name  = dict["name"]
        self.habit = dict["habit"]
        self.load_history(dict["history"])
        self.streak = dict["streak"]
    
    def summary(self):
        """
        Analyzes the current streak status and prints a motivational summary 
        to the console.
        
        Logic:
        - Checks if the streak is safe (done today).
        - Checks if the streak is at risk (done yesterday, needs to be done today).
        - Checks if the streak is broken (missed a day).
        """
        today = date.today()
        if(self.history != []):
            if((today.day - self.history[len(self.history) - 1].day) == 1):
                print(f"Streak of {self.streak} days is about to break...")
            elif(today.day != self.history[len(self.history) - 1].day):
                print("Streak just broke")
                self.streak = 0
            else:
                print(f"Streak of {self.streak} days safe for today...")
        else:
            print("Streak Never Started...")
    
    def print_all(self):
        """
        Debug method to print all attributes of the habit.
        """
        dict = self.to_dict()
        for keys, values in dict.items():
            print(f"{keys}\t:\t{values}")
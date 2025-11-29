import json
import difflib
import os

class Storage:
    valid_habits = {}
    def __init__(self):
        pass
    
    @staticmethod
    def data_path():
        cwd = os.getcwd()
        if not os.path.exists("data"):
            os.makedirs("data")
        os.chdir("data")
        new_cwd = os.getcwd()
        os.chdir(cwd)
        return str(new_cwd)
    
    @staticmethod
    def load_json(path):
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
        path = path + "\data.json"
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_Valid_habits(cls,path):
        path = path + "\\valid_habits.json"
        with open(path, "r") as f:
            temp = json.load(f).get("habits")
            for i in temp:
                cls.valid_habits.update({i.get("name").lower() : i.get("category").lower()})

    @classmethod
    def is_valid_habit(cls, habit_name):
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
        habit_name = habit_name.lower().strip()

        suggestions = difflib.get_close_matches(
            habit_name,
            list(cls.valid_habits.keys()),
            n=n,
            cutoff=0.55  # allow loose matches for better suggestions
        )

        return suggestions
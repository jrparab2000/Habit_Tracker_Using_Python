import json
import os

class Storage:

    def __init__(self):
        pass
    
    @staticmethod
    def data_path():
        cwd = os.getcwd()
        os.chdir("Project")
        os.chdir("habit_tracker")
        # print(os.getcwd())
        if not os.path.exists("data"):
            os.makedirs("data")
        os.chdir("data")
        new_cwd = os.getcwd()
        # print(os.getcwd())
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
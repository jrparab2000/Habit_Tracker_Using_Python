from habit_tracker import Habit_Tracker

class User:
    def __init__(self):
        self.users = {}

    def add_user(self, userId, name):
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
        str_userId = Habit_Tracker.check_str(userId)
        if(str_userId != None):
            if str_userId in self.users.keys():
                self.users.pop(str_userId)
                return True
        return False
    
    def store_user(self):
        dict = {}
        for keys, values in self.users.items():
            dict.update({keys : values.store_habits()})
        return dict
    
    def load_user(self,users):
        for keys, values in users.items():
            h = Habit_Tracker(values["name"])
            dict = values
            dict.pop("name")
            h.load_habits(dict)
            self.users.update({keys: h})

    def get_name(self, userId):
        str_userId = Habit_Tracker.check_str(userId)
        if str_userId != None:
            return self.users[str_userId].name
        
    def print_users(self):
        count = 1
        for keys in self.users.keys():
            print(f"{count}.\t{keys}")
            count += 1
    
    def print_all(self):
        for keys, values in self.users.items():
            print()
            print(f"============================ User: {keys} ==============================")
            values.print_all()

    def print_habits(self,userId):
        self.users[userId].print_habits()

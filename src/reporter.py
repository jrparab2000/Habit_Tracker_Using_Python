from user import User
from storage import Storage
from api_client import APIClient


class Reporter():
    u = User()

    @classmethod
    def welcome(cls):
        print("-----------Welcome To Habit Manger-----------")
        print("Checking for current logs...")
        str_path = Storage.data_path()
        data = Storage.load_json(str_path)
        if data != {}:
            cls.u.load_user(data)
            print("Data loaded successfully...")
        else:
            print("No file found using system for 1st time")


    @staticmethod    
    def menu():
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
        cls.u.print_users()
    
    @classmethod
    def enter_user(cls):
        while True:
            userId = input(f"Enter UserID (Enter 0 to go back): ")
            if userId == "0":
                return ""
            else:
                if cls.u.check_user(userId):
                    return userId
                
    @classmethod
    def user_menu(cls,userId):
        while True:
            print()
            print(f"---------------Welcome {cls.u.get_name(userId)}---------------")
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
        while True:
            habit = input(f"Enter Habit (Enter 0 to go back): ")
            if habit == "0":
                break
            else:
                if cls.u.users[userId].mark_as_done(habit):
                    break 

    @classmethod
    def delete_habit(cls,userId):
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
        str_path = Storage.data_path()
        data = cls.u.store_user()
        Storage.save_json(str_path, data)
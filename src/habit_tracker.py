from habit import Habit

class Habit_Tracker:
    def __init__(self, name, datapath="data/habits.json"):
        self.name = name
        self.datapath = datapath
        self.habits = {}
        
    def add_habit(self, habit_name):
        # name_str = self.check_str(name)
        # if name_str != None:
        habit_name_str = self.check_str(habit_name)
        if habit_name_str != None:
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

    def mark_as_done(self, habit_name):
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
        for keys, values in habits.items():
            h = Habit()
            h.from_dict(values)
            self.habits.update({keys : h})

    def store_habits(self):
        dict = {"name" : self.name}
        for keys, values in self.habits.items():
            dict.update({keys : values.to_dict()})
        return dict
    
    def print_all(self):
        print(f"Name:\t{self.name}")
        for keys, values in self.habits.items():
            print(f"-------{keys}-------")
            values.print_all()
    
    def print_habits(self):
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
        try:
            return str(temp_str).lower()
        except:
            print("string casting failed try entering a string...")
            return None
   
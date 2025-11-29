from datetime import date

class Habit:
    def __init__(self, name = "", habit = ""):
        self.name = name
        self.habit = habit
        self.streak = 0
        self.history = []

    def mark_as_done(self):
        today = date.today()
        if today not in self.history:
            if((today.day - self.history[len(self.history) - 1].day) == 1):
                self.streak += 1
            else:
                self.streak = 1
            self.history.append(today)
            return True
        return False
    
    def check_done(self):
        today = date.today()
        if today in self.history:
            return True
        else:
            return False
        
    def store_history(self):
        return [d.isoformat() for d in self.history]
    
    def load_history(self, json_history):
        self.history = [date.fromisoformat(s) for s in json_history]
    
    def to_dict(self):
        return {
            "name" : self.name,
            "habit" : self.habit,
            "history" : self.store_history(),
            "streak" : self.streak  
        }
    
    def from_dict(self, dict):
        self.name  = dict["name"]
        self.habit = dict["habit"]
        self.load_history(dict["history"])
        self.streak = dict["streak"]
    
    def print_all(self):
        dict = self.to_dict()
        for keys, values in dict.items():
            print(f"{keys}\t:\t{values}")
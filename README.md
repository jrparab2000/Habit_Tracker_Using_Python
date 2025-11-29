# 🧩 Habit Tracker – Command Line Habit Management Tool

A simple and effective command-line tool to **manage daily habits**, **track streaks**, and **stay consistent**.  
This project allows you to create users, add habits, track progress, and get motivational quotes—helping you stay focused on personal growth.

## 🚀 Features

### 👤 Multi-User Support
- Add users  
- List existing users  
- Switch between users  
- Delete users  

### 📅 Habit Tracking
- Add new habits  
- View all habits  
- Mark habits as completed  
- Track habit streaks  
- Delete habits  

### 💬 Motivational Quotes
Each time you log in as a user, a motivational quote is displayed to encourage consistent progress.

### 💾 Persistent Data Storage
- Data is stored in `.json` format  
- Manual save required to make changes permanent  

### 🔍 Habit Suggestions
- Uses fuzzy matching to suggest similar habits  
- Suggestion database includes ~200 common habits  
- Custom habits can still be added freely

## 🛠 Setup Instructions

Before running the program, you need to set up your environment.

### 1️⃣ Activate the Virtual Environment (Recommended)

```
.\virtual_env\myenv\Scripts\Activate
```

### 2️⃣ Install Required Dependencies (If Needed)

If not using the virtual environment:

```
pip install requests
```

### 3️⃣ Run the Application

```
python main.py
```

## 📜 Main Menu

```
---------------Main Menu---------------
1.      Add User
2.      List Users
3.      Enter Current User
4.      Save
5.      Print all
6.      Exit
Enter your choice:
```

### Recommended First Step
Choose **Option 1: Add User** to create your profile.

Then proceed with:

👉 **Option 3: Enter Current User** to open the User Menu.

## 👤 User Menu

```
---------------Welcome <username>---------------
Summary:-
Your Habit of study:
Streak just broke
Your Habit of cycling:
Streak Never Started...

Motivation:-
The grass is greener where you water it.
1.      View Habits
2.      Add New Habit
3.      Mark Habit as Done for today
4.      Delete a Habit
5.      Delete this User
6.      Go Back
7.      Save
Enter your choice:
```

## ⚠️ Important: Saving Your Data

Changes are **NOT automatically saved** to the JSON file.

To save permanently:

- Use **Option 7** in the User Menu  
- Or **Option 4** in the Main Menu  

## 🔍 Habit Suggestions

- The system suggests similar habits using fuzzy matching  
- Based on a database of ~200 common habits  
- You can add any habit even if not suggested  

## 📈 Future Scope

- Export habits to CSV  
- Create a GUI version  
- Habit analytics (graphs/charts)  
- Calendar-based streak visualization  

## 📦 Example Project Structure

```
src/
│   main.py
│   user.py
│   habit.py
│   habit_tracker.py
│   reporter.py
│   storage.py
│   api_client.py
data/
│   data.json
│   valid_habits.json
virtual_env/
```

## 🙌 Thank You for Using Habit Tracker!

Stay consistent. Build great habits. Improve every day.

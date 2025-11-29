🧩 Habit Tracker – Command Line Habit Management Tool

A simple and effective command-line tool to manage daily habits, track streaks, and stay consistent.
This project allows you to create users, add habits, track progress, and get motivational quotes—helping you stay focused on personal growth.

🚀 Features
👤 Multi-User Support

Add users

List existing users

Switch between users

Delete users

📅 Habit Tracking

Add new habits

View all habits

Mark habits as completed

Track habit streaks

Delete habits

💬 Motivational Quotes

Each time you log in as a user, a motivational quote is displayed to encourage consistent progress.

💾 Persistent Data Storage

Data is stored in .json format

Manual save required to make changes permanent

🔍 Habit Suggestions

Uses fuzzy matching to suggest similar habits

Suggestion database includes ~200 common habits

Custom habits can still be added freely

🛠 Setup Instructions

Before running the program, you need to set up your environment.

1️⃣ Activate the Virtual Environment (Recommended)

If using the provided environment:

.\virtual_env\myenv\Scripts\Activate

2️⃣ Install Required Dependencies (If Needed)

If not using the virtual environment, install dependencies:

pip install requests

3️⃣ Run the Application

Start the tool using:

python main.py

📜 Main Menu

After running the program, you will see:

---------------Main Menu---------------
1.      Add User
2.      List Users
3.      Enter Current User
4.      Save
5.      Print all
6.      Exit
Enter your choice:

⭐ Recommended First Step

Choose Option 1: Add User to create your profile.

You will be asked for:

UserID

User Name

Then proceed with:

👉 Option 3: Enter Current User
to open the User Menu.

👤 User Menu

After selecting a user, you will see:

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

What You Can Do Here:

View your entire habit list

Add new habits

Mark habits as completed

Delete habits

Delete the current user

Save your progress

⚠️ Important: Saving Your Data

Changes are NOT automatically saved to the JSON file.

To save permanently:

Use Option 7 in the User Menu

Or Option 4 in the Main Menu

If you exit without saving, unsaved changes will be lost.

🔍 Habit Suggestions

When adding a new habit:

The system suggests similar habits from a database of ~200 common habits

Suggestions are based on fuzzy matching

You can still add any habit you want, even if not in the database

📈 Future Scope

Planned or possible improvements:

Export habit data to CSV for easier analysis

A GUI version for smoother user experience

Habit analytics and charts

Calendar-based streak tracking

📦 Example Project Structure
src/
│   main.py
│   user.py
│   habit.py
│   habit_matcher.py
│   tracker.py
│   storage.py
│   api_client.py
data/
│   habits.json
│   habits_db.json

🙌 Thank You for Using Habit Tracker!

Stay consistent. Build great habits. Improve every day.
If you'd like help adding more features or documentation, just let me know!
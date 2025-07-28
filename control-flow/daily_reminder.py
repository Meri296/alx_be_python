# daily_reminder.py

# Step 1: Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process the Task Based on Priority and Time Sensitivity
reminder_message = ""

match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _:
        reminder_message = f"'{task}' has an unknown priority level"

# Add time sensitivity
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += ". Consider completing it when you have free time."

# Step 3: Provide a Customized Reminder
print(f"Reminder: {reminder_message}")

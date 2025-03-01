import os
import datetime
import random  # Added import for randomization

# Get the current year
current_year = datetime.datetime.now().year

# Get the month as input
month = int(input("Enter the month (1-12): "))

# Check if the month is valid
if month < 1 or month > 12:
    print("Invalid month. Please enter a number between 1 and 12.")
    exit()

# Calculate the number of days in the given month
days_in_month = (datetime.date(current_year, month, 1) + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)
num_days = days_in_month.day

# Ensure the file exists
if not os.path.exists("file.txt"):
    with open("file.txt", "w") as f:
        f.write("")

# Perform random number of commits for each day of the month (minimum 50)
for day in range(1, num_days + 1):
    # Generate a random number of commits between 50 and a random max (between 60 and 100)
    max_commits = random.randint(60, 100)
    num_commits = random.randint(50, max_commits)
    
    print(f"Day {day}: Making {num_commits} commits")
    
    for _ in range(num_commits):
        date_str = f"{current_year}-{month:02d}-{day:02d}"
        with open("file.txt", "a") as f:
            f.write(date_str + '\n')
        os.system("git add .")
        commit_command = f"git commit --date=\"{date_str}\" -m 'commit'"
        os.system(commit_command)

# Push the commits to the remote repository
os.system("git push origin main")

import os
import datetime
import random
import subprocess  # Better for executing commands than os.system

# Get the year as input
year = int(input("Enter the year: "))

# Ensure the file exists
if not os.path.exists("file.txt"):
    with open("file.txt", "w") as f:
        pass  # Empty write is faster than writing an empty string

# Prepare git commands - using subprocess with shell=False is safer and faster
git_add = ["git", "add", "."]

# Precompute date ranges for the entire year
days_in_year = 366 if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 365

print(f"Making commits for all {days_in_year} days of {year}...")

# Build all the dates at once for efficiency
dates = []
current_date = datetime.date(year, 1, 1)
for _ in range(days_in_year):
    dates.append(current_date)
    current_date += datetime.timedelta(days=1)

# Batch file writes for better performance
with open("file.txt", "a") as f:
    for date in dates:
        # Generate a random number of commits between 50 and 90
        num_commits = random.randint(50, 90)
        
        print(f"{date.strftime('%Y-%m-%d')}: Making {num_commits} commits")
        
        date_str = date.strftime('%Y-%m-%d')
        
        # Write all dates for this day at once
        for _ in range(num_commits):
            f.write(date_str + '\n')
        
        # Flush to ensure content is written
        f.flush()
        
        # Git operations - only add once per day
        subprocess.run(git_add, check=True)
        
        # Make all commits for the day
        for _ in range(num_commits):
            commit_command = ["git", "commit", f"--date={date_str}", "-m", "commit"]
            subprocess.run(commit_command, check=True)

# Push the commits to the remote repository
print("Pushing commits to remote repository...")
subprocess.run(["git", "push", "origin", "main"], check=True)

print(f"Successfully made commits for all days in {year}")

# import os
# import random

# if not os.path.exists("file.txt"):
#     with open("file.txt", "w") as f:
#         f.write("")

# for i in range(1, 800):
#     for j in range(0, random.randint(1, 10)):
#         d = str(i) + ' days ago'
#         with open("file.txt", "a") as f:
#             f.write(d + '\n')
#         os.system("git add .")
#         commit_command = f"git commit --date=\"{d}\" -m 'commit'"
#         os.system(commit_command)

# os.system("git push origin main")


import os
import datetime

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

# Perform 20 commits for each day of the month
for day in range(1, num_days + 1):
    for _ in range(20):
        date_str = f"{current_year}-{month:02d}-{day:02d}"
        with open("file.txt", "a") as f:
            f.write(date_str + '\n')
        os.system("git add .")
        commit_command = f"git commit --date=\"{date_str}\" -m 'commit'"
        os.system(commit_command)

# Push the commits to the remote repository
os.system("git push origin main")

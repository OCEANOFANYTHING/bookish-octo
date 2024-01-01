import os
import datetime
import random
import subprocess  # Better for executing commands than os.system

# Get the year as input
year = int(input("Enter the year: "))

# Get GitHub email and name for proper attribution
github_email = input("Enter your GitHub email address: ")
github_name = input("Enter your GitHub username: ")

# Configure Git with the provided credentials for this repository
subprocess.run(["git", "config", "user.email", github_email], check=True)
subprocess.run(["git", "config", "user.name", github_name], check=True)

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

total_commits = 0

# Process each day
for date in dates:
    # Generate a random number of commits between 50 and 90
    num_commits = random.randint(50, 90)
    
    print(f"{date.strftime('%Y-%m-%d')}: Making {num_commits} commits")
    
    date_str = date.strftime('%Y-%m-%d')
    
    # Make unique changes and commits for each commit in the day
    for i in range(num_commits):
        # Write unique content for each commit
        with open("file.txt", "a") as f:
            f.write(f"{date_str}-commit-{i+1}\n")
        
        # Add and commit
        subprocess.run(git_add, check=True)
        
        try:
            # Use GIT_AUTHOR_DATE and GIT_COMMITTER_DATE environment variables for better compatibility
            env = os.environ.copy()
            env['GIT_AUTHOR_DATE'] = f"{date_str}T12:00:00"
            env['GIT_COMMITTER_DATE'] = f"{date_str}T12:00:00"
            
            commit_command = ["git", "commit", "-m", f"commit-{date_str}-{i+1}"]
            subprocess.run(commit_command, env=env, check=True)
            total_commits += 1
        except subprocess.CalledProcessError:
            print(f"Warning: Commit failed for {date_str}-{i+1}, continuing with next commit")
            continue

# Push the commits to the remote repository
print(f"Pushing {total_commits} commits to remote repository...")
try:
    subprocess.run(["git", "push", "-f", "origin", "main"], check=True)
    print(f"Successfully made {total_commits} commits for all days in {year}")
except subprocess.CalledProcessError:
    print("Push failed. You may need to push manually with 'git push -f origin main'")

print("\nIMPORTANT: For commits to show in your GitHub contribution graph:")
print("1. Make sure you used the same email address associated with your GitHub account")
print("2. Verify the repository is public on GitHub")
print("3. Check that you're pushing to the default branch (main or master)")

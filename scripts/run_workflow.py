import subprocess
from datetime import datetime
import os

def run(cmd):
    print(f"\nRunning: {cmd}")
    subprocess.run(cmd, shell=True)

print("Starting automated workflow...")

# Pull latest changes
run("git pull")

# Check repo status
status = subprocess.check_output(
    "git status --porcelain",
    shell=True
).decode()

print("\nUpdating documentation...")

os.makedirs("docs", exist_ok=True)

with open("docs/automation_log.txt", "a") as f:
    f.write(
        f"Workflow executed at {datetime.now()}\n"
    )

if status.strip():

    print("\nChanges detected — committing.")

    run("git add .")
    run('git commit -m "Automated workflow update"')
    run("git push")

else:

    print("\nNo changes detected — skipping commit.")

print("\nWorkflow complete.")

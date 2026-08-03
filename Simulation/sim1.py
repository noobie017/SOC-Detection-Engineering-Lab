import datetime
import time
import os
import random

# ============== CONFIG ==============
LOG_FILE = r"C:\Temp\normal_user_activity.log"
START_DATE = datetime.date(2026, 8, 3)   # Change to whatever Monday you want
DAYS = 5                                 # Monday to Friday
WORK_START = 6                           # 06:00
WORK_END = 15                            # 15:00
EVENTS_PER_DAY = 8                       # How many "login / activity" events per day
# ====================================

def write_log(timestamp, message):
    line = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} | NORMAL | {message}"
    print(line)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def generate_week():
    print(f"Generating normal user routine for {DAYS} days starting {START_DATE}")
    print(f"Log file: {LOG_FILE}\n")

    current_date = START_DATE

    for day in range(DAYS):
        # Skip weekends automatically if you start on Monday
        if current_date.weekday() >= 5:  # 5=Saturday, 6=Sunday
            current_date += datetime.timedelta(days=1)
            continue

        print(f"--- {current_date.strftime('%A %Y-%m-%d')} ---")

        # Generate several events spread across the work day
        for i in range(EVENTS_PER_DAY):
            # Random time between 06:00 and 15:00
            hour = random.randint(WORK_START, WORK_END - 1)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)

            event_time = datetime.datetime.combine(
                current_date, 
                datetime.time(hour, minute, second)
            )

            # Simple realistic messages
            activities = [
                "User logon successful (interactive)",
                "User session started",
                "Outlook process launched",
                "Browser started - normal browsing",
                "File Explorer opened",
                "User locked workstation",
                "User unlocked workstation",
                "Logoff / session end"
            ]
            msg = random.choice(activities)
            write_log(event_time, msg)

            # Tiny pause so the file writes cleanly
            time.sleep(0.05)

        current_date += datetime.timedelta(days=1)

    print(f"\nDone! {DAYS} days of normal activity written to:")
    print(LOG_FILE)

if __name__ == "__main__":
    generate_week()

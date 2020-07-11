from datetime import timedelta

def seconds_per_hours(hours):
    return 60 * 60 * hours

def seconds_per_minutes(minutes):
    return 60 * minutes

def main():
    hours = int(input("Add hours: "))
    minutes = int(input("Add minutes: "))

    seconds = seconds_per_hours(hours) + seconds_per_minutes(minutes)
    print(f"There are {seconds} seconds in {hours} hours {minutes} minutes")

    # Using timedelta

    delta = timedelta(hours=hours, minutes=minutes)
    print(f"timedelta: {int(delta.total_seconds())}")

if __name__ == "__main__":
    main()
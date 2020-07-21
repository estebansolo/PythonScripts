from datetime import datetime

def next_birthday(date, now):
    if date < now:
        date = date.replace(year=date.year + 1)

    diff = date - now
    hours, seconds = divmod(diff.seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)

    return (diff.days, hours, minutes, seconds)

def main():
    print("Next Birthday".center(50))
    print("*" * 50)

    now = datetime.now()

    while True:
        try:
            day = int(input("Day: "))
            month = int(input("Month (numeric): "))
            converted_date = datetime(day=day, month=month, year=now.year)
        except:
            print("There was an error, please try again.")
        else:
            break
    
    birthday = next_birthday(converted_date, now)
    print(f"Your next birthday is in {birthday[0]} days, {birthday[1]} hours, {birthday[2]} minutes, {birthday[3]} seconds.")

if __name__ == "__main__":
    main()
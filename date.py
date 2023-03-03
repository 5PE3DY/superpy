import datetime
import csv
import os


def init_date():
    if "day.csv":
        os.remove("day.csv")
    with open("day.csv", "w", newline="") as time_file:
        today = datetime.date.today()
        today_string = today.strftime("%Y-%m-%d")
        fields = ["date"]
        date_writer = csv.DictWriter(time_file, fieldnames=fields)
        date_writer.writeheader()
        date_writer.writerow({"date": today_string})
    today = get_day()
    print(f"Current date is: {today}")


def get_day():
    with open("day.csv", "r") as day_file:
        reader = csv.reader(day_file)
        next(reader)
        for line in reader:
            today = line[0]
            day = datetime.datetime.strptime(today, "%Y-%m-%d").date()
            return day

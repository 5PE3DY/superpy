# Imports
import argparse
import csv
import datetime
import os
from graph import get_graph
from date import get_day, init_date
from tables import inventory_table
from report_list import (
    create_inventory_report,
    create_revenue_report,
    create_profit_report,
)

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.


def buy():
    if args.product_name is None:
        raise SyntaxError("Product name not listed")
    elif args.price is None:
        raise SyntaxError("Price not listed")
    elif args.exp_date is None:
        raise SyntaxError("Expiration Date not listed")
    with open("bought.csv", "r") as bought_file:
        reader = csv.DictReader(bought_file)
        lines = len(list(reader))
        id = lines + 1
    with open("bought.csv", "a", newline="") as bought_file:
        fields = ["id", "product_name", "buy_date", "buy_price", "exp_date"]
        bought_writer = csv.DictWriter(bought_file, fieldnames=fields)
        line = {
            "id": id,
            "product_name": args.product_name,
            "buy_date": get_day(),
            "buy_price": args.price,
            "exp_date": args.exp_date,
        }
        bought_writer.writerow(line)
    print("You bought this product!")


def sell():
    if args.product_name is None:
        raise SyntaxError("Product name not listed")
    elif args.price is None:
        raise SyntaxError("Price not listed")
    with open("sold.csv", "r") as sold_file:
        bought_id_list = []
        total_rows = 0
        reader = csv.DictReader(sold_file)
        for item in reader:
            bought_id_list.append(item["bought_id"])
            total_rows += 1
        id = total_rows + 1
    with open("bought.csv", "r") as bought_file:
        reader = csv.DictReader(bought_file)
        for line in reader:
            if str(line["id"]) not in bought_id_list:
                if args.product_name == line["product_name"]:
                    today = int(get_day().strftime("%Y%m%d"))
                    exp_date_int = int(
                        datetime.datetime.strptime(
                            line["exp_date"], "%Y-%m-%d"
                        ).strftime("%Y%m%d")
                    )
                    if exp_date_int > today:
                        bought_id = line["id"]
                        with open("sold.csv", "a", newline="") as sold_file:
                            fieldnames = ["id", "bought_id", "sell_date", "sell_price"]
                            sold_writer = csv.DictWriter(
                                sold_file, fieldnames=fieldnames
                            )
                            new_line = {
                                "id": id,
                                "bought_id": bought_id,
                                "sell_date": get_day(),
                                "sell_price": args.price,
                            }
                            sold_writer.writerow(new_line)
                            print("You sold this product!")
                            break
        else:
            raise ValueError("This Product is not in stock!")


def report():

    if args.inventory:
        # In case report --inventory --today
        if args.today:
            create_inventory_report()
            print("Created today's inventory report!")
            inventory_table()
        # in case report --inventory --yesterday
        elif args.yesterday:
            change_date(-1)
            create_inventory_report()
            print("created yesterday's inventory report!")
            inventory_table()
            change_date(1)
        # in case report --inventory --date
        elif args.date:
            date_int = int(
                datetime.datetime.strptime(args.date, "%Y-%m-%d").strftime("%Y%m%d")
            )
            today = int(get_day().strftime("%Y%m%d"))
            delta = date_int - today
            change_date(delta)
            print(f"Created a inventory report of {args.date}")
            create_inventory_report()
            inventory_table()
            change_date(0 - delta)
        elif args.last_week:
            raise SyntaxError(
                "Only use --last_week for a profit-report or revenue-report"
            )
        else:
            print("Created today's inventory report!")
            create_inventory_report()
            inventory_table()
    elif args.revenue:
        # in case report --revenue --today
        if args.today:
            revenue = create_revenue_report()
            print(f"Today's revenue is {revenue}, so far.")
        # in case report --revenue --yesterday
        elif args.yesterday:
            change_date(-1)
            todayy = get_day()
            print(todayy)
            revenue = create_revenue_report()
            print(f"Yesterday's revenue was {revenue}")
            change_date(1)
        # in case report --revenue --date
        elif args.date:
            date_int = int(
                datetime.datetime.strptime(args.date, "%Y-%m-%d").strftime("%Y%m%d")
            )
            today = int(get_day().strftime("%Y%m%d"))
            delta = date_int - today
            change_date(delta)
            revenue = create_revenue_report()
            change_date(0 - delta)
            print(f"Revenue on {args.date} was {revenue}")
        # in case report --revenue --last_week
        elif args.last_week:
            i = 7
            revenue_list = []
            date_list = []
            while i > 0:
                change_date(0 - i)
                date = get_day().strftime("%Y-%m-%d")
                date_list.append(date)
                rev = create_revenue_report()
                revenue_list.append(rev)
                change_date(i)
                i -= 1
            rev = create_revenue_report()
            revenue_list.append(rev)
            date = get_day().strftime("%Y-%m-%d")
            date_list.append(date)
            # in case report --revenue --last_week --show_graph
            if args.show_graph:
                get_graph(date_list, revenue_list, "Revenue")
                print("Graph created in Revenue_graph.png")
            else:
                total_revenue = sum(revenue_list)
                print(f"Last week's revenue was {total_revenue}")
        else:
            revenue = create_revenue_report()
            print(f"Today's revenue is {revenue}, so far.")
    elif args.profit:
        # in case report --profit --today
        if args.today:
            profit = create_profit_report()
            print(f"Today's profit is {profit}, so far.")
        # in case report --profit --yesterday
        elif args.yesterday:
            change_date(-1)
            profit = create_profit_report()
            print(f"Yesterdays profit was {profit}.")
            change_date(1)
        # in case report --profit --date
        elif args.date:
            date_int = int(
                datetime.datetime.strptime(args.date, "%Y-%m-%d").strftime("%Y%m%d")
            )
            today = int(get_day().strftime("%Y%m%d"))
            delta = date_int - today
            change_date(delta)
            profit = create_profit_report()
            change_date(0 - delta)
            print(f"Profit on {args.date} was {profit}")
        # in case report --profit --last_week
        elif args.last_week:
            i = 7
            profit_list = []
            date_list = []
            while i > 0:
                change_date(0 - i)
                date = get_day().strftime("%Y-%m-%d")
                date_list.append(date)
                prof = create_profit_report()
                profit_list.append(prof)
                change_date(i)
                i -= 1
            prof = create_profit_report()
            profit_list.append(prof)
            date = get_day().strftime("%Y-%m-%d")
            date_list.append(date)
            # in case report --profit --last_week --show_graph
            if args.show_graph:
                get_graph(date_list, profit_list, "Profit")
                print("Graph created in Profit_graph.png")
            else:
                total_profit = sum(profit_list)
                print(f"Last week's profit was {total_profit}")
        else:
            profit = create_profit_report()
            print(f"Today's profit is {profit}, so far.")
    else:
        raise SyntaxError("Forgot to specify report type!")


def change_date(number=None):
    if args.advance_date:
        number = args.advance_date
    with open("day.csv", "r") as time_file:
        reader = csv.reader(time_file)
        next(reader)
        for line in reader:
            for item in line:
                found_day = datetime.datetime.strptime(item, "%Y-%m-%d")
                delta = datetime.timedelta(days=number)
                new_day = found_day + delta
                new_day_string = new_day.strftime("%Y-%m-%d")
                with open("day.csv", "w", newline="") as time_file:
                    names = ["date"]
                    writer = csv.DictWriter(time_file, fieldnames=names)
                    writer.writeheader()
                    writer.writerow({"date": new_day_string})
    if args.advance_date:
        today = get_day()
        print(f"Date set to {today}")


def export_to_csv():
    if args.expired_items:
        try:
            os.remove("expired_report.csv")
        except FileNotFoundError:
            pass
        today = get_day()
        today_string = today.strftime("%Y%m%d")
        today_int = int(today_string)
        with open("sold.csv", "r") as sold_file:
            reader = csv.reader(sold_file)
            sold_id_list = []
            for line in reader:
                sold_id_list.append(line[1])
        with open("bought.csv", "r") as bought_file:
            reader = csv.DictReader(bought_file)
            for line in reader:
                exp_date = line["exp_date"]
                exp_date_int = int(
                    datetime.datetime.strptime(exp_date, "%Y-%m-%d").strftime("%Y%m%d")
                )
                if exp_date_int < today_int:
                    if line["id"] not in sold_id_list:
                        with open("expired_report.csv", "a") as expired_report:
                            fieldnames = [
                                "id",
                                "product_name",
                                "buy_date",
                                "buy_price",
                                "exp_date",
                            ]
                            writer = csv.DictWriter(
                                expired_report, fieldnames=fieldnames
                            )
                            writer.writerow(line)
            if os.path.exists("expired_report.csv"):
                print("expired_report.csv created!")
            else:
                print("No records to be exported!")
    if args.double_items:
        try:
            os.remove("double_item_report.csv")
        except FileNotFoundError:
            pass
        create_inventory_report()
        with open("inventory.csv", "r") as inventory_file:
            item_list = []
            duplicate_item_list = []
            reader = csv.reader(inventory_file)
            for line in reader:
                if line[1] not in item_list:
                    item_list.append(line[1])
                else:
                    duplicate_item_list.append(line[1])
        with open("inventory.csv", "r") as inventory_file:
            reader = csv.reader(inventory_file)
            for line in reader:
                if line[1] in duplicate_item_list:
                    with open(
                        "double_item_report.csv", "a", newline=""
                    ) as double_item_report:
                        writer = csv.writer(double_item_report)
                        writer.writerow(line)
        if os.path.exists("double_item_report.csv"):
            print("double_item_report.csv created!")
        else:
            print("No records to be exported!")


# This is the group of functions which comprise the main commands.
function_map = {
    "buy": buy,
    "report": report,
    "sell": sell,
    "init": init_date,
    "time-change": change_date,
    "export": export_to_csv,
}


parser = argparse.ArgumentParser(description="Update or report stock values")
parser.add_argument(
    "command",
    choices=function_map.keys(),
    help=">>>> init <<<<  Use on start of program to initialize a date in date.csv >>>> buy <<<<  Use to add item to inventory. Provide --product_name, --price and --exp_date >>>> sell <<<<  Use to sell a product from your inventory. Provide --product_name and --price >>>> report <<<<  Use to report --inventory --revenue or --profit >>>> time-change <<<<  Use to change the date. Provide --advance_date. >>>> export <<<< use to export data to csv-files. Provide --exp_items or --double_items",
)
parser.add_argument(
    "--inventory", action="store_true", help="Ask report function for inventory report"
)
parser.add_argument(
    "--profit", action="store_true", help="Ask report function for profit report"
)
parser.add_argument(
    "--revenue", action="store_true", help="Ask report function for revenue report"
)
parser.add_argument(
    "--expired_items",
    action="store_true",
    help="Use with export command to create csv-file with expired items in stock",
)
parser.add_argument(
    "--double_items",
    action="store_true",
    help="Use with export command to show a list of all items in stock at least twice",
)
parser.add_argument(
    "--product_name", type=str, help="Description of product", metavar=""
)
parser.add_argument(
    "--price",
    type=float,
    help="Price for which the product was sold/bought",
    metavar="",
)
parser.add_argument(
    "--exp_date",
    type=str,
    help="product expiration date in YYYY-MM-DD format",
    metavar="",
)
parser.add_argument(
    "--advance_date",
    type=int,
    help="Amount of days to advance the date. Can be negative",
    metavar="",
)
parser.add_argument(
    "--show_graph",
    action="store_true",
    help="Use with --last week to show bar graph of revenue or profit ",
)
parser.add_argument("--today", action="store_true", help="Ask for report of today")
parser.add_argument(
    "--yesterday", action="store_true", help="Ask for report of yesterday"
)
parser.add_argument(
    "--last_week",
    action="store_true",
    help="Add to create report over last week. Only with report --profit or report --revenue",
)
parser.add_argument(
    "--date", type=str, help="Ask for report of specific date", metavar=""
)

args = parser.parse_args()
func = function_map[args.command]
func()

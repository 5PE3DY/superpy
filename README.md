# superpy
With python created a super market programm voor this assignment

INSTRUCTIONS

1. Initialize new date
running 'python main.py init' creates a "day.csv" file which contains today's date. This date can be altered.

2. Change date
running 'python main.py time-change --advance time {int}' advances the time forwards if a positive integer and backwards is a
negative integer is provided. This overwrites the "day.csv" file.

EXAMPLE: python main.py time-change --advance time 2

3. Buy products
running 'python main.py buy --product_name {str} --price {float} --exp_date {str YYYY-MM-DD}' adds an item to the inventory.
The bought items are added to "bought.csv"

EXAMPLE: python main.py buy --product_name cheese --price 3.2 --exp_date 2022-04-01

4. Sell products
running 'python main.py sell --product_name {str} --price {float}' sells an item, if the item is in stock. The sold items are 
added to "sold.csv"

EXAMPLE: python main.py sell --product_name cheese --price 4.8

5. Report list

5.1 Inventory report
running 'python main.py report --inventory' creates an inventory report, both in the terminal and in "inventory.csv". You can
specify --today, --yesterday or --date {str YYYY-MM-DD} to see an inventory report from a specific day. If not specified, --today
is default.

EXAMPLE: python main.py report --inventory --yesterday

5.2 Revenue report
running 'python main.py report --revenue' returns the revenue. You can specify --today, --yesterday --last_week or --date 
{str YYYY-MM-DD} to get the revenue from a specific day. If not specified, --today is default. Use --last_week with --show_graph
to see a bar graph of last week's revenue.

EXAMPLE: python main.py report --revenue --date 2022-02-17

5.3 Profit report
running 'python main.py report --profit' returns the profit. You can specify --today, --yesterday --last_week or --date 
{str YYYY-MM-DD} to get the profit from a specific day. If not specified, --today is default. Use --last_week with --show_graph
to see a bar graph of last week's profit.

EXAMPLE: python main.py report --profit --last_week --show_graph

6. Export

6.1 Export Expired Items to csv
running 'python main.py export --expired_items' creates a CSV-file with all items past the expiration date, currently in stock.

EXAMPLE: python main.py export --expired_items

6.2 Export Duplicate Items to csv
running 'python main.py export --double_items' creates a CSV-file with all duplicate items, currently in stock.

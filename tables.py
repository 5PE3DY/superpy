from rich.console import Console
from rich.table import Table
import csv


def inventory_table():
    table = Table(title="Inventory")
    table.add_column("Product name", style="cyan")
    table.add_column("Purchase price", style="magenta")
    table.add_column("Expiration Date", style="green")
    with open("inventory.csv", "r") as inventory_file:
        reader = csv.reader(inventory_file)
        for line in reader:
            table.add_row(line[1], line[3], line[4])
    console = Console()
    console.print(table)

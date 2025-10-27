"""
Inventory Management System.

A simple system to manage stock items with add, remove,
and reporting functions.
"""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory.
    Args:
        item (str): Name of the item to add.
        qty (int): Quantity to add.
        logs (list, optional): List to append log messages to.
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    timestamp = str(datetime.now())
    log_message = f"{timestamp}: Added {qty} of {item}"
    logs.append(log_message)


def remove_item(item, qty):
    """
    Remove some quantity of item from inventory.
    Args:
        item (str): Name of item to be removed.
        qty (int): The amount to be remove.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Item '{item}' not found in inventory")


def get_qty(item):
    """
    Get the quantity of an item present in the inventory.
    Args:
        item (str): Name item.
    Returns:
        int: Quantity in stock.
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.
    Args:
        file (str): Path to the JSON file to load. Defaults to 'inventory.json'
    """
    global stock_data  # pylint: disable=global-statement
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.loads(f.read())


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.
    Args:
        file (str): Path to the JSON file to save. Defaults to 'inventory.json'
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


def print_data():
    """Print a report of all items currently in inventory."""
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(threshold=5):
    """
    Check for items below a threshold quantity.
    Args:
        threshold (int): Minimum quantity threshold. Defaults to 5.
    Returns:
        list: List of item names below the threshold.
    """
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():
    """Run main program to demonstrate inventory system functionality."""
    add_item("apple", 10)
    add_item("banana", -2)
    # add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)  # not found
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print('Direct print - no eval needed')


main()

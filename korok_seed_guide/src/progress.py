"""
Module: progress
This module provides functions to save and load Korok seed progress using JSON files.
"""

import json


def save_progress(korok_seeds, filename="progress.json"):
    """
    Save the current Korok seed progress to a file.

    Args:
        korok_seeds (list[dict]): The current list of all Korok seeds.
        filename (str): The name of the file to save the progress to (default: 'progress.json').
    """
    with open(filename, "w") as file:
        json.dump(korok_seeds, file)


def load_progress(filename="progress.json"):
    """
    Load Korok seed progress from a file.

    Args:
        filename (str): The name of the file to load progress from (default: 'progress.json').

    Returns:
        list[dict] or None: The loaded seed progress, or None if the file does not exist.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

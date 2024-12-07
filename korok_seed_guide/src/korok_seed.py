"""
Module: korok_seeds
This module manages Korok seed data and provides functions to interact with the seed dataset.
"""

korok_seeds = [
    {"id": 1, "location": "Great Plateau", "coordinates": (100, 200), "found": False},
    {"id": 2, "location": "Dueling Peaks", "coordinates": (150, 250), "found": False},
    # More seeds can be added here...
]


def get_seeds_by_region(region):
    """
    Retrieve all Korok seeds in a specific region.

    Args:
        region (str): The name of the region to filter seeds by.

    Returns:
        list[dict]: A list of seed dictionaries matching the specified region.
    """
    return [seed for seed in korok_seeds if seed["location"] == region]


def mark_seed_as_found(seed_id):
    """
    Mark a specific Korok seed as found.

    Args:
        seed_id (int): The unique identifier of the seed to mark.

    Returns:
        bool: True if the seed was found and marked, False if the seed ID does not exist.
    """
    seed = next((s for s in korok_seeds if s["id"] == seed_id), None)
    if seed:
        seed["found"] = True
        return True
    return False
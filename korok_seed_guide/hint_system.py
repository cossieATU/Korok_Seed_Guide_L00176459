"""
Module: hint_system
This module provides functionality to generate Korok seed hints.
"""

from math import sqrt


def get_seed_hint(player_coords, hint_cost, credits, korok_seeds):
    """
    Generate a hint for the closest unfound Korok seed.

    Args:
        player_coords (tuple): Player's current coordinates (x, y).
        hint_cost (int): The cost of a hint in credits.
        credits (Credits): An instance of the Credits class to manage deductions.
        korok_seeds (list[dict]): A list of all Korok seeds.

    Returns:
        dict or None: The closest unfound seed's details, or None if credits are insufficient.
    """
    if not credits.deduct_credits(hint_cost):
        return None

    # Find the closest unfound seed
    closest_seed = None
    closest_distance = float("inf")

    for seed in korok_seeds:
        if not seed["found"]:
            distance = sqrt(
                (seed["coordinates"][0] - player_coords[0]) ** 2 +
                (seed["coordinates"][1] - player_coords[1]) ** 2
            )
            if distance < closest_distance:
                closest_distance = distance
                closest_seed = seed

    return closest_seed

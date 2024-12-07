"""
Module: credits
This module implements a credits system for managing the player's credit balance.
"""


class Credits:
    """
    A class to manage player credits.
    """

    def __init__(self):
        """
        Initialize a new Credits instance with a zero balance.
        """
        self._balance = 0

    def add_credits(self, amount):
        """
        Add credits to the player's balance.

        Args:
            amount (int): The number of credits to add.
        """
        self._balance += amount

    def deduct_credits(self, amount):
        """
        Deduct credits from the player's balance.

        Args:
            amount (int): The number of credits to deduct.

        Returns:
            bool: True if the deduction was successful, False otherwise.
        """
        if self._balance >= amount:
            self._balance -= amount
            return True
        return False

    def get_balance(self):
        """
        Get the current credit balance.

        Returns:
            int: The player's current balance.
        """
        return self._balance

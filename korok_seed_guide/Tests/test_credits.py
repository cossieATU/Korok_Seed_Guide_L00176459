# test_credits.py

import pytest
from credits import Credits

# Test the initial balance
def test_initial_balance():
    credit_system = Credits()
    assert credit_system.get_balance() == 0  # The balance should be 0 initially.

# Test adding credits to the balance
def test_add_credits():
    credit_system = Credits()
    credit_system.add_credits(100)
    assert credit_system.get_balance() == 100  # After adding 100, balance should be 100.
    
    credit_system.add_credits(50)
    assert credit_system.get_balance() == 150  # After adding 50, balance should be 150.

# Test adding zero credits to the balance
def test_add_zero_credits():
    credit_system = Credits()
    credit_system.add_credits(0)  # Add zero credits
    assert credit_system.get_balance() == 0  # Balance should remain unchanged.

# Test deducting credits from the balance (successful case)
def test_deduct_credits_success():
    credit_system = Credits()
    credit_system.add_credits(100)  # Add 100 credits
    result = credit_system.deduct_credits(50)  # Deduct 50 credits
    assert result is True  # The deduction should be successful
    assert credit_system.get_balance() == 50  # Balance should be 50 after deduction.

# Test deducting credits from the balance (failure case)
def test_deduct_credits_failure():
    credit_system = Credits()
    credit_system.add_credits(100)  # Add 100 credits
    result = credit_system.deduct_credits(150)  # Attempt to deduct 150 credits, more than available
    assert result is False  # The deduction should fail
    assert credit_system.get_balance() == 100  # Balance should remain 100.

# Test deducting credits when no credits are available
def test_deduct_credits_no_balance():
    credit_system = Credits()
    result = credit_system.deduct_credits(10)  # Attempt to deduct when no credits are present
    assert result is False  # The deduction should fail
    assert credit_system.get_balance() == 0  # Balance should still be 0.

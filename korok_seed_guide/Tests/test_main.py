import pytest
from unittest.mock import patch, MagicMock
from main import display_main_menu, main


def test_display_main_menu(capsys):
    """
    Test the display_main_menu function to ensure it prints the correct menu options.
    """
    display_main_menu()
    captured = capsys.readouterr()
    expected_output = (
        "\nKorok Seed Guide\n"
        "1. View seeds by region\n"
        "2. Mark seed as found\n"
        "3. Get seed hint\n"
        "4. Save progress\n"
        "5. Load progress\n"
        "6. Check credits balance\n"
        "0. Exit\n"
    )
    assert captured.out == expected_output


@patch('main.get_seeds_by_region')
@patch('builtins.input', side_effect=["1", "Hyrule Field", "0"])  # Option 1, Region, Exit
@patch('builtins.print')
def test_view_seeds_by_region(mock_print, mock_input, mock_get_seeds_by_region):
    """
    Test the 'View seeds by region' functionality.
    """
    mock_get_seeds_by_region.return_value = [
        {"id": 1, "location": "Near Tree", "found": False},
        {"id": 2, "location": "By River", "found": True},
    ]

    with patch('main.korok_seeds', []):  # Mock korok_seeds
        main()

    mock_print.assert_any_call("Seed ID: 1, Location: Near Tree, Status: Not Found")
    mock_print.assert_any_call("Seed ID: 2, Location: By River, Status: Found")
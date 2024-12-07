"""
Module: main
This module serves as the entry point for the Korok Seed Guide application.
"""

from korok_seeds import korok_seeds, get_seeds_by_region, mark_seed_as_found
from credits import Credits
from hint_system import get_seed_hint
from progress import save_progress, load_progress


def display_main_menu():
    """
    Display the main menu of the application.
    """
    print("\nKorok Seed Guide")
    print("1. View seeds by region")
    print("2. Mark seed as found")
    print("3. Get seed hint")
    print("4. Save progress")
    print("5. Load progress")
    print("6. Check credits balance")
    print("0. Exit")


def main():
    """
    Main function to run the application.
    """
    credits = Credits()
    credits.add_credits(50)  # Starting balance

    while True:
        display_main_menu()
        choice = input("Select an option: ")

        if choice == "1":
            region = input("Enter region name: ")
            seeds = get_seeds_by_region(region)
            if seeds:
                for seed in seeds:
                    status = "Found" if seed["found"] else "Not Found"
                    print(f"Seed ID: {seed['id']}, Location: {seed['location']}, Status: {status}")
            else:
                print("No seeds found in this region.")

        elif choice == "2":
            try:
                seed_id = int(input("Enter seed ID to mark as found: "))
                if mark_seed_as_found(seed_id):
                    print(f"Seed {seed_id} marked as found.")
                else:
                    print("Seed ID not found.")
            except ValueError:
                print("Invalid seed ID.")

        elif choice == "3":
            player_coords = tuple(map(int, input("Enter your coordinates (x y): ").split()))
            hint_cost = 10
            hint = get_seed_hint(player_coords, hint_cost, credits, korok_seeds)
            if hint:
                print(f"Hint: Look near {hint['location']} at {hint['coordinates']}.")
            else:
                print("Not enough credits or no seeds left!")

        elif choice == "4":
            save_progress(korok_seeds)
            print("Progress saved.")

        elif choice == "5":
            loaded_data = load_progress()
            if loaded_data:
                korok_seeds[:] = loaded_data  # Update in-place
                print("Progress loaded.")
            else:
                print("No saved progress found.")

        elif choice == "6":
            print(f"Credits balance: {credits.get_balance()}")

        elif choice == "0":
            print("Exiting Korok Seed Guide.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

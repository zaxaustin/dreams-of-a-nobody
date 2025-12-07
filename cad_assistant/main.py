
import sys
import os

# Add the parent directory to sys.path so modules can be imported if run directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cad_assistant import materials
from cad_assistant import tips
from cad_assistant import prototype_logger

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("========================================")
    print("       CAD & PROTOTYPING ASSISTANT      ")
    print("========================================")

def show_materials_menu():
    while True:
        clear_screen()
        print_header()
        print("\n--- Material Guide ---")
        available = materials.list_materials()
        for i, mat in enumerate(available):
            print(f"{i+1}. {mat}")
        print("0. Back")

        choice = input("\nSelect a material (0-{}): ".format(len(available)))

        if choice == '0':
            break

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(available):
                mat_name = available[idx]
                info = materials.get_material_info(mat_name)

                print(f"\n--- {mat_name} ---")
                print(f"Description: {info['description']}")
                print(f"Nozzle Temp: {info['nozzle_temp']}")
                print(f"Bed Temp:    {info['bed_temp']}")
                print(f"Shrinkage:   {info['shrinkage']}")
                print("Pros:")
                for pro in info['pros']:
                    print(f"  + {pro}")
                print("Cons:")
                for con in info['cons']:
                    print(f"  - {con}")

                input("\nPress Enter to continue...")
            else:
                input("Invalid selection. Press Enter...")
        except ValueError:
            input("Invalid input. Press Enter...")

def show_tips_menu():
    while True:
        clear_screen()
        print_header()
        print("\n--- Design Tips ---")
        categories = tips.get_all_categories()
        for i, cat in enumerate(categories):
            print(f"{i+1}. {cat}")
        print(f"{len(categories)+1}. Get Random Tip")
        print("0. Back")

        choice = input(f"\nSelect a category (0-{len(categories)+1}): ")

        if choice == '0':
            break

        try:
            idx = int(choice) - 1
            if idx == len(categories):
                print(f"\n{tips.get_random_tip()}")
                input("\nPress Enter to continue...")
            elif 0 <= idx < len(categories):
                cat = categories[idx]
                cat_tips = tips.get_tips_by_category(cat)
                print(f"\n--- {cat} Tips ---")
                for t in cat_tips:
                    print(f"* {t}")
                input("\nPress Enter to continue...")
            else:
                input("Invalid selection. Press Enter...")
        except ValueError:
            input("Invalid input. Press Enter...")

def show_logger_menu():
    while True:
        clear_screen()
        print_header()
        print("\n--- Prototype Logger ---")
        print("1. List Ideas")
        print("2. Add New Idea")
        print("3. Delete Idea")
        print("0. Back")

        choice = input("\nSelect an option: ")

        if choice == '0':
            break
        elif choice == '1':
            ideas = prototype_logger.list_ideas()
            if not ideas:
                print("\nNo ideas saved yet.")
            else:
                print(f"\nFound {len(ideas)} ideas:")
                for i, idea in enumerate(ideas):
                    print(f"\n[{i+1}] {idea['title']} ({idea['timestamp']})")
                    print(f"    {idea['description']}")
            input("\nPress Enter to continue...")
        elif choice == '2':
            print("\nNew Idea Entry:")
            title = input("Title: ")
            if title:
                desc = input("Description: ")
                prototype_logger.save_idea(title, desc)
                print("Idea saved!")
            else:
                print("Title cannot be empty.")
            input("\nPress Enter to continue...")
        elif choice == '3':
            ideas = prototype_logger.list_ideas()
            if not ideas:
                print("\nNo ideas to delete.")
                input("\nPress Enter to continue...")
                continue

            for i, idea in enumerate(ideas):
                print(f"[{i+1}] {idea['title']}")

            idx_str = input("\nEnter number to delete (0 to cancel): ")
            try:
                idx = int(idx_str) - 1
                if idx == -1:
                    pass
                elif 0 <= idx < len(ideas):
                    deleted = prototype_logger.delete_idea(idx)
                    print(f"Deleted: {deleted['title']}")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Invalid input.")
            input("\nPress Enter to continue...")

def main():
    while True:
        clear_screen()
        print_header()
        print("\nMain Menu:")
        print("1. Material Guide")
        print("2. Design Tips")
        print("3. Prototype Logger")
        print("0. Exit")

        choice = input("\nSelect an option: ")

        if choice == '1':
            show_materials_menu()
        elif choice == '2':
            show_tips_menu()
        elif choice == '3':
            show_logger_menu()
        elif choice == '0':
            print("\nGoodbye!")
            break
        else:
            input("\nInvalid option. Press Enter...")

if __name__ == "__main__":
    main()

available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = {}

while current_choice != '0':
    current_choice = input("> ")
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Adding {chosen_part}.")
        print(f"Your setup: {computer_parts}")
    else:
        print("Not available. Available parts are:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")

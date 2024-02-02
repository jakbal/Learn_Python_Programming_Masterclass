available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = []

while current_choice != '0':
    print(computer_parts)
    current_choice = input("> ")
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part not in computer_parts:
            print(f"Adding {chosen_part}.")
            computer_parts.append(chosen_part)
        else:
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
    else:
        print("Not available. Available parts are:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")

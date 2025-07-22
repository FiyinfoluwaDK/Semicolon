def display_menu(menu, level=0):
    for index, item in enumerate(menu, 1):
        if isinstance(item, tuple):
            print("  " * level + f"{index}. {item[0]}")
            display_menu(item[1], level + 1)
        else:
            print("  " * level + f"{index}. {item}")

def get_user_choice(max_choice):
    while True:
        choice = input("\nEnter your choice (0 to go back, q to quit): ")
        if choice.lower() == 'q':
            return 'q'
        if choice == '0' and max_choice != 0:
            return 0
        if choice.isdigit():
            choice_num = int(choice)
            if 1 <= choice_num <= max_choice:
                return choice_num
            else:
                print(f"Please enter a number between 1 and {max_choice}, 0 to go back, or 'q' to quit.")
        else:
            print(f"Please enter a valid number, 0 to go back, or 'q' to quit.")

def navigate_menu(menu, path=None):
    if path is None:
        path = []
    display_menu(menu)
    max_choice = len(menu)
    choice = get_user_choice(max_choice)
    if choice == 'q':
        return
    elif choice == 0:
        if path:
            path.pop()
            navigate_menu(get_menu_at_path(main_menu, path), path)
        return
    else:
        path.append(choice - 1)
        selected_item = menu[choice - 1]
        if isinstance(selected_item, tuple):
            navigate_menu(selected_item[1], path)
        else:
            print(f"\nSelected: {selected_item}")
            input("Press Enter to continue...")
            navigate_menu(menu, path)

def get_menu_at_path(menu, path):
    current_menu = menu
    for index in path:
        current_menu = current_menu[index][1] if isinstance(current_menu[index], tuple) else current_menu
    return current_menu

main_menu = [
    ("Phone book", [
        "Search",
        "Service Nos",
        "Add name",
        "Erase",
        "Edit",
        "Assign tone",
        "Send b'card",
        ("Options", [
            "Type of view",
            "Memory status"
        ]),
        "Speed dials",
        "Voice tags"
    ]),
    ("Messages", [
        "Write messages",
        "Inbox",
        "Outbox",
        "Picture messages",
        "Templates",
        "Smileys",
        ("Message Settings", [
            ("Set", [
                "Message counter",
                "Messages sent as",
                "Message validity"
            ]),
            ("Common", [
                "Delivery reports",
                "Reply via same centre",
                "Character support"
            ])
        ]),
        "Info service",
        "Voice mailbox",
        "Service command number"
    ]),
    "Chat",
    ("Call register", [
        "Missed calls",
        "Received calls",
        "Dialled numbers",
        "Erase recent call lists",
        ("Show call duration", [
            "Last call duration",
            "All calls duration",
            "Received calls duration",
            "Dialled calls duration",
            "Clear timers"
        ]),
        ("Show call costs", [
            "Last call cost",
            "All calls cost",
            "Clear counters"
        ]),
        ("Call cost settings", [
            "Call cost limit",
            "Show cost in"
        ]),
        "Prepaid credit"
    ]),
    ("Tones", [
        "Ringing Tone",
        "Ringing Volume",
        "Incoming call alert",
        "Composer",
        "Message alert tone",
        "Keypad tones",
        "Warning and game tones",
        "Vibrating alert",
        "Screen saver"
    ]),
    ("Settings", [
        ("Call settings", [
            "Automatic redial",
            "Speed dialing",
            "Call waiting options",
            "Own call options",
            "Phone line in use",
            "Automatic answer"
        ]),
        ("Phone Settings", [
            "Language",
            "Cell info display",
            "Welcome note",
            "Network selection",
            "Lights",
            "Confirm SIM service actions"
        ]),
        ("Security options", [
            "PIN code request",
            "Call barring service",
            "Fixed dialing",
            "Closed user group",
            "Change access codes"
        ]),
        "Restore Factory settings"
    ]),
    "Call divert",
    "Games",
    "Calculator",
    "Reminders",
    ("Clock", [
        "Alarm clock",
        "Clock settings",
        "Date Setting",
        "Stopwatch",
        "Countdown timer",
        "Auto update of date and time"
    ]),
    "Profiles",
    "SIM services"
]

print("=== Phone Menu ===")
navigate_menu(main_menu)
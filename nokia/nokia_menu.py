menu = ("""

WELCOME TO NOKIA
1. Phonebook
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
    """)

print(menu)
menu_options = input("Enter any number from (1 - 13) ")

match (menu_options):
    case "1": 
            print("Phonebook")
phone_book_menu = ("""
PHONEBOOK
1. Search
2. Service Nos
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dial
10. Voice tags
 """)
print(phone_book_menu)
phone_book_options = input("Enter any number from 1 - 10: ")

    
match(phone_book_options):
    case "1": print("Search")
    case "2": print("Service Nos")
    case "3": print("Add name")
    case "4": print("Erase")
    case "5": print("Edit")
    case "6": print("Assign tone")
    case "7": print("Send b'card")

    case "8":
             print("Options")
options = ("""
1. Type of view
2. Memory status
""")
print(options)
option_options = input("Enter any number from 1 - 2: ")

match(option_options):
    case "1": print("Type of view")
    case "2": print("Memory status")

print(menu)
match(phone_book_options):
    case "9": print("Speed dial")
    case "10": print("Voice tags")
    

match(menu_options):
    case "2":
            print("Messages")
messaging_menu = ("""
MESSAGES
1. Write messages
2. Inbox
3. Outbox
4. Picture
5. Templates
6. Smileys
7. Messages settings
8. Info service
9. Voice mailbox number
10. Service command editor
""")
print(messaging_menu)
messaging_options = input("Enter any number from 1 - 10")

match(messaging_options):
        case "1": print("Write messages")
        case "2": print("Inbox")
        case "3": print("Outbox")
        case "4": print("Picture")
        case "5": print("Templates")
        case "6": print("Smiley")
        case "7":
                 print("Messages settings")
message_setting = ("""
1. Set 1
2. Common
""")
print(message_setting )
message_setting_options = input("Enter any number from 1 - 2 ")

match(message_setting_options):
    case "1":
             print("Set 1")
set_menu = ("""
1. Message centre number
2. Messages sent as
3. Message validity
""")
print(set_menu)
set_menu_options = input("Enter any number from 1 - 3")

match(set_menu_options):
    case "1": print("Message centre number")
    case "2": print("Messages sent as")
    case "3": print("Message validity")

match(message_setting_options):
    case "2":
             print("Common")
common_menu = ("""
1. Delivery reports
2. Reply via same centre
3. Character support
""")
print(common_menu)
common_menu_options = input("Enter any number from 1 - 3")

match(common_menu_options ):
    case "1": print("Delivery reports")
    case "2": print("Reply via same centre")
    case "3": print("Character support")


match(messaging_options):
        case "8": print("Info service")
        case "9": print("Voice mailbox number")
        case "10": print("Service command editor")


match (menu_options):
    case "3": print("Chat")
    case "4": 
            print("Call register")
call_menu = ("""
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
""")
print(call_menu)
call_menu_options = input("Enter any number from 1 - 8 ")

match (call_menu_options):
    case "1": print("Missed calls")
    case "2": print("Received calls")
    case "3": print("Dialled numbers")
    case "4": print("Erase recent call lists")
    case "5":
             print("Show call duration")
show_call_duration_menu = ("""
1. Last call duration
2. All calls' cost duration
3. Received calls' duration
4. Dialled calls' duration
5. Clear timers
""")
print(show_call_duration_menu)
show_call_duration_options = input("Enter any option from 1 - 5 ")

match(show_call_duration_options):
    case "1": print("Last call duration")
    case "2": print("All calls' cost duration") 
    case "3": print("Received calls' duration") 
    case "4": print("Dialled calls' duration") 
    case "5": print("Clear timers")     


match (call_menu_options):
    case "6":
             print("Show call costs")
show_call_costs_menu = ("""
1. Last call costs
2. All calls' cost
3. Clear counters
""")
print(show_call_costs_menu)
show_call_cost_options = input("Enter any option from 1 - 3 ")

match(show_call_cost_options):
    case "1": print("Last call costs")
    case "1": print("All calls' cost")
    case "1": print("Clear counters")


match (call_menu_options):
    case "7":
             print("Call cost settings")
call_cost_settings_menu = ("""
1. Call cost limit
2. Show costs in
""")
print(call_cost_settings_menu)
call_cost_settings_options = input("Enter any number from 1 - 2 ")

match(call_cost_settings_options):
    case "1": print("Call cost limit")
    case "2": print("Show costs in")

match (call_menu_options):
    case "8": print("Prepaid credits")


match (menu_options):
    case "5": 
            print("Tones")
tones_menu = ("""
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
""")
print(tones_menu)
tones_options = input("Enter any number from 1 - 9 ")

match(tones_options):
    case "1": print("Ringing tone")
    case "2": print("Ringing volume")
    case "3": print("Incoming call alert")
    case "4": print("Composer")
    case "5": print("Message alert tone")
    case "6": print("Keypad tones")
    case "7": print("Warning and game tones")
    case "8": print("Vibrating alert")
    case "9": print("Screen saver")


match (menu_options):
    case "6":
             print("Settings")
settings_menu = ("""
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
""")
print(settings_menu)
settings_options = input("Enter any number from 1 - 4 ")

match(settings_options):
    case "1":
             print("Call settings")
call_settings_menu = ("""
1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
""")
print(call_settings_menu)
call_settings_options = input("Enter any number from 1 - 6 ")

match(call_settings_options):
    case "1": print("Automatic redial")
    case "2": print("Speed dialling")
    case "3": print("Call waiting options")
    case "4": print("Own number sending")
    case "5": print("Phone line in use")
    case "6": print("Automatic answer")

match(settings_options):
    case "2":
             print("Phone settings")
phone_settings_menu = ("""
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Lights
6. Confirm SIM service actions
""")
print(phone_settings_menu)
phone_settings_options = input("Enter any number from 1 - 6 ")

match(phone_settings_options):
    case "1": print("Language")
    case "2": print("Cell info display")
    case "3": print("Welcome note")
    case "4": print("Network selection")
    case "5": print("Lights")
    case "6": print("Confirm SIM service actions")


match(settings_options):
    case "3":
             print("Security settings")
security_settings_menu = ("""
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Phone security
6. Change access codes
""")
print(security_settings_menu)
security_settings_options = input("Enter any number from 1 - 6 ")

match(security_settings_options):
    case "1": print("PIN code request")
    case "2": print("Call barring service")
    case "3": print("Fixed dialling")
    case "4": print("Closed user group") 
    case "5": print("Phone security")
    case "1": print("Change access codes")


match(settings_options):
    case "4": print("Restore factory settings")



match (menu_options):
    case "7": print("Call divert")
    case "8": print("Games")
    case "9": print("Calculator")
    case "10": print("Reminders")
    case "11": 
            print("Clock")
clock_menu = ("""
1. Alarm clock
2. Clock settings
3. Date settings
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
""")
print(clock_menu)
clock_options = input("Enter any option from 1 - 6 ")

match(clock_options ):
    case "1": print("Alarm clock")
    case "2": print("Clock settings")
    case "3": print("Date settings")
    case "4": print("Stopwatch")
    case "5": print("Countdown timer")
    case "6": print("Auto update of date and time")


match (menu_options):
    case "12": print("Profiles")
    case "13": print("SIM services")



















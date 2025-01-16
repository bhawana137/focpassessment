import random
import json
from datetime import datetime
import os

# Load responses from JSON file
def load_responses(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Could not load responses. The file does not exist.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in responses file.")
        return {}

# Log chat to a file
def log_chat(messages):
    try:
        with open("chat_log.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Chat session started: {timestamp}\n")
            for msg in messages:
                file.write(msg + "\n")
            file.write("\n")
    except:
        print("Error: Could not save the chat log.")

# Offer to resume or review a previous session
def resume_session():
    file_name = "chat_log.txt"
    if os.path.exists(file_name):
        if os.path.getsize(file_name) == 0:
            print("DEBUG: chat_log.txt exists but is empty.")
            return False, [], None, None
        print("Would you like to review or resume your previous session? (review/resume/skip): ", end="")
        choice = input().strip().lower()
        if choice == "review":
            with open(file_name, "r") as file:
                print("\nPrevious Session:\n")
                print(file.read())  # Display the entire chat log
            return False, [], None, None  # Start a new session after reviewing
        elif choice == "resume":
            with open(file_name, "r") as file:
                logs = file.readlines()
                print("\nResuming your last session:\n")
                for log in logs[-10:]:  # Display the last 10 lines
                    print(log.strip())
            # Extract the last known chatbot and user names
            user_name, chatbot_name = extract_names_from_logs(logs)
            return True, logs, user_name, chatbot_name  # Continue the session
    else:
        print("No previous session found.")
    return False, [], None, None  # Start fresh if no file is found or resume is skipped

# Extract names from the previous session logs
def extract_names_from_logs(logs):
    user_name, chatbot_name = None, None
    for line in logs:
        if "Hi" in line and "I'm" in line:  # Look for the chatbot's greeting
            parts = line.split()
            user_name = parts[1].strip(",!")
            chatbot_name = parts[-1].strip(".")
            break
    return user_name, chatbot_name

# Main chatbot logic
def start_chat():
    resume, previous_logs, user_name, chatbot_name = resume_session()
    if resume:
        print("You can continue the chat, or type 'bye' to exit.\n")
        responses = load_responses("responses.json")
        if not responses:
            print("Error: Responses are missing. Chat may not work as expected.\n")
        messages = previous_logs  # Start with previous logs
    else:
        print("********************************************")
        print("Welcome to the University of Poppleton Chat! ")
        print("********************************************\n")
        user_name = input("What's your name? ").strip()
        chatbot_name = input("Would you like to name the chatbot? (Press Enter to skip): ").strip()
        if not chatbot_name:
            chatbot_name = random.choice(["Bhawana", "Celina", "Smriti", "Sneha", "Yuri"])
        print(f"\nHi {user_name}! I'm {chatbot_name}, your virtual assistant.")
        print("You can ask me about the university or type 'help' for suggestions.")
        responses = load_responses("responses.json")
        if not responses:
            print("Error: Responses are missing. Chat may not work as expected.\n")
        messages = []

    follow_up_context = None
    disconnection_counter = 0  # Counter for user inputs

    while True:
        user_input = input("You: ").strip().lower()
        messages.append(f"You: {user_input}")

        disconnection_counter += 1  # Increment counter

        # Disconnect after 5 inputs or with a small random chance
        if disconnection_counter >= 5 or random.random() < 0.03:
            print(f"{chatbot_name}: Oops, I got disconnected! Please restart the chat.")
            messages.append(f"{chatbot_name}: Oops, I got disconnected!")
            break

        # Exit conditions
        if user_input in ["bye", "quit", "exit"]:
            print(f"{chatbot_name}: Goodbye, {user_name}! Have a great day.")
            messages.append(f"{chatbot_name}: Goodbye, {user_name}!")
            break

        # Help command
        if user_input == "help":
            print(f"{chatbot_name}: Here are some topics you can ask me about:")
            print("- Coffee bar timings\n- Library hours\n- Admissions\n- Sports facilities\n- Exam schedules")
            messages.append(f"{chatbot_name}: Provided help topics.")
            continue

        # Handle follow-up context
        if follow_up_context:
            for follow_up in follow_up_context.get("follow_ups", []):
                if follow_up["key"] == user_input:
                    print(f"{chatbot_name}: {follow_up['reply']}")
                    messages.append(f"{chatbot_name}: {follow_up['reply']}")
                    break
            else:
                follow_up_context = None  # Reset context if no match

        # Respond to keywords
        if not follow_up_context:
            for keyword, info in responses.items():
                if keyword in user_input:
                    print(f"{chatbot_name}: {info['details']}")
                    messages.append(f"{chatbot_name}: {info['details']}")
                    follow_up_context = info
                    if "follow_ups" in info:
                        follow_up_suggestions = ", ".join([f"'{f['key']}'" for f in info["follow_ups"]])
                        print(f"{chatbot_name}: You might also want to ask about: {follow_up_suggestions}")
                        messages.append(f"{chatbot_name}: Suggested follow-ups: {follow_up_suggestions}")
                    break
            else:
                print(f"{chatbot_name}: I'm sorry, I didn't understand that. Can you try asking differently?")
                messages.append(f"{chatbot_name}: Could not understand.")

    # Save the chat log
    log_chat(messages)

# Run the chatbot
start_chat()

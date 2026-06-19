import datetime
import random
import json
import os

user_data_file = "user_data.json"

jokes = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the Python developer calm? Because he handled exceptions.",
    "Why did the laptop get cold? Because it left its Windows open.",
    "Why did the coder quit his job? Because he didn't get arrays.",
    "Why was the Java book sad? Because it had too many classes.",
    "Why do programmers hate nature? Too many bugs.",
    "What is a programmer's favourite place? The Foo Bar.",
    "Why did the keyboard break up with the mouse? Too many clicks.",
    "Why was the computer tired? It had too many tabs open."
]

unused_jokes = []


def load_user_data():
    if os.path.exists(user_data_file):
        with open(user_data_file, "r") as file:
            return json.load(file)
    return {"name": ""}


def save_user_data(data):
    with open(user_data_file, "w") as file:
        json.dump(data, file)


def save_chat(user, bot):
    with open("chat_history.txt", "a") as file:
        file.write(f"You: {user}\nBot: {bot}\n\n")


def calculate(expression):
    try:
        answer = eval(expression)
        return f"The answer is {answer}"
    except:
        return "Please enter a valid calculation."


def show_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def show_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def get_joke():
    global unused_jokes

    if not unused_jokes:
        unused_jokes = jokes.copy()
        random.shuffle(unused_jokes)

    return unused_jokes.pop()


def get_response(user_input, user_data):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey"]

    if "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        user_data["name"] = name
        save_user_data(user_data)
        return f"Nice to meet you, {name}!"

    elif any(word in user_input for word in greetings):
        if user_data["name"]:
            return f"Hello {user_data['name']}! How can I help you today?"
        return "Hello! Please tell me your name using: my name is Garvit"

    elif "how are you" in user_input:
        return "I am doing great! Thanks for asking."

    elif "time" in user_input:
        return f"The current time is {show_time()}"

    elif "date" in user_input:
        return f"Today's date is {show_date()}"

    elif "calculate" in user_input:
        expression = user_input.replace("calculate", "").strip()
        return calculate(expression)

    elif "joke" in user_input:
        return get_joke()

    elif "clear history" in user_input:
        open("chat_history.txt", "w").close()
        return "Chat history has been cleared."

    elif "help" in user_input:
        return """
You can ask me:
- hello
- my name is Garvit
- how are you
- time
- date
- calculate 20+30
- tell me a joke
- clear history
- bye
"""

    elif "bye" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I did not understand. Type 'help' to see commands."


def start_chatbot():
    user_data = load_user_data()

    print("Bot: Welcome to Smart Rule-Based Chatbot")
    print("Bot: Type 'help' to see commands.")
    print("Bot: Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        response = get_response(user_input, user_data)

        print("Bot:", response)

        save_chat(user_input, response)

        if "bye" in user_input.lower():
            break

start_chatbot()

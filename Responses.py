from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "start"):
        return "Hey! How's it going?"

    if user_message in ("who are you", "who are you?"):
        return "I am a Responsive Bot Made by @dsurareddy"

    if user_message in ("Whats Up", "What's Up Bro?"):
        return "Feeling Better"

    if user_message in ("date", "date?"):
        now = datetime.now()
        date = now.strftime("%d/%m/%y")
        return str(date)

    if user_message in ("time", "time?"):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        return str(time)




    return "I Don't Understand You."

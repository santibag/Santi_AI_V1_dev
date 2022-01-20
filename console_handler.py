"""This file runs the console mode of the app."""
from conversation_handler import message_evaluation


def console_app():
    while True:
        # It will ask for a message

        user_message = input("\nPlease tell me something:\n")
        print(message_evaluation(user_message))

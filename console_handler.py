"""This file runs the console mode of the app."""
from conversation_handler import answer_evaluation


def console_app():
    while True:
        # It will ask for a message

        user_answer = input("\nPlease tell me something:\n")
        print(answer_evaluation(user_answer))

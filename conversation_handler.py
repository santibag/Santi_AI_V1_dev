"""Decides what to do with every received message.
Asks memory handler to save or provide the received message's data."""
from file_handler import log_it
import memory_handler
import datetime
ai_memory = memory_handler.ai_memory


def reply_human(result, message_dictionary):
    reply_text = result
    return result


def message_evaluation(message):
    """Decides what to do with the user message. It's like the heart of the program."""
    log_it("Input received: " + message)
    message_dictionary = memory_handler.memory_check(message)
    message_time = datetime.datetime.now().strftime("%X %x")
    if "bool" in message_dictionary:
        log_it("Unknown message")
        message_dictionary = {"name": message, "count": 1, "last received": message_time}
        memory_handler.memory_update(message_dictionary, action="add")
        log_it("message added to the memory.")
        result = "I don't know this."
        log_it("message evaluation succeeded!\n")

    else:
        memory_handler.memory_update(message_dictionary, action="update")
        log_it("Known message. message's counter increased to {}.".format(message_dictionary["count"]))
        result = "I know this :D I've seen this {} times before!".format(message_dictionary["count"])
        log_it("message evaluation succeeded!\n")
    return result

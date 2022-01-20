"""Decides what to do with every received answer.
Asks memory handler to save or provide the received answer's data."""
from file_handler import log_it
import memory_handler
import datetime
ai_memory = memory_handler.ai_memory


def answer_evaluation(answer):
    """Decides what to do with the user answer. It's like the heart of the program."""
    log_it("Input received: " + answer)
    answer_dictionary = memory_handler.memory_check(answer)
    answer_time = datetime.datetime.now().strftime("%X %x")
    if "bool" in answer_dictionary:
        log_it("Unknown answer")
        answer_dictionary = {"name": answer, "count": 1, "last received": answer_time}
        memory_handler.memory_update(answer_dictionary, action="add")
        log_it("Answer added to the memory.")
        result = "I don't know this."
        log_it("Answer evaluation succeeded!\n")
        return result

    else:
        memory_handler.memory_update(answer_dictionary, action="update")
        log_it("Known answer. Answer's counter increased to {}.".format(answer_dictionary["count"]))
        result = "I know this :D I've seen this {} times before!".format(answer_dictionary["count"])
        log_it("Answer evaluation succeeded!\n")
        return result

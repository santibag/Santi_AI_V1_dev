"""Manages the memory related tasks."""

import file_handler
import datetime

memoryfile_name = "previous_user_inputs.aimind"
ai_memory = file_handler.aiload(memoryfile_name)


def memory_check(message, memory=ai_memory):
    """Checks if the message is in the AI memory.\n
    Returns a dictionary {"bool": False} if not inside\n
    Returns the dictionary of the message if inside"""
    if len(memory) == 0:
        return {"bool": False}
    else:
        for element in memory:
            if element["name"] == message:
                return element
    return {"bool": False}


def memory_update(message_dictionary, action, memory=ai_memory, memoryfile=memoryfile_name):
    """Adds new messages into the AI memory as a dictionary. {"name": message, "count": 1}\n
    Updates counters of known messages\n
    Pickles the memory into the memory file"""
    if action == "add":
        memory.append(message_dictionary)
    if action == "update":
        message_dictionary["count"] += 1
        message_dictionary["last received"] = datetime.datetime.now().strftime("%X %x")
    if action == "remove":
        memory.remove(message_dictionary)

    file_handler.aisave(memory, memoryfile)

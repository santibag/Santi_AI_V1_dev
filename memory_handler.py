"""Manages the memory related tasks."""

import file_handler
import datetime

memoryfile_name = "previous_user_inputs.aimind"
ai_memory = file_handler.aiload(memoryfile_name)


def memory_check(answer, memory=ai_memory):
    """Checks if the answer is in the AI memory.\n
    Returns a dictionary {"bool": False} if not inside\n
    Returns the dictionary of the answer if inside"""
    if len(memory) == 0:
        return {"bool": False}
    else:
        for element in memory:
            if element["name"] == answer:
                return element
    return {"bool": False}


def memory_update(answer_dictionary, action, memory=ai_memory, memoryfile=memoryfile_name):
    """Adds new answers into the AI memory as a dictionary. {"name": answer, "count": 1}\n
    Updates counters of known answers\n
    Pickles the memory into the memory file"""
    if action == "add":
        memory.append(answer_dictionary)
    if action == "update":
        answer_dictionary["count"] += 1
        answer_dictionary["last received"] = datetime.datetime.now().strftime("%X %x")
    if action == "remove":
        memory.remove(answer_dictionary)

    file_handler.aisave(memory, memoryfile)

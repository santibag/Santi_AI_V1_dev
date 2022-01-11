"""Manages the memory related tasks."""

import file_handler

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


def memory_update(answer, memory=ai_memory, memoryfile=memoryfile_name, add=False):
    """Adds new answers into the AI memory as a dictionary. {"name": answer, "count": 1}\n
    Updates counters of known answers\n
    Pickles the memory into the memory file"""
    if add:
        element = {"name": answer, "count": 1}
        memory.append(element)
    else:
        answer["count"] += 1

    file_handler.aisave(memory, memoryfile)

import file_handler
memoryfile_name = "previous_user_inputs.aimind"
ai_memory = file_handler.aiload(memoryfile_name)


# Checks if the answer is in the AI memory.
# Returns a dictionary {"bool": False} if not inside
# Returns the dictionary of the answer if inside
def memory_check(answer, memory=ai_memory):
    if len(memory) == 0:
        return {"bool": False}
    else:
        for element in memory:
            if element["name"] == answer:
                return element
    return {"bool": False}


# Adds new answers into the AI memory as a dictionary. Format is the append() parameter
# Updates counters of known answers
# Pickles the memory into the memory file
def memory_update(answer, memory=ai_memory, memoryfile=memoryfile_name, add=False):
    if add:
        element = {"name": answer, "count": 1}
        memory.append(element)
    else:
        answer["count"] += 1

    file_handler.aisave(memory, memoryfile)

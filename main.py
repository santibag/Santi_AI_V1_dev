import pickle
memoryfile_name = "previous_user_inputs.aimind"


def memory_init(memoryfile):
    try:
        with open(memoryfile, "rb") as f:
            history = pickle.load(f)
            f.close()
        return history
    except FileNotFoundError:
        return []


ai_memory = memory_init(memoryfile_name)


# Checks if the answer is in the AI memory.
# Returns a dictionary {"bool": False} if not inside
# Returns the dictionary of the answer if inside
def memory_check(answer, memory):
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
def memory_update(answer, memory,  memoryfile, add=False):
    if add:
        element = {"name": answer, "count": 1}
        memory.append(element)
    else:
        answer["count"] += 1

    with open(memoryfile, "wb") as f:
        pickle.dump(memory, f)
        f.close()


# Decides what to do with the user answer. It's like the heart of the program.
def answer_evaluation(memory, memoryfile):
    # It will ask for a message
    answer = input("Please tell me something:\n")

    # Remember: memory_check() returns a dictionary with only bool if the answer is not known.
    # False return is checked first because a known answer will return answer dictionary, instead.
    answer_dictionary = memory_check(answer, memory)
    if "bool" in answer_dictionary:
        print("I don't know this.")
        memory_update(answer, memory, memoryfile, add=True)
    else:
        print("I know this :D I've seen this {} times before!".format(answer_dictionary["count"]))
        memory_update(answer_dictionary, memory, memoryfile)


working = True

while working:
    answer_evaluation(ai_memory, memoryfile_name)

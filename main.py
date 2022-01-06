ai_memory = []


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


# Adds the answer into the AI memory. Format is in the append below.
def memorize_answer(answer, memory):
    memory.append({"name": answer, "count": 1})


# Decides what to do with the user answer. It's like the heart of the program.
def answer_evaluation(answer, memory):
    # Remember: memory_check() returns False if the answer is not known
    # False return is checked first because the True return is not a bool but a dictionary return
    answer_dictionary = memory_check(answer, memory)
    if "bool" in answer_dictionary:
        print("I don't know this.")
        memorize_answer(answer, memory)
    else:
        print("I know this :D I've seen this {} times before!".format(answer_dictionary["count"]))
        answer_dictionary["count"] += 1


working = True

while working:
    answer_evaluation(input("Please tell me something:\n"), ai_memory)

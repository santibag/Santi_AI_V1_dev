import memory_handler
ai_memory = memory_handler.ai_memory


# Decides what to do with the user answer. It's like the heart of the program.
def answer_evaluation(answer):
    # Remember: memory_check() returns a dictionary with only bool if the answer is not known.
    # False return is checked first because a known answer will return answer dictionary, instead.
    answer_dictionary = memory_handler.memory_check(answer)
    if "bool" in answer_dictionary:
        print("I don't know this.")
        memory_handler.memory_update(answer, add=True)
    elif "function" in answer_dictionary:
        special_answer(answer_dictionary)
    else:
        print("I know this :D I've seen this {} times before!".format(answer_dictionary["count"]))
        memory_handler.memory_update(answer_dictionary)


# Evaluates the answers that have assigned functions, like closing the AI
def special_answer(answer, memory=ai_memory):
    if answer["function"] == "close":
        quit()
    if answer["function"] == "show everything":
        for i in memory:
            print(i)
    else:
        print("You could somehow find an unavailable function.\n"
              "Don't try this at home. <3")

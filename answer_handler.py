"""Decides what to do with every received answer.
Asks memory handler to save or provide the received answer's data."""
import file_handler
import memory_handler
ai_memory = memory_handler.ai_memory


def special_answer(answer_dictionary, memory=ai_memory):
    """Evaluates the answers that have assigned tasks, like closing the AI."""
    file_handler.log_it("Special answer being evaluated!", warn=True)

    if answer_dictionary["function"] == "close":
        file_handler.log_it("Close command received. AI is stopping.")
        print("Thank you for chatting with me :D Bye :D")
        quit()

    elif answer_dictionary["function"] == "show everything":
        for i in memory:
            print(i)

    elif answer_dictionary["function"] == "add special":
        new_answer = input("\nPlease enter the command to be added:\n")
        new_answer_function = input("Please enter the new answer's function:\n")
        answer_dictionary = {"name": new_answer, "count": 1, "function": new_answer_function}

        memory_handler.memory_update(answer_dictionary, action="add")
        print("New special answer {} is added!".format(new_answer))

    elif answer_dictionary["function"] == "remove answer":
        target_answer = input("\nPlease enter the answer to be removed:\n")
        answer_dictionary = memory_handler.memory_check(target_answer)
        if "bool" in answer_dictionary:
            print("This answer is not known.")
        else:
            memory_handler.memory_update(answer_dictionary, action="remove")
            print("The answer {} is removed!".format(answer_dictionary["name"]))

    else:
        file_handler.log_it("""You could somehow find an unavailable function. 
        Don't try this at home. <3""", warn=True)


def answer_evaluation(answer):
    """Decides what to do with the user answer. It's like the heart of the program."""
    answer_dictionary = memory_handler.memory_check(answer)

    if "bool" in answer_dictionary:
        print("I don't know this.")
        answer_dictionary = {"name": answer, "count": 1}
        memory_handler.memory_update(answer_dictionary, action="add")
        file_handler.log_it("Answer added to the memory.")

    elif "function" in answer_dictionary:
        file_handler.log_it("Special answer received!", warn=True)
        special_answer(answer_dictionary)

    else:
        print("I know this :D I've seen this {} times before!".format(answer_dictionary["count"]))
        memory_handler.memory_update(answer_dictionary, action="count")
        file_handler.log_it("Known answer. Answer's counter increased.")

    file_handler.log_it("Answer evaluation succeeded!\n")

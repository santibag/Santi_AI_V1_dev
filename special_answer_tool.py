"""Lets you use a special answer function without running the AI"""

if __name__ != "__main__":
    print("Module import error! quit() applied for punishment XD")
    quit()

from answer_handler import special_answer

# Never modify this, unless you have a reason! The tool runs just fine as it is!
function = input("\nEnter the answer(WARNING: Type the function correctly!):\n")

answer_dictionary = {"name": "answer", "function": function}
special_answer(answer_dictionary)

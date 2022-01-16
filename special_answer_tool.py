"""Lets you use a special answer function without running the AI"""

from answer_handler import special_answer

# Never modify this, unless you have a reason! The tool runs just fine as it is!
function = input("\nEnter the answer(WARNING: Type the function correctly!):\n")

answer_dictionary = {"name": "answer", "function": function}
special_answer(answer_dictionary)

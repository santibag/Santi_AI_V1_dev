import answer_handler
from file_handler import log_it

log_it("Log started!\n", initial=True)

while True:
    # It will ask for a message
    user_answer = input("Please tell me something:\n")
    log_it("Input received: "+user_answer)
    answer_handler.answer_evaluation(user_answer)

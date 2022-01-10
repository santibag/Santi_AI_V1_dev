import answer_handler

while True:
    # It will ask for a message
    user_answer = input("Please tell me something:\n")
    answer_handler.answer_evaluation(user_answer)

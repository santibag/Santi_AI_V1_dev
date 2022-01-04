# AI Memory is a list of answers and repetition counts
AIMemory = []


# Checks if the answer is in the memory and tells if it is
def evaluate_user_answer(user_answer, memory):
    if user_answer in memory:
        print("I know this!")
    else:
        print("I don't know this")


# Adds the answer to the AI memory
# If the answer is a repeat, it increases the count, instead
def memorize(answer, memory):
    if answer not in memory:
        memory.append(answer)  # The answer is memorized as a tuple of (Answer,repetition count)

    # else:
    #     print(AIMemory)


#########################################################
# The main loop below
ProgramIsRunning = True

while ProgramIsRunning:
    # Answer and evaluation
    UserAnswer = input("Please write your message:\n")
    evaluate_user_answer(UserAnswer, AIMemory)

    # Memorizing the answer
    memorize(UserAnswer, AIMemory)
#########################################################

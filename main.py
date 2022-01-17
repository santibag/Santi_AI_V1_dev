from file_handler import log_it

log_it("Log started!\n", initial=True)
log_it("GUI being initialized.")

# Possible values: "gui", "console"
running_mode = "gui"

# If GUI mode is chosen, the console mode will be ignored and the AI will run in GUI mode.
if running_mode == "gui":
    from gui_handler import start_gui
    start_gui()

# If console mode is chosen, the loop below will start AI in console mode
elif running_mode == "console":
    import answer_handler
    while True:
        # It will ask for a message
        user_answer = input("\nPlease tell me something:\n")
        log_it("Input received: "+user_answer)
        answer_handler.answer_evaluation(user_answer)

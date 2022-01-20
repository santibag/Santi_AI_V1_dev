from file_handler import log_it

log_it("Log started!\n", initial=True)

# Possible values: "gui", "console"
running_mode = "gui"
log_it("Running mode: {}".format(running_mode))


# If GUI mode is chosen, the console mode will be ignored and the AI will run in GUI mode.
if running_mode == "gui":
    log_it("Initializing GUI.")
    from gui_handler import start_gui
    start_gui()


# If console mode is chosen, the loop below will start AI in console mode
elif running_mode == "console":
    log_it("Initializing console.")
    from console_handler import console_app
    console_app()

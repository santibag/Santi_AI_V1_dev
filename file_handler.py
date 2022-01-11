import pickle


def husave(data, file_name, generate=False):
    """Saves human-readable files. Generates the file if it doesn't exist."""
    if generate:
        mode = "w"
    else:
        mode = "a"
    with open(file_name, mode) as f:
        f.writelines(data)
        f.close()


def log_it(event, warn=False, initial=False):
    """Saves events into log.txt file.
    Resets log.txt at the start of the AI."""
    if initial:
        husave(event+"\n", "log.txt", generate=True)
    else:
        husave(event+"\n", "log.txt")
    if warn:
        print(event)


def aisave(data, file_name):
    """Pickles AI mind's data. Generates the file if it doesn't exist."""
    with open(file_name, "wb") as f:
        pickle.dump(data, f)
        f.close()


def aiload(file_name):
    """Loads pickle files or generates them if they don't exist.
    Returns the date or an empty list."""
    try:
        with open(file_name, "rb") as f:
            data = pickle.load(f)
            f.close()
        return data
    except FileNotFoundError:
        log_it("File Handler says: Aiload couldn't find {0}. Generating {0}.".format(file_name))
        aisave(None, file_name)
        data = []
        return data


def huload(file_name):
    """Loads human-readable files. Generates if they don't exist."""
    try:
        with open(file_name, "r") as f:
            data = f.readlines()
            f.close()
        return data
    except FileNotFoundError:
        log_it("File Handler says: Huload couldn't find {0}. Generating {0}.".format(file_name))
        husave(None, file_name)
        data = []
        return data

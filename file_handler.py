import pickle


def aiload(file_name):
    try:
        with open(file_name, "rb") as f:
            data = pickle.load(f)
            f.close()
        return data
    except FileNotFoundError:
        with open("log.txt", "a") as f:
            f.write("File Handler says: Load ailang couldn't find {0}. Generating {0}.".format(file_name))
            f.close()
        with open(file_name, "wb") as f:
            data = pickle.load(f)
            f.close()
            return data


def aisave(data, file_name):
    with open(file_name, "wb") as f:
        pickle.dump(data, f)
        f.close()


def huload(file_name):
    try:
        with open(file_name, "r") as f:
            data = f.readlines()
            f.close()
        return data
    except FileNotFoundError:
        with open("log.txt", "a") as f:
            f.write("File Handler says: Load hulang couldn't find {0}. Generating {0}.".format(file_name))
            f.close()
        with open(file_name, "wb") as f:
            data = ""
            f.close()
            return data


def husave(data, file_name):
    with open(file_name, "w") as f:
        f.writelines(data)
        f.close()

# Generates a copy of the known messages file in human language, so you can see the contents

import pickle

with open("previous_user_inputs.aimind", "rb") as f:
    data = pickle.load(f)
    f.close()

print(type(data))

for i, t in enumerate(data):
    data[i] = str(t) + "\n"

print(type(data))

with open("previous_user_inputs.humind", "w") as f:
    f.writelines(data)
    f.close()

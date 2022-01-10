# Generates a copy of the known messages file in human language, so you can see the contents
import file_handler
aimind_file = "previous_user_inputs.aimind"
humind_file = "previous_user_inputs.humind"

data = file_handler.aiload(aimind_file)

for i, t in enumerate(data):
    data[i] = str(t) + "\n"

file_handler.husave(data, humind_file, generate=True)

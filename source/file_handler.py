import json
import os


# LOAD DATA
def load_data(filename, default_data):

    if not os.path.exists(filename):

        with open(filename, "w") as file:
            json.dump(default_data, file, indent=4)

        return default_data

    with open(filename, "r") as file:
        return json.load(file)


# SAVE DATA
def save_data(filename, data):

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
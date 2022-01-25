

import json


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}


class data():

    def save_value(name, value, savedAs, debug=False):
        """
        Saves a value in a JSON file.

        [summary]

        Args:
            name ([key]): [Name of Key]
            value ([type]): [Value in Key]
            savedAs ([file]): [JSON filename]
            debug (bool, optional): Defaults to False.
        """

        if value != None:
            SAVED_DATA = savedAs+".json"
            data = load_data(SAVED_DATA)

            key = name
            data[key] = value
            save_data(SAVED_DATA, data)
            if debug is True:
                print("Saved Data.")
            else:
                pass
        else:
            print("Unknown Value.")

    def load_value(name, key, debug=False):
        """[summary]

        Returns:
            value ([type]): [Value in Key]
        """

        if key != None:
            LOAD_DATA = name+".json"
            data = load_data(LOAD_DATA)

            key = key
            load_data(LOAD_DATA)
            if debug is True:
                print("Loaded Data.")
                return data[key]
            else:
                return data[key]
        else:
            print("Unknown Value.")

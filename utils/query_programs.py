"""
This class reads the file which stores locations of application binary
"""
import platform
import distro
import os


def read_command_file():
    """
    Function reads a files contents and returns it in a dictionary.
    """
    print('Reading file...')
    command_file_path = '../application_location.txt'
    dic = {}

    # Get k and val from file:
    if os.path.exists(command_file_path):
        with open(command_file_path, 'r') as f:
            try:
                for line in f:
                    data = line.split()
                    if len(data) == 2:
                        key, value = data[0], data[1]
                        dic[key] = value

                print(dic)
                return dic
            except:
                print('Error processing file')
    else:
        print('File not found')


def query_dictionary(commands_dictionary, query):
    """
    Function that loops though commands_dictionary
    to find a match to the query
    Functions returns the key which is the command
    """
    print(commands_dictionary)

    # Read key and value from dic
    for k, val in commands_dictionary.items():
        if query.lower() == k:
            print('print value', k)
            return val  # return command

    return None  # return None as none was found

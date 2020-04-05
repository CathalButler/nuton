from chatterbot.logic import LogicAdapter
import subprocess

"""
:Author - Cathal Butler
Custom Logic Adapter class that will handle opening applications when
When a user requests to open one.
Refs: 
https://chatterbot.readthedocs.io/en/0.8.7/logic/create-a-logic-adapter.html#logic-adapter-methods
https://www.tutorialdocs.com/tutorial/chatterbot/logic-adapters.html
"""


class ApplicationAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        :param statement: A statement, that closely matches an input to the chat bot.
        Return true if the input statment contains
        'open' 'an' 'application'
        """
        if statement.text.startswith('open'):
            return True
        else:
            return False

    # TODO - This function acts very weird, may cause issues later so I am marking it with this todo
    def process(self, statement, **kwargs):
        """
        :param statement: input from user
        Function to process request
        """

        from utils.query_programs import read_command_file
        from utils.query_programs import query_dictionary
        from chatterbot.conversation import Statement
        print(statement)

        # Post pressing of the statement, need to remove the beginner of it
        # The second word is the name of the application so slip and take the last word
        temp = statement.text.split()
        print(temp[-1])

        results = read_command_file()  # Read file
        final = query_dictionary(results, temp[-1])  # query

        result = exec_command(final)
        msg_statement = Statement("Application has been opened")
        error_statement = Statement("Error")

        if result is not "Error":
            return msg_statement
        else:
            return error_statement


def exec_command(command):
    print(command)
    try:
        subprocess.Popen(command)
        return
    except subprocess.CalledProcessError as error:
        print('Subprocess error: ', error)
        return error

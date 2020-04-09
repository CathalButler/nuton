from chatterbot.logic import LogicAdapter

"""
:Author - Cathal Butler
Custom Logic Adapter class that will handle weather requests from the user
Refs: 
https://chatterbot.readthedocs.io/en/0.8.7/logic/create-a-logic-adapter.html#logic-adapter-methods
https://www.tutorialdocs.com/tutorial/chatterbot/logic-adapters.html
"""


class NotesAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        Checks can this adapter process the request made by the user
        """
        if statement.text.startswith('make a note') or statement.text.startswith('read me my note'):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters):
        """
           :param statement: input from user
           :param additional_response_selection_parameters
           :return response_statement and confidence number
           Function to create a note from the users input =
           """
        import requests
        from chatterbot.conversation import Statement
        import time
        # https://stackoverflow.com/questions/18867986/python-output-file-with-timestamp

        if statement.text.startswith('make a note'):
            # File name with time stamp to be saved in the notes folder
            noteFile = 'notes/note.txt'

            # Open file to begin writing
            out = open(noteFile, "w")
            for line in statement.text.replace('make a note ', ''):
                out.write(line)

            out.write("\n")
            out.close()

            response = Statement(text="Your note has been saved")
            response.confidence = 1
            return response

        else:
            file_name = 'notes/note.txt'
            try:
                file_in = open(file_name, "r")
                response = Statement(text=file_in.read())
                response.confidence = 1
                return response

            except FileNotFoundError:
                response = Statement(text="No previous notes saved.")
                response.confidence = 1
                return response

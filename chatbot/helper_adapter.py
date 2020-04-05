from chatterbot.logic import LogicAdapter

"""
:Author - Cathal Butler
Custom Logic Adapter class to handle responding to a user that asks what can the bot do
Refs: 
https://chatterbot.readthedocs.io/en/0.8.7/logic/create-a-logic-adapter.html#logic-adapter-methods
https://www.tutorialdocs.com/tutorial/chatterbot/logic-adapters.html
"""


class HelperAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains
        what is listed in the 'words' array below
        """
        if statement.text.startswith('What can you do'):
            print(True)
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        """
           :param input_statement: input from user
           :param additional_response_selection_parameters
           Function to process weather request
           """
        from chatterbot.conversation import Statement

        response_statement = Statement(text='I Nuton can tell you the weather in any city you wish, I can open an'
                                            'application for you, I can tell you the time and I can also do maths but '
                                            'thats obvious I am a computer')
        confidence = 1
        response_statement.confidence = confidence

        return response_statement

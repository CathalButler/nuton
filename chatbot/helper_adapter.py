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
        what is listed in the int he queries array
        """
        queries = ['what can you do', 'help', 'display examples']
        if any(x in statement.text for x in queries):
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

        if input_statement.text == 'display examples':
            response_statement = Statement(text='1. Maths : What is four plus four? '
                                                '2. Lunch Application: open chrome - this will do a look up '
                                                'in the applications list(hardcoded atm) '
                                                '3. Weather: what temperature is it in Galway - Maybe add onto this '
                                                'this')
            confidence = 1
            response_statement.confidence = confidence
            return response_statement
        else:
            response_statement = Statement(
                text='Hey! My name is Nuton! I can give you the weather for any location,'
                     ' I can open applications for you, along with more help!')
            confidence = 1
            response_statement.confidence = confidence
            return response_statement

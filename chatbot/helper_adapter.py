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
        anything listed in the the queries array
        """
        queries = ['what can you do', 'help', 'display examples']
        if any(x in statement.text for x in queries):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        """
           :param input_statement: input from user
           :param additional_response_selection_parameters
           Function to handle returning information message to the user
        """
        from chatterbot.conversation import Statement

        if input_statement.text == 'display examples':
            response_statement = Statement(text='1. Maths, What is four plus four? '
                                                '2. Lunch Application, open chrome or open twitter '
                                                '3. Weather, what temperature is it in Galway '
                                                '4. Time, what time is it '
                                                '5. Note, "make a note" followed by what you wish to add "the weather '
                                                'is very nice today" and to retrieve the note say "read me my note"')
            confidence = 1
            response_statement.confidence = confidence
            return response_statement
        else:
            response_statement = Statement(
                text='Hey! My name is Nuton! I can give you the weather for any location,'
                     'I can open applications for you, along with more help! If you like some examples say "display '
                     'examples"')
            confidence = 1
            response_statement.confidence = confidence
            return response_statement

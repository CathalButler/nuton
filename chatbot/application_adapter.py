import webbrowser
from chatterbot.logic import LogicAdapter
import subprocess

"""
:Author - Cathal Butler
Custom Logic Adapter class that will handle opening applications and websites when a user requests one.
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
        Return true if the input statement contains any of the words listed in the array
        below
        """
        words = ['open', 'launch', 'run']
        if any(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, statement, additional_response_selection_parameters):
        """
        :param statement: input from user
        :param additional_response_selection_parameters
        :return msg_statement : response message and confidence number
        Function to process opening an applications or website as a subprocess
        """
        from utils.query_programs import read_command_file
        from utils.query_programs import query_dictionary
        from chatterbot.conversation import Statement

        # Post pressing of the statement, store the last word from the statement
        temp = statement.text.split()

        results = read_command_file()  # Read file
        apps = query_dictionary(results, temp[-1])  # query
        msg_statement = Statement("")

        if apps is None:  # If no app is found
            if query_websites(temp[-1]):  # check for website list
                msg_statement.text = "Website has been opened"
                msg_statement.confidence = 1
                return msg_statement
            else:
                msg_statement.text = "Error processing request, did you give application or web site name?"
                msg_statement.confidence = 1
                return msg_statement
        else:
            msg_statement.text = "Application has been opened"
            msg_statement.confidence = 1
            if exec_command(apps):
                return msg_statement
            else:
                msg_statement = "Error opening application, application may not be defined in applications list."
                msg_statement.confidence = 1
                return msg_statement


def exec_command(command):
    """
    Function which will start a subprocess of an application
    that has been passed into it.
    :param command: target application path
    :return: boolean, True if process has been started else False
    """
    try:
        subprocess.Popen(command)
        return True
    except subprocess.CalledProcessError as error:
        print('Subprocess error: ', error)
        return False


def query_websites(site_name):
    """
    Function that will open a website a browser if it exits
    :param site_name: website name
    :return: boolean, True if a match is found else false
    """
    # Variables
    website = ["facebook", "github", "linkedin", "youtube", "skynews", "outlook", "gmail", "google", "twitter",
               "amazon", "reddit", "netflix"]
    # Loop though array and try match the requested website:
    for site in website:
        if site == site_name:
            # Open webpage in browser
            webbrowser.open(site + '.com')
            return True

    return False

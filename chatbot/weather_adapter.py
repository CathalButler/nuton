from chatterbot.logic import LogicAdapter

"""
:Author - Cathal Butler
Custom Logic Adapter class that will handle weather requests from the user
Refs: 
https://chatterbot.readthedocs.io/en/0.8.7/logic/create-a-logic-adapter.html#logic-adapter-methods
https://www.tutorialdocs.com/tutorial/chatterbot/logic-adapters.html
"""


class WeatherAdapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        """
        Return true if the input statement contains
        what is listed in the 'words' array below
        """
        # sentences = ['what temperature is it in', 'Whats the weather like in', '' 'it' 'in']
        if statement.text.startswith('what temperature is it in'):
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
        import requests
        from chatterbot.conversation import Statement
        api_key = 'fd0c6f39f71a0d238c09fd22789cc73c'
        # Post pressing of the statement, taking the last word as that is the name of the city
        temp = input_statement.text.split()
        print(temp[-1])

        # Weather request for current forecast sent to open weather map
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + temp[-1] + '&units=metric' + '&appid=' + api_key
        response = requests.get(url)  # Execute http request
        data = response.json()  # Data return from api

        if response.status_code == 200:
            confidence = 1
        else:
            confidence = 0

        # Build response
        temperature = data.get('main')['temp']
        response_statement = Statement(text='The current temperature is {}'.format(round(temperature)) + ' degrees')
        response_statement.confidence = confidence

        return response_statement

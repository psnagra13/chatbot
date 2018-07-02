from library.format.responseFormat import chatbotResponseFormat
from library.format.responseFormat import userResponseFormat
from library.response.getResponse import getResponse

import time


class chatbot:

    def __init__(self,chatbotName = "Jarvis" ,userName= "You"):
        self.variables = {
            'chatbotName' : chatbotName ,
            'userName' : userName
        }

    # A function that responds to a user's message: respond
    def respond(self,message):
        # Concatenate the user's message to the end of a standard bot respone
        bot_message = getResponse (message)
        bot_message = self.formatResponse(bot_message)
        # Return the result
        return bot_message

    def formatResponse (self , response):
        for key in self.variables.keys():
            response = response.replace('##' + key, self.variables[key])
        return response

    def printMessageAndResponse (self,message, response):

        # print userResponseFormat(self.variables['userName'],message)
        print chatbotResponseFormat(self.variables['chatbotName'],response)



if __name__ == "__main__":

    testbot = chatbot()

    # message = "Hello Chatbot "
    # response = testbot.respond (message)
    # testbot.printMessageAndResponse (message ,response)
    # print "\n*********************************************************"
    # print "*********************************************************\n"
    #
    # message = "what's your name?"
    # response = testbot.respond (message)
    # testbot.printMessageAndResponse (message ,response)
    # print "\n*********************************************************"
    # print "*********************************************************\n"


    while (1):

        message = raw_input()

        response = testbot.respond(message)
        time.sleep(1)
        testbot.printMessageAndResponse(message, response)
        if message == "bye":
            break







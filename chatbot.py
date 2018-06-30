from library.format.responseFormat import chatbotResponseFormat
from library.format.responseFormat import userResponseFormat
from library.response.getResponse import getResponse


class chatbot:

    def __init__(self,chatbotName = "Jarvis" ,userName= "Tony Stark"):
        self.chatbotName = chatbotName
        self.userName = userName

    # A function that responds to a user's message: respond
    def respond(self,message):
        # Concatenate the user's message to the end of a standard bot respone
        bot_message = getResponse (message)
        # Return the result
        return bot_message

    def printMessageAndResponse (self,message, response):

        print userResponseFormat(self.userName,message)
        print chatbotResponseFormat(self.chatbotName,response)



if __name__ == "__main__":

    testbot = chatbot()
    message = "Hello Chatbot "
    response = testbot.respond (message)
    testbot.printMessageAndResponse (message ,response)
    print "\n*********************************************************"
    print "*********************************************************\n"






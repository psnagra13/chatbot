from echoMessage import echoMessage
from listOfResponses import responses
from patternMatch import matchPattern
from grammar import replace_pronouns
from intentMatch import respondTomessage
import random




def getResponse (message):
    # response = echoMessage(message)


    if message in responses:
        bot_message = random.choice(responses[message])
        return bot_message

    bot_message = respondTomessage(message)

    if bot_message is not None:
        return bot_message

    if  message.endswith("?"):

        bot_message = matchPattern(message)
        if (bot_message == None):
            bot_message = random.choice(responses["question"])
        else:
            bot_message = replace_pronouns(bot_message)

        return bot_message



    bot_message = random.choice(responses["statement"])
    return bot_message



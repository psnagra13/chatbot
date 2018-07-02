from echoMessage import echoMessage
from listOfResponses import responses
from patternMatch import matchPattern
from grammar import replace_pronouns

import random
import re



def getResponse (message):
    # response = echoMessage(message)


    if message in responses:
        bot_message = random.choice(responses[message])

    elif  message.endswith("?"):

        bot_message = matchPattern(message)
        if (bot_message == None):
            bot_message = random.choice(responses["question"])

    else:
        bot_message = random.choice(responses["statement"])

    bot_message = replace_pronouns(bot_message)

    return bot_message



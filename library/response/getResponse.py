from echoMessage import echoMessage
from listOfResponses import responses
import random


def getResponse (message):
    # response = echoMessage(message)





    if message in responses:
        bot_message = random.choice(responses[message])

    elif  message.endswith("?"):
        bot_message = random.choice(responses["question"])

    else:
        bot_message = random.choice(responses["statement"])

    return bot_message




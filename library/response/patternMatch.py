from listOfPatterns import patterns
import random
import re

def matchPattern (message):
    bot_message = None
    # Iterate over the rules dictionary
    for pattern, resp in patterns.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(resp)
            if '{0}' in response:
                bot_message = response.replace('{0}', match.group(1))

    return bot_message


from intentAndResponses import responses
from intentAndResponses import keywords
import re

def generatePatternFromKeywords (keywords):
    patterns = {}
    # Iterate over the keywords dictionary
    for intent, keys in keywords.items():
        # Create regular expressions and compile them into pattern objects
        patterns[intent] = re.compile('|'.join(keys))
    return patterns

def getIntent(message):
    patterns = generatePatternFromKeywords(keywords)
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message
        match = re.search(pattern, message)
        if match is not None:
            matched_intent = intent
    return matched_intent


def getResponse(intent,message):
    key = intent

    if intent in responses:
        key = intent
        return responses[key]
    else:
        return None

# Define a respond function
def respondTomessage(message):
    # Call the match_intent function
    intent = getIntent(message)

    response = getResponse(intent , message)

    return response

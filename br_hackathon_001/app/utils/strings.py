from flask import Blueprint

# strings_bp = Blueprint('strings', __name__)

def getTopCharacters(inputString, noOfCharacters):
    sortedCharacters = getSortedCharacters(inputString)
    return sortedCharacters[0: noOfCharacters]

def getSortedCharacters(inputString):
    inputString = inputString.strip()
    inputString = inputString.upper()

    characterCount = {}
    for character in inputString:
        characterCount.update({character: inputString.count(character)})

    sortedCharacters2 = [v[0] for v in sorted(characterCount.items(), key=lambda kv: (-kv[1], kv[0]))]        
    return sortedCharacters2
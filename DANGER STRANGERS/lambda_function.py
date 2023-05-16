import json

def lambda_handler(event, context)
    # Extract the username and password from the event
    username = event['username']
    password = event['password']
    
    # Do some processing with the username and password here...
    # For example, you could store it in a database, validate it, etc.
    
    # Create a dictionary with the collected username and password information
    collected_info = {
        'username' username,
        'password' password
    }
    
    # Convert the dictionary to JSON format
    response_body = json.dumps(collected_info)
    
    # Create a response object with the JSON body
    response = {
        'statusCode' 200,
        'body' response_body,
        'headers' {
            'Content-Type' 'applicationjson'
        }
    }
    
    # Return the response object
    return response
#--------------------------------------------------------------------------------------------------------------------------
# import the JSON utility package
import json
# import the Python math library
import math

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):

# extract the two numbers from the Lambda service's event object
    mathResult = math.pow(int(event['base']), int(event['exponent']))

    # return a properly formatted JSON object
    return {
    'statusCode': 200,
    'body': json.dumps('Your result is ' + str(mathResult))
    }
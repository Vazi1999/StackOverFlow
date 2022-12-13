from pip._vendor import requests




########################################################################


try:
#need to pass the code to check it .
    x="https"
    print(int(x))
except Exception as error:
    error_message = str(error)
    print("The error is: " + error_message)
    #change the
    




##################################################################

## https://api.stackexchange.com/docs/search#order=desc&min=120&sort=votes&intitle=division%20by%20zero&filter=default&site=stackoverflow

## https://api.stackexchange.com/docs/search#order=desc&min=120&sort=relevance&intitle=division%20by%20zero&filter=default&site=stackoverflow

## https://api.stackexchange.com/docs/search#order=desc&sort=relevance&intitle=division%20by%20zero&filter=default&site=stackoverflow

## https://api.stackexchange.com/docs/search#order=desc&sort=relevance&intitle=invalid%20literal%20for%20int()%20with%20base%2010&filter=default&site=stackoverflow



# Set the base URL for the Stack Exchange API
base_url = "https://api.stackexchange.com/2.3"

# Set your API key
api_key = "zSMudZtOD6STp9KlT6TLLg(("

# Set the parameters for your query
params = {
    "site": "stackoverflow",
    "client_id": "24988",
    "client_secret": "2W7nr4j8WE8CNyY4)tUNGA((",
    "key": api_key
}

# Send the request to the API
response = requests.get(base_url + "/questions", params=params)

# Print the response data
print(response.json())



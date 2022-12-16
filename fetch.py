from pip._vendor import requests
import json
import webbrowser

def get_queryset(erorr):
    String = ""
    for word in erorr.split():
        String += word + "%20"
        
    String = String[:-3]  # delete the last %20
    erorr_query = "https://api.stackexchange.com/docs/search#order=desc&sort=votes&intitle=" + String + "&filter=default&site=stackoverflow"
    return erorr_query

def openStack(response):
    data_json = json.loads(response)
    counter = 0 
    for item in data_json["items"]:
        link = item["link"]
        webbrowser.open(link, new=2) # open the link with the specified link.   
        counter += 1
        if counter == 3: # to open only 3 webpagess
            break   

def fetch_stackoverflow(choice,user_input):
    #params:
    params = {
            "site": "stackoverflow",
            "client_id": "24988",
            "client_secret": "2W7nr4j8WE8CNyY4)tUNGA((",
            "key": "zSMudZtOD6STp9KlT6TLLg(("
        }
    if choice == 1: # write the problem yourself.
        # Set the base URL for the Stack Exchange API
        reqeust = get_queryset(user_input)
        # Send the request to the API
        response = requests.get(reqeust, params=params)
        # Check if the request was successful
        if response.status_code == 200:
            openStack(response)
        else:
            print("Request didnt go as planned!" + response.status_code)
    else:
        try:
        #need to pass the code to check it .
            with open(user_input) as f:
                code = f.read()
                exec(code)
        except FileNotFoundError:#couldnt find the filename.
            print("File not found!")
            exit(1)
        except Exception as error:
            error_message = str(error)
            # Set the base URL for the Stack Exchange API
            reqeust = get_queryset(error_message)
            # Send the request to the API
            response = requests.get(reqeust, params=params)
            # Check if the request was successful
            if response.status_code == 200:
                openStack(response)
            else:
                print("Request didnt go as planned :( " + response.status_code)
            
            return True




import requests
import os
from datetime import datetime

PIXELA_USERNAME = "stingzld"
PIXELA_TOKEN = os.environ['PIXELA_TOKEN']

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
WEBHOOK_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/webhooks"
HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

GRAPH_ID = "coding-graph"


# -------------------------------- FUNCTIONS -------------------------------- #
def choose_date():
    choice = input("Are you using today's date?\n"
                   "Enter 'Y' for yes, 'N' for no:  ")

    if choice.lower() == "y":
        today = datetime.now()
        today_formatted = today.strftime("%Y%m%d")
        return today_formatted
    elif choice.lower() == "n":
        date = input("Enter the date in the yyyyMMdd format:  ")
        return date
    else:
        print("Invalid Date")
        exit()


def choose_quantity():
    return input("Enter the number of minutes you coded:  ")


def create_user():
    user_params = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    return requests.post(url=PIXELA_ENDPOINT, json=user_params)


def create_graph():
    graph_params = {
        "id": GRAPH_ID,
        "name": "Coding Graph",
        "unit": "minutes",
        "type": "int",
        "color": "shibafu",
        "timezone": "America/Chicago"
    }

    return requests.post(url=GRAPH_ENDPOINT,
                         json=graph_params,
                         headers=HEADERS
                         )


def delete_graph():
    return requests.delete(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}",
                           headers=HEADERS
                           )


def post_pixel():
    date = choose_date()
    quantity = choose_quantity()

    pixel_params = {
        "date": date,
        "quantity": quantity
    }

    return requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}",
                         json=pixel_params,
                         headers=HEADERS
                         )


def update_pixel():
    date = choose_date()
    quantity = choose_quantity()

    pixel_params = {
        "quantity": quantity
    }

    return requests.put(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{date}",
                        json=pixel_params,
                        headers=HEADERS
                        )


def delete_pixel():
    date = choose_date()

    return requests.delete(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/{date}",
                           headers=HEADERS
                           )


def stopwatch_webhook():
    webhook_params = {
        "graphID": GRAPH_ID,
        "type": "stopwatch"
    }

    return requests.post(url=WEBHOOK_ENDPOINT,
                         json=webhook_params,
                         headers=HEADERS
                         )


def stopwatch():
    return requests.post(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/stopwatch",
                         headers=HEADERS
                         )


# -------------------------------- MAIN CODE -------------------------------- #
more_to_do = True
while more_to_do:
    action = input("\nWhich of the following would you like to do?\n"
                   "Press 1 to Create a User\n"
                   "Press 2 to Create a Graph\n"
                   "Press 3 to Delete a Graph\n"
                   "Press 4 to Post a Pixel\n"
                   "Press 5 to Update a Pixel\n"
                   "Press 6 to Delete a Pixel\n"
                   "Press 7 to Create Stopwatch Webhook\n"
                   "Press 8 to Start/Stop the Stopwatch\n")
    response = None

    if action == "1":
        response = create_user()
    elif action == "2":
        response = create_graph()
    elif action == "3":
        response = delete_graph()
    elif action == "4":
        response = post_pixel()
    elif action == "5":
        response = update_pixel()
    elif action == "6":
        response = delete_pixel()
    elif action == "7":
        response = stopwatch_webhook()
    elif action == "8":
        response = stopwatch()

    print(response.status_code)
    print(response.text)

    choice = input("\nWould you like to perform another action?\n"
                   "Enter 'Y' for yes, 'N' for no:  ")

    if choice.lower() == "n":
        more_to_do = False

#Event Concierge
# Install required packages
# pip install requests
# pip install openai
import os
import json
from dotenv import load_dotenv
import requests
import openai

# Load environment variables from .env file
load_dotenv()

# Load configuration from JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

# Extract API keys and default values, using environment variables if available
eventbrite_api_key = os.getenv("EVENTBRITE_API_KEY", config.get("eventbrite_api_key"))
openai_api_key = os.getenv("OPENAI_API_KEY", config.get("openai_api_key"))
location = os.getenv("DEFAULT_LOCATION", config.get("default_location"))
interests = os.getenv("DEFAULT_INTERESTS", config.get("default_interests")).split(',')

def get_events_from_eventbrite(location: str, interests: list) -> list:
    url = "https://www.eventbriteapi.com/v3/events/search/"
    headers = {
        "Authorization": f"Bearer {eventbrite_api_key}",
    }
    params = {
        "q": ",".join(interests),
        "location.address": location,
        "sort_by": "date",
        "expand": "venue",
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return []
    data = response.json()
    events = []
    for event in data.get("events", []):
        event_info = {
            "name": event["name"]["text"],
            "description": event["description"]["text"],
            "start_time": event["start"]["local"],
            "end_time": event["end"]["local"],
            "url": event["url"],
            "venue": event["venue"]["name"],
            "address": event["venue"]["address"]["localized_address_display"],
        }
        events.append(event_info)
    return events

def chat_with_agent(prompt):
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI event concierge."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    user_input = "Find events related to technology and music in Grand Rapids, MI."
    agent_response = chat_with_agent(user_input)
    print(agent_response)

    events = get_events_from_eventbrite(location, interests)
    for event in events:
        print(f"Name: {event['name']}")
        print(f"Description: {event['description']}")
        print(f"Start Time: {event['start_time']}")
        print(f"End Time: {event['end_time']}")
        print(f"URL: {event['url']}")
        print(f"Venue: {event['venue']}")
        print(f"Address: {event['address']}\n")
import os
import json
from dotenv import load_dotenv
import requests
import openai

# Load environment variables
load_dotenv()

# Load configuration from JSON file
with open('config.json', 'r') as f:
    config = json.load(f)

# Extract API keys and default values
eventbrite_api_key = os.getenv("EVENTBRITE_API_KEY", config["eventbrite_api_key"])
openai_api_key = os.getenv("OPENAI_API_KEY", config["openai_api_key"])
location = config["default_location"]
interests = config["default_interests"]

def get_events_from_eventbrite(location: str, interests: list) -> list:
    url = "https://www.eventbriteapi.com/v3/events/search/"
    headers = {
        "Authorization": f"Bearer {eventbrite_api_key}",
    }
    params = {
        "q": ",".join(interests),
        "location.address": location,
        "sort_by": "date",
        "expand": "venue",
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return []
    data = response.json()
    events = []
    for event in data.get("events", []):
        event_info = {
            "name": event["name"]["text"],
            "description": event["description"]["text"],
            "start_time": event["start"]["local"],
            "end_time": event["end"]["local"],
            "url": event["url"],
            "venue": event["venue"]["name"],
            "address": event["venue"]["address"]["localized_address_display"],
        }
        events.append(event_info)
    return events

def chat_with_agent(prompt):
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI event concierge."},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    user_input = "Find events related to technology and music in Grand Rapids, MI."
    agent_response = chat_with_agent(user_input)
    print(agent_response)

    events = get_events_from_eventbrite(location, interests)
    for event in events:
        print(f"Name: {event['name']}")
        print(f"Description: {event['description']}")
        print(f"Start Time: {event['start_time']}")
        print(f"End Time: {event['end_time']}")
        print(f"URL: {event['url']}")
        print(f"Venue: {event['venue']}")
        print(f"Address: {event['address']}\n")

import requests
import openai
import json

{
  "version": "0.2.0",
  "configurations": 
  [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "$/Users/russhopkinson/Desktop/Event Concierge/Event Concierge.py",  // Path to your main script
      "console": "integratedTerminal",
      "args": [],  // Additional arguments
      "cwd": "${workspaceFolder}",  // Working directory
      "env": 
      {  // Environment variables
        "MY_ENV_VAR": "value"
      }
    }
  ]
}


# Function to fetch events from Eventbrite API
def get_events_from_eventbrite(location: str, interests: list) -> list:
    # Replace 'your_eventbrite_api_key' with your actual Eventbrite API key
    eventbrite_api_key = "your_eventbrite_api_key"
    url = "https://www.eventbriteapi.com/v3/events/search/"
    
    headers = {
        "Authorization": f"Bearer {eventbrite_api_key}",  # Corrected variable name
    }

    params = {
        "q": ",".join(interests),  # Convert list of interests to a comma-separated string
        "location.address": location,
        "sort_by": "date",  # Sort by date; other options are available
        "expand": "venue",
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return []  # Provide the response text for better debugging

    data = response.json()
    events = []

    for event in data.get("events", []):
        event_info = {
            "name": event["name"]["text"],
            "description": event["description"]["text"],
            "start_time": event["start"]["local"],
            "end_time": event["end"]["local"],
            "url": event["url"],
            "venue": event["venue"]["name"],
            "address": event["venue"]["address"]["localized_address_display"],
        }
        events.append(event_info)

    return events

# Example usage of get_events_from_eventbrite
location = "Grand Rapids, MI"
interests = ["technology", "art", "music"]
events = get_events_from_eventbrite(location, interests)

# Print the events
for event in events:
    print(f"Name: {event['name']}")
    print(f"Description: {event['description']}")
    print(f"Start Time: {event['start_time']}")
    print(f"End Time: {event['end_time']}")
    print(f"URL: {event['url']}")
    print(f"Venue: {event['venue']}")
    print(f"Address: {event['address']}")
    print()

# OpenAI API key setup
# Replace 'your_openai_api_key' with your actual OpenAI API key
openai.api_key = "your_openai_api_key"

# Function to interact with ChatGPT
def chat_with_agent(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI event concierge."},
                  {"role": "user", "content": prompt}],
    )
    return response.choices[0].message["content"]

# Example usage of chat_with_agent
user_input = "Find events related to technology and music in Grand Rapids, MI."
agent_response = chat_with_agent(user_input)
print(agent_response)

# Function to format event details
def format_event_details(events):
    formatted_events = []
    for event in events:
        formatted_event = (
            f"**{event['name']}**\n"
            f"{event['description']}\n"
            f"**Start Time**: {event['start_time']}\n"
            f"**End Time**: {event['end_time']}\n"
            f"**Venue**: {event['venue']}\n"
            f"**Address**: {event['address']}\n"
            f"[Event Link]({event['url']})\n"
        )
        formatted_events.append(formatted_event)
    return "\n\n".join(formatted_events)

# Example usage of formatting events
formatted_events = format_event_details(events)
print(formatted_events)



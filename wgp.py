import requests
from PIL import Image
from io import BytesIO
import time
import json
import time

# API Key is obtained from here:  https://rapidapi.com/inutil-inutil-default/api/mywhinlite
api_key = input("Please enter your x-rapidapi-key: ")

status_url = "https://mywhinlite.p.rapidapi.com/status"
qr_url = "https://mywhinlite.p.rapidapi.com/getqr"
groups_url = "https://mywhinlite.p.rapidapi.com/groups/mygroups"
headers = {
    "x-rapidapi-host": "mywhinlite.p.rapidapi.com",
    "x-rapidapi-key": api_key
}

def get_qr_code():
    try:
        qr_response = requests.get(qr_url, headers=headers)
        if qr_response.ok:
            image = Image.open(BytesIO(qr_response.content))
            print("Ensure light mode is used. Scan the QR within 20 seconds...")
            image.show()
            time.sleep(20)
            print("The QR expired. Please request a new one.")
        else:
            print(f"Error rendering QR: {qr_response.status_code}, {qr_response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching QR: {e}")

def check_status():
    try:
        status_response = requests.get(status_url, headers=headers)
        
        if status_response.ok:
            status_message = status_response.json().get("Info", "").lower()
            if "logged to the whatsapp network" in status_message:
                print("Instance is running and logged in.")
            else:
                print(f"Unexpected status message: {status_message}")
        else:
            status_message = status_response.json().get("Info", "").lower()
            if "not associated" in status_message:
                print("Instance not enroled. Requesting new QR...")
                get_qr_code()
            else:
                print(f"Response error: {status_response.status_code}, {status_response.text}")
                
    except requests.exceptions.RequestException as e:
        print(f"Status error: {e}")


def list_groups():
    try:
        response = requests.post(groups_url, headers=headers, json={})
        if response.status_code == 200:
            response_data = response.json()
            
            jids = list(set(item.get('Name') for item in response_data))
            print()
            print("These are all the WhatsApp groups you are a member of:")
            print()
            
            for i, jid in enumerate(jids, 1):
                print(f"{i}. {jid}")
                time.sleep(0.1)
            
            print()
            print(f"You are a member of {len(jids)} whatsapp groups in total.")
            print()

            selected_index = input("Enter the number of the group you want to work with: ")

            if selected_index.isdigit() and 1 <= int(selected_index) <= len(jids):
                selected_jid = jids[int(selected_index) - 1]
                print(f"The JID selected is: {selected_jid}")
                return selected_jid
            else:
                print("Invalid selection. Please choose a valid group number.")
                return None
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def fetch_group_participants(selected_jid):
    try:
        response = requests.post(groups_url, headers=headers, json={})
        if response.status_code == 200:
            response_data = response.json()
            
            selected_group = next((item for item in response_data if item.get('Name') == selected_jid), None)
            
            if selected_group:
                participants = selected_group.get('Participants', [])
                phone_numbers = [jid.split('@')[0] for participant in participants for jid in [participant.get('JID', '')]]
                phone_numbers_json = json.dumps(phone_numbers, indent=4)
                
                print("These are the group participants (JSON):")
                print(phone_numbers_json)

                # Ask user if they want to exit or list groups again
                choice = input("Enter 'exit' to quit or 'list' to view all groups again: ").strip().lower()
                if choice == 'exit':
                    print("Exiting...")
                    exit()
                elif choice == 'list':
                    return True
                else:
                    print("Invalid choice.")
                    return False
            else:
                print(f"There is no group with the JID entered: {selected_jid}")
                return False
                
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False

check_status()

while True:
    selected_jid = list_groups()
    if selected_jid:
        if not fetch_group_participants(selected_jid):
            break
    else:
        break

import json
import base64
import os
import requests
from dotenv import load_dotenv
load_dotenv()

class Texter:

    def __init__(self) -> None:
        self.__base_URL = "https://api.messagemedia.com/v1/messages"
        self.__api_key = os.getenv("API_KEY")
        self.__client_secret = os.getenv("API_SECRET")
        self.__authorization_header = self.__build_authorization_header()

    def __build_authorization_header(self) -> str:
        header_input = f"{self.__api_key}:{self.__client_secret}"
        header_bytes = header_input.encode('ascii')
        header_B64 = base64.b64encode(header_bytes)
        authorization_header = header_B64.decode('ascii')
        return authorization_header

    def __build_request_headers(self) -> dict:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Basic {self.__authorization_header}'
        }
        return headers

    def build_request_body(self, recipients: list) -> str:
        request_body = {
            "messages": []
        }

        for recipient in recipients:
            request_body["messages"].append({
                "content": f"Good morning {recipient['first_name']},\n\nI hope you had a great weekend!\n\nJust a friendly reminder to do a RAT test.\n\nYour friendly neighbourhood techy :)",
                "destination_number": f"{recipient['phone_number']}",
                "delivery_report": True,
                "format": "SMS"
            })

        return json.dumps(request_body)

    def send_text_messages(self, request_body: str) -> dict:
        headers = self.__build_request_headers()
        response = requests.post(self.__base_URL, request_body, headers=headers)
        return response

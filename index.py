import os
from texter import Texter
from dotenv import load_dotenv
load_dotenv()

TEST_MODE = False


RECIPIENTS = [
    {
        "first_name": "Nathan",
        "last_name": "Winspear",
        "phone_number": "+6421856498"
    }
] if TEST_MODE else [
    {
        "first_name": "Elliot",
        "last_name": "Alderson",
        "phone_number": "+6421856498"
    },
    {
        "first_name": "Bianca",
        "last_name": "Kulbegovic",
        "phone_number": "+642102618665"
    },
    {
        "first_name": "Kavindi",
        "last_name": "Nagahawatte",
        "phone_number": "+6421848159"
    },
    {
        "first_name": "William",
        "last_name": "Potter",
        "phone_number": "+64275802343"
    }
]

def main() -> None:
    txtr = Texter()
    request_body = txtr.build_request_body(RECIPIENTS)
    response = txtr.send_text_messages(request_body)

main()

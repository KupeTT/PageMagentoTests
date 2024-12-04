import os

from dotenv import load_dotenv

load_dotenv()

class Data:

    PASSWORD = os.getenv("PASSWORD")
    EMAIL = os.getenv("EMAIL")

    FIRST_NAME_CREATE = os.getenv("FIRST_NAME_CREATE")
    LAST_NAME_CREATE = os.getenv("LAST_NAME_CREATE")
    EMAIL_CREATE = os.getenv("EMAIL_CREATE")
    PASSWORD_CREATE = os.getenv("PASSWORD_CREATE")

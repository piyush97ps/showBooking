from typing import Dict

class User:

    def __init__(self, user_name) -> None:
        self.user_name = user_name
        self.booked_show: dict = []

    def get_user_name(self) -> str:
        return self.user_name

    def get_booked_show(self) -> list:
        return self.booked_show

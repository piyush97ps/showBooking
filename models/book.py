from typing import Dict, Tuple
from datetime import datetime
import Show
import User
from enum import Enum

class BookingStatus(Enum):
    pending = "pending" # waiting list
    confirmed = "confirmed"
    cancelled = "cancelled"

class Book:

    def __init__(self, show: Show, user: User, ticket_count: int = 1) -> None:
        self.booking_id: str = f"{show.name}_{user.user_name}"
        self.show: Show = show
        self.user: User = user
        self.ticket_count: str = ticket_count
        self.booking_status: BookingStatus = BookingStatus.pending

    def get_booking_id(self) -> str:
        return self.booking_id

    def get_booking_show(self) -> tuple:
        return self.show

    def get_booking_user(self) -> str:
        return self.user

    def get_booking_count(self) -> int:
        return self.ticket_count

    def update_status(self, status: BookingStatus) -> str:
        self.booking_status = status

    def __repr__(self) -> str:
        return f"Booking of Show: {self.show.name}, for user: {self.user.user_name}, Status: {str(self.booking_status)}"

from typing import Dict, Tuple, List
from datetime import datetime
from showBooking.models.book import Book

class Show:

    def __init__(self, name: str, genres: str, capacity: int, slot: Tuple[datetime]) -> None:
        self.name: str = name
        self.slot: tuple = slot
        self.genres: str = genres
        self.capacity: int = capacity
        self.available_capacity: int = capacity
        self.booking_queue: List[Book] = []
        self.active_booking: Dict[str, Book] = {}

    def get_show_name(self) -> str:
        return self.name

    def get_show_timing(self) -> tuple:
        return self.slot
    def get_show_start_time(self) -> datetime:
        return self.slot[0]

    def get_show_genre(self) -> str:
        return self.genres

    def get_total_capacity(self) -> int:
        return self.capacity

    def get_available_capacity(self) -> int:
        return self.available_capacity

    def update_available_capacity(self, book_count) -> bool:
        if book_count > self.available_capacity:
            raise Exception(f"Booking count {book_count} is greater then the available capacity {self.available_capacity}")
        self.available_capacity -= book_count
        return True

    def cancel_active_booking(self, booking_id) -> bool:
        if booking_id not in self.active_booking:
            return False
        booking = self.active_booking.pop(booking_id)
        self.available_capacity += booking.ticket_count

    def assign_booking_from_queue(self) -> bool:
        if not self.booking_queue:
            return True
        for booking in self.booking_queue:
            if booking.ticket_count <= self.available_capacity:
                self.active_booking[booking.booking_id] = booking
                return True
        return False

    def add_booking(self, booking: Book) -> bool:
        if booking.booking_id in self.active_booking:
            return False
        elif booking.ticket_count <= self.available_capacity:
            self.active_booking[booking.booking_id] = booking
            self.available_capacity -= booking.ticket_count
            return True
        return False

    def __repr__(self) -> str:
        return f"{self.name}, genres: {self.genres}, Timing: {self.slot[0]} - {self.slot[1]}, Total Capacity: {self.capacity}, Available Capacity: {self.available_capacity}"

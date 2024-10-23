from typing import Dict, Tuple, List
from datetime import datetime, date
from models import book, Show, User

class BookingManager:

    def __init__(self) -> None:
        self.show_by_genres: Dict[str, List[Show]] = {}
        self.booking: Dict[str, List[book]] = {}
        self.users: Dict[str, User] = {}
        self.set_booking_slot_data()

    def set_booking_slot_data(self):
        booking_date = date.today()
        self.booking_slot_range = (
            datetime(booking_date.year, booking_date.month, booking_date.day, 9, 0, 0),
             datetime(booking_date.year, booking_date.month, booking_date.day, 21, 0, 0))
        self.slot_map: dict = {
            (datetime(booking_date.year, booking_date.month, booking_date.day, 9 + i, 0, 0),
             datetime(booking_date.year, booking_date.month, booking_date.day, 10 + i, 0, 0)): None
            for i in range(12)}
    
    def showAvailByGenre(self, genre):
        return self.show_by_genres.get(genre)

    def onboardShowSlots(self):
        all_slow = self.show_by_genres.values()
        sort_by_slot = sorted(all_slow, lambda show: show.get_show_start_time())
        return sort_by_slot

    def add_user(self, user_name) -> bool:
        if user_name in self.users:
            raise Exception(f"User with user name: {user_name}, Already Exist")
        user = User(user_name=user_name)
        self.users[user_name] = user
        return user

    def cancelBookingId(self, booking_id) -> bool:
        if booking_id not in self.booking:
            raise Exception(f"No Booking Exist for give booking Id: {booking_id}")
        booking_to_cancel = self.booking.get(booking_id)
        show = booking_to_cancel.show
        user = booking_to_cancel.user
        show.cancel_active_booking(booking_id)
        show.assign_booking_from_queue()
        return True

    def registerShow(self, name: str, genres: str, capacity: int, slot: Tuple[datetime]) -> str:
        if slot not in self.slot_map:
            return "Invalid Slot, Slot Should be of 1 hour and between 9 AM to 9 PM"
        elif self.slot_map.get(slot):
            return "Slot Already booked"
        show = Show(name, genres, capacity, slot)
        self.slot_map[slot] = show
        return f"{show.name} show is registered !!"

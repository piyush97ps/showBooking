## github link: https://github.com/piyush97ps/showBooking

from datetime import datetime, date
from service.bookingManager import BookingManager

today = date.today()

if __name__ == "__main__":
    booking_manager = BookingManager()
    slot = (datetime(today.year, today.month, today.day, 9, 0, 0),
             datetime(today.year, today.month, today.day, 10, 0, 0))
    res = booking_manager.registerShow(name = "TMKOC", genre="Comedy", slot=slot)
    print(res)

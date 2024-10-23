import json
import pytest

from unittest.mock import patch, Mock
import unittest

from showBooking.service.bookingManager import BookingManager


class TestBooking(unittest.TestCase):


    def test_booking_manager(self, mock_post, mock_slingshot, mock_template):
        payload_data = json.load(open("./showBooking/test/booking.json"))
        for idx, data in enumerate(payload_data):
            input_data = data.get("input")
            output_data = data.get("output")

            self.assertDictEqual({}, output_data)

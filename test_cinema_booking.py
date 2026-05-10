import pytest
from cinema_booking import CinemaBooking



def test_valid_name():
    booking = CinemaBooking()

    result = booking.validate_name("John Smith")

    assert result is True


def test_name_without_surname():
    booking = CinemaBooking()

    with pytest.raises(ValueError):
        booking.validate_name("John")


def test_empty_name():
    booking = CinemaBooking()

    with pytest.raises(ValueError):
        booking.validate_name("")


def test_invalid_name_type():
    booking = CinemaBooking()

    with pytest.raises(ValueError):
        booking.validate_name(123)



def test_child_morning_price():
    booking = CinemaBooking()

    result = booking.get_ticket_price(10, "morning")

    assert result == 80.0


def test_teen_day_price():
    booking = CinemaBooking()

    result = booking.get_ticket_price(15, "day")

    assert result == 150


def test_adult_evening_price():
    booking = CinemaBooking()

    result = booking.get_ticket_price(25, "evening")

    assert result == 240.0


def test_negative_age():
    booking = CinemaBooking()

    with pytest.raises(ValueError):
        booking.get_ticket_price(-1, "day")


def test_invalid_session():
    booking = CinemaBooking()

    with pytest.raises(ValueError):
        booking.get_ticket_price(20, "night")


def test_boundary_age_12():
    booking = CinemaBooking()

    result = booking.get_ticket_price(12, "day")

    assert result == 100


def test_boundary_age_13():
    booking = CinemaBooking()

    result = booking.get_ticket_price(13, "day")

    assert result == 150



def test_successful_booking():

    booking = CinemaBooking()

    result = booking.book_ticket(
        "Anna Brown",
        20,
        "day"
    )
    assert "Booking confirmed" in result
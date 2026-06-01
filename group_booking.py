from cinema_booking import CinemaBooking


def book_group(people, session):
    cinema_booking = CinemaBooking()

    bookings = []
    total = 0
    count = 0

    for person in people:
        name = person[0]
        age = person[1]

        if age < 0:
            continue

        try:
            price = cinema_booking.get_ticket_price(age, session)
        except ValueError:
            price = 0

        if price != 0:
            bookings.append(name + " - " + str(price))
            total = total + price
            count = count + 1


    if count > 10:
        total = total * 0.8
    elif count > 5:
        total = total * 0.9

    txt = ""
    for item in bookings:
        txt = txt + item + "\n"

    txt = txt + "Total: " + str(round(total, 2)) + " for " + str(count) + " tickets"

    return txt
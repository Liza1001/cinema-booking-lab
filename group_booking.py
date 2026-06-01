from cinema_booking import CinemaBooking

<<<<<<< HEAD

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
=======
# import datetime  # for future logging


def book_group(ppl, s):
    cb = CinemaBooking()
    lst = []
    total = 0
    cnt = 0
    for person in ppl:
        nm = person[0]
        a = person[1]
        if a < 0:
            continue
        try:
            pr = cb.get_ticket_price(a, s)
        except:
            pr = 0
        if pr != 0:
            lst.append(nm + " - " + str(pr))
            total = total + pr
            cnt = cnt + 1
            # logged = nm
    if cnt > 5:
        total = total * 0.9
    elif cnt > 10:
        total = total * 0.8
    txt = ""
    for item in lst:
        txt = txt + item + "\n"
    txt = txt + "Total: " + str(round(total, 2)) + " for " + str(cnt) + " tickets"
    return txt
>>>>>>> 7b7a215db4e7fde709e37cc831e015c31e4496fc

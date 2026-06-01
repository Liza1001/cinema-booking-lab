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
📄 Файл test_group_booking.py
from group_booking import book_group


def test_single_adult():
    result = book_group([("Anna Brown", 20)], "day")
    assert "1 tickets" in result


def test_group_two():
    result = book_group([("A B", 20), ("C D", 20)], "day")
    assert "2 tickets" in result


def test_group_discount_over_5():
    people = [("N" + str(i) + " S", 20) for i in range(6)]
    result = book_group(people, "day")
    assert "1080" in result


def test_skips_negative_age():
    result = book_group([("A B", -5), ("C D", 20)], "day")
    assert "1 tickets" in result


def test_empty_group():
    result = book_group([], "day")
    assert "0 tickets" in result


def test_invalid_session():
    result = book_group([("A B", 20)], "night")
    assert "0 tickets" in result

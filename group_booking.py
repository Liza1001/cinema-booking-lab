from cinema_booking import CinemaBooking

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

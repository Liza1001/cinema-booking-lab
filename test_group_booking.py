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

class CinemaBooking:

    def validate_name(self, full_name: str) -> bool:
    

        if not isinstance(full_name, str):
            raise ValueError("Name must be a string")

        words = full_name.strip().split()

        if len(words) < 2:
            raise ValueError("Enter name and surname")

        return True


    def get_ticket_price(self, age: int, session: str) -> float:

        if age < 0:
            raise ValueError("Age cannot be negative")

        sessions = ["morning", "day", "evening"]

        if session not in sessions:
            raise ValueError("Invalid session")


        if age <= 12:
            price = 100
        elif age <= 17:
            price = 150
        else:
            price = 200


        if session == "morning":
            price *= 0.8

        elif session == "day":
            price *= 1

        elif session == "evening":
            price *= 1.2

        return round(price, 2)


    def book_ticket(self, full_name: str, age: int, session: str) -> str:


        self.validate_name(full_name)

        price = self.get_ticket_price(age, session)

        return f"Booking confirmed for {full_name}. Price: {price}"
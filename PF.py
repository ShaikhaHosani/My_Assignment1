# Library for datetime formatting
import datetime

# Guest Class and methods
class Guest:
    def __init__(self, name, email, phone, address, loyalty_points):
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__loyalty_points = loyalty_points

    # Get Name Method
    def get_name(self):
        return self.__name

    # Get Email Method
    def get_email(self):
        return self.__email

    # Get Phone Method
    def get_phone(self):
        return self.__phone

    # Get Address Method
    def get_address(self):
        return self.__address

    # Get Loyalty Points Method
    def get_loyalty_points(self):
        return self.__loyalty_points

    # Set Name Method
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone

    def set_address(self, address):
        self.__address = address

    def set_loyalty_points(self, points):
        self.__loyalty_points = points

    def make_reservation(self):
        pass  # This method is used for making a reservation

    def modify_reservation(self):
        pass  # This method allows the guest to modify an existing reservation

    def cancel_reservation(self):
        pass  # This method allows the guest to cancel an existing reservation


# Reservation Class and methods
class Reservation:
    def __init__(self, confirmation_number, check_in_date, check_out_date, room_type, number_of_guests, number_of_rooms):
        self.__confirmation_number = confirmation_number
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__room_type = room_type
        self.__number_of_guests = number_of_guests
        self.__number_of_rooms = number_of_rooms
        self.__total_charges = 0.0
        self.__status = "Confirmed"
        self.__priceline_trip_number = ""

    def get_confirmation_number(self):
        return self.__confirmation_number

    def get_check_in_date(self):
        return self.__check_in_date

    def get_check_out_date(self):
        return self.__check_out_date

    def get_room_type(self):
        return self.__room_type

    def get_number_of_guests(self):
        return self.__number_of_guests

    def get_number_of_rooms(self):
        return self.__number_of_rooms

    def get_total_charges(self):
        return self.__total_charges

    def set_total_charges(self, charges):
        self.__total_charges = charges

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_priceline_trip_number(self):
        return self.__priceline_trip_number

    def set_priceline_trip_number(self, trip_number):
        self.__priceline_trip_number = trip_number

    # Calculate Night method using datetime library for formatting
    def calculate_nights(self):
        check_in = datetime.datetime.strptime(self.__check_in_date, "%a, %b %d, %Y")
        check_out = datetime.datetime.strptime(self.__check_out_date, "%a, %b %d, %Y")
        return (check_out - check_in).days

    def calculate_charges(self):
        pass  # This method is used for calculating charges

    def generate_confirmation(self):
        pass  # This method creates a confirmation message or document for the reservation


# Room Class and methods
class Room:
    def __init__(self, room_number, room_type, rate, floor, amenities):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__rate = rate
        self.__floor = floor
        self.__amenities = amenities

    def get_room_number(self):
        return self.__room_number

    def get_room_type(self):
        return self.__room_type

    def get_rate(self):
        return self.__rate

    def get_floor(self):
        return self.__floor

    def get_amenities(self):
        return self.__amenities

    def check_availability(self):
        pass  # This method should verify if the room is available for the given dates


# Payment Class and methods
class Payment:
    def __init__(self, amount, payment_method, billing_address, payment_date, payment_status):
        self.__amount = amount
        self.__payment_method = payment_method
        self.__billing_address = billing_address
        self.__payment_date = payment_date
        self.__payment_status = payment_status

    def get_amount(self):
        return self.__amount

    def get_payment_method(self):
        return self.__payment_method

    def get_billing_address(self):
        return self.__billing_address

    def get_payment_date(self):
        return self.__payment_date

    def get_payment_status(self):
        return self.__payment_status

    def process_payment(self):
        pass  # This method handles payment processing

    def generate_receipt(self):
        pass  # This method creates a receipt or confirmation document for the payment


# Hotel Class and methods
class Hotel:
    def __init__(self, name, address, city, state, zip_code, phone):
        self.__name = name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_full_address(self):
        return self.__address + "\n" + self.__city + ", " + self.__state + "\n" + self.__zip_code

    def get_phone(self):
        return self.__phone


# Objects that populate information
guest = Guest("Ted Vera", "tedvera@mac.com", "505-851-1418", "123 Main St, Los Alamos, NM", 1200)
room = Room("101", "Queen Beds /No Smoking/Desk/Safe/Coffee Maker in Room/Hair Dryer", 89.95, 1, ["WiFi", "TV", "Mini Bar"])
reservation = Reservation("52523887", "Sun, Aug 22, 2010", "Tue, Aug 24, 2010", room.get_room_type(), 2, 1)
reservation.set_total_charges(201.48)
reservation.set_priceline_trip_number("15549850358")
payment = Payment(201.48, "Mastercard (ending in 9954)", "123 Main St, Los Alamos, NM", "08/22/2010", "Completed")
hotel = Hotel("Comfort Inn & Suites Los Alamos", "2455 Trinity Drive", "Los Alamos", "NM", "87544", "505-661-1110")

# Display information to the user
print("Your Reservation is Confirmed")
print("Thank you for your reservation. Please print your hotel receipt and show it at check-in.\n")

# Show guest information
print("Your Name: " + guest.get_name())
print("Your Email: " + guest.get_email())
print("Priceline Trip Number: " + reservation.get_priceline_trip_number())
print("Hotel Confirmation Number: " + reservation.get_confirmation_number())
print()

# Display hotel information
print(hotel.get_name())
print(hotel.get_full_address())
print("Phone: " + hotel.get_phone())
print()

# Check-in and Check-out details
print("Check-In: " + reservation.get_check_in_date() + " - 03:00 PM")
print("Check-Out: " + reservation.get_check_out_date() + " - 12:00 PM")
print("Number Of Nights: " + str(reservation.calculate_nights()))
print("Number Of Rooms: " + str(reservation.get_number_of_rooms()))
print()

# Display room assignment information
print("--------------------------------------------------------------------")
print("Room 1: " + guest.get_name())
print("--------------------------------------------------------------------")
print("Room Type: " + reservation.get_room_type())
print()

# Summary of charges
print("Summary of Charges")
print("Billing Name: Ted H Vera")
print("Credit Card: " + payment.get_payment_method())
print("Room Cost: $" + str(room.get_rate()))
print("Rooms: " + str(reservation.get_number_of_rooms()))
print("Nights: " + str(reservation.calculate_nights()))

# Calculate the subtotal for the room charges
room_subtotal = room.get_rate() * reservation.calculate_nights()
print("Room Subtotal: $" + str(room_subtotal))

# Calculate taxes and fees by subtracting the room subtotal from the total charges
taxes_and_fees = reservation.get_total_charges() - room_subtotal
print("Taxes and Fees: $" + str(taxes_and_fees))
print()

# Display the total charges
print("Total Charges: $" + str(reservation.get_total_charges()))
print("(All prices are in US dollars)")

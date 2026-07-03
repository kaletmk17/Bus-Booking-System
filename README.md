# 🚌 Bus Ticket Booking System

A modern **Bus Ticket Booking System** built with **Python** and **Tkinter**. This desktop application provides an intuitive graphical interface for booking bus tickets, calculating fares, generating ticket receipts, and saving bookings as text files.

---

## 📌 Features

* Modern and user-friendly Tkinter GUI
* Professional blue and white interface
* Passenger information form
* Automatic fare calculation
* 5% GST calculation
* Random Ticket ID generation
* Random Seat Number allocation
* Ticket receipt generation
* Save ticket as a `.txt` file
* Input validation
* Clear form functionality
* Exit confirmation dialog

---

## 🛠️ Technologies Used

* Python 3.x
* Tkinter
* ttk
* tkinter.messagebox
* random
* datetime
* os
* re

---

## 📋 Booking Details

The application collects the following information:

* Passenger Name
* Age
* Gender
* Mobile Number
* Email Address
* Source City
* Destination City
* Journey Date
* Bus Type
* Number of Seats
* Boarding Point
* Dropping Point

---

## 💰 Fare Structure

| Bus Type       | Price per Seat |
| -------------- | -------------: |
| AC Sleeper     |           ₹800 |
| AC Seater      |           ₹600 |
| Non-AC Sleeper |           ₹500 |
| Non-AC Seater  |           ₹400 |

Additional Charges:

* GST: **5%**

---

## 🎫 Ticket Includes

* Ticket ID
* Booking Date & Time
* Passenger Details
* Journey Information
* Seat Number
* Bus Type
* Fare Breakdown
* GST
* Total Amount
* Booking Status

---

## 📂 Project Structure

```text
BusTicketBooking/
│
├── bus_booking_system.py
├── README.md
└── ticket_BT-XXXXXX.txt
```

---

## ▶️ How to Run

1. Install Python 3.x.
2. Download or clone this repository.
3. Open the project in **Visual Studio Code**.
4. Open the terminal.
5. Run the following command:

```bash
python bus_booking_system.py
```

---

## ✅ Validation

The application validates:

* Required fields
* Valid email address
* 10-digit mobile number
* Numeric age
* Valid journey date
* Number of seats greater than zero

---

## 📸 Application Workflow

1. Enter passenger details.
2. Select the bus type.
3. Enter the number of seats.
4. Click **Calculate Fare**.
5. Click **Book Ticket**.
6. View the generated ticket receipt.
7. Save the ticket as a text file if required.

---

## 🚀 Future Enhancements

* Database integration (SQLite/MySQL)
* User login system
* Admin dashboard
* Online payment gateway
* PDF ticket generation
* QR code generation
* Bus schedule management
* Ticket cancellation
* Booking history
* Search and update bookings

---

## 👨‍💻 Author

**Tushar Kale**

Master of Computer Applications (MCA)

---

## 📄 License

This project is created for educational and learning purposes. You are free to use and modify it for personal or academic projects.

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!

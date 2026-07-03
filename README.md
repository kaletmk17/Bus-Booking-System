# 🚌 Bus Ticket Booking System

A modern **Bus Ticket Booking System** developed using **Python** and **Tkinter**. This desktop application provides a clean and professional graphical user interface (GUI) for booking bus tickets, calculating fares, generating ticket receipts, and saving bookings as text files.

---

# 📸 Application Screenshots

## 🏠 Home Screen

![Home Screen](/Images/HomePage.png)

## 💰 Fare Calculation

![Fare Calculation](/Images/Fare%20Calculation.png)

## 🎫 Booking Confirmed
![Booking Confirmed](/Images/Booking%20Confirmed.png)


## 🎫 Ticket Download
![Ticket Download](/Images/TicketDownload.png)


## 🎫 Ticket Receipt

![Ticket Receipt](/Images/TicketReceipt%20Preview.png)




> 
---

# ✨ Features

- 🎫 Bus ticket booking with a modern GUI
- 👤 Passenger information management
- 🚌 Source and destination city selection
- 📅 Journey date selection
- 🚍 Multiple bus type options
- 💺 Seat selection (1–10 seats)
- 💰 Automatic fare calculation
- 🧾 5% GST calculation
- 💳 Service charge calculation
- 🎟️ Random Ticket ID generation
- 💺 Automatic seat number allocation
- 📄 Ticket receipt preview
- 💾 Save ticket as a `.txt` file
- 🖨️ Print-ready ticket preview
- 🧹 Clear form functionality
- ✅ Complete input validation
- ❌ Exit confirmation dialog
- 🎨 Modern blue and white professional UI

---

# 🛠️ Technologies Used

- Python 3.x
- Tkinter
- ttk
- tkinter.messagebox
- random
- datetime
- os
- re

---

# 📋 Passenger Information

The application collects the following details:

- Passenger Name
- Age
- Gender
- Mobile Number
- Email Address
- Source City
- Destination City
- Journey Date
- Bus Type
- Number of Seats
- Boarding Point
- Dropping Point

---

# 💰 Fare Structure

| Bus Type | Price per Seat |
|-----------|---------------:|
| AC Sleeper | ₹800 |
| AC Seater | ₹600 |
| Non-AC Sleeper | ₹500 |
| Non-AC Seater | ₹400 |

### Additional Charges

- GST: **5%**
- Service Charge: **₹30**

---

# 🎫 Generated Ticket Includes

- Ticket ID
- Booking Date & Time
- Passenger Details
- Journey Details
- Bus Number
- Bus Type
- Seat Number(s)
- Departure Time
- Arrival Time
- Base Fare
- GST
- Service Charge
- Total Fare
- Booking Status

---

# 📂 Project Structure

```text
Bus-Ticket-Booking-System/
│
├── bus_booking_system.py
├── README.md
├── images/
│   ├── home.png
│   ├── fare-calculation.png
│   └── ticket-receipt.png
└── ticket_BT-XXXXXX.txt
```

---

# ▶️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Bus-Ticket-Booking-System.git
```

### 2️⃣ Open the Project

```bash
cd Bus-Ticket-Booking-System
```

### 3️⃣ Run the Application

```bash
python bus_booking_system.py
```

---

# ✅ Input Validation

The application validates:

- Required fields
- Passenger name
- Numeric age
- Valid email address
- 10-digit mobile number
- Journey date
- Source and destination cities
- Number of seats
- Boarding point
- Dropping point

---

# 📸 Application Workflow

1. Enter passenger details.
2. Select source and destination.
3. Choose the journey date.
4. Select the bus type.
5. Select the number of seats.
6. Click **Calculate Fare**.
7. Review the fare details.
8. Click **Book Ticket**.
9. View the generated ticket receipt.
10. Save the ticket as a text file.

---

# 🚀 Future Enhancements

- 🗄️ Database Integration (MySQL/SQLite)
- 🔐 User Login & Registration
- 👨‍💼 Admin Dashboard
- 💳 Online Payment Gateway
- 📄 PDF Ticket Generation
- 📧 Email Ticket Delivery
- 📱 SMS Notifications
- 🔳 QR Code Generation
- 🚌 Bus Schedule Management
- ❌ Ticket Cancellation
- 📜 Booking History
- 🔍 Search & Update Bookings
- 🌙 Dark Mode

---

# 👨‍💻 Author

**Tushar Kale**

**Master of Computer Applications (MCA)**

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is developed for **educational and learning purposes**.

You are free to use, modify, and improve this project for personal or academic use.

---

# ⭐ Show Your Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It motivates me to build more useful open-source projects.

---
**Made with ❤️ using Python & Tkinter**
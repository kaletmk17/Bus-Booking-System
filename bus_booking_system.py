

# Bus Ticket Booking System



import tkinter as tk
from tkinter import ttk, messagebox
import random
import datetime
import re
import os

class BusBookingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Ticket Booking System")
        self.root.geometry("1000x650")
        
        # Center the window on screen for a professional feel
        self.center_window(1000, 650)
        
        # Define modern color palette
        self.COLOR_BG = "#f4f6f9"           # Light blue-gray canvas background
        self.COLOR_HEADER = "#1a365d"       # Deep Royal Blue for main banners
        self.COLOR_CARD_BG = "#ffffff"      # Pure white for containers
        self.COLOR_TEXT = "#2d3748"         # Charcoal dark grey for read/labels
        self.COLOR_TEXT_LIGHT = "#718096"   # Muted gray for placeholders/notes
        
        # Button Themes (Normal state background, Hover background, Foreground text)
        self.BTN_CALC = {"bg": "#3182ce", "hover": "#2b6cb0", "fg": "#ffffff"}   # Slate Blue
        self.BTN_BOOK = {"bg": "#1a365d", "hover": "#102a43", "fg": "#ffffff"}   # Navy Blue
        self.BTN_PRINT = {"bg": "#319795", "hover": "#2c7a7b", "fg": "#ffffff"}  # Teal
        self.BTN_SAVE = {"bg": "#38a169", "hover": "#2f855a", "fg": "#ffffff"}   # Forest Green
        self.BTN_CLEAR = {"bg": "#718096", "hover": "#4a5568", "fg": "#ffffff"}  # Medium Gray
        self.BTN_EXIT = {"bg": "#e53e3e", "hover": "#c53030", "fg": "#ffffff"}   # Crimson Red
        
        # List of default cities for source/destination comboboxes
        self.CITIES = [
            "Ahmedabad", "Bangalore", "Bhopal", "Chandigarh", "Chennai", 
            "Delhi", "Goa", "Hyderabad", "Indore", "Jaipur", "Kochi", 
            "Kolkata", "Lucknow", "Mumbai", "Patna", "Pune", "Surat"
        ]
        
        # Store currently active booking data dictionary
        self.current_ticket_data = None
        
        # Setup form text variables
        self.init_variables()
        
        # Configure application styles
        self.configure_styles()
        
        # Render visual components
        self.create_widgets()

    def center_window(self, width, height):
        """Centers the Tkinter window on the primary screen monitor."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def init_variables(self):
        """Initializes all Tkinter input variables with default values."""
        self.var_name = tk.StringVar()
        self.var_age = tk.StringVar()
        self.var_gender = tk.StringVar(value="Male")
        self.var_mobile = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_source = tk.StringVar()
        self.var_destination = tk.StringVar()
        self.var_journey_date = tk.StringVar()
        self.var_bus_type = tk.StringVar(value="AC Sleeper")
        self.var_seats = tk.StringVar(value="1")
        self.var_boarding = tk.StringVar()
        self.var_dropping = tk.StringVar()
        
        # Fare display variables
        self.var_base_fare = tk.StringVar(value="₹0.00")
        self.var_gst = tk.StringVar(value="₹0.00")
        self.var_service_charge = tk.StringVar(value="₹30.00") # flat service charge
        self.var_total_fare = tk.StringVar(value="₹0.00")
        
        # Automatically set Journey Date to today to simplify user entry
        today_str = datetime.date.today().strftime("%d/%m/%Y")
        self.var_journey_date.set(today_str)

    def configure_styles(self):
        """Configures ttk styles for the modern layout theme."""
        self.root.configure(bg=self.COLOR_BG)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure frames background
        self.style.configure("TFrame", background=self.COLOR_BG)
        
        # Set text widgets aesthetics
        self.style.configure("TLabel", background=self.COLOR_CARD_BG, foreground=self.COLOR_TEXT, font=("Segoe UI", 9))
        self.style.configure("TEntry", fieldbackground="#ffffff", background="#ffffff", font=("Segoe UI", 9))
        self.style.configure("TCombobox", fieldbackground="#ffffff", background="#ffffff", font=("Segoe UI", 9))
        
        # Modern taller entries using style configuration
        self.style.configure("TEntry", padding=5)
        self.style.configure("TCombobox", padding=4)
        
        # Fix Combobox dropdown color mapping in read-only mode
        self.style.map('TCombobox', fieldbackground=[('readonly', '#ffffff')])
        self.style.map('TCombobox', selectbackground=[('readonly', '#1a365d')])
        self.style.map('TCombobox', selectforeground=[('readonly', '#ffffff')])

    def create_custom_button(self, parent, text, command, colors):
        """Creates a modern flat button with responsive hover effects."""
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=colors["bg"],
            fg=colors["fg"],
            activebackground=colors["hover"],
            activeforeground=colors["fg"],
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=0,
            cursor="hand2",
            pady=8
        )
        # Bind hover events
        btn.bind("<Enter>", lambda e, hover_color=colors["hover"]: btn.configure(bg=hover_color))
        btn.bind("<Leave>", lambda e, normal_color=colors["bg"]: btn.configure(bg=normal_color))
        return btn

    def create_widgets(self):
        """Builds and packs the layout widgets of the application."""
        # 1. Header Section
        header_frame = tk.Frame(self.root, bg=self.COLOR_HEADER, height=60)
        header_frame.pack(fill="x", side="top")
        
        header_label = tk.Label(
            header_frame, 
            text="🚌 Bus Ticket Booking System", 
            font=("Segoe UI", 18, "bold"), 
            bg=self.COLOR_HEADER, 
            fg="#ffffff"
        )
        header_label.pack(pady=12)
        
        # 2. Main Work Panel containing Left (Form) and Right (Receipt)
        main_frame = tk.Frame(self.root, bg=self.COLOR_BG)
        main_frame.pack(fill="both", expand=True, padx=20, pady=15)
        
        # Grid splits: 55% Left, 45% Right
        main_frame.columnconfigure(0, weight=11, uniform="group1")
        main_frame.columnconfigure(1, weight=9, uniform="group1")
        main_frame.rowconfigure(0, weight=1)
        
        # 3. Left Panel - Booking Form Frame (Styled Card)
        left_card = tk.Frame(
            main_frame, 
            bg=self.COLOR_CARD_BG, 
            highlightbackground="#cbd5e0", 
            highlightthickness=1, 
            bd=0
        )
        left_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        form_title = tk.Label(
            left_card, 
            text="Passenger & Journey Details", 
            font=("Segoe UI", 12, "bold"), 
            bg=self.COLOR_CARD_BG, 
            fg=self.COLOR_HEADER
        )
        form_title.pack(anchor="w", padx=15, pady=(12, 6))
        
        # Grid layout for individual Form Fields
        fields_frame = tk.Frame(left_card, bg=self.COLOR_CARD_BG)
        fields_frame.pack(fill="x", padx=15, pady=0)
        
        fields_frame.columnconfigure(0, weight=1)
        fields_frame.columnconfigure(1, weight=1)
        
        # Helper inline to reduce vertical code size
        def create_field_label(text, r, c, pad_x):
            lbl = tk.Label(fields_frame, text=text, font=("Segoe UI", 9, "bold"), bg=self.COLOR_CARD_BG, fg=self.COLOR_TEXT)
            lbl.grid(row=r, column=c, sticky="w", padx=pad_x, pady=(4, 1))
            return lbl

        # Row 0: Passenger Name & Age
        create_field_label("Passenger Name *", 0, 0, (0, 10))
        self.ent_name = ttk.Entry(fields_frame, textvariable=self.var_name)
        self.ent_name.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=(0, 4))
        
        create_field_label("Age *", 0, 1, (10, 0))
        self.ent_age = ttk.Entry(fields_frame, textvariable=self.var_age)
        self.ent_age.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=(0, 4))
        
        # Row 1: Gender & Mobile
        create_field_label("Gender *", 2, 0, (0, 10))
        self.cmb_gender = ttk.Combobox(fields_frame, textvariable=self.var_gender, values=["Male", "Female", "Other"], state="readonly")
        self.cmb_gender.grid(row=3, column=0, sticky="ew", padx=(0, 10), pady=(0, 4))
        
        create_field_label("Mobile Number *", 2, 1, (10, 0))
        self.ent_mobile = ttk.Entry(fields_frame, textvariable=self.var_mobile)
        self.ent_mobile.grid(row=3, column=1, sticky="ew", padx=(10, 0), pady=(0, 4))
        
        # Row 2: Email & Source
        create_field_label("Email Address *", 4, 0, (0, 10))
        self.ent_email = ttk.Entry(fields_frame, textvariable=self.var_email)
        self.ent_email.grid(row=5, column=0, sticky="ew", padx=(0, 10), pady=(0, 4))
        
        create_field_label("Source City *", 4, 1, (10, 0))
        self.cmb_source = ttk.Combobox(fields_frame, textvariable=self.var_source, values=self.CITIES)
        self.cmb_source.grid(row=5, column=1, sticky="ew", padx=(10, 0), pady=(0, 4))
        
        # Row 3: Destination & Journey Date
        create_field_label("Destination City *", 6, 0, (0, 10))
        self.cmb_destination = ttk.Combobox(fields_frame, textvariable=self.var_destination, values=self.CITIES)
        self.cmb_destination.grid(row=7, column=0, sticky="ew", padx=(0, 10), pady=(0, 4))
        
        create_field_label("Journey Date (DD/MM/YYYY) *", 6, 1, (10, 0))
        self.ent_journey_date = ttk.Entry(fields_frame, textvariable=self.var_journey_date)
        self.ent_journey_date.grid(row=7, column=1, sticky="ew", padx=(10, 0), pady=(0, 4))
        
        # Row 4: Bus Type & Number of Seats
        create_field_label("Bus Type *", 8, 0, (0, 10))
        self.cmb_bus_type = ttk.Combobox(fields_frame, textvariable=self.var_bus_type, values=["AC Sleeper", "AC Seater", "Non-AC Sleeper", "Non-AC Seater"], state="readonly")
        self.cmb_bus_type.grid(row=9, column=0, sticky="ew", padx=(0, 10), pady=(0, 4))
        
        create_field_label("Number of Seats *", 8, 1, (10, 0))
        self.cmb_seats = ttk.Combobox(fields_frame, textvariable=self.var_seats, values=[str(x) for x in range(1, 11)], state="readonly")
        self.cmb_seats.grid(row=9, column=1, sticky="ew", padx=(10, 0), pady=(0, 4))
        
        # Row 5: Boarding & Dropping Points
        create_field_label("Boarding Point *", 10, 0, (0, 10))
        self.ent_boarding = ttk.Entry(fields_frame, textvariable=self.var_boarding)
        self.ent_boarding.grid(row=11, column=0, sticky="ew", padx=(0, 10), pady=(0, 4))
        
        create_field_label("Dropping Point *", 10, 1, (10, 0))
        self.ent_dropping = ttk.Entry(fields_frame, textvariable=self.var_dropping)
        self.ent_dropping.grid(row=11, column=1, sticky="ew", padx=(10, 0), pady=(0, 4))
        
        # 4. Left Panel - Fare Details Section
        fare_frame = tk.LabelFrame(
            left_card, 
            text=" Fare Details ", 
            font=("Segoe UI", 10, "bold"), 
            bg=self.COLOR_CARD_BG, 
            fg=self.COLOR_HEADER,
            highlightbackground="#e2e8f0", 
            highlightthickness=1, 
            bd=0, 
            padx=10, 
            pady=6
        )
        fare_frame.pack(fill="x", padx=15, pady=(8, 4))
        
        fare_frame.columnconfigure(0, weight=1)
        fare_frame.columnconfigure(1, weight=1)
        fare_frame.columnconfigure(2, weight=1)
        fare_frame.columnconfigure(3, weight=1)
        
        # Base Fare Label & Read-only Display
        lbl_base = tk.Label(fare_frame, text="Base Fare:", bg=self.COLOR_CARD_BG, font=("Segoe UI", 9))
        lbl_base.grid(row=0, column=0, sticky="e", padx=(2, 5), pady=2)
        ent_base = ttk.Entry(fare_frame, textvariable=self.var_base_fare, state="readonly", width=12, justify="right")
        ent_base.grid(row=0, column=1, sticky="w", padx=(0, 8), pady=2)
        
        # GST Display
        lbl_gst_f = tk.Label(fare_frame, text="GST (5%):", bg=self.COLOR_CARD_BG, font=("Segoe UI", 9))
        lbl_gst_f.grid(row=0, column=2, sticky="e", padx=(2, 5), pady=2)
        ent_gst_f = ttk.Entry(fare_frame, textvariable=self.var_gst, state="readonly", width=12, justify="right")
        ent_gst_f.grid(row=0, column=3, sticky="w", padx=(0, 8), pady=2)
        
        # Service Charge Display
        lbl_sc = tk.Label(fare_frame, text="Service Chg:", bg=self.COLOR_CARD_BG, font=("Segoe UI", 9))
        lbl_sc.grid(row=1, column=0, sticky="e", padx=(2, 5), pady=2)
        ent_sc = ttk.Entry(fare_frame, textvariable=self.var_service_charge, state="readonly", width=12, justify="right")
        ent_sc.grid(row=1, column=1, sticky="w", padx=(0, 8), pady=2)
        
        # Total Fare Display
        lbl_total = tk.Label(fare_frame, text="Total Fare:", bg=self.COLOR_CARD_BG, font=("Segoe UI", 9, "bold"), fg=self.COLOR_HEADER)
        lbl_total.grid(row=1, column=2, sticky="e", padx=(2, 5), pady=2)
        ent_total = ttk.Entry(fare_frame, textvariable=self.var_total_fare, state="readonly", width=12, justify="right")
        ent_total.grid(row=1, column=3, sticky="w", padx=(0, 8), pady=2)
        
        # 5. Left Panel - Control Buttons Section
        btn_frame = tk.Frame(left_card, bg=self.COLOR_CARD_BG)
        btn_frame.pack(fill="x", padx=15, pady=(8, 12))
        
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)
        
        # Command buttons instantiation
        self.btn_calc = self.create_custom_button(btn_frame, "🧮 Calculate Fare", self.action_calculate_fare, self.BTN_CALC)
        self.btn_calc.grid(row=0, column=0, sticky="ew", padx=(0, 4), pady=(0, 6))
        
        self.btn_book = self.create_custom_button(btn_frame, "🎫 Book Ticket", self.action_book_ticket, self.BTN_BOOK)
        self.btn_book.grid(row=0, column=1, sticky="ew", padx=(4, 0), pady=(0, 6))
        
        self.btn_print = self.create_custom_button(btn_frame, "🖨️ Print Ticket", self.action_print_ticket, self.BTN_PRINT)
        self.btn_print.grid(row=1, column=0, sticky="ew", padx=(0, 4), pady=(0, 6))
        
        self.btn_save = self.create_custom_button(btn_frame, "💾 Save Ticket File", self.action_save_ticket, self.BTN_SAVE)
        self.btn_save.grid(row=1, column=1, sticky="ew", padx=(4, 0), pady=(0, 6))
        
        self.btn_clear = self.create_custom_button(btn_frame, "🧹 Clear Form", self.action_clear_fields, self.BTN_CLEAR)
        self.btn_clear.grid(row=2, column=0, sticky="ew", padx=(0, 4), pady=0)
        
        self.btn_exit = self.create_custom_button(btn_frame, "❌ Exit System", self.action_exit_app, self.BTN_EXIT)
        self.btn_exit.grid(row=2, column=1, sticky="ew", padx=(4, 0), pady=0)
        
        # 6. Right Panel - Ticket Receipt Card Frame
        right_card = tk.Frame(
            main_frame, 
            bg=self.COLOR_CARD_BG, 
            highlightbackground="#cbd5e0", 
            highlightthickness=1, 
            bd=0
        )
        right_card.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        lbl_receipt_title = tk.Label(
            right_card, 
            text="📄 Ticket Receipt Preview", 
            font=("Segoe UI", 12, "bold"), 
            bg=self.COLOR_CARD_BG, 
            fg=self.COLOR_HEADER
        )
        lbl_receipt_title.pack(anchor="w", padx=15, pady=(12, 6))
        
        # Nested Frame for text area and dual scrollbars
        text_container = tk.Frame(right_card, bg="#f7fafc")
        text_container.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
        self.receipt_text = tk.Text(
            text_container,
            font=("Consolas", 10),
            bg="#ffffff",
            fg="#2d3748",
            bd=0,
            highlightthickness=1,
            highlightbackground="#cbd5e0",
            wrap="none"
        )
        scrollbar_y = ttk.Scrollbar(text_container, orient="vertical", command=self.receipt_text.yview)
        scrollbar_x = ttk.Scrollbar(text_container, orient="horizontal", command=self.receipt_text.xview)
        
        self.receipt_text.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        self.receipt_text.pack(side="left", fill="both", expand=True)
        
        # Set placeholder text
        self.set_receipt_placeholder()

    def set_receipt_placeholder(self):
        """Displays helper instructions in the ticket receipt panel."""
        self.receipt_text.configure(state="normal")
        self.receipt_text.delete("1.0", "end")
        placeholder = (
            "\n" * 7 +
            "            ==============================\n"
            "                 No active booking.\n"
            "            ==============================\n\n"
            "            1. Fill out booking form details.\n"
            "            2. Click 'Calculate Fare' to review.\n"
            "            3. Click 'Book Ticket' to process.\n"
            "            4. Click 'Print Ticket' to preview receipt."
        )
        self.receipt_text.insert("1.0", placeholder)
        self.receipt_text.configure(state="disabled")

    def perform_fare_calculation(self):
        """Helper function that executes fare math logic and returns details."""
        bus_type = self.var_bus_type.get()
        seats_str = self.var_seats.get()
        
        if not seats_str.isdigit() or int(seats_str) <= 0:
            raise ValueError("Number of seats must be a positive integer.")
            
        seats = int(seats_str)
        rate_map = {
            "AC Sleeper": 800,
            "AC Seater": 600,
            "Non-AC Sleeper": 500,
            "Non-AC Seater": 400
        }
        
        rate = rate_map.get(bus_type, 400)
        base_fare = rate * seats
        gst = base_fare * 0.05
        service_charge = 30.0
        total_fare = base_fare + gst + service_charge
        
        return base_fare, gst, service_charge, total_fare, rate

    def action_calculate_fare(self, show_msg=True):
        """Handles Fare Calculation request and updates read-only form entries."""
        try:
            # Simple validation on seats
            seats_str = self.var_seats.get().strip()
            if not seats_str:
                messagebox.showerror("Validation Error", "Please select or input number of seats.")
                return None
                
            base_fare, gst, service_charge, total, rate = self.perform_fare_calculation()
            
            # Format UI variables
            self.var_base_fare.set(f"₹{base_fare:.2f}")
            self.var_gst.set(f"₹{gst:.2f}")
            self.var_service_charge.set(f"₹{service_charge:.2f}")
            self.var_total_fare.set(f"₹{total:.2f}")
            
            if show_msg:
                messagebox.showinfo(
                    "Fare Calculation", 
                    f"Fare Details calculated:\n"
                    f"-------------------------\n"
                    f"Fare per Seat : ₹{rate:.2f}\n"
                    f"Seats         : {self.var_seats.get()}\n"
                    f"Base Fare     : ₹{base_fare:.2f}\n"
                    f"GST (5%)      : ₹{gst:.2f}\n"
                    f"Service Chg.  : ₹{service_charge:.2f}\n"
                    f"-------------------------\n"
                    f"Total Fare    : ₹{total:.2f}"
                )
            return base_fare, gst, service_charge, total
        except ValueError as ve:
            messagebox.showerror("Validation Error", str(ve))
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate fare: {str(e)}")
            return None

    def action_book_ticket(self):
        """Validates all client-side inputs, generates ticket components and triggers receipt."""
        try:
            # Extract inputs
            name = self.var_name.get().strip()
            age_str = self.var_age.get().strip()
            gender = self.var_gender.get().strip()
            mobile = self.var_mobile.get().strip()
            email = self.var_email.get().strip()
            source = self.var_source.get().strip()
            destination = self.var_destination.get().strip()
            journey_date = self.var_journey_date.get().strip()
            bus_type = self.var_bus_type.get().strip()
            seats_str = self.var_seats.get().strip()
            boarding = self.var_boarding.get().strip()
            dropping = self.var_dropping.get().strip()
            
            # 1. Validation check for general empty inputs
            required_fields = {
                "Passenger Name": name,
                "Age": age_str,
                "Gender": gender,
                "Mobile Number": mobile,
                "Email": email,
                "Source City": source,
                "Destination City": destination,
                "Journey Date": journey_date,
                "Bus Type": bus_type,
                "Number of Seats": seats_str,
                "Boarding Point": boarding,
                "Dropping Point": dropping
            }
            
            for label, value in required_fields.items():
                if not value:
                    messagebox.showerror("Validation Error", f"The field '{label}' is required and cannot be empty.")
                    return
            
            # 2. Strict Input validation
            # Passenger Name check
            if not re.match(r"^[a-zA-Z\s.]+$", name):
                messagebox.showerror("Validation Error", "Passenger Name must contain only alphabets, spaces, or periods.")
                return
                
            # Age integer check
            if not age_str.isdigit():
                messagebox.showerror("Validation Error", "Age must be a valid number.")
                return
            age = int(age_str)
            if age < 1 or age > 120:
                messagebox.showerror("Validation Error", "Age must be a logical value between 1 and 120.")
                return
                
            # Mobile number check
            if not mobile.isdigit() or len(mobile) != 10:
                messagebox.showerror("Validation Error", "Mobile Number must be exactly 10 digits.")
                return
                
            # Email pattern check
            email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            if not re.match(email_regex, email):
                messagebox.showerror("Validation Error", "Please provide a valid email address.")
                return
                
            # City conflicts check
            if source.lower() == destination.lower():
                messagebox.showerror("Validation Error", "Source City and Destination City cannot be the same.")
                return
                
            # Date structure and logic check
            try:
                j_date = datetime.datetime.strptime(journey_date, "%d/%m/%Y").date()
                if j_date < datetime.date.today():
                    messagebox.showerror("Validation Error", "Journey Date cannot be in the past.")
                    return
            except ValueError:
                messagebox.showerror("Validation Error", "Journey Date must be a valid calendar date in DD/MM/YYYY format.")
                return
                
            # Seats integer check
            if not seats_str.isdigit() or int(seats_str) <= 0:
                messagebox.showerror("Validation Error", "Seats must be a positive integer.")
                return
            seats = int(seats_str)
            
            # 3. Process Fare
            fare_details = self.action_calculate_fare(show_msg=False)
            if not fare_details:
                return # Error message already triggered
            base_fare, gst, service_charge, total = fare_details
            
            # 4. Generate Random Booking Variables
            # Random Ticket ID (BT-XXXXXX)
            ticket_id = f"BT-{random.randint(100000, 999999)}"
            
            # Current Date & Time
            booking_date = datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")
            
            # Random Bus Number
            states = ["DL", "MH", "KA", "UP", "HR", "GJ", "TS", "TN", "WB"]
            bus_no = f"{random.choice(states)}-{random.randint(1, 99):02d}-{random.choice(['A','B','C','D','S','R'])}{random.choice(['A','B','C','D','E','F','Z'])}-{random.randint(1000, 9999)}"
            
            # Random Seat Numbers
            start_seat = random.randint(1, 30)
            seat_numbers = [f"S{start_seat + i}" for i in range(seats)]
            seats_str_val = ", ".join(seat_numbers)
            
            # Random Departure & Arrival times
            dep_hour = random.randint(6, 23)
            dep_min = random.choice([0, 15, 30, 45])
            dep_dt = datetime.datetime(2026, 7, 3, dep_hour, dep_min)
            dep_time = dep_dt.strftime("%I:%M %p")
            
            # Calculate Arrival time (add 6 to 12 hours)
            duration = random.randint(6, 12)
            arr_dt = dep_dt + datetime.timedelta(hours=duration, minutes=30)
            arr_time = arr_dt.strftime("%I:%M %p")
            if arr_dt.day > dep_dt.day:
                arr_time += " (Next Day)"
                
            # Store generated data in state
            self.current_ticket_data = {
                "ticket_id": ticket_id,
                "booking_date": booking_date,
                "name": name,
                "age": age,
                "gender": gender,
                "mobile": mobile,
                "email": email,
                "source": source,
                "destination": destination,
                "journey_date": journey_date,
                "dep_time": dep_time,
                "arr_time": arr_time,
                "bus_type": bus_type,
                "bus_no": bus_no,
                "seats_str": seats_str_val,
                "base_fare": base_fare,
                "gst": gst,
                "service_charge": service_charge,
                "total_fare": total
            }
            
            # Trigger success dialog
            messagebox.showinfo(
                "Booking Confirmed", 
                f"Ticket booked successfully!\n\n"
                f"Ticket ID: {ticket_id}\n"
                f"Seat Number(s): {seats_str_val}\n"
                f"Total Fare: ₹{total:.2f}\n\n"
                f"Click 'Print Ticket' to preview receipt."
            )
            
            # Auto-print to receipt frame on booking for better flow
            self.action_print_ticket()
            
        except Exception as e:
            messagebox.showerror("Booking Error", f"An unexpected error occurred: {str(e)}")

    def action_print_ticket(self):
        """Displays the booked ticket into the right receipt section."""
        if not self.current_ticket_data:
            messagebox.showerror("Print Error", "No active booking found. Please complete the booking form first.")
            return
            
        try:
            # Enable text edits
            self.receipt_text.configure(state="normal")
            self.receipt_text.delete("1.0", "end")
            
            d = self.current_ticket_data
            
            receipt_content = f"""========================================
               BUS TICKET
========================================
Ticket ID      : {d['ticket_id']}
Booking Date   : {d['booking_date']}
Passenger Name : {d['name']}
Age            : {d['age']}
Gender         : {d['gender']}
Mobile         : {d['mobile']}
Email          : {d['email']}

FROM           : {d['source']}
TO             : {d['destination']}

Journey Date   : {d['journey_date']}
Departure Time : {d['dep_time']}
Arrival Time   : {d['arr_time']}

Bus Type       : {d['bus_type']}
Bus Number     : {d['bus_no']}
Seat Number(s) : {d['seats_str']}

Base Fare      : ₹{d['base_fare']:.2f}
GST            : ₹{d['gst']:.2f}
Service Charge : ₹{d['service_charge']:.2f}
Total          : ₹{d['total_fare']:.2f}

Status : CONFIRMED

Thank You!
Have a Safe Journey.
========================================
"""
            # Insert and make read-only
            self.receipt_text.insert("1.0", receipt_content)
            self.receipt_text.configure(state="disabled")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to display ticket preview: {str(e)}")

    def action_save_ticket(self):
        """Saves the formatted receipt block to a local .txt file."""
        if not self.current_ticket_data:
            messagebox.showerror("Save Error", "No ticket is available to save. Please book a ticket first.")
            return
            
        try:
            ticket_content = self.receipt_text.get("1.0", "end-1c")
            if "No active booking." in ticket_content or not ticket_content.strip():
                messagebox.showerror("Save Error", "Ticket receipt preview has not been rendered.")
                return
                
            ticket_id = self.current_ticket_data["ticket_id"]
            filename = f"ticket_{ticket_id}.txt"
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(ticket_content)
                
            abs_path = os.path.abspath(filename)
            messagebox.showinfo(
                "Save Successful", 
                f"Ticket text file saved successfully!\n\n"
                f"Filename: {filename}\n"
                f"Location: {abs_path}"
            )
        except Exception as e:
            messagebox.showerror("Save Error", f"An error occurred while saving the file: {str(e)}")

    def action_clear_fields(self):
        """Clears all inputs on the form and resets receipt preview."""
        # Clean StringVars
        self.var_name.set("")
        self.var_age.set("")
        self.var_gender.set("Male")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_source.set("")
        self.var_destination.set("")
        self.var_boarding.set("")
        self.var_dropping.set("")
        
        # Reset Journey date to today
        today_str = datetime.date.today().strftime("%d/%m/%Y")
        self.var_journey_date.set(today_str)
        
        # Reset Bus types
        self.var_bus_type.set("AC Sleeper")
        self.var_seats.set("1")
        
        # Reset Fare Variables
        self.var_base_fare.set("₹0.00")
        self.var_gst.set("₹0.00")
        self.var_service_charge.set("₹30.00")
        self.var_total_fare.set("₹0.00")
        
        # Clean state variables
        self.current_ticket_data = None
        
        # Reset receipt UI block
        self.set_receipt_placeholder()
        
        # Visual alert
        messagebox.showinfo("Form Reset", "All entries have been cleared successfully.")

    def action_exit_app(self):
        """Prompts confirmation dialog and shuts down the window loop."""
        confirm = messagebox.askyesno("Exit Confirmation", "Are you sure you want to close the Bus Ticket Booking System?")
        if confirm:
            self.root.destroy()

if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()
    
    # Initialize the app class
    app = BusBookingSystem(root)
    
    # Launch window event loop
    root.mainloop()

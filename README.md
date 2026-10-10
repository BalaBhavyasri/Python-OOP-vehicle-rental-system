# Python-OOP-vehicle-rental-system
A menu-driven vehicle rental application built with Python, demonstrating encapsulation, inheritance, polymorphism, abstraction, and other OOP concepts.

# 🚗 Vehicle Rental System Using Python OOP

## 📌 Project Overview
The Vehicle Rental System is a simple, menu-driven Python application developed using Object-Oriented Programming (OOP) concepts. It allows users to view available vehicles, rent cars and bikes, calculate rental charges, return vehicles, and view rental history.

This project demonstrates how OOP principles can be applied to develop a real-world management system.

## 🎯 Objectives
- Understand and implement Python OOP concepts.
- Manage vehicle availability and rental records.
- Calculate rental charges based on vehicle type and rental duration.
- Practice exception handling and input validation.

## ✨ Features
- 🚘 Display available cars and bikes.
- 📝 Rent vehicles by entering their IDs.
- 💰 Calculate rental costs automatically.
- 🔄 Return rented vehicles and update availability.
- 📋 Maintain rental history during program execution.
- ⚠️ Handle invalid inputs and unavailable vehicles.
- 📊 Display the total number of vehicles.

## 🛠️ Technologies Used
- **Programming Language:** Python
- **Concepts:** Object-Oriented Programming
- **Modules:** `abc` (Abstract Base Classes)
- **Interface:** Command-Line Interface (CLI)
- **External Libraries:** None

## 🧠 OOP Concepts Implemented

| Concept | Implementation |
|---|---|
| Classes and Objects | `Vehicle`, `Car`, `Bike`, `Customer`, `RentalSystem` |
| Encapsulation | Private attributes for rental price and availability |
| Inheritance | `Car` and `Bike` inherit from `Vehicle` |
| Polymorphism | Vehicle-specific `calculate_rent()` methods |
| Abstraction | Abstract `Vehicle` class using `ABC` |
| Constructors | `__init__()` initializes objects |
| Method Overriding | `Car` and `Bike` implement their own rent calculations |
| Composition | `RentalSystem` manages vehicles and rental records |
| Class Methods | `get_vehicle_count()` |
| Static Methods | `validate_days()` |
| Exception Handling | Handles invalid rental durations and inputs |

## 📂 Project Structure

```text
Vehicle-Rental-System/
│
├── vehicle_rental.py
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites
- Python 3.10 or later
- VS Code or any Python-supported editor

### Steps to Run

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Vehicle-Rental-System
   ```

3. Run the application:

   ```bash
   python vehicle_rental.py
   ```

No additional packages or installations are required.

## 🖥️ Application Menu

```text
===== VEHICLE RENTAL SYSTEM =====
1. Display vehicles
2. Rent a vehicle
3. Return a vehicle
4. Rental history
5. Total vehicle count
6. Exit
```

## 🚙 Sample Vehicles

| Vehicle ID | Brand | Type | Rent per Day |
|---|---|---|---:|
| C101 | Toyota | Car | ₹2,000 |
| C102 | Hyundai | Car | ₹1,800 |
| B101 | Honda | Bike | ₹500 |
| B102 | Yamaha | Bike | ₹600 |

Bikes receive a 10% discount on the base rental price.

## 🔮 Future Enhancements
- Store rental records in a database.
- Add customer registration and login.
- Generate printable rental receipts.
- Add vehicle search and filtering.
- Build a graphical user interface using Tkinter.
- Implement date-based rentals and late-return charges.

## 🎓 Learning Outcomes
Through this project, I gained practical experience in designing classes, implementing the four pillars of OOP, managing object relationships, validating user inputs, and handling exceptions in Python.




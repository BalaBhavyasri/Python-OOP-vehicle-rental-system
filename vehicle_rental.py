
from abc import ABC, abstractmethod


# 1. ABSTRACTION
class Vehicle(ABC):
    vehicle_count = 0

    def __init__(self, vehicle_id, brand, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.__rent_per_day = rent_per_day  # Encapsulation
        self.__available = True
        Vehicle.vehicle_count += 1

    @property
    def rent_per_day(self):
        return self.__rent_per_day

    @property
    def available(self):
        return self.__available

    def set_availability(self, status):
        self.__available = status

    @abstractmethod
    def calculate_rent(self, days):
        pass

    def display(self):
        status = "Available" if self.available else "Rented"
        print(
            f"ID: {self.vehicle_id} | "
            f"Brand: {self.brand} | "
            f"Rent/day: Rs.{self.rent_per_day} | "
            f"Status: {status}"
        )

    @classmethod
    def get_vehicle_count(cls):
        return Vehicle.vehicle_count

    @staticmethod
    def validate_days(days):
        if days <= 0:
            raise ValueError("Rental days must be positive.")
        return True


# 2. INHERITANCE
class Car(Vehicle):
    def calculate_rent(self, days):
        self.validate_days(days)
        return self.rent_per_day * days


class Bike(Vehicle):
    def calculate_rent(self, days):
        self.validate_days(days)
        return self.rent_per_day * days * 0.9


# Customer class
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id


# 3. COMPOSITION
class RentalSystem:
    def __init__(self):
        self.vehicles = [
            Car("C101", "Toyota", 2000),
            Car("C102", "Hyundai", 1800),
            Bike("B101", "Honda", 500),
            Bike("B102", "Yamaha", 600)
        ]
        self.rentals = []

    def show_vehicles(self):
        print("\n--- Vehicle List ---")
        for vehicle in self.vehicles:
            vehicle.display()

    def rent_vehicle(self):
        vehicle_id = input("Enter vehicle ID: ").strip()

        vehicle = next(
            (v for v in self.vehicles
             if v.vehicle_id == vehicle_id),
            None
        )

        if vehicle is None:
            print("Vehicle not found.")
            return

        if not vehicle.available:
            print("Sorry, this vehicle is already rented.")
            return

        try:
            days = int(input("Enter rental days: "))
            Vehicle.validate_days(days)

            name = input("Enter customer name: ").strip()
            if not name:
                print("Customer name cannot be empty.")
                return

            customer = Customer(name, f"U{len(self.rentals) + 1}")
            amount = vehicle.calculate_rent(days)

            vehicle.set_availability(False)

            self.rentals.append({
                "customer": customer,
                "vehicle": vehicle,
                "days": days,
                "amount": amount
            })

            print("\n--- Rental Successful ---")
            print(f"Customer: {customer.name}")
            print(f"Vehicle: {vehicle.brand}")
            print(f"Days: {days}")
            print(f"Total rent: Rs.{amount:.2f}")

        except ValueError as error:
            print("Invalid input:", error)

    def return_vehicle(self):
        vehicle_id = input("Enter vehicle ID to return: ").strip()

        for rental in self.rentals:
            vehicle = rental["vehicle"]

            if (vehicle.vehicle_id == vehicle_id
                    and not vehicle.available):
                vehicle.set_availability(True)
                print(f"{vehicle.brand} returned successfully.")
                return

        print("No active rental found for that vehicle.")

    def show_history(self):
        print("\n--- Rental History ---")

        if not self.rentals:
            print("No rentals recorded.")
            return

        for rental in self.rentals:
            print(
                f"Customer: {rental['customer'].name} | "
                f"Vehicle: {rental['vehicle'].brand} | "
                f"Days: {rental['days']} | "
                f"Amount: Rs.{rental['amount']:.2f} | "
                f"Status: "
                f"{'Returned' if rental['vehicle'].available else 'Rented'}"
            )


# Main program
def main():
    system = RentalSystem()

    while True:
        print("\n===== VEHICLE RENTAL SYSTEM =====")
        print("1. Display vehicles")
        print("2. Rent a vehicle")
        print("3. Return a vehicle")
        print("4. Rental history")
        print("5. Total vehicle count")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            system.show_vehicles()
        elif choice == "2":
            system.rent_vehicle()
        elif choice == "3":
            system.return_vehicle()
        elif choice == "4":
            system.show_history()
        elif choice == "5":
            print("Total vehicles:",
                  Vehicle.get_vehicle_count())
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

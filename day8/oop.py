class vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class car(vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"{super().display_info()} with {self.num_doors} doors"

class motorcycle(vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        sidecar_info = "with a sidecar" if self.has_sidecar else "without a sidecar"
        return f"{super().display_info()} {sidecar_info}"

vehicles = []
while True:
    print("1. Add Car")
    print("2. Add Motorcycle")
    print("3. Display Vehicles")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        year = input("Enter car year: ")
        num_doors = input("Enter number of doors: ")
        vehicles.append(car(make, model, year, num_doors))
        print("Car added successfully.")
    elif choice == '2':
        make = input("Enter motorcycle make: ")
        model = input("Enter motorcycle model: ")
        year = input("Enter motorcycle year: ")
        has_sidecar = input("Does it have a sidecar? (yes/no): ").lower() == 'yes'
        vehicles.append(motorcycle(make, model, year, has_sidecar))
        print("Motorcycle added successfully.")
    elif choice == '3':
        if vehicles:
            for v in vehicles:
                print(v.display_info())
        else:
            print("No vehicles found.")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


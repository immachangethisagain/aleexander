# PHYSICS CALCULATOR

# Function for Force
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    result = mass * acceleration
    print("Force =", result, "N")


# Function for Kinetic Energy
def kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    result = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", result, "J")


# Function for Voltage
def voltage():
    current = float(input("Enter current (A): "))
    resistance = float(input("Enter resistance (Ω): "))
    result = current * resistance
    print("Voltage =", result, "V")


# Function for Potential Energy
def potential_energy():
    mass = float(input("Enter mass (kg): "))
    height = float(input("Enter height (m): "))
    gravity = 9.8
    result = mass * gravity * height
    print("Potential Energy =", result, "J")


# Function for Work
def work():
    force_value = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    result = force_value * distance
    print("Work Done =", result, "J")


# Main program
while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Force")
    print("2. Kinetic Energy")
    print("3. Voltage")
    print("4. Potential Energy")
    print("5. Work")

    choice = input("Choose an operation (1-5): ")

    if choice == "1":
        force()

    elif choice == "2":
        kinetic_energy()

    elif choice == "3":
        voltage()

    elif choice == "4":
        potential_energy()

    elif choice == "5":
        work()

    else:
        print("Invalid choice. Please choose between 1 and 5.")

    # Ask the user if they want to continue
    continue_program = input("\nDo you want to perform another calculation? (yes/no): ")

    if continue_program.lower() != "yes":
        print("Thank you for using the Physics Calculator!")
        break
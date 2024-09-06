import math

def calculate_carbon_footprint(electricity, gas, oil, car, flights):
    # Conversion factors (approximate values)
    ELECTRICITY_FACTOR = 0.4  # kg CO2 per kWh
    GAS_FACTOR = 2.3  # kg CO2 per m3
    OIL_FACTOR = 2.6  # kg CO2 per liter
    CAR_FACTOR = 0.2  # kg CO2 per km
    FLIGHT_FACTOR = 200  # kg CO2 per hour of flight

    total = (
        electricity * ELECTRICITY_FACTOR +
        gas * GAS_FACTOR +
        oil * OIL_FACTOR +
        car * CAR_FACTOR +
        flights * FLIGHT_FACTOR
    )

    return total

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to the Carbon Footprint Calculator!")
    print("Please enter your monthly usage for the following:")

    electricity = get_float_input("Electricity usage (in kWh): ")
    gas = get_float_input("Natural gas usage (in m3): ")
    oil = get_float_input("Oil usage (in liters): ")
    car = get_float_input("Car travel distance (in km): ")
    flights = get_float_input("Flight hours: ")

    footprint = calculate_carbon_footprint(electricity, gas, oil, car, flights)

    print(f"\nYour estimated monthly carbon footprint is {footprint:.2f} kg CO2.")
    print(f"Your estimated yearly carbon footprint is {footprint * 12:.2f} kg CO2.")

    # Context for the result
    average_global_footprint = 4000  # kg CO2 per year
    if footprint * 12 < average_global_footprint:
        print("Your carbon footprint is below the global average. Great job!")
    else:
        print("Your carbon footprint is above the global average. Consider ways to reduce your impact.")

    print("\nTips to reduce your carbon footprint:")
    print("1. Use energy-efficient appliances")
    print("2. Reduce car usage and consider public transportation")
    print("3. Minimize air travel")
    print("4. Use renewable energy sources")
    print("5. Reduce, reuse, and recycle")

if __name__ == "__main__":
    main()
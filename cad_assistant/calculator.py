
def calculate_cost(weight_g, cost_per_kg):
    """
    Calculates the cost of the material for a print.

    Args:
        weight_g (float): Weight of the print in grams.
        cost_per_kg (float): Cost of the filament spool per kilogram.

    Returns:
        float: Estimated cost.
    """
    if weight_g < 0 or cost_per_kg < 0:
        return 0.0

    cost_per_g = cost_per_kg / 1000.0
    return weight_g * cost_per_g

def calculate_total_cost(weight_g, cost_per_kg, print_time_hours, power_watts, electricity_cost_kwh):
    """
    Calculates total cost including electricity.

    Args:
        weight_g (float): Weight in grams.
        cost_per_kg (float): Filament cost per kg.
        print_time_hours (float): Duration of print in hours.
        power_watts (float): Average power consumption of printer in Watts.
        electricity_cost_kwh (float): Cost of electricity per kWh.

    Returns:
        float: Total estimated cost.
    """
    material_cost = calculate_cost(weight_g, cost_per_kg)

    energy_kwh = (power_watts * print_time_hours) / 1000.0
    energy_cost = energy_kwh * electricity_cost_kwh

    return material_cost + energy_cost

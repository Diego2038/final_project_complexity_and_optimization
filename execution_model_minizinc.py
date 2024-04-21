

from minizinc import Instance, Model, Solver
import re

def insert_model(params):
    """Function to execute minizinc model through the netx params:
    - n
    - m
    - consecutive_high_days_allowed
    - high_regime_percentage
    - capacity
    - production_cost
    - demand
    - payment_per_mw
    - G
    
    Example:
    params = {
        "n": 3,
        "m": 3,
        "consecutive_high_days_allowed": 1,
        "high_regime_percentage": 80,
        "capacity": [10, 300, 50],
        "production_cost": [23.5, 13.7, 31.0],
        "demand": [[300, 149, 250], [89, 52, 135], [97, 110, 89]],
        "payment_per_mw": [40.2, 55.6, 45.9],
        "G": 50
    }
    
    insert_model(params)
    """
    try:
        model = Model("PlantaFuentes/PlantaEnergia.mzn")
        solver = Solver.lookup("coin-bc")
        instance = Instance(solver, model)
        for key, value in params.items():
            instance[key] = value
        result = instance.solve()
        return str(result)
    except Exception as e:
        print(f"There's an error! OOOPPPS: {type(e)} - {e}")


def parse_data(input_string):
    """Function to obtain three variables according to str and its description
    
    Example:
    
    input_string = \"""
      Net Profit: 73250.0
      Production:
      Plant 1: 300, 300, 300, 300
      Plant 2: 200, 150, 150, 200
      Plant 3: 400, 330, 390, 350
      Delivered:
      Customer 1: 220, 150, 200, 180
      Customer 2: 100, 80, 90, 110
      Customer 3: 130, 110, 120, 100
      Customer 4: 200, 190, 180, 210
      Customer 5: 150, 140, 130, 160
      Customer 6: 100, 110, 120, 90
      \"""

    net_profit, plants, customers = parse_data(input_string)
    
    """
    # Use regular expressions to find the values in the string
    net_profit_match = re.search(r'Net Profit:\s*([0-9.]+)', input_string)
    plants_matches = re.findall(r'Plant\s*\d+:\s*([0-9, ]+)', input_string)
    customers_matches = re.findall(r'Customer\s*\d+:\s*([0-9, ]+)', input_string)

    # Convert the matches to the desired format
    net_profit = float(net_profit_match.group(1)) if net_profit_match else None
    plants = [list(map(int, plant.split(','))) for plant in plants_matches] if plants_matches else []
    customers = [list(map(int, customer.split(','))) for customer in customers_matches] if customers_matches else []

    return net_profit, plants, customers



def get_results(params):
    """
    Function to get the results according to the problem's parameters,
    and the answer is the values of production plant, mw delivered to customers and net profit through the three respective variables
    """
    result_str = insert_model(params)
    net_profit, plants, customers = parse_data(result_str)
    return net_profit, plants, customers



from minizinc import Instance, Model, Solver

def insert_model(table, total):
  try:
    model = Model("PlantaFuentes/PlantaEnergia.mzn")
    solver = Solver.lookup("coin-bc")
    instance = Instance(solver, model)
    instance["n"] = 3
    instance["m"] = 3
    instance["consecutive_high_days_allowed"] = 1
    instance["high_regime_percentage"] = 80
    instance["capacity"] = [10, 300, 50]
    instance["production_cost"] = [23.5, 13.7, 31.0]
    instance["demand"] = [
      [300, 149, 250],
      [89, 52, 135],
      [97, 110, 89]
    ]
    instance["payment_per_mw"] = [40.2, 55.6, 45.9]
    instance["G"] = 50
    result = instance.solve()
    print("La respuesta es:")
    print(result)
  except Exception as e:
    print(f"Hay un error! {type(e)} - {e}")

insert_model(None, None)
  
  
  
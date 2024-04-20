

import os

result = os.popen(" minizinc --solver COIN-BC PlantaFuentes/PlantaEnergia.mzn PlantaFuentes/Datos1.dzn")
print(str(result))
import random
# Function to check for fusion
def Fusion (particle_1, particle_2, limit=15):
    energy_sum=particle_1.energy + particle_2.energy
    if energy_sum >= limit:
        print(f"Fusion happened. Energy total: {energy_sum}")
    else:
        print(f"No fusion happened. Energy total: {energy_sum}")

# particle class
class particle:
    def __init__(self,energy):
        self.energy=energy
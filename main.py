import random
from fusion_particle import Fusion
from fusion_particle import particle


particle_1=particle(random.randint(1, 13))
particle_2=particle(random.randint(1, 13))

print("---Fusion trying to occur---")
print(f"Particle 1 energy: {particle_1.energy}")
print(f"Particle 2 energy: {particle_2.energy}")

Fusion(particle_1, particle_2)
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Define the Particle class
class Particle:
    def _init_(self, position, velocity, mass, radius):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.radius = radius

# Compute the gravitational force between two particles
def compute_gravitational_force(p1, p2, G):
    r = p2.position - p1.position
    distance = np.linalg.norm(r)
    force_magnitude = G * p1.mass * p2.mass / distance**2
    force_direction = r / distance
    return force_magnitude * force_direction

# Update the positions and velocities of all particles based on gravitational forces
def update_positions_and_velocities(particles, dt, G):
    for p1 in particles:
        force = np.zeros(2)
        for p2 in particles:
            if p1 != p2:
                force += compute_gravitational_force(p1, p2, G)
        p1.velocity += force / p1.mass * dt
        p1.position += p1.velocity * dt

# Create a list of particles with random positions, velocities, masses, and radii
def create_particles(n, box_size):
    particles = []
    for _ in range(n):
        position = np.random.rand(2) * box_size
        velocity = np.random.randn(2) * 0.1
        mass = np.random.rand() * 5 + 0.5
        radius = mass * 0.2
        particles.append(Particle(position, velocity, mass, radius))
    return particles

# Simulate the movement of particles for the given number of steps
def simulate(particles, G, dt, num_steps):
    positions = []
    for _ in range(num_steps):
        update_positions_and_velocities(particles, dt, G)
        positions.append([p.position.copy() for p in particles])
    return np.array(positions)

# Animate the simulation using the particle positions
def animate(particles, positions):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    scatters = [ax.scatter(p.position[0], p.position[1], s=p.radius*100) for p in particles]

    def update(frame):
        for i, scatter in enumerate(scatters):
            scatter.set_offsets(positions[frame, i])

    ani = FuncAnimation(fig, update, frames=range(len(positions)), interval=20)
    plt.show()

# Main function to run the simulation and animate the results
if _name_ == "_main_":
    np.random.seed(int(time.time()))

    n_particles = 10
    box_size = 10
    G = 1e-4
    dt = 0.01
    num_steps = 1000

    particles = create_particles(n_particles, box_size)
    positions = simulate(particles, G, dt, num_steps)
    animate(particles, positions)

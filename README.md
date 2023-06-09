# OneMoreThing
Intel oneAPI project<br><br>
This code defines a Particle class to store the properties of each particle (position, velocity, mass, and radius). The main functions are:
1. compute_gravitational_force: Computes the gravitational force between two particles using Newton's law of gravitation.
2. update_positions_and_velocities: Updates the positions and velocities of all particles based on the gravitational forces acting on them.
3. create_particles: Creates a list of particles with random positions, velocities, masses, and radii.
4. simulate: Simulates the movement of particles for the given number of steps, recording their positions at each step.
5. animate: Animate the simulation using the recorded particle positions.

In the if _name_ == "_main_" block, the script:

1. Initializes a random seed based on the current time.
2. Sets the number of particles, the size of the simulation box, the gravitational constant, the time step, and the number of steps for the simulation.
3. Creates the particles.
4. Runs the simulation to obtain the positions of the particles over time.
5. Animates the simulation using the particle positions.
6. The code uses the numpy library for efficient numerical computations and the matplotlib library for visualizing the results. The Intel oneMKL and oneDNN libraries optimize the performance of these operations on Intel hardware, although the code does not explicitly invoke oneAPI components<br><br>
![1](https://user-images.githubusercontent.com/81735768/225823583-1a81e763-427f-4e85-9380-8f24066c28e9.jpg)<br><br>
![2](https://user-images.githubusercontent.com/81735768/225823595-d5a10161-851a-40f7-9221-42d1d974bdb3.jpg)<br><br>
![3](https://user-images.githubusercontent.com/81735768/225823611-4077fe13-7f01-412c-980c-3d2e7cc2ef09.jpg)

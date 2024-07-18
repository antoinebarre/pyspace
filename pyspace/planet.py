from vpython import sphere, vector, color, mag, norm, rate

class CelestialBody:
    def __init__(self, name, mass, radius, position, velocity, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.sphere = sphere(pos=self.position, radius=self.radius, color=color, make_trail=True)
    
    def update_position(self, dt):
        self.position += self.velocity * dt
        self.sphere.pos = self.position
    
    def apply_force(self, force, dt):
        acceleration = force / self.mass
        self.velocity += acceleration * dt

class Simulation:
    def __init__(self, bodies, dt):
        self.bodies = bodies
        self.dt = dt
        self.G = 6.67430e-11  # Gravitational constant

    def calculate_gravitational_force(self, body1, body2):
        r = body2.position - body1.position
        force_magnitude = self.G * body1.mass * body2.mass / mag(r)**2
        force_direction = norm(r)
        return force_magnitude * force_direction

    def update(self):
        for body in self.bodies:
            net_force = vector(0, 0, 0)
            for other_body in self.bodies:
                if other_body != body:
                    force = self.calculate_gravitational_force(body, other_body)
                    net_force += force
            body.apply_force(net_force, self.dt)
        
        for body in self.bodies:
            body.update_position(self.dt)
    
    def run(self, steps):
        for _ in range(steps):
            rate(100)  # Control the speed of the simulation
            self.update()

# Initial positions (in meters)
pos_sun = vector(0, 0, 0)
pos_earth = vector(1.496e11, 0, 0)  # Approx 1 AU from Sun
pos_moon = pos_earth + vector(3.844e8, 0, 0)  # Approx 384,400 km from Earth

# Initial velocities (in meters per second)
vel_sun = vector(0, 0, 0)
vel_earth = vector(0, 29783, 0)  # Approx orbital speed of Earth
vel_moon = vel_earth + vector(0, 1022, 0)  # Approx orbital speed of Moon relative to Earth

# Create celestial bodies
sun = CelestialBody("Sun", 1.989e30, 6.96e8, pos_sun, vel_sun, color.yellow)
earth = CelestialBody("Earth", 5.972e24, 6.371e6, pos_earth, vel_earth, color.blue)
moon = CelestialBody("Moon", 7.348e22, 1.737e6, pos_moon, vel_moon, color.gray(0.5))

# Create simulation with a time step of 1 hour
simulation = Simulation([sun, earth, moon], 3600)

# Run the simulation for a certain number of steps
simulation.run(steps=10000)

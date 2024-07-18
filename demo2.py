# GlowScript 2.2 VPython 

from vpython import *


#constants
R=15e9
Re=150e9
Ms=2e30
Me=6e24
G=6.67e-11

#creating the Sun, set the initial position
sun=sphere(pos=vector(0,0,0), radius=R, color=color.yellow)
sun.m=Ms
#sun.p=vector(0,0,0)*sun.m

#creating Earth, set the initial position and momentum
earth=sphere(pos=vector(Re,0,0), radius=0.4*R, color=color.green)
earth.m=Me
earth.p=vector(0,30e3,0)*earth.m

#Some physics
#here I set the momentum of sun so that the total momentum is zero
sun.p=-(earth.p)

#aesthetics
attach_trail(sun)
attach_trail(earth)

#initial time and time step
t=0
dt=50

#now the serious coding 
while t<15000000000:
    rate(10**5)

    #vector from sun to earth
    rse=earth.pos-sun.pos

    #Newton's law of gravitation
    #Fse is the force the Sun exerts on the Earth
    Fse=-G*sun.m*earth.m*norm(rse)/mag(rse)**2

    #Fes is the force the Earth exerts on the Sun. By Newton's third law,
    Fes=-Fse

    #update momentum (with total vector force)
    #Newton's second law
    earth.p=earth.p+(Fse)*dt
    sun.p=sun.p+(Fes)*dt

    #update position
    #relation between momentum and position vectors
    sun.pos=sun.pos+sun.p*dt/sun.m
    earth.pos=earth.pos+earth.p*dt/earth.m
    t=t+dt
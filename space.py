from vpython import *
bs = []

R = 0.05
Rstart = 3
m = 0.1
G = .001
k = 1000
w = vector(0,0.07,0)
pole = cylinder(pos=vector(0,-Rstart,0),axis=vector(0,2*Rstart,0),radius=R,color=color.yellow)

N = 100
n = 0
while n<N:
  rt = Rstart*vector(2*random()-1,2*random()-1,2*random()-1)
  if mag(rt)<Rstart:
   bs = bs + [sphere(pos=rt, radius=R)]
   n = n + 1

v0=0.2
for b in bs:
  b.m = m
  rxz = vector(b.pos.x,0,b.pos.z)
  vt = cross(w,rxz)
  b.p = b.m*vt
  #b.p = b.m*v0*vector(2*random()-1,2*random()-1,2*random()-1)
  b.F = vector(0,0,0)
  
t = 0
dt = 0.01

def collide(b1,b2):
  #return true if b1 is overlapping b2
  rtt = b1.pos-b2.pos
  if mag(rtt)<b1.radius+b2.radius:
    return(True)
  else:
    return(False)

def setcollide(b1,b2):
  ptot = b1.p+b2.p
  vtot = ptot/(b1.m+b2.m)
  b1.p = b1.m*vtot
  b2.p = b2.m*vtot
    
  #if two balls collide conserve momentum and set velocitie equal

while t<56:
  rate(1000)
  for i in range(len(bs)):
    bs[i].F = vector(0,0,0)
    for j in range(len(bs)):
      if i!=j:
        rt = bs[j].pos-bs[i].pos
        bs[i].F = bs[i].F + G*bs[i].m*bs[j].m*norm(rt)/mag(rt)
        if collide(bs[i],bs[j]):
          setcollide(bs[i],bs[j])
  
  for b in bs:
    b.p = b.p + b.F*dt
    b.pos = b.pos + b.p*dt/b.m
  t = t + dt

shell=sphere(pos=vector(0,0,0),radius=Rstart,opacity=0.4)
tball1 = sphere(pos=vector(Rstart,0,0),radius=2*R, color=color.red)
theta=80*pi/180
tball2= sphere(pos=(Rstart)*vector(cos(theta),sin(theta),0),radius=2*R,color=color.cyan)
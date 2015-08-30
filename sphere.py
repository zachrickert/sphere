#sphere.py

#Calculates the surface area and the volume of a sphere given a radius

import math

def main():
  r = input("How long is the radius? ")

  v = 4.0 * r**3 * math.pi / 3.0
  sa = 4.0 * r**2 * math.pi

  print("For a sphere with " + str(r) + " radius: ")
  print("\t * Volume = " + str(v))
  print("\t * Surface Area = " +str(sa))

main()

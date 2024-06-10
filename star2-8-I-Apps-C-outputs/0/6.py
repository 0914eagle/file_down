
from math import sqrt, hypot
def dot(a, b):
  return a[0]*b[0]+a[1]*b[1]
def time_to_point(headquarter, destination, max_velocity, wind):
  a = headquarter
  b = destination
  v = max_velocity
  w = wind
  velocity_headquarter = (v*dot(a, w)/dot(w, w), v*dot(a, w)/dot(w, w))
  velocity_destination = (v*dot(b, w)/dot(w, w), v*dot(b, w)/dot(w, w))
  distance = hypot(a[0]-b[0], a[1]-b[1])
  time = distance/v
  return time
def get_time(headquarter, destination, max_velocity, wind_1, wind_2, t):
  time_1 = time_to_point(headquarter, destination, max_velocity, wind_1)
  time_2 = time_to_point(headquarter, destination, max_velocity, wind_2)
  time_to_destination = time_1 + time_2
  return time_to_destination
x_1, y_1, x_2, y_2 = map(int, input().split())
max_velocity, t = map(int, input().split())
wind_1_x, wind_1_y = map(int, input().split())
wind_2_x, wind_2_y = map(int, input().split())
headquarter = (x_1, y_1)
destination = (x_2, y_2)
wind_1 = (wind_1_x, wind_1_y)
wind_2 = (wind_2_x, wind_2_y)
time_to_destination = get_time(headquarter, destination, max_velocity, wind_1, wind_2, t)
print(time_to_destination)


# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict
import numpy as np
import time
import random
import math

start = time.time()

init_temp = 0.1
end_temp = 100

temp_min = 1
temp_max = 100

temp = end_temp
#temp = temp_min
a = b = c = d = 0
sum = a + b + c + d
E = sum
dict = {}
dict_unstable = {}
dict_check_unstable = {}

alpha = 0.84
arr = []
r_arr = []
j = 0
i = -180
while(i <= 180):
  arr.append(i)
  j = j + 1
  i = i + 15

print("\n")
print("Qubit possible values: ", arr)
k = 0
x = 0
y = 0
finite_x = 0

print("\n")
print("Simulation Started...")
while(temp > 0.1):
  # while(E > 0):
  for p in arr:
    for q in arr:
      for r in arr:
        for s in arr:
          a = p
          b = q
          c = r
          d = s
          y = y + 1
          sum = a + b + c + d
          Enew = sum
          # print(Enew)
          delta_E = abs(Enew - E)
          if delta_E == 0:
            # print("True Equilibrium: 1st qubit = ", a, ", 2nd qubit = ", b, ", 3rd qubit = ", c, ", 4th qubit = ", d, ", Energy = ", sum, ", delta_E = ", delta_E)
            # print("k = ", k, " Enew = ", abs(sum))
            key = k
            dict.setdefault(key, [])
            dict[key].append(a)
            dict[key].append(b)
            dict[key].append(c)
            dict[key].append(d)
            x = x + 1
            finite_x = finite_x + 1
          else:
            r = random.random()
            if abs(sum) < 0.5:
              if(r < math.exp(-(delta_E/temp))):
                # print("r = ", r, ", k = ", k, " Enew = ", abs(sum))
                r_arr.append(r)
                # print("True Probabilistic Equilibrium: ", delta_E)
                key = k
                dict.setdefault(key, [])
                dict[key].append(a)
                dict[key].append(b)
                dict[key].append(c)
                dict[key].append(d)
                x = x + 1
            else:
              key = k
              dict_unstable.setdefault(key, [])
              dict_unstable[key].append(a)
              dict_unstable[key].append(b)
              dict_unstable[key].append(c)
              dict_unstable[key].append(d)
              check_unstable = a + b + c + d
              dict_check_unstable[key] = sum
          k = k + 1
  temp = temp*alpha

end = time.time()


#print(dict)
#print(dict_unstable)

keys = list(dict_check_unstable.keys())
values = list(dict_check_unstable.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
 
#print(sorted_dict)

print("\n")
print("Total Number of States: ", y)
print("Number of Stable States: ", x)
print("Number of Unstable States: ", y-x)
print("Percentage of Stability (Stability Ratio): ", format((x*100)/y, '.5f'))

print("\n")
print("Total Number of States without probabislitic r-value: : ", y)
print("Number of finite Stable States without probabislitic r-value: ", finite_x)
print("Number of finite Unstable States without probabislitic r-value: ", y-finite_x)
#print("Percentage of Stability without probabislitic r-value (Stability Ratio1): ", round((finite_x*100)/y, 5), "%")
print("Percentage of Stability without probabislitic r-value (Stability Ratio): ", format((finite_x*100)/y, '.5f'))

print("\n")

print("Percentage of finite_x vs. r-stable states (Difference of probabilistic stable states and finite stable states without probabilistic r-value): ", format(((x - finite_x)*100)/y, '.5f'))
print("\n")

print("Simulation Completed !")
# print("Simulation time: ", (end - start)*1000, " milliseconds")
print("Elapsed Simulation Time: ", format(end - start, '.5f'), " seconds")

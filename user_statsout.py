"""

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""

import statistics

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)

var=statistics.variance(scores)
stdev=statistics.stdev(scores)
lowest=min(scores)
highest=max(scores)
# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

slope, intercept = statistics.linear_regression(x_times, y_temps)

y_future=13
x_future = round(slope * y_future + intercept)

print()
print("=============================================================")
print()
print("Here's some XY data (2 variables, together):")
print()
print(f"x (years experience):{x_times}")
print()
print(f"y (modules mastered):{y_temps}")
print()
print("Calculate the slope and intercept of a best fit straight line:")
print()
print(f"   slope = {slope:.2f}")
print(f"   intercept = { intercept:.2f}")
print()
print("Let's use our best fit line to PREDICT a future value.")
print()
print(f"   At future x = {x_future:d},")
print(f"   we predict the value of y will be { y_future:d}.")
print()
print("How'd we do? Does this make sense given the data?")
print()

if len(x_times) != len(y_temps):
    print("ERROR: The related sets are not the same size.")
    print(f"      {len(x_times)}!={len(y_temps)}")
    quit()
    
    
    
    
    
    
    
    
    
    output
    
    Here's some XY data (2 variables, together):

x (years experience):[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

y (modules mastered):[2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]

Calculate the slope and intercept of a best fit straight line:

   slope = 2.78
   intercept = 3.12

Let's use our best fit line to PREDICT a future value.

   At future x = 39,
   we predict the value of y will be 13.

How'd we do? Does this make sense given the data?

from numpy import * #import everything from the numpy library into the current namespace
arr = (1,2,3,4,5)
print(arr)

arr = linspace(0,15,40) #0-15 (40 values given)
print(arr)

arr = arange(1,20,4) #arange(start, stop, step) → generates values [start, start+step, start+2*step, ...] up to but not including stop.
print(arr)

arr = logspace(1,40,5) #logspace(start, stop, num) Generates num numbers evenly spaced on a logarithmic scale.
print(arr)
print(arr[0])

arr = ones(5, int) #ones(n, dtype) creates a NumPy array of length n filled with 1s.
print(arr)

arr = zeros(5, int) #zeros(n, dtype) creates a NumPy array of length n filled with 0s.
print(arr)
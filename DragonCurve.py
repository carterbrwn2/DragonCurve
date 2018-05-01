# Author: Carter Brown

# Implements a regular paperfold sequence (dragon curve sequence) generator. Executes n (from input) cycles.

start = [1]
end = []
x = 1

n = int(input())

for i in range(1, n+1):
    x = 1
    start.reverse()
    for j in range(1, 2**(i+1)):
        if j % 2 != 0:
            if x:
                end.append(x)
                x = 0
            else:
                end.append(x)
                x = 1
        else:
            end.append(start.pop())
    start = end
    end = []

print(start)

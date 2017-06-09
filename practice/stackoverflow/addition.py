import sys
if len(sys.argv) < 3: #script name + 2 other arguments required
 print("Provide at least two numbers")
else:
 n=int(sys.argv[1])
 m=int(sys.argv[2])
 print(n+m)
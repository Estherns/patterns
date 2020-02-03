def patterns():
  n = int(input("Please enter ther number of rows: "))
  for i in range(0, n+1):
    for j in range(i):
        print("*", end = " ")
    print()

patterns()
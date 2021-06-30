
#exercise 1
my_range = range(22, 105)
for x in my_range:
 if x % 4 == 0:
  print(x)
#exercise 2
my_range1 = reversed(range(20, 200))
for z in my_range1:
 if z % 3 != 0 and z % 5 == 0:
  print(z)
#exercise 3
my_range2 = range(123, 567)
l=[]
for c in my_range2:
    if c % 5 == 0 or c % 6 == 0:
        l.append(c)
print(sum(l))








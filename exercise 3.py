my_range2= range (123, 567)
l=[]
for c in my_range2:
    if c % 5 == 0 or c % 6 == 0:
        l.append(c)
print(sum(l))







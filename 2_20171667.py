f = open("p2_data.txt", 'r')
for line in f:
    a, b = line.split()
    a = float(a)
    b = float(b)
    print('{:.2f} + {:.2f} = {:.2f}'.format(a, b, a+b))
f.close()

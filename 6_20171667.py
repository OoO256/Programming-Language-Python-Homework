file = open('./p6_data.txt')
for line in file:
    country, pop, area = line.split()
    density = int(pop)/int(area)

    if(density >= 1000):
        how_populate = 'very densely populated'
    elif(density >= 500):
        how_populate = 'densely populated'
    elif(density >= 300):
        how_populate = 'normally populated'
    elif(density >= 100):
        how_populate = 'sparsely populated'
    else:        
        how_populate = 'very sparsely populated'

    print('{} is {}'.format(country, how_populate))
    
file.close()

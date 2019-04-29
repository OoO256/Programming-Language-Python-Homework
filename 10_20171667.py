dict = {}
dict_city = {}
num_international = 0
num_domestic = 0


file = open('./p10_data.txt')
for line in file:
    code, city, status, num_filghts = line.split()
    dict[(code, city, status)] = int(num_filghts)
    
for d in dict.items():
    key, num_filghts = d
    code, city, status = key

    if (status == 'international'):
        num_international += num_filghts
    elif (status == 'domestic'):
        num_domestic += num_filghts

    if(city not in dict_city):
        dict_city[city] = 0

    dict_city[city] += num_filghts


print('*** Category : city ***')
print('')
for dc in dict_city.items():
    print('{} : {}'.format(dc[0], dc[1]))

print('')
print('')


print('*** Category : status ***')
print('')
print('domestic :', num_domestic)
print('international :', num_international)
file.close()

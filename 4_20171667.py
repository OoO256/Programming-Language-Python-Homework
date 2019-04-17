print('--------------------------')
print("< 학생 성적 >")
print('--------------------------')

scores = []
f = open("p4_data.txt", 'r')
for line in f:
    id, s1, s2, s3, s4 = line.split()
    scores.append([int(id), int(s1), int(s2), int(s3), int(s4)])
    print(int(id), scores[-1][1:])
    
print('--------------------------')
print("< 평균 >")
print('--------------------------')
for line in scores:
    print('{} - {:.2f}'.format(line[0], (sum(line[1:]) - min(line[1:]))/3))

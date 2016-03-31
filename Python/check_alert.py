lines = [line.rstrip('\n') for line in open('alert_read.txt')]
alerts = ['']*20
alerts[0]=lines[0]
final = []
j=1
days= 'Mon','Tue','Wed','Thu','Fri','Sat','Sun'
for i in range(1,30):
    words= lines[i].split(' ')
    if((int(words[0][:3] in days) & int(lines[i-1].split(' ')[0][:3]=='ORA'))|
	(int(words[0][:3] == 'ORA') & int(lines[i-1].split(' ')[0][:3] in days))):
       alerts[j]=lines[i]
       j=j+1
    elif (int(words[0][:3] in days) & int(lines[i-1].split(' ')[0][:3] in days)):
       alerts[j-1]=lines[i]
print(alerts)
import sys
# define main function to read, cleanse and write
def main(ifile, ofile):
    lines = [line.rstrip('\n') for line in open(ifile)]
    alerts = ['']*2000
    days = 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'
    alerts[0]=lines[0]
    j=1
# cleansing of data for errors
    for i in range(1,len(lines)):
        words= lines[i].split(' ')
        if((len(words)>3) & ("RABAX:" not in words) & ("ThIErrHandle:" not in words)):
            if(int(words[1][:3] in days) & int(alerts[j-1].split(' ')[1][:3] in days)):
                alerts[j-1] = lines[i]
            elif int(words[1][:3] not in days):
                for word in words:
                    if (("ERR" in word) | ("err" in word) | ("Err" in word)):
                        alerts[j]=lines[i]
                        j=j+1
            elif(int(words[1][:3] in days)):
                alerts[j]=lines[i]
                j=j+1
# Write the formatted and filtered content to output file
    foo = open(ofile,'w')
    foo.writelines(["%s\n" % x  for x in alerts if x])
    print("Output file written")
    foo.close()
if __name__=='__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
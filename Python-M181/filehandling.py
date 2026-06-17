import csv
file=open('employee.csv','w+',newline='')
read=csv.writer(file)
read.writerows([[8528,'king',8000],[274,'blake',2000]])
# write=csv.reader(file)
# for i in write:
#      print(i)
# file.close()

import csv
file=open('employee.csv','a+',newline='')
read=csv.writer(file)
read.writerows([[8528,'king',8000],[274,'blake',2000]])
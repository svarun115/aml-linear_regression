import csv
import numpy as np
import math

data=[]
with open('Mobile_Data.csv','rb') as f:
	data=f.readlines()

x_train=[]
y_train=[]

data=data[1:]
for row in data:
	r=row.split(",")
	vec=r[2:8]
	vec.insert(0,1)
	temp = list(map(float,vec))
	x_train.append(temp)
	y_train.append(float(r[8].strip()))

x_test=[]
y_test=[]

x_test=x_train[int(0.8*len(x_train)):]
y_test=y_train[int(0.8*len(y_train)):]

x_train=x_train[:int(0.8*len(x_train))]
y_train=y_train[:int(0.8*len(y_train))]

x_train=np.matrix(x_train)
y_train=np.matrix(y_train)
x_test=np.matrix(x_test)
y_test=np.matrix(y_test)

x_dag=np.linalg.pinv(x_train)

w=x_dag*np.transpose(y_train)
#print "The parameter matrix obtained is:",w

Y=(x_test*w).transpose()

Y=Y.tolist()
y_test=y_test.tolist()

print "Actual output:\n",y_test,"\n\n"
print "Expected output:\n",Y,"\n\n"
s=0
error=[]
#calculating root mean square error
for i in range(len(Y[0])):
	error.append(((Y[0][i]-y_test[0][i])/y_test[0][i])**2)


for term in error:
	s+=term
 
rms_error=(math.sqrt(s/len(error)))*100
print "The root mean square error obtained is :",rms_error,"%"



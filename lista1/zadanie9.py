import math
a=int(input())
b=int(input())
z=complex(a,b)
Mz=math.sqrt(a*a+b*b)
Az=math.sin((a/Mz)*math.pi/180)
print('z=',z,'\t','|z|=',Mz,'\t','arg(z)',(Az))
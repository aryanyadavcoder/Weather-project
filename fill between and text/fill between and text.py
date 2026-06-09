"""
Mean
Median 1,2,3,4,5,6 (3+4)/2=3.5 (a[2] + a[3])n=5 n//2=2, n//2+1
"""
import matplotlib.pyplot as plt
def findRange(data):
    max,min=data[0],data[0]
    for i in data:
        if i>max:
            max=i
        elif i<min:
            min=i
    return max-min            
                
def findVariance(data,mean,n):
    sumx2=0
    for i in data:
        sumx2+=(i-mean)*(i-mean)
    return sumx2/n,(sumx2/n)**.5     
def findStandardDeviation(data,mean,n):
    v,x=findVariance(data,mean,n)  
    return v**.5
         
def findMean(data,n):
    sum=0
    for x in data:
        sum+=x
    return sum,sum/n
def fillData(data,n):
    datalist=[data for i in range(n)]  
    return datalist 
a=[5,8,12,4,16,2,0,0,0,0,0,0]
# a.sort()
n=len(a)
x=[i+1 for i in range(n)]
# print(a,n,x)
s,mean=findMean(a,n)
print(s,mean)


variance,i=findVariance(a,mean,n)
standarddeviation=findStandardDeviation(a,mean,n)
datarange=findRange(a)
print(f"Range={datarange},Variance={variance}, Standard Deviation={standarddeviation}, Mean={mean}")
dmean=fillData(mean,n)
# print(dmean)
plt.plot(x,a,label="Data",color="green",marker="o")
for xi,ai in zip(x,a):
    plt.text(xi,ai,f"({xi},{ai})")
sdtop=[i + standarddeviation for i in a]
sdbottom=[i - standarddeviation for i in a]
plt.fill_between(x,sdbottom,sdtop,label="Range")    



plt.plot(x,dmean,label="Mean",color="blue",marker="o")
plt.title("Statistics")
plt.xlabel("Index")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.show ()

"""

plt.fill between
plt.text
range was redefined

"""
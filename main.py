import pandas as pd
import math
import openpyxl
import matplotlib.pyplot as plt



def findMean(df):
    row,col=df.shape


    return(df["price"].sum() / len(df["price"]))


def findMedian(df):
    temp=0
    df = df.sort_values(by=["price"])

    if  len(df["price"])%2==0 :

        temp=(df.iloc[int(len(df["price"])/2),1]+df.iloc[(int(len(df["price"])/2)+1),1])/2
        return(temp)
    else:
        temp=int((len(df["price"])+1)/2)
        return(df.iloc[temp,1])

#population variance
def findVariance(df):
    temp=0
    x=0
    Mean= (findMean(df))
    while(x<len(df["price"])) :
        temp=(math.pow((df.iloc[x,1]-Mean),2))/(len(df["price"]))
        x=x+1

    return  temp

def findStandardDeviation(df):
    Mean = int(findMean(df))
    var= findVariance(df)
    return  math.sqrt(var)

def findStandardError(df):
    temp=0
    std= findStandardDeviation(df)
    temp = std/ math.sqrt(len(df["price"]))
    return temp

def findDistrubation(df):
    Mean = findMean(df)
    Median = findMedian(df)
    if Mean==Median:
        return "Symmetric Distribution"
    elif Mean<Median:
        return "Right Skewed Distribution"
    elif Mean>Median:
        return "Left Skewed Distribution"


    # 0 1 2 3 4 5 6 7 8
def findOutliers(df):
    temp=0
    Q1=0
    Q3=0
    #Interquartile range
    IQR=0
    # l=low, High =High
    lOutlier=0
    hOutlier=0
    df = df.sort_values(by=["price"])
    if len(df["price"]) % 2 == 0:
        temp=(int(len(df["price"])-1)-int(len(df["price"]) / 2))/2+int(len(df["price"]) / 2)
        Q3=df.iloc[temp,1]
        temp = int(len(df["price"]) / 2)-(int(len(df["price"]) - 1) - int(len(df["price"]) / 2)) / 2
        Q1=df.iloc[temp,1]
    else:
        if (int((len(df["price"]) + 1) / 2)%2==0):
            temp = (int((len(df["price"]) + 1) / 2) ) / 2
            temp =int(temp)
            Q1 = int(df.iloc[temp, 1])
            temp += int((len(df["price"]) + 1) / 2)
            Q3 = df.iloc[temp, 1]

        else:
            temp = (int((len(df["price"]) + 1) / 2)-1)/2
            Q1= (df.iloc[temp,1]+df.iloc[temp+1,1])/2
            temp+=int((len(df["price"]) + 1) / 2)
            Q3=(df.iloc[temp,1]+df.iloc[temp+1,1])/2

    IQR=Q3-Q1
    lOutlier=Q1-(IQR*1.5)
    HOutlier = Q3 + (IQR * 1.5)
    x = 0
    while (x < len(df["price"])):

        if df.iloc[x,1] <lOutlier or df.iloc[x,1]>HOutlier:
            print(df.iloc[x,1],end=', ')
        x += 1


def find95ConfidenceIntervalforMean(df,sampleNumber):
    lowerBound = 0
    upperBound = 0
    Z = 1.96
    Std = findStandardDeviation(df)
    dfSample = df["price"].sample(n=sampleNumber)
    dfSampleMean = (dfSample.sum() / len(dfSample))
    lowerBound = dfSampleMean - (Z * Std / math.sqrt(sampleNumber))
    upperBound = dfSampleMean * (Z * Std / math.sqrt(sampleNumber))
    print("Lower Bound =", lowerBound)
    print("Upper Bound =", upperBound)
    print("[", lowerBound, ",", upperBound, "]")

def find95ConfidenceIntervalforVariance(df,sampleNumber):
    lowerBound = 0
    upperBound = 0
    Mean = findMean(df)
    var = findVariance(df)
    Z = 1.96
    dfSample = df["price"].sample(n=sampleNumber)
    dfSampleMean = (dfSample.sum() / len(dfSample))

    temp = 0
    x = 0
    while (x < len(dfSample)):
        temp = (math.pow((df.iloc[x, 1] - Mean), 2)) / (len(dfSample))
        x = x + 1


    sampleVar=temp
    lowerBound=(Mean-dfSampleMean)-Z*(math.sqrt((var/len(df))+(sampleVar/len(dfSample))))
    upperBound=(Mean-dfSampleMean)+Z*(math.sqrt((var/len(df))+(sampleVar/len(dfSample))))
    print("Lower Bound =", lowerBound)
    print("Upper Bound =", upperBound)
    print("[", lowerBound, ",", upperBound, "]")


def findSampleSize(df):
#Z*StandardDeviation/√sampleSize=MarginOfError
#sampleSize=(MarginofError/Z*s)^2
    Z=1.645
    Margin=0.1
    Mean=findStandardDeviation(df)
    sampleSize=math.pow(Margin/Z*Mean,2)
    return(sampleSize)









df = pd.read_excel(r'C:\Users\Ahmet\PycharmProjects\proje\merc.xlsx')

print(findMean(df))
print(findMedian(df))
print(findVariance(df))
print(findStandardDeviation(df))
findOutliers(df)
print(findDistrubation(df))
find95ConfidenceIntervalforMean(df,15)
find95ConfidenceIntervalforVariance(df,15)
print(findSampleSize(df))





df = df.sort_values(by=["price"])

#Histogram
df.plot(y='price', kind='hist')
plt.show()

#BOXPLOT
df.boxplot(column=["price"])
plt.show()
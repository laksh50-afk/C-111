import csv
import pandas as pd
import statistics 
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

#plotting the graph
fig = ff.create_distplot([data], ['reading_time'], show_hist= False)
fig.show()

# calculating the mean and standard deviation of the population data
mean_of_sample1 = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Mean of the sampling distribution :", mean_of_sample1)
print("Standard deviation of the sampling distribution : ", std_deviation)


# find the mean of 100 datapoints 1000 times
def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean

meanList=[]
for i in range(0,1000):
    setOfMeans=randomSetOfMean(100)
    meanList.append(setOfMeans)

std_deviation = statistics.stdev(meanList)
mean = statistics.mean(meanList)
print("Mean of the sample ", mean)
print("Standard deviation of the sample : ", std_deviation)

FirstStdevStart,FirstStdevEnd=mean-std_deviation,mean+std_deviation 
SecondStdevStart,SecondStdevEnd=mean-(2*std_deviation),mean+(2*std_deviation)
ThirdStdevStart,ThirdStdevEnd=mean-(3*std_deviation),mean+(3*std_deviation)

fig = ff.create_distplot([meanList], ['reading_time'], show_hist= False)
fig.add_trace(go.Scatter( x=[mean,mean],y=[0,0.20], mode ='lines', name = 'Mean'))
fig.add_trace(go.Scatter(x=[FirstStdevStart,FirstStdevStart],y= [0,0.17],mode ='lines', name = 'FirstStdevStart'))
fig.add_trace(go.Scatter(x=[FirstStdevEnd,FirstStdevEnd],y= [0,0.17],mode ='lines', name = 'FirstStdevEnd'))
fig.add_trace(go.Scatter(x=[SecondStdevStart,SecondStdevStart],y= [0,0.17],mode ='lines', name = 'SecondStdevStart'))
fig.add_trace(go.Scatter(x=[SecondStdevEnd,SecondStdevEnd],y= [0,0.17],mode ='lines', name = 'SecondStdevEnd'))
fig.add_trace(go.Scatter(x=[ThirdStdevStart,ThirdStdevStart],y= [0,0.17],mode ='lines', name = 'ThirdStdevStart'))
fig.add_trace(go.Scatter(x=[ThirdStdevEnd,ThirdStdevEnd],y= [0,0.17],mode ='lines', name = 'ThirdStdevEnd'))
fig.show()

z_score=(mean_of_sample1 - mean)/std_deviation
print("the z score is : ",z_score)


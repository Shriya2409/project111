import csv
import plotly_express as px
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("data.csv")

data=df["Math_score"].tolist()


#fig=ff.create_distplot([data], ["Math score"], show_hist=False)
#fig.show()

mean=statistics.mean(data)
std=statistics.stdev(data)
print(mean)
print(std)

def random_set(counter):
    data_set=[]
    for i in range(0, counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    mean=statistics.mean(data_set)    
    return mean

def setup():
    meanlist=[]
    for i in range (0, 1000):
        set_of_means=random_set(100)
        meanlist.append(set_of_means)
    
    sampling_mean=statistics.mean(meanlist)
    sampling_std=statistics.stdev(meanlist)
    print(sampling_mean)
    print(sampling_std)

    df1=pd.read_csv("sampling1.csv")
    df2=pd.read_csv("sampling2.csv")
    df3=pd.read_csv("sampling3.csv")

    data1=df1["Math_score"].tolist()
    data2=df2["Math_score"].tolist()
    data3=df3["Math_score"].tolist()

    mean1=statistics.mean(data1)
    mean2=statistics.mean(data2)
    mean3=statistics.mean(data3)

    std1=statistics.stdev(data1)
    std2=statistics.stdev(data2)
    std3=statistics.stdev(data3)

    print(mean1)
    print(mean2)
    print(mean3)
    print(std1)
    print(std2)
    print(std3)

    z_score1=(mean1-sampling_mean)/sampling_std
    z_score2=(mean2-sampling_mean)/sampling_std
    z_score3=(mean3-sampling_mean)/sampling_std

    print(z_score1)
    print(z_score2)
    print(z_score3)

    first_sd_start=mean-2*sampling_std
    first_sd_end=mean+2*sampling_std

    second_sd_start=mean-2*sampling_std
    second_sd_end=mean+2*sampling_std

    third_sd_start=mean-3*sampling_std
    third_sd_end=mean+3*sampling_std

    fig=ff.create_distplot([meanlist], ["Math score"], show_hist=False)    
    fig.add_trace(go.Scatter(x=[mean,mean], y=[0,0.17], mode="lines", name=mean))
    fig.add_trace(go.Scatter(x=[first_sd_end, first_sd_end], y=[0,0.17], mode="lines", name="first sd"))
    fig.add_trace(go.Scatter(x=[mean1, mean1], y=[0,0.17], mode="lines", name="mean1"))
    fig.add_trace(go.Scatter(x=[mean2, mean2], y=[0,0.17], mode="lines", name="mean2"))
    fig.add_trace(go.Scatter(x=[mean3, mean3], y=[0,0.17], mode="lines", name="mean3"))


    fig.show()
    





setup()


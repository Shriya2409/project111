import csv
import plotly_express as px
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()

population_mean=statistics.mean(data)
population_std=statistics.stdev(data)
print(population_mean)
print(population_std)

def random_set(counter):
    data_set=[]
    for i in range(0, counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        data_set.append(value)
    mean=statistics.mean(data_set)    
    return mean

def setup():
    mean_list=[]
    for i in range(0, 100):
        set_of_means=random_set(30)
        mean_list.append(set_of_means)
    df=mean_list
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()
    sampling_mean=statistics.mean(mean_list)
    print(sampling_mean)
    std=statistics.stdev(mean_list)
    print(std) 

setup()


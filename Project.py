import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
import numpy as np
import scipy.stats as sta


#read csv file into dataframe
df = pd.read_csv("6 months.csv")
print (df.info())


###1  coloumn-NT
#taking only NT column
sample1 = df["NT"]

#Measure of central Tendency of Data 


#descriptive statistics: mean,mode,median
mean_of_NT = stats.mean(sample1)
median_of_NT =stats.median(sample1)
mode_of_NT = stats.mode(sample1)

#print the mean, mode and median of the NT
print("\nThe median value of NT is: %.2f"%median_of_NT)
print("\nThe mean value of NT is: %.2f"%mean_of_NT)
print("\nThe mode value of NT is: %.2f"%mode_of_NT)

#Q1 Quartile 1 of NT,NSW,ACT,WA,Tas,SA,VIC and QLD
print(df.quantile(q=(0.25,0.50,0.75)))

#Measure of Dispersion

#Range,Variance and deviation
variance= stats.variance(sample1)
deviation= sample1.std(ddof=1)

df['NT'].head()
range1_NT= max(df['NT'].head()) -min(df['NT'].head())



#Print the varience and deviation for the sample
print("\nThe variance in NT is: %.2f"%variance)
print("\nThe deviation in NT is: %.2f"%deviation)
print("\nThe range in NT is: %.2f"%range1_NT)

#Data Visualization


#histogram of NSW, median as central tendency
df1= df["NT"]
bin_width= 0.25
bin_count = int(mean_of_NT/bin_width)

#plot the histogram: median as central tendency
plt.hist(sample1,color="green",edgecolor= "black", bins = bin_count)
plt.title("Histogram of Number of Cases in NT")
plt.xlabel("Number of cases")
plt.ylabel("NT")
plt.show()




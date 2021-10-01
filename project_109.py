import csv
import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")

mathList = df["mathscore"].tolist()

math_mean = statistics.mean(mathList)
math_mode = statistics.mode(mathList)
math_median = statistics.median(mathList)

print("Mean, Median, Mode of math is... {},{},{} respectiveley".format(math_mean,math_median,math_mode))

mathstdev = statistics.stdev(mathList)


mathFirststdevStart,mathFirststdevEnd = math_mean - mathstdev,math_mean + mathstdev
mathSecondstdevStart,mathSecondstdevEnd = math_mean - (mathstdev*2),math_mean + (mathstdev*2)
mathThirdstdevStart,mathThirdstdevEnd = math_mean - (mathstdev*3),math_mean + (mathstdev*3)


mathlistofdatawithin1stdev = [Result for Result in mathList if Result > mathFirststdevStart and Result < mathFirststdevEnd]
mathlistofdatawithin2stdev = [Result for Result in mathList if Result > mathSecondstdevStart and Result < mathSecondstdevEnd]
mathlistofdatawithin3stdev = [Result for Result in mathList if Result > mathThirdstdevStart and Result < mathThirdstdevEnd]


print("{}% of data lies within 1 standard deviation".format(len(mathlistofdatawithin1stdev)*100.0/len(mathList)))
print("{}% of data lies within 2 standard deviation".format(len(mathlistofdatawithin2stdev)*100.0/len(mathList)))
print("{}% of data lies within 3 standard deviation".format(len(mathlistofdatawithin3stdev)*100.0/len(mathList)))



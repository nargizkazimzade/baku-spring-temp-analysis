import pandas as pd
#dropped the useless metadata contained in first 9 rows
df = pd.read_csv('baku_2005_2026.csv', skiprows=9)

#renamed the columns with shorter ones
df.columns = ["date", "temp"]

#formatted my combined date data to a more readable format
df["date"] = pd.to_datetime(df["date"])

#extracting day from columns
df["day"] = df["date"].dt.date

#taking all rows with same day and treat them as a group
df.groupby("day")

#taking daily average temperature of each day
daily_avg = df.groupby("day")["temp"].mean()
#print(daily_avg) #yepp it works yaay

#we cannot do the exact same for monthly average because
#days are unique, months are not, so we should specify year+month
#extract year and month columns
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

#treating as a group again and taking average of each year+month
monthly_average = df.groupby(["year", "month"])["temp"].mean().reset_index()
#print(monthly_average) #it wooorks

#lets define what spring means aka extract only march april may
spring = monthly_average[monthly_average["month"].isin([3,4,5])]
#print(spring) #now we have 65 rows, only springs of each year

#ill also make a late spring including only april and may bc march is cold in Baku
late_spring = monthly_average[monthly_average["month"].isin([4,5])]

#lets calculate spring average
spring_average = spring.groupby("year")["temp"].mean().reset_index()
#print(spring_average) #now we have average spring temperature of each year, 22 rows

#lets make an avg of late spring too
late_spring_average = late_spring.groupby("year")["temp"].mean().reset_index()

#i just remembered i had some nan values so i did a quick check if its
#worth attention or nah, skip it. my data was good enough
#print(df.groupby(["year", "month"])["temp"].count())

#lets plot the spring avg of each year
import matplotlib.pyplot as plt
import numpy as np

#my og plotting code
plt.plot(spring_average["year"], spring_average["temp"], marker = "o", color = "lightpink", label = "Spring Temperature")

#lets plot late spring as well
plt.plot(late_spring_average["year"], late_spring_average["temp"], marker = "o", color = "lightgreen", label = "Late Spring Temperature")

#its a wiggly jiggly graph so lets add a trend line
#lets define x and y properly
x = spring_average["year"]
y = spring_average["temp"]

#lets make the same procedures for late spring
x_late = late_spring_average["year"]
y_late = late_spring_average["temp"]

#calculate the polynomial coefs
coefficients = np.polyfit(x, y, 1)

#coef for late
coefficients_late = np.polyfit(x_late, y_late, 1)

#create a math func from coefs
trend_function = np.poly1d(coefficients)

#func for late
trend_function_late = np.poly1d(coefficients_late)

#plot the trendline
plt.plot(x, trend_function(x), color = "pink", linestyle = "--", label = "SpringTrendline")

#plot for late
plt.plot(x_late, trend_function_late(x_late), color = "green", linestyle = "--", label = "LateSpringTrendline")

#my formatting teehee
plt.xticks(spring_average["year"], rotation = 45)
plt.title("Spring Temperature Trend in Baku")
plt.xlabel("Year")
plt.ylabel("Temperature *C")
plt.legend()

plt.tight_layout()
plt.show()

#its doooone! it nicely shows both full spring in pink and late spring in green
#theres an interesting trend showing average spring temperature stays constant around 11 degrees
#but april and may shows slightly downward slope
#we can say that march is slightly getting warmer





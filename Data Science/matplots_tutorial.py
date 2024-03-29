import matplotlib.pyplot as plt 

x_days = [1,2,3,4,5]

y_price1 = [9,9.5,10.5,10,12]
y_price2 = [11,12,10.5,11.5,12.5]


plt.title("Stock Movement")
plt.xlabel("week days")
plt.ylabel("Price in USD")



plt.plot(x_days,y_price1,label = "Stock 1")

plt.legend(loc=2, fontsize=12)

plt.show()

#plot all the plots alongside
plt.figure() #before creating any chart

#saving the figure
plt.savefig("images/abcd.png")

#subplot in a grid way
plt.subplot(2,2,1) #means 2*2 grid and 1st position

#tight layout so that no overfigures
plt.tight_layout()

# histogram
plt.hist(age_list,bins,histtype="bar",rwidth=0.9)


#boxplot
plt.boxplot(sales_list)

#pie chart
plt.pie(city_values,labels=city_names,autopct="%.2f%%")

#Scatter chart
plt.scatter(s_list, c_list)

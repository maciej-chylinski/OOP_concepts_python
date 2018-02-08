#https://campus.datacamp.com/courses/intermediate-python-for-data-science/matplotlib?ex=13

gdp_cap = [974.58033839999996,
 5937.0295259999984,
 6223.3674650000003,
 4797.2312670000001,
 12779.379639999999,
 34435.367439999995,
 36126.492700000003,
 29796.048340000001,
 1391.253792,
 33692.605080000001,
 1441.2848730000001,
 3822.137084,
 7446.2988029999997,
 12569.851769999999,
 9065.8008250000003,
 10680.792820000001,
 1217.0329939999999,
 430.07069159999998,
 1713.7786860000001,
 2042.0952400000001,
 36319.235009999997,
 706.01653699999997,
 1704.0637240000001,
 13171.638849999999,
 4959.1148540000004,
 7006.5804189999999,
 986.14787920000003,
 277.55185870000003,
 3632.5577979999998,
 9645.06142,
 1544.7501119999999,
 14619.222719999998,
 8948.1029230000004,
 22833.308509999999,
 35278.418740000001,
 2082.4815670000007,
 6025.3747520000015,
 6873.2623260000009,
 5581.1809979999998,
 5728.3535140000004,
 12154.089749999999,
 641.36952360000021,
 690.80557590000001,
 33207.0844,
 30470.0167,
 13206.48452,
 752.74972649999995,
 32170.37442,
 1327.6089099999999,
 27538.41188,
 5186.0500030000003,
 942.6542111,
 579.23174299999982,
 1201.637154,
 3548.3308460000007,
 39724.978669999997,
 18008.944439999999,
 36180.789190000003,
 2452.210407,
 3540.6515639999998,
 11605.71449,
 4471.0619059999999,
 40675.996350000001,
 25523.277099999999,
 28569.719700000001,
 7320.8802620000015,
 31656.068060000001,
 4519.4611709999999,
 1463.249282,
 1593.06548,
 23348.139730000006,
 47306.989780000004,
 10461.05868,
 1569.3314419999999,
 414.5073415,
 12057.49928,
 1044.7701259999999,
 759.34991009999999,
 12451.6558,
 1042.581557,
 1803.151496,
 10956.991120000001,
 11977.57496,
 3095.7722710000007,
 9253.896111,
 3820.1752299999998,
 823.68562050000003,
 944.0,
 4811.0604290000001,
 1091.359778,
 36797.933319999996,
 25185.009109999999,
 2749.3209649999999,
 619.67689239999982,
 2013.9773049999999,
 49357.190170000002,
 22316.192869999999,
 2605.94758,
 9809.1856360000002,
 4172.8384640000004,
 7408.9055609999996,
 3190.4810160000002,
 15389.924680000002,
 20509.64777,
 19328.709009999999,
 7670.122558,
 10808.47561,
 863.08846390000019,
 1598.4350890000001,
 21654.83194,
 1712.4721360000001,
 9786.5347139999994,
 862.54075610000018,
 47143.179640000002,
 18678.314350000001,
 25768.257590000001,
 926.14106830000003,
 9269.6578079999999,
 28821.063699999999,
 3970.0954069999998,
 2602.3949950000001,
 4513.4806429999999,
 33859.748350000002,
 37506.419070000004,
 4184.5480889999999,
 28718.276839999999,
 1107.482182,
 7458.3963269999977,
 882.9699437999999,
 18008.509239999999,
 7092.9230250000001,
 8458.2763840000007,
 1056.3801209999999,
 33203.261279999999,
 42951.65309,
 10611.46299,
 11415.805689999999,
 2441.5764039999999,
 3025.3497980000002,
 2280.769906,
 1271.211593,
 469.70929810000007]


life_exp =[43.828000000000003,
 76.423000000000002,
 72.301000000000002,
 42.731000000000002,
 75.319999999999993,
 81.234999999999999,
 79.828999999999994,
 75.635000000000005,
 64.061999999999998,
 79.441000000000003,
 56.728000000000002,
 65.554000000000002,
 74.852000000000004,
 50.728000000000002,
 72.390000000000001,
 73.004999999999995,
 52.295000000000002,
 49.579999999999998,
 59.722999999999999,
 50.43,
 80.653000000000006,
 44.741000000000007,
 50.651000000000003,
 78.552999999999997,
 72.960999999999999,
 72.888999999999996,
 65.152000000000001,
 46.462000000000003,
 55.322000000000003,
 78.781999999999996,
 48.328000000000003,
 75.748000000000005,
 78.272999999999996,
 76.486000000000004,
 78.331999999999994,
 54.790999999999997,
 72.234999999999999,
 74.994,
 71.338000000000022,
 71.878,
 51.578999999999994,
 58.039999999999999,
 52.947000000000003,
 79.313000000000002,
 80.656999999999996,
 56.734999999999999,
 59.448,
 79.406000000000006,
 60.021999999999998,
 79.483000000000004,
 70.259,
 56.006999999999998,
 46.388000000000012,
 60.915999999999997,
 70.198000000000008,
 82.207999999999998,
 73.338000000000022,
 81.757000000000005,
 64.698000000000008,
 70.650000000000006,
 70.963999999999999,
 59.545000000000002,
 78.885000000000005,
 80.745000000000005,
 80.546000000000006,
 72.566999999999993,
 82.602999999999994,
 72.534999999999997,
 54.109999999999999,
 67.296999999999997,
 78.623000000000005,
 77.588000000000022,
 71.992999999999995,
 42.591999999999999,
 45.677999999999997,
 73.951999999999998,
 59.443000000000012,
 48.302999999999997,
 74.241,
 54.466999999999999,
 64.164000000000001,
 72.801000000000002,
 76.194999999999993,
 66.802999999999997,
 74.543000000000006,
 71.164000000000001,
 42.082000000000001,
 62.069000000000003,
 52.906000000000013,
 63.784999999999997,
 79.762,
 80.203999999999994,
 72.899000000000001,
 56.866999999999997,
 46.859000000000002,
 80.195999999999998,
 75.640000000000001,
 65.483000000000004,
 75.536999999999978,
 71.751999999999995,
 71.421000000000006,
 71.688000000000002,
 75.563000000000002,
 78.097999999999999,
 78.746000000000024,
 76.441999999999993,
 72.475999999999999,
 46.241999999999997,
 65.528000000000006,
 72.777000000000001,
 63.061999999999998,
 74.001999999999995,
 42.568000000000012,
 79.971999999999994,
 74.662999999999997,
 77.926000000000002,
 48.158999999999999,
 49.338999999999999,
 80.941000000000003,
 72.396000000000001,
 58.555999999999997,
 39.613,
 80.884,
 81.701000000000022,
 74.143000000000001,
 78.400000000000006,
 52.517000000000003,
 70.616,
 58.420000000000002,
 69.819000000000003,
 73.923000000000002,
 71.777000000000001,
 51.542000000000002,
 79.424999999999997,
 78.242000000000004,
 76.384,
 73.747,
 74.248999999999995,
 73.421999999999997,
 62.698,
 42.383999999999993,
 43.487000000000002]


pop =  [31.889923,
 3.6005229999999999,
 33.333216,
 12.420476000000001,
 40.301926999999999,
 20.434176000000001,
 8.199783,
 0.70857300000000001,
 150.448339,
 10.392226000000001,
 8.0783140000000007,
 9.1191519999999997,
 4.5521979999999997,
 1.6391309999999999,
 190.01064700000001,
 7.3228580000000001,
 14.326203,
 8.3905049999999992,
 14.131857999999999,
 17.696293000000001,
 33.390141,
 4.3690379999999998,
 10.238807,
 16.284741,
 1318.683096,
 44.227550000000001,
 0.71096000000000004,
 64.606758999999997,
 3.8006099999999998,
 4.1338840000000001,
 18.013408999999999,
 4.4933120000000004,
 11.416987000000001,
 10.228744000000001,
 5.4681199999999999,
 0.49637399999999998,
 9.3196220000000007,
 13.75568,
 80.264543000000003,
 6.9396880000000003,
 0.55120100000000005,
 4.9065849999999998,
 76.511887000000002,
 5.2384599999999999,
 61.083916000000002,
 1.4548669999999999,
 1.6883589999999999,
 82.400996000000006,
 22.873338,
 10.706289999999999,
 12.572927999999999,
 9.9478139999999993,
 1.4720409999999999,
 8.5028140000000008,
 7.4837629999999997,
 6.9804120000000003,
 9.9561080000000004,
 0.301931,
 1110.3963309999999,
 223.547,
 69.453569999999999,
 27.499638000000001,
 4.1090859999999996,
 6.426679,
 58.147733000000002,
 2.780132,
 127.467972,
 6.0531930000000003,
 35.610177,
 23.301725000000001,
 49.044789999999999,
 2.5055589999999999,
 3.921278,
 2.0126490000000001,
 3.1939419999999998,
 6.0369140000000003,
 19.167653999999999,
 13.327078999999999,
 24.821286000000001,
 12.031795000000001,
 3.2700650000000002,
 1.250882,
 108.700891,
 2.8741270000000001,
 0.68473600000000001,
 33.757174999999997,
 19.951656,
 47.761980000000001,
 2.0550799999999998,
 28.901789999999998,
 16.570613000000002,
 4.1157709999999996,
 5.6753559999999998,
 12.894864999999999,
 135.03116399999999,
 4.6279260000000004,
 3.2048969999999999,
 169.27061699999999,
 3.2421730000000002,
 6.6671469999999999,
 28.674757,
 91.077286999999998,
 38.518241000000003,
 10.642836000000001,
 3.942491,
 0.79809399999999997,
 22.276056000000001,
 8.8605879999999999,
 0.19957900000000001,
 27.601037999999999,
 12.267493,
 10.150264999999999,
 6.1445619999999996,
 4.5530090000000003,
 5.4475020000000001,
 2.0092449999999999,
 9.1187729999999991,
 43.997827999999998,
 40.448191000000001,
 20.378239000000001,
 42.292929000000001,
 1.1330659999999999,
 9.0310880000000004,
 7.5546610000000003,
 19.314747000000001,
 23.174294,
 38.13964,
 65.068149000000005,
 5.7015789999999997,
 1.056608,
 10.276158000000001,
 71.158647000000002,
 29.170397999999999,
 60.776237999999999,
 301.13994700000001,
 3.4474960000000001,
 26.084662000000002,
 85.262355999999997,
 4.018332,
 22.211742999999998,
 11.746034999999999,
 12.311143]


col=['red',
 'green',
 'blue',
 'blue',
 'yellow',
 'black',
 'green',
 'red',
 'red',
 'green',
 'blue',
 'yellow',
 'green',
 'blue',
 'yellow',
 'green',
 'blue',
 'blue',
 'red',
 'blue',
 'yellow',
 'blue',
 'blue',
 'yellow',
 'red',
 'yellow',
 'blue',
 'blue',
 'blue',
 'yellow',
 'blue',
 'green',
 'yellow',
 'green',
 'green',
 'blue',
 'yellow',
 'yellow',
 'blue',
 'yellow',
 'blue',
 'blue',
 'blue',
 'green',
 'green',
 'blue',
 'blue',
 'green',
 'blue',
 'green',
 'yellow',
 'blue',
 'blue',
 'yellow',
 'yellow',
 'red',
 'green',
 'green',
 'red',
 'red',
 'red',
 'red',
 'green',
 'red',
 'green',
 'yellow',
 'red',
 'red',
 'blue',
 'red',
 'red',
 'red',
 'red',
 'blue',
 'blue',
 'blue',
 'blue',
 'blue',
 'red',
 'blue',
 'blue',
 'blue',
 'yellow',
 'red',
 'green',
 'blue',
 'blue',
 'red',
 'blue',
 'red',
 'green',
 'black',
 'yellow',
 'blue',
 'blue',
 'green',
 'red',
 'red',
 'yellow',
 'yellow',
 'yellow',
 'red',
 'green',
 'green',
 'yellow',
 'blue',
 'green',
 'blue',
 'blue',
 'red',
 'blue',
 'green',
 'blue',
 'red',
 'green',
 'green',
 'blue',
 'blue',
 'green',
 'red',
 'blue',
 'blue',
 'green',
 'green',
 'red',
 'red',
 'blue',
 'red',
 'blue',
 'yellow',
 'blue',
 'green',
 'blue',
 'green',
 'yellow',
 'yellow',
 'yellow',
 'red',
 'red',
 'red',
 'blue',
 'blue']

"""
import numpy as np
#operacje na listach
x = ["a","b", "c"]
y = x
y[1] = "z" # zmieniamy element [1] w obu tablicach x oraz z

#aby nie zmianiać, trzeba by zrobić przypisanie y = x[:] tzw. slicing lub
#y = list(x)

#max
maximal = max(x) #wybiera maxymalną wartość z listy
#zaokroąglanie
round(1.68, 1)
round(1.68)

print(np.array([1,2,3]))
"""

"""
[0]
#matplotlob
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
#plt.plot(year, pop)
plt.scatter(year, pop)
plt.show()


[1]
# Print the last item from year and pop
print(year[-1])
print(pop[-1])


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

# Display the plot with plt.show()
plt.show()
#https://campus.datacamp.com/courses/intermediate-python-for-data-science/matplotlib?ex=3
"""

[2]
"""
Line Plot (2): Interpretation
Have another look at the plot you created in the previous exercise; it's shown on the right. Based on the plot, in approximately what year will there be more than ten billion human beings on this planet?

INSTRUCTIONS
35XP
Possible Answers
2040
press 1
2060
press 2
2085
press 3
2095
press 4

Submit Answer
HINT
You can check the population for a particular year by checking out the plot. If you want the exact result, use pop[year.index(2030)], to get the population for 2030, for example.
"""


"""
[3]
# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()


[4]

import matplotlib.pyplot as plt
# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()


[5]
# Import package
import matplotlib.pyplot as plt

# Build Scatter plot
plt.scatter(pop, life_exp)

# Show plot
plt.show()
"""
"""
[6]
"""

"""
#Histograms
[a]
# Build histogram with 5 bins
plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins = 20)

# Show and clean up again
plt.show()
plt.clf()


[b]
# Histogram of life_exp, 15 bins
plt.hist(life_exp, bins = 15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950, bins = 15)

# Show and clear plot again
plt.show()
plt.clf()
"""
"""
#[7]
import matplotlib.pyplot as plt
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)


# Add title
plt.title(title)

# After customizing, display the plot
plt.show()
"""


"""
Ticks
The customizations you've coded up to now are available in the script, in a more concise form.

In the video, Filip has demonstrated how you could control the y-ticks by specifying two arguments:

plt.yticks([0,1,2], ["one","two","three"])
In this example, the ticks corresponding to the numbers 0, 1 and 2 will be replaced by one, two and three, respectively.

Let's do a similar thing for the x-axis of your world development chart, with the xticks() function. The tick values 1000, 10000 and 100000 should be replaced by 1k, 10k and 100k. To this end, two lists have already been created for you: tick_val and tick_lab.

INSTRUCTIONS
Use tick_val and tick_lab as inputs to the xticks() function to make the the plot more readable.
As usual, display the plot with plt.show() after you've added the customizations.
"""
"""
#ticks
# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000,10000,100000]
tick_lab = ['1k','10k','100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val, tick_lab)

# After customizing, display the plot
plt.show()
"""

#[8] bubble chart
"""
Run the script to see how the plot changes.
Looks good, but increasing the size of the bubbles will make things stand out more.
Import the numpy package as np.
Use np.array() to create a numpy array from the list pop. Call this Numpy array np_pop.
Double the values in np_pop by assigning np_pop * 2 to np_pop again. Because np_pop is a Numpy array, each array element will be doubled.
Change the s argument inside plt.scatter() to be np_pop instead of pop.
"""
"""
# Import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop * 2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()
"""


"""
#[9] coloring plots
Colors
The code you've written up to now is available in the script on the right.

The next step is making the plot more colorful! To do this, a list col has been created for you. It's a list with a color for each corresponding country, depending on the continent the country is part of.

How did we make the list col you ask? The Gapminder data contains a list continent with the continent each country belongs to. A dictionary is constructed that maps continents onto colors:

dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
Nothing to worry about now; you will learn about dictionaries in the next chapter.

INSTRUCTIONS
100XP
Add c = col to the arguments of the plt.scatter() function.
Change the opacity of the bubbles by setting the alpha argument to 0.8 inside plt.scatter(). Alpha can be set from zero to one, where zero is totally transparent, and one is not at all transparent.
"""
"""
# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()
"""

#[10]
"""
Additional Customizations
If you have another look at the script, under # Additional Customizations, you'll see that there are two plt.text() functions now. They add the words "India" and "China" in the plot.

INSTRUCTIONS
Add plt.grid(True) after the plt.text() calls so that gridlines are drawn on the plot.
"""
"""
import matplotlib.pyplot as plt
import numpy as np

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
"""

#badanie korelacji
#np.corrcoef(gdp_cap, life_exp)


"""
import wx
# Some classes to use for the notebook pages.  Obviously you would
# want to use something more meaningful for your application, these
# are just for illustration.

class PageOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageOne object", (20,20))

class PageTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageTwo object", (40,40))

class PageThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageThree object", (60,60))


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Simple Notebook Example")

        # Here we create a panel and a notebook on the panel
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        # create the page windows as children of the notebook
        page1 = PageOne(nb)
        page2 = PageTwo(nb)
        page3 = PageThree(nb)

        # add the pages to the notebook with the label to show on the tab
        nb.AddPage(page1, "Page 1")
        nb.AddPage(page2, "Page 2")
        nb.AddPage(page3, "Page 3")

        # finally, put the notebook in a sizer for the panel to manage
        # the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
"""

import pandas as pd
df = pd.read_csv('C:\Users\mchylinx\Desktop\sample_csv', index_col='month')
df

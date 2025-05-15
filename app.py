import numpy as np
#Seasons
Seasons = ["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
Sdict = {"2010":0,"2011":1,"2012":2,"2013":3,"2014":4,"2015":5,"2016":6,"2017":7,"2018":8,"2019":9}
#Players
Players = ["Sachin","Rahul","Smith","Sami","Pollard","Morris","Samson","Dhoni","Kohli","Sky"]
Pdict = {"Sachin":0,"Rahul":1,"Smith":2,"Sami":3,"Pollard":4,"Morris":5,"Samson":6,"Dhoni":7,"Kohli":8,"Sky":9}
#Salaries
Sachin_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
Rahul_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
Smith_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Sami_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
Pollard_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
Morris_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Samson_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
Dhoni_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
Kohli_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
Sky_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]
#Matrix
Salary = np.array([Sachin_Salary, Rahul_Salary, Smith_Salary, Sami_Salary, Pollard_Salary, Morris_Salary, Samson_Salary, Dhoni_Salary, Kohli_Salary, Sky_Salary])
#Games 
Sachin_G = [80,77,82,82,73,82,58,78,6,35]
Rahul_G = [82,57,82,79,76,72,60,72,79,80]
Smith_G = [79,78,75,81,76,79,62,76,77,69]
Sami_G = [80,65,77,66,69,77,55,67,77,40]
Pollard_G = [82,82,82,79,82,78,54,76,71,41]
Morris_G = [70,69,67,77,70,77,57,74,79,44]
Samson_G = [78,64,80,78,45,80,60,70,62,82]
Dhoni_G = [35,35,80,74,82,78,66,81,81,27]
Kohli_G = [40,40,40,81,78,81,39,0,10,51]
Sky_G = [75,51,51,79,77,76,49,69,54,62]

Points = np.array([Sachin_PTS, Rahul_PTS, Smith_PTS, Sami_PTS, Pollard_PTS, Morris_PTS, Samson_PTS, Dhoni_PTS, Kohli_PTS, Sky_PTS]) 

Pdict
Pdict['Sachin']
#Sachin is the key and 0 is the value
#if we call the key then it will return its value

Pdict['Dhoni']
Games[0]
Games[Pdict['Sachin']]
Salary/Games
 np.round(Salary/Games)
#The round function gives the round off values
# it will remove the decimal values
# and it will giver the approximate values
# example 199335.937 was written as 199336.


import warnings
warnings.filterwarnings('ignore')
# This is used for removing the warnings in the code
# Usually the warnings are given in the red color
# but we ignore the warnings by using the above the code

import numpy as np
import matplotlib.pyplot as plt
# matplotlib is the package in the python
# it is used for visualisation of the data

%matplotlib inline
# it is used for plotting all the visualisations within the boundary

Salary
# it will give the salary of each and every player
# from the past 10 years
Salary[0]
Pdict
plt.plot(Salary[0])
# at 0 we are having the player sachin
# it will plot the salary of the player sachin
plt.plot(Salary[0],color='green', marker='o', linestyle='dashed')
# color option gives the change of color to the given graph 
%matplotlib inline
plt.rcParams['figure.figsize']=10,5
#Params means the parameters
#10----> is the width of the graph
#5-----> is the height of the graph
plt.plot(Salary[0],c='Blue',ls='--')
# c is the color
# ls is the line style
%matplotlib inline
plt.rcParams['figure.figsize']=1,5
plt.plot(Salary[0])
# the height and the width of the graph are 
%matplotlib inline
plt.rcParams['figure.figsize']=7,4
plt.plot(Salary[0],c='Green',ls='--',marker='s',ms=8)

list(range(0,10))

Sdict
Pdict
plt.plot(Salary[0],c='blue',ls='--',marker='s',ms=7)
plt.xticks(list(range(0,10)),Seasons)
plt.show()
# xticks means x-axis
# yticks means y-axis
# on x-axis we have plotted the seasons
# on y-axis we will be having the salaries
# so that we can see the salary graph of sachin
plt.plot(Salary[8],c='red',ls='--',marker='s',ms=3)
plt.xticks(list(range(0,10)),Seasons)
plt.show()
plt.plot(Salary[0],c='blue',ls='--',marker='s',ms=7)
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
plt.show()
# by using the keyword 'rotation' we can change the seasons
# from horizontal to vertical
plt.plot(Salary[0],c='blue',ls='--',marker='s',ms=7)
plt.xticks(list(range(0,10)),Seasons,rotation='horizontal')
plt.show()
# the rotation function gives the direction of rotation 
# in which the given seasons or any other variables can changed
plt.plot(Salary[0],c='Green',ls='--',marker='s',ms=7,label=Players[0])
plt.plot(Salary[1],c='Blue',ls=":",marker='o',ms=7,label=Players[1])

plt.xticks(list(range(0,10)),Seasons,rotation='horizontal')
plt.show()
plt.plot(Salary[0],c='Green',ls='--',marker='s',ms=7,label=Players[0])
plt.plot(Salary[1],c='Blue',ls=":",marker='o',ms=5,label=Players[1])
plt.plot(Salary[2],c='purple',ls='-',marker='^',ms=8,label=Players[2])
plt.plot(Salary[3],c='Red',ls="--",marker='d',ms=8,label=Players[3])

plt.legend()

plt.xticks(list(range(0,10)),Seasons,rotation='horizontal')

plt.show()
# the legend() function gives the color wise 
# representation of the players
# sachin---->green
# rahul----->blue
# smith----->purple
# sami------>red
# This gives the positioning of the legend in the graph
Location String      Location Code
        ==================   =============
        'best' (Axes only)   0
        'upper right'        1
        'upper left'         2
        'lower left'         3
        'lower right'        4
        'right'              5
        'center left'        6
        'center right'       7
        'lower center'       8
        'upper center'       9
        'center'             10

plt.plot(Salary[0],c='Green',ls='--',marker='s',ms=7,label=Players[0])
plt.plot(Salary[1],c='Blue',ls=":",marker='o',ms=5,label=Players[1])
plt.plot(Salary[2],c='purple',ls='-',marker='^',ms=8,label=Players[2])
plt.plot(Salary[3],c='Red',ls="--",marker='d',ms=8,label=Players[3])

plt.xticks(list(range(0,10)),Seasons,rotation='horizontal')

plt.legend(loc='lower right',bbox_to_anchor=(0.5,1))
plt.show()
# loc is used to specify the location of the legend

















import matplotlib.pyplot as plt
import json
import os

filenames = [
    'graph_data/pokedex.json',
    'graph_data/population_data.json',
    'graph_data/china_data'
]

pop = []
china_pop = []
with open('graph_data/population_data.json','r') as f1, open('graph_data/china_data.json', 'r') as f2, open('graph_data/pokedex.json') as f3:
    text = f1.read()
    text2 = f2.read()
    text3 = f3.read()
pop = json.loads(text)
china_pop = json.loads(text2)


value = []
year1 = 2010
year1_value = 309321666
value.append(year1_value)
year2 = 2011
year2_value = 311556874
value.append(year2_value)
year3 = 2012
year3_value = 313830990
value.append(year3_value)
year4 = 2013
year4_value = 315993715
value.append(year4_value)
year5 = 2014
year5_value = 318301008
value.append(year5_value)
year6 = 2015
year6_value = 320635163
value.append(year6_value)
year7 = 2016
year7_value = 322941311
value.append(year7_value)
year8 = 2017
year8_value = 324985539
value.append(year8_value)
year9 = 2018
year9_value = 326687501
value.append(year9_value)
year10 = 2019
year10_value = 328239523
value.append(year10_value)


china_value = []
c_year1 = 2010
c_year1_value = 1337705000
china_value.append(c_year1_value)
c_year2 = 2011
c_year2_value = 1344130000
china_value.append(c_year2_value)
c_year3 = 2012
c_year3_value = 1350695000
china_value.append(c_year3_value)
c_year4 = 2013
c_year4_value = 1357380000
china_value.append(c_year4_value)
c_year5 = 2014
c_year5_value = 1364270000
china_value.append(c_year5_value)
c_year6 = 2015
c_year6_value = 1371220000
china_value.append(c_year6_value)
c_year7 = 2016
c_year7_value = 1378665000
china_value.append(c_year7_value)
c_year8 = 2017
c_year8_value = 1386395000
china_value.append(c_year8_value)
c_year9 = 2018
c_year9_value = 1392730000
china_value.append(c_year9_value)
c_year10 = 2019
c_year10_value = 1397715000
china_value.append(c_year10_value)

fig, ax = plt.subplots()
ax.set(xlabel='year')
ax.set(ylabel='total population in billions')
ax.plot(value, label = 'US Population')
ax.plot(china_value, label = 'China Population')
ax.legend()
plt.show()


fig, ax = plt.subplots()
ax.set(
    xlabel='Number of Pokemon',
    ylabel='Pokemon Types',
    )

heights = []
title = []
type1 = 'fire'
type1_value = 12
heights.append(type1_value)
title.append(type1)
type2 = 'grass'
type2_value = 14
heights.append(type2_value)
title.append(type2)
type3 = 'water'
type3_value = 32
heights.append(type3_value)
title.append(type3)
type4 = 'bug'
type4_value = 12
heights.append(type4_value)
title.append(type4)
type5 = 'poison'
type5_value = 33
heights.append(type5_value)
title.append(type5)
type6 = 'flying'
type6_value = 19
heights.append(type6_value)
title.append(type6)
type7 = 'normal'
type7_value = 22
heights.append(type7_value)
title.append(type7)
type8 = 'electric'
type8_value = 9
heights.append(type8_value)
title.append(type8)
type9 = 'ground'
type9_value = 14
heights.append(type9_value)
title.append(type9)
type10 = 'fighting'
type10_value = 8
heights.append(type10_value)
title.append(type10)
type11 = 'psychic'
type11_value = 14
heights.append(type11_value)
title.append(type11)
type12 = 'rock'
type12_value = 11
heights.append(type12_value)
title.append(type12)
type13 = 'dragon'
type13_value = 3
heights.append(type13_value)
title.append(type13)
type14 = 'ice'
type14_value = 5
heights.append(type14_value)
title.append(type14)
type15 = 'ghost'
type15_value = 3
heights.append(type15_value)
title.append(type15)

ax.barh(title,heights,.5,0,)

plt.show()



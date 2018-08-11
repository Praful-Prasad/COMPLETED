# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:02:41 2018

@author: praful
"""
# -*- coding: utf-8 -*-


import matplotlib.pyplot as panda

vehicles=['Beast Animals','Other Land Animals','Birds','Water Animals','Reptiles']
number=[150,400,225,175,50]
panda.pie(number,labels=vehicles,startangle=90,colors=['r','b','g','black','y'],shadow=True,explode=(0.1,0.1,0.1,0.1,0.1),autopct='%0.2f%%')
panda.ylabel('Type of Vehicles')
panda.legend(vehicles,loc="center right")

panda.title('Total vehicles for each type of vehicle', bbox={'facecolor':'0.9', 'pad':2})
print('\n\n\n')
panda.axis("equal")


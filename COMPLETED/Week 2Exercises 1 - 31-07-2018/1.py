# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:02:41 2018

@author: praful
"""
# -*- coding: utf-8 -*-


import matplotlib.pyplot as panda

vehicles=['Cars','Motorbikes','Vans',	'Buses','Total vehicles']
number=[140,70,55,5,270]
panda.pie(number,labels=vehicles,colors=['r','b','g','black','y'],shadow=True,explode=(0.1,0.1,0.1,0.1,0.1),autopct='%0.2f%%')
panda.ylabel('Type of Vehicles')
panda.legend(vehicles,loc="center right")
panda.title('Total vehicles for each type of vehicle', bbox={'facecolor':'0.8', 'pad':5})

panda.axis("equal")


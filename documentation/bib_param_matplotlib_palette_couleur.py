# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:47:48 2024

@author: forstera

Ce fichier .py contient les parametres utiles pour definir le type de tracer de carte (cmap, unit, levels,..)
"""

import sys
import matplotlib.colors as mcolors
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
import matplotlib.colors as mcolors
from bokeh.palettes import YlOrBr
import matplotlib.cm as cm

vmin_var={}
vmax_var={}
levels_var={}
cmap_var={}
norm_var={}
titre_label_var={}
size_titre_label_var={}
unit_var={}
size_label_var={}

# --- Paramètres tracé

for var in ['ifm']:
    levels_var[var]=[0,5,10,15,20,30,40,50,60,80,100,150,300]
    cmap_data = ["#ffffe5","#fff7bc","#fee391","#fec44f","#fe9929","#ec7014","#cc4c02","#a83c09","#993404","#742802","#411900","#000000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'IFM')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25

for var in ['ifm_gtc20','ifm_gtc25','ifm_gtc30','ifm_gtc35','ifm_gtc40']:
#    levels_var[var]=[0,10,20,40,50,60,70,80,90]
#    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    levels_var[var]=[0,5,10,15,20,30,40,50,60,70,80,90,100,110,120,130,140]
    cmap_data = ['#F7F7F7','#F5E9CA','#F0DB9D','#E8CE70','#DFBC4B','#DBA73E','#D79135','#D27B30','#CB6530','#C14F30','#B53930','#A72033','#980643','#830356','#631766','#37216C']

    #levels_var[var]=[0,5,10,15,20,30,40,50,60,80,100,150,300]
    #cmap_data = ["#ffffe5","#fff7bc","#fee391","#fec44f","#fe9929","#ec7014","#cc4c02","#a83c09","#993404","#742802","#411900","#000000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'IFM')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25


for var in ['diff_ifm_gtc20','diff_ifm_gtc25','diff_ifm_gtc30','diff_ifm_gtc35','diff_ifm_gtc40']:
#    levels_var[var]=[0,10,20,40,50,60,70,80,90]
#    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    levels_var[var]=[-30,-25,-20,-15,-10,-5,5,10,15,20,25,30,35,40,45,50]
#    cmap_data = ['#67001f','#b2182b','#d6604d','#f4a582','#fddbc7','#f7f7f7','#d1e5f0','#92c5de','#4393c3','#2166ac','#053061']

    cmap_data = ['#053061','#2166ac','#4393c3','#92c5de','#d1e5f0','#f7f7f7','#fddbc7','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    #levels_var[var]=[0,5,10,15,20,30,40,50,60,80,100,150,300]
    #cmap_data = ["#ffffe5","#fff7bc","#fee391","#fec44f","#fe9929","#ec7014","#cc4c02","#a83c09","#993404","#742802","#411900","#000000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'IFM')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25



for var in ['iep']:
    levels_var[var]=[1,2,3,4,5,6]
    cmap_data = ["#152eff","#25ff29","#fdff38","#fb7d07","#e50000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'IEP')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25


for var in ['ipi']:
    levels_var[var]=[0,5,10,13,17,21,25,33,41,50,100]
    cmap_data = ["#06470c","#39ad48","#8ee53f","#e6f2a2","#fffd78","#ffb07c","#fd8d49","#fe4b03","#e50000","#840000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'IPI')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25



for var in ['ipi_diff','ifm_diff']:
    levels_var[var]=[-9,-8,-7,-6,-5,-4,-2,-1,0,1,2,3,4,5,6,7,8]
    cmap_data = ['#004529','#006837','#238443','#41ab5d','#78c679','#addd8e','#d9f0a3','#f7fcb9',"#ffffe5","#fff7bc","#fee391","#fec44f","#fe9929","#ec7014","#cc4c02","#a83c09","#993404","#742802","#411900","#000000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'IPI')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25


for var in ['icd']:
    levels_var[var]=[0,50,100,150,200,250,400]
    cmap_data = ["#152eff","#0485d1","#40fd14","#fff917","#ffad01","#e50000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ICD')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25

for var in ['icd_diff']:
    levels_var[var]=[-60,-50,-40,-30,-20,-10,0]
    cmap_data = ["#152eff","#0485d1","#40fd14","#fff917","#ffad01","#e50000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ICD')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25


for var in ['icl']:
    levels_var[var]=[0,65,84,89,93,96,100]
    cmap_data = ["#0c1793","#247afd","#13eac9","#d0e429","#fdb915","#9b7a01"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ICL')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25



for var in ['icl_diff']:
    levels_var[var]=[-20,-15,-10,-8,-6,-4,0]
    cmap_data = ["#0c1793","#247afd","#13eac9","#d0e429","#fdb915","#9b7a01"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ICL')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25



for var in ['ih_diff']:
    levels_var[var]=[-60,-55,-50,-45,-40,-35,-30,-25,-20,-15,-10,-5,0]
    cmap_data = ["#02590f","#028f1e","#8ee53f","#e6f2a2","#fcf679","#ffb07c","#ff964f","#ff5b00","#e50000","#c04e01","#742802","#000000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'IH')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25



for var in ['ih']:
    levels_var[var]=[0,10,20,30,40,50,70,100,120,150,175,250,400]
    cmap_data = ["#02590f","#028f1e","#8ee53f","#e6f2a2","#fcf679","#ffb07c","#ff964f","#ff5b00","#e50000","#c04e01","#742802","#000000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'IH')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25


for var in ['iis']:
    levels_var[var]=[0,50,100,200,300,400,500,600,700,850,1000,1200,1500]
    cmap_data = ["#02590f","#028f1e","#8ee53f","#e6f2a2","#fcf679","#ffb07c","#ff964f","#ff5b00","#e50000","#c04e01","#742802","#000000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'IIS')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25


for var in ['iis_diff']:
    levels_var[var]=[-35,-30,-25,-20,-15,-10,-8,-6,-4,-2,0]
#    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_data = ["#02590f","#028f1e","#8ee53f","#e6f2a2","#fcf679","#ffb07c","#ff964f","#ff5b00","#e50000","#c04e01","#742802","#000000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'IIS')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25


for var in ['nsv2']:
    levels_var[var]=[0.5,1.5,2.5,3.5,4.5,5.5]
    cmap_data = ["deepskyblue","mediumseagreen","yellow","red","black"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'NSV2')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25

for var in ['tr']:
    levels_var[var]=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,30,35,40,50,60,70,80,90,100]
    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d','#800026','#bd0026','#e31a1c','#fc4e2a','#fd8d3c','#feb24c','#fed976','#ffeda0','#ffffcc','#ffffd9','#edf8b1','#c7e9b4','#7fcdbb','#41b6c4','#1d91c0','#225ea8','#253494','#081d58',"deepskyblue","mediumseagreen","yellow"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TR')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25

#for var in ['ANOMd_pr']:
#    levels_var[var]=[-600,-500,-400,-300,-200,-100,0,100,200,300,400,500,600]
#    cmap_data = ['#993404','#d95f0e','#fe9929','#fec44f','#fee391','#ffffd4','#ffffcc','#d9f0a3','#addd8e','#78c679','#31a354','#006837']
#    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ANOMd_PR')
#    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
#    size_titre_label_var[var] = 30
#    unit_var[var] = ''
#    size_label_var[var] = 25

for var in ['REUNION_PRCPTOT_ANOMd']:
    levels_var[var]=[-700,-600,-500,-400,-300,-200,-100,-50,0,50,100,200,300,400,500,600,700]
    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ANOMd_PR')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm/day'
    size_label_var[var] = 25


for var in ['REUNION_Rx1D_ANOMd']:
    levels_var[var]=[-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80]
    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ANOMd_PR')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm/day'
    size_label_var[var] = 25

for var in ['REUNION_Rx5D_ANOMd']:
    levels_var[var]=[-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80]
    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ANOMd_PR')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm/day'
    size_label_var[var] = 25



for var in ['REUNION_PRCPTOT_ANOMrd']:
    levels_var[var]=[-70,-60,-50,-40,-30,-20,-10,-5,0,5,10,20,30,40,50,60,70]
    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ANOMrd_PR')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = '%'
    size_label_var[var] = 25

for var in ['REUNION_Rx1D_ANOMrd','REUNION_Rx5D_ANOMrd']:
    levels_var[var]=[-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]
    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ANOMrd_PR')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = '%'
    size_label_var[var] = 25




for var in ['MAYOTTE_PRCPTOT_ANOMrd']:
#   saison seche
#    levels_var[var]=[-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]
# saison humide
    levels_var[var]=[-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]
    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'ANOMrd_PR')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = '%'
    size_label_var[var] = 25


for var in ['MAYOTTE_PRCPTOT_ANOMd']:
    levels_var[var]=[-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80]
    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'MAYOTTE_PRCPTOT_ANOMd')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm/day'
    size_label_var[var] = 25


for var in ['MAYOTTE_TX32D','REUNION_TX26D','REUNION_TX27D']:
    levels_var[var]=[0,10,20,30,50,75,100,125,150,175,200,225,250,275,300,325,350]
    cmap_data = ['#F7F7F7','#F5E9CA','#F0DB9D','#E8CE70','#DFBC4B','#DBA73E','#D79135','#D27B30','#CB6530','#C14F30','#B53930','#A72033','#980643','#830356','#631766','#37216C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_TX31D','REUNION_TX32D','REUNION_TX33D','REUNION_TX34D','REUNION_TM22TM28D','REUNION_TM26TM33D','REUNION_TM26TM33D-0-3000m']:
    levels_var[var]=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160]
    cmap_data = ['#F7F7F7','#F5E9CA','#F0DB9D','#E8CE70','#DFBC4B','#DBA73E','#D79135','#D27B30','#CB6530','#C14F30','#B53930','#A72033','#980643','#830356','#631766','#37216C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_TX33D_ANOMd','REUNION_TX34D_ANOMd','REUNION_TX26D_ANOMd','REUNION_TX27D_ANOMd','REUNION_TX31D_ANOMd','REUNION_TX32D_ANOMd','REUNION_TM22TM28D_ANOMd','REUNION_TM26TM33D_ANOMd','REUNION_TM26TM33D-0-3000m_ANOMd']:
    levels_var[var]=[0,10,20,40,60,80,100,120,140]
    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D_ANOMd')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['MAYOTTE_TX32D_ANOMd']:
    levels_var[var]=[0,20,40,60,80,100,120,140,160]
    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D_ANOMd')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_TX35D','REUNION_TX36D','REUNION_TX40D','MAYOTTE_TX35D','MAYOTTE_TX40D']:
    levels_var[var]=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    cmap_data = ['#F7F7F7','#F5E9CA','#F0DB9D','#E8CE70','#DFBC4B','#DBA73E','#D79135','#D27B30','#CB6530','#C14F30','#B53930','#A72033','#980643','#830356','#631766','#37216C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12

for var in ['REUNION_TX35D_ANOMd','MAYOTTE_TX35D_ANOMd','MAYOTTE_TX40D_ANOMd']:
    levels_var[var]=[0,2,4,6,8,10,12,14,16]
    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_TN26D']:
    levels_var[var]=[0,2,4,6,8,10,15,20,25,30,35,40,45,50,55,60]
    cmap_data = ['#F7F7F7','#F5E9CA','#F0DB9D','#E8CE70','#DFBC4B','#DBA73E','#D79135','#D27B30','#CB6530','#C14F30','#B53930','#A72033','#980643','#830356','#631766','#37216C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_TN25D','REUNION_TN24D']:
    levels_var[var]=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
    cmap_data = ['#F7F7F7','#F5E9CA','#F0DB9D','#E8CE70','#DFBC4B','#DBA73E','#D79135','#D27B30','#CB6530','#C14F30','#B53930','#A72033','#980643','#830356','#631766','#37216C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['MAYOTTE_TN26D']:
    levels_var[var]=[0,5,10,15,20,25,30,35,40,45,50,60,70,80,90,100,110]
    cmap_data = ['#F7F7F7','#F5E9CA','#F0DB9D','#E8CE70','#DFBC4B','#DBA73E','#D79135','#D27B30','#CB6530','#C14F30','#B53930','#A72033','#980643','#830356','#631766','#37216C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_TN26D_ANOMd']:
    levels_var[var]=[0,4,6,8,10,15,20,25,30]
    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_TN25D_ANOMd','REUNION_TN24D_ANOMd']:
    levels_var[var]=[0,5,10,15,20,25,30,35,40]
    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['MAYOTTE_TN26D_ANOMd']:
    levels_var[var]=[0,10,20,30,40,50,60,70,80]
    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TX31D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12



for var in ['REUNION_TXx','MAYOTTE_TXx']:
    levels_var[var]=[16,18,20,22,24,26,28,30,32,34,36,38,40]
    cmap_data = ['#002F44','#023D70','#006594','#007EA6','#16A9BD','#43C3CB','#A3D483','#E0C653','#D79235','#D07330','#B83D30','#A41A36','#6C1363']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TMm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12

for var in ['REUNION_TXx_ANOMd','MAYOTTE_TXx_ANOMd']:
    levels_var[var]=[0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2.0,2.2]
    cmap_data = ['#FAE1D7','#FAD1BF','#F9C0A8','#F7B091','#F2A07D','#E99071','#E08066','#D7705B','#CD6050','#C24F45','#B83E3B','#AD2B31','#9C1F2C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TMm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12


for var in ['REUNION_TNx','REUNION_TNn','MAYOTTE_TNx']:
    levels_var[var]=[8,10,12,14,16,18,20,22,24,26,28,30,32]
    cmap_data = ['#002F44','#023D70','#006594','#007EA6','#16A9BD','#43C3CB','#A3D483','#E0C653','#D79235','#D07330','#B83D30','#A41A36','#6C1363']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TMm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12

for var in ['REUNION_TNn']:
    levels_var[var]=[2,4,6,8,10,12,14,16,18,20,22,24,26]
    cmap_data = ['#002F44','#023D70','#006594','#007EA6','#16A9BD','#43C3CB','#A3D483','#E0C653','#D79235','#D07330','#B83D30','#A41A36','#6C1363']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TMm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12


for var in ['REUNION_TNx_ANOMd','REUNION_TNn_ANOMd','MAYOTTE_TNx_ANOMd','REUNION_TNn_ANOMd']:
    levels_var[var]=[0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2.0,2.2]
    cmap_data = ['#FAE1D7','#FAD1BF','#F9C0A8','#F7B091','#F2A07D','#E99071','#E08066','#D7705B','#CD6050','#C24F45','#B83E3B','#AD2B31','#9C1F2C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TMm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12




for var in ['REUNION_TMm','MAYOTTE_TMm','temp','tasmax']:
    levels_var[var]=[12,14,16,18,20,22,24,26,28,30,32,34,36]
    cmap_data = ['#002F44','#023D70','#006594','#007EA6','#16A9BD','#43C3CB','#A3D483','#E0C653','#D79235','#D07330','#B83D30','#A41A36','#6C1363']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TMm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12

for var in ['REUNION_DTRm','REUNION_ETR']:
    levels_var[var]=[0,1,2,3,4,5,6,7,8,9,10,11,12]
    cmap_data = ['#002F44','#023D70','#006594','#007EA6','#16A9BD','#43C3CB','#A3D483','#E0C653','#D79235','#D07330','#B83D30','#A41A36','#6C1363']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'DTRm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12


for var in ['REUNION_GD10']:
    levels_var[var]=[1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000]
    cmap_data = ['#002F44','#023D70','#006594','#007EA6','#16A9BD','#43C3CB','#A3D483','#E0C653','#D79235','#D07330','#B83D30','#A41A36','#6C1363']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'DTRm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12


for var in ['REUNION_GD10_ANOMd']:
    levels_var[var]=[100,200,300,400,500,600,700,800,900]
    cmap_data = ['#FACDB9','#F6AD8C','#E88D6F','#D56E59','#C14E44','#AC2A31','#8A1327','#68001F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TMm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12



for var in ['REUNION_ETR']:
    levels_var[var]=[12,13,14,15,16,17,18,19,20,21,22,23,24]
    cmap_data = ['#002F44','#023D70','#006594','#007EA6','#16A9BD','#43C3CB','#A3D483','#E0C653','#D79235','#D07330','#B83D30','#A41A36','#6C1363']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'DTRm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12


for var in ['REUNION_DTRm_ANOMd','REUNION_ETR_ANOMd']:
    levels_var[var]=[-0.3,-0.2,-0.1,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7]
    cmap_data = ['#73A9D3','#8FC4DE','#BEDAE9','#FACDB9','#F6AD8C','#E88D6F','#D56E59','#C14E44','#AC2A31','#8A1327']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TMm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12



for var in ['REUNION_TMm_ANOMd','MAYOTTE_TMm_ANOMd']:
    levels_var[var]=[0,0.2,0.4,0.6,0.8,1,1.2,1.4,1.6,1.8,2.0,2.2]
    cmap_data = ['#FAE1D7','#FAD1BF','#F9C0A8','#F7B091','#F2A07D','#E99071','#E08066','#D7705B','#CD6050','#C24F45','#B83E3B','#AD2B31','#9C1F2C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TMm')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '°C'
    size_label_var[var] = 12


for var in ['REUNION_CWD','MAYOTTE_CWD']:
    levels_var[var]=[0,2,4,6,8,10,12,14,16,18,20,25,30,35,40,45]
    cmap_data = ['#F7F7F7','#E0EBD3','#C8DEB0','#AFD28D','#97C182','#7FB07A','#66A073','#4D906D','#347F68','#176F62','#005E55','#004E43','#003E37','#003D5A','#003372','#331D79']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'CDD')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12

for var in ['REUNION_CWD_ANOMd','MAYOTTE_CWD_ANOMd']:
    levels_var[var]=[-20,-15,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,15,20]
    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'CWD')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['MAYOTTE_CDD']:
    levels_var[var]=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75]
    cmap_data = ['#F7F7F7','#F0EAD0','#E7DEAA','#DDD284','#D1C462','#C8B353','#BEA144','#B59037','#AB7F2A','#A06E1E','#955E13','#884F09','#754307','#633906','#5B2800','#6C0000']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'CDD')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_CDD']:
    levels_var[var]=[0,2,4,6,8,10,12,14,16,18,20,25,30,35,40,45]
    cmap_data = ['#F7F7F7','#F0EAD0','#E7DEAA','#DDD284','#D1C462','#C8B353','#BEA144','#B59037','#AB7F2A','#A06E1E','#955E13','#884F09','#754307','#633906','#5B2800','#6C0000']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'CDD')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12



for var in ['REUNION_CDD_ANOMd','MAYOTTE_CDD_ANOMd']:
    levels_var[var]=[-20,-15,-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,15,20]
    cmap_data = ['#003D2F','#005248','#046961','#1F8078','#34978F','#66ACA4','#8FC0BA','#B6D4D1','#E9CAAC','#DDB180','#CF9856','#BE7F2B','#A5681B','#8D520A','#704007','#543004']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'CDD')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_RR100D']:
    levels_var[var]=[0,1,2,3,4,5,6,8]
    cmap_data = ['#F7F7F7','#C8DEB0','#95C081','#649F72','#317E67','#005D53','#003D58','#331D79']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'RR10D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12

for var in ['REUNION_RR10D','MAYOTTE_RR10D','REUNION_RR20D']:
    levels_var[var]=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,85]
    cmap_data = ['#F7F7F7','#E0EBD3','#C8DEB0','#AFD28D','#97C182','#7FB07A','#66A073','#4D906D','#347F68','#176F62','#005E55','#004E43','#003E37','#003D5A','#003372','#331D79']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'RR10D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12

for var in ['REUNION_RR50D','REUNION_SDII']:
    levels_var[var]=[0,2,4,6,8,10,15,20,25,30,35,40,45,50,55,60]
    cmap_data = ['#F7F7F7','#E0EBD3','#C8DEB0','#AFD28D','#97C182','#7FB07A','#66A073','#4D906D','#347F68','#176F62','#005E55','#004E43','#003E37','#003D5A','#003372','#331D79']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'RR10D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_RRq95refTOT','REUNION_RRq99refTOT']:
    levels_var[var]=[0,2,4,6,8,10,15,20,25,30,35,40,45,50,55,60]
    cmap_data = ['#F7F7F7','#E0EBD3','#C8DEB0','#AFD28D','#97C182','#7FB07A','#66A073','#4D906D','#347F68','#176F62','#005E55','#004E43','#003E37','#003D5A','#003372','#331D79']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'RR10D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '%'
    size_label_var[var] = 12


for var in ['REUNION_RRq95refTOT_ANOMd','REUNION_RRq99refTOT_ANOMd']:
    levels_var[var]=[-9,-8,-7,-6,-5,-4,-2,-1,0,1,2,3,4,5,6,7,8]
    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'RR10D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '%'
    size_label_var[var] = 12



for var in ['REUNION_RR10D_ANOMd','MAYOTTE_RR10D_ANOMd','REUNION_RR20D_ANOMd','REUNION_RR50D_ANOMd','REUNION_SDII_ANOMd']:
    levels_var[var]=[-9,-8,-7,-6,-5,-4,-2,-1,0,1,2,3,4,5,6,7,8]
    cmap_data = ['#543004','#704007','#8D520A','#A5681B','#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F','#1F8078','#046961','#005248','#003D2F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'RR10D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_RR10D_ANOMrd','MAYOTTE_RR10D_ANOMrd','REUNION_SDII_ANOMrd','REUNION_RRq95refTOT_ANOMrd','REUNION_RRq99refTOT_ANOMrd']:
    levels_var[var]=[-25,-20,-15,-10,-8,-6,-4,0,4,6,8,10,15,20,25]
#     cmap_data = ['#6C0000','#603706','#7F4908','#986115','#AA7D29','#BA993E','#CAB756','#DCD282','#A7CC88','#81B27A','#599770','#307D67','#00635A','#00493C','#003A65']
    cmap_data = ['#6C0000','#603706','#7F4908','#986115','#AA7D29','#BA993E','#CAB756','#DCD282','#A7CC88','#81B27A','#599770','#307D67','#00635A','#00493C','#003A65']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'RR10D')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '%'
    size_label_var[var] = 12

for var in ['REUNION_RR100D_ANOMd']:
    levels_var[var]=[-4,-3,-2,-1,0,1,2,3,4]
#    cmap_data = ['#7F4908','#986115','#AA7D29','#BA993E','#CAB756','#DCD282','#A7CC88','#81B27A','#599770','#307D67','#00635A']
#    cmap_data = ['#6C0000','#834B08','#AA7D29','#C8B454','#6EA575','#207464','#004235','#331D79']
    cmap_data = ['#BE7F2B','#CF9856','#DDB180','#E9CAAC','#B6D4D1','#8FC0BA','#66ACA4','#34978F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'RR100D_ANOMd')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12




for var in ['REUNION_CDDcold24','REUNION_CDDcold25','REUNION_CDDcold26','REUNION_CDDcold27']:
    levels_var[var]=[0,50,100,150,200,250,300,400,500,600,700,800,900,1000,1100,1200,1300]
    cmap_data = ['#F7F7F7','#F5E9CA','#F0DB9D','#E8CE70','#DFBC4B','#DBA73E','#D79135','#D27B30','#CB6530','#C14F30','#B53930','#A72033','#980643','#830356','#631766','#37216C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'CDDcold24')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12



for var in ['REUNION_CDDcold24_ANOMd','REUNION_CDDcold25_ANOMd','REUNION_CDDcold26_ANOMd','REUNION_CDDcold27_ANOMd']:
    levels_var[var]=[0,50,100,150,200,300,400,500,600]
    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'CDDcold24_ANOMd')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_SU','REUNION_TR','REUNION_TR25D']:
    levels_var[var]=[0,10,20,40,60,80,100,125,150,175,200,225,250,275,300,325,350]
    cmap_data = ['#F7F7F7','#F5E9CA','#F0DB9D','#E8CE70','#DFBC4B','#DBA73E','#D79135','#D27B30','#CB6530','#C14F30','#B53930','#A72033','#980643','#830356','#631766','#37216C']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'CDDcold24')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12


for var in ['REUNION_SU_ANOMd','REUNION_TR_ANOMd','REUNION_TR25D_ANOMd']:
    levels_var[var]=[0,20,40,60,80,100,120,140,160]
    cmap_data = ['#fff5f0','#fee0d2','#fcbba1','#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'CDDcold24_ANOMd')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'Nombre de jours'
    size_label_var[var] = 12




for var in ['REUNION_PRCPTOT']:
    vmin_var[var]=0
    vmax_var[var]=13000
    levels_var[var]=[0,50,100,200,400,600,800,1000,1500,2000,2500,3000,3500,4000,4500]
    cmap_data = ['#6C0000','#743005','#8A470E','#A05F1A','#B67727','#C69338','#CEB04F','#C1CE78','#91BD80','#6FA675','#4D906D','#297966','#006363','#00527D','#003A7D']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'PRCPTOT')
#    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
#    titre_label_var[var] = 'Cumul annuel moyen ('
    size_titre_label_var[var] = 17
    unit_var[var] = 'mm'
    size_label_var[var] = 12


for var in ['REUNION_Rx1D']:
    levels_var[var]=[0,25,50,75,100,150,200,250,300,350,400,450,500,550,600]
    cmap_data = ['#6C0000','#743005','#8A470E','#A05F1A','#B67727','#C69338','#CEB04F','#C1CE78','#91BD80','#6FA675','#4D906D','#297966','#006363','#00527D','#003A7D']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'PRCPTOT')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'mm'
    size_label_var[var] = 12


for var in ['REUNION_Rx5D']:
    levels_var[var]=[0,50,100,150,200,250,300,350,400,500,600,700,800,900,1000]
    cmap_data = ['#6C0000','#743005','#8A470E','#A05F1A','#B67727','#C69338','#CEB04F','#C1CE78','#91BD80','#6FA675','#4D906D','#297966','#006363','#00527D','#003A7D']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'PRCPTOT')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'mm'
    size_label_var[var] = 12



for var in ['MAYOTTE_PRCPTOT']:
    #valeurs pour la saison seche
#    levels_var[var]=[0,25,50,75,100,125,150,175,200,250,300,325,350,375,400]
    #valeurs pourl a saison humide
    levels_var[var]=[500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1800,1900,2000]
    cmap_data = ['#6C0000','#743005','#8A470E','#A05F1A','#B67727','#C69338','#CEB04F','#C1CE78','#91BD80','#6FA675','#4D906D','#297966','#006363','#00527D','#003A7D']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'PRCPTOT')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'mm'
    size_label_var[var] = 12


for var in ['tf']:
    levels_var[var]=[0,5,10,15,20,25,30,35,40,45,50]
    cmap_data = ['#ffffe5','#fff7bc','#fee391','#fec44f','#fe9929','#ec7014','#cc4c02','#993404','#662506',"#000000"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TF')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25

for var in ['tu']:
    levels_var[var]=[0,10,20,30,40,50,60,70,80,90,100]
    cmap_data = ["#af6f09","#bf9005","#fac205","#ffffcc","#c7e9b4","#7fcdbb","#41b6c4","#2c7fb8","#253494","#000435"]
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'TU')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25


for var in ['tt']:
    vmin_var[var]=0
    vmax_var[var]=36
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],2)
    cmap_var[var] = plt.cm.hot_r
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25

for var in ['prtot','pr']:
    vmin_var[var]=0
    vmax_var[var]=100
    levels_var[var]=[0,1,2,3,4,5,6,7,8,9,10,12,15,20,25,30,35,40,45,50,55,60,70,80,90,100]
    cmap_var[var] = plt.cm.BrBG
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Precipitation ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm)'
    size_label_var[var] = 25

for var in ['prtotAdjust']:
    vmin_var[var]=0
    vmax_var[var]=13000
    levels_var[var]=[0,50,100,200,400,600,800,1000,1500,2000,2500,3000,3500,4000,
                     4500,5000,5500,6000,6500,7000,8000,9000,10000,11000,12000,13000]
    cmap_var[var] = plt.cm.BrBG
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Cumul annuel moyen ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm)'
    size_label_var[var] = 25
    
for var in ['pr_commune']:
    vmin_var[var]=0
    vmax_var[var]=6650
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],150)
    cmap_var[var] = plt.cm.BrBG
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Cumul annuel moyen ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm)'
    size_label_var[var] = 25
    
for var in ['tasmaxAdjust']:
    vmin_var[var]=8
    vmax_var[var]=35
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],0.5)
    cmap_var[var] = plt.cm.jet
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Tempe. annuelle max moy. ('
    size_titre_label_var[var] = 30
    unit_var[var] = '°C)'
    size_label_var[var] = 25
    
for var in ['tasminAdjust']:
    vmin_var[var]=8
    vmax_var[var]=35
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],0.5)
    cmap_var[var] = plt.cm.jet
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Tempe. annuelle min. moy. ('
    size_titre_label_var[var] = 30
    unit_var[var] = '°C)'
    size_label_var[var] = 25
    
for var in ['tasAdjust']:
    vmin_var[var]=8
    vmax_var[var]=35
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],0.5)
    cmap_var[var] = plt.cm.jet
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Tempe. annuelle moy. ('
    size_titre_label_var[var] = 30
    unit_var[var] = '°C)'
    size_label_var[var] = 25
    
for var in ['zs']:
    vmin_var[var]=0
    vmax_var[var]=2600
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],100)
    orig_cmap = plt.cm.terrain
    min_val, max_val = 0.28,1
    colors = orig_cmap(np.linspace(min_val, max_val, len(levels_var[var])))
    cmap_var[var] = matplotlib.colors.LinearSegmentedColormap.from_list("mycmap", colors)
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Orographie ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'm)'
    size_label_var[var] = 25
    
for var in ['hursmaxAdjust','hursminAdjust']:
    vmin_var[var]=0
    vmax_var[var]=102
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],2)
    cmap_var[var] = plt.cm.RdYlBu
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Humidité ('
    size_titre_label_var[var] = 30
    unit_var[var] = '%)'
    size_label_var[var] = 25
    
for var in ['rsdsAdjust']:
    vmin_var[var]=0
    vmax_var[var]=3250
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],250)
    cmap_var[var] = plt.cm.RdYlBu_r
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Rayonnement journalier moy ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'W m$^{2}$)'
    size_label_var[var] = 25

#for var in ['sfcWindAdjust','sfcWind']:
#    vmin_var[var]=0
#    vmax_var[var]=11
#    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],0.5)
#    cmap_var[var] = plt.cm.jet
#    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
#    titre_label_var[var] = 'Vitesse du vent ('
#    size_titre_label_var[var] = 30
#    unit_var[var] = 'm s$^{-1}$)'
#    size_label_var[var] = 25



for var in ['hursmin']:
    levels_var[var]=[0,5,10,15,20,25,30,40,50,60,70,80,90,100]
    cmap_data = ['#BA801A','#B69235','#9AA244','#71AC5D','#39B280','#00B5A9','#00B5CD','#21A8D9','#1D98CA','#1B88BB','#1B79AC','#136B9A','#005F82','#005469','#00494F']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'hursmin')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = '%'
    size_label_var[var] = 25
    titre_label_var[var] = 'Humidité'


for var in ['sfcWindAdjust','sfcWind']:
    levels_var[var]=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    cmap_data = ['#FFFFFF','#FFEBD1','#FFD7A2','#FDC472','#F6AD50','#EE9448','#E57C43','#DD6249','#D7495E','#C63875','#A73990','#7646A7','#633594','#512381','#3F116E']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'WIND')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'm/s'
    size_label_var[var] = 25
    titre_label_var[var] = 'Vitesse du vent '


for var in ['sfcWindAdjustmax','sfcWindmax']:
    levels_var[var]=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28]
    cmap_data = ['#FFFFFF','#FFEBD1','#FFD7A2','#FDC472','#F6AD50','#EE9448','#E57C43','#DD6249','#D7495E','#C63875','#A73990','#7646A7','#633594','#512381','#3F116E']
    cmap_var[var] = mcolors.ListedColormap(cmap_data,'WIND')
    norm_var[var] =  mcolors.BoundaryNorm(levels_var[var], cmap_var[var].N)
    size_titre_label_var[var] = 17
    unit_var[var] = 'm/s'
    size_label_var[var] = 17
    titre_label_var[var] = 'Vitesse du vent '



for var in ['eto']:
    vmin_var[var]=2
    vmax_var[var]=5.25
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],0.25)
    cmap_var[var] = plt.cm.YlOrBr
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Evapotranspiration de référence ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm)'
    size_label_var[var] = 25
    
for var in ['et0']:
    vmin_var[var]=2
    vmax_var[var]=5.25
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],0.25)
    cmap_var[var] = plt.cm.YlOrBr
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Evapotranspiration theorique en ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm)'
    size_label_var[var] = 25    

for var in ['etm']:
    vmin_var[var]=2
    vmax_var[var]=5.25
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],0.25)
    cmap_var[var] = plt.cm.YlOrBr
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Evapotranspiration maximale en ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm)'
    size_label_var[var] = 25
    
for var in ['etr']:
    vmin_var[var]=0
    vmax_var[var]=2.75
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],0.25)
    cmap_var[var] = plt.cm.YlOrBr
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Evapotranspiration réelle ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm)'
    size_label_var[var] = 25
    
for var in ['ts']:
    vmin_var[var]=0
    vmax_var[var]=1.05
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],0.05)
    cmap_var[var] = plt.cm.YlGn
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Taux de saturation'
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25
    
for var in ['ru']:
    vmin_var[var]=0
    vmax_var[var]=85
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],5)
    cmap_var[var] = plt.cm.YlGnBu
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Niveau de remplissage du RU ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm)'
    size_label_var[var] = 25
    
for var in ['deficit']:
    vmin_var[var]=0
    vmax_var[var]=350
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],25)
    cmap_var[var] = plt.cm.YlOrRd #plt.cm.gist_heat_r #plt.cm.afmhot_r #plt.cm.gist_ncar #plt.cm.afmhot_r
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=False)
    
    titre_label_var[var] = 'Nombre de jours par an avec def. hydri.'
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25
    
for var in ['diff_T']:
    vmin_var[var]=-2
    vmax_var[var]=2.2
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],0.2)
    cmap_var[var] = plt.cm.bwr
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Difference de température ('
    size_titre_label_var[var] = 30
    unit_var[var] = '°C)'
    size_label_var[var] = 25

for var in ['diff_pr']:
    vmin_var[var]=-200
    vmax_var[var]=220
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],20)
    cmap_var[var] = plt.cm.bwr
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=True)
    titre_label_var[var] = 'Difference de precipitation ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'mm)'
    size_label_var[var] = 25
    
    
for var in ['densite']:
    vmin_var[var]=0
    vmax_var[var]=6500
    levels_var[var]=np.arange(vmin_var[var],vmax_var[var],500)
    cmap_var[var] = plt.cm.Blues 
    norm_var[var] = BoundaryNorm(levels_var[var], ncolors=cmap_var[var].N, clip=False)
    titre_label_var[var] = 'Densite ('
    size_titre_label_var[var] = 30
    unit_var[var] = 'hab/km$^2$)'
    size_label_var[var] = 25
    
for var in ['cover']:
    levels_var[var]=[10, 20, 30, 40, 50, 60, 80, 90]
    cmap_data = [(0/256,100/256,0/256), (249/256, 106/256, 31/256), (255/256, 255/256, 76/256), (140, 150/256, 255/256), (250/256, 0/256, 0/256), (180/256, 180/256, 180/256), (101/256, 163/256, 62/256),  (0/256,100/256,200/256)]
    cmap_var[var] = mcolors.ListedColormap(cmap_data, 'Test')
    norm_var[var] = None
    titre_label_var[var] = ''
    size_titre_label_var[var] = 30
    unit_var[var] = ''
    size_label_var[var] = 25



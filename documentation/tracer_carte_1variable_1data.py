#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
"""
permet de tracer la carte moyenne d'une variable sur tous les pas de temps d'un fichier
"""

import xarray as xr
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER,LATITUDE_FORMATTER
import matplotlib.ticker as mticker
import matplotlib.colors as mcolors

### Chemins des donnees
#A COMPLETER/ADAPTER :
chemin_file=''
ds_data=xr.open_dataset(chemin_file+'')

### Lecture de la variable
#A COMPLETER/ADAPTER :
variable=''
val_data=ds_data[variable].values
moy_data=np.nanmean(val_data,axis=0) #moyenne temporelle
lats_data=ds_data.lat.values #ou ds_data.latitude.values
lons_data=ds_data.lon.values #ou ds_data.longitude.values

#############################################################
##################### Figure ###############################
#############################################################

#### Parametres d'affichage
fig_width_cm = 52
fig_height_cm = 32
inches_per_cm = 1 / 2.54
fig_width = fig_width_cm * inches_per_cm # width in inches
fig_height = fig_height_cm * inches_per_cm       # height in inches
fig_size = [fig_width, fig_height]
myfig, axarr = plt.subplots(1,1,figsize=fig_size)#,constrained_layout=True)
myfig.set_size_inches(fig_size)
parameters={'figure.titlesize':25}
plt.rcParams.update(parameters)

axarr.axis('off')

### Zone et projection
#A ADAPTER :
lat_lim=[-26,-12]
lon_lim=[-155.5,-141.5]
map_proj=ccrs.PlateCarree()

ax=plt.subplot(1,1,1,projection=map_proj)
### Grille et fond de carte
ax.set_extent([lon_lim[0],lon_lim[1],lat_lim[0],lat_lim[1]])
ax.coastlines('10m',color='black',linewidth=0.8)
gl=ax.gridlines(crs=map_proj,draw_labels=True,linewidth=1,linestyle='--',color='grey',alpha=0.3)
gl.top_labels=False
gl.right_labels=False
xticks=1
yticks=1
gl.xlocator=mticker.FixedLocator(np.arange(lon_lim[0],lon_lim[1]+xticks,xticks))
gl.ylocator=mticker.FixedLocator(np.arange(lat_lim[0],lat_lim[1]+yticks,yticks))
gl.xformatter=LONGITUDE_FORMATTER
gl.yformatter=LATITUDE_FORMATTER
gl.xlabel_style={'size':8,'color':'gray'}
gl.ylabel_style={'size':8,'color':'gray'}

#Colorbar
#A ADAPTER :
colormap = mpl.cm.jet
valmin=0
valmax=55
ecart=5
levels=np.arange(valmin,valmax,ecart)
norm_mean=mcolors.BoundaryNorm(levels,colormap.N)

###Avec contours et sans colorbar prédéfinie
mm=ax.contourf(lons_data, lats_data, moy_data,transform=ccrs.PlateCarree(),cmap=colormap)
cbar=plt.colorbar(mm,orientation='vertical',shrink=0.7,drawedges='True')
#A COMPLETER :
cbar.set_label('',fontsize=17)

"""
###Avec contours et avec colorbar prédéfinie
mm=ax.contourf(lons_data, lats_data, moy_data,vmin=valmin,vmax=valmax,levels=levels,transform=ccrs.PlateCarree(),cmap=colormap)
cbar=plt.colorbar(mm,orientation='vertical',shrink=0.7,drawedges='True')
#A COMPLETER :
cbar.set_label('',fontsize=17)
cbar.set_ticks(levels,labels=levels,fontsize=13)
"""
"""
###Avec pcolormesh et avec colorbar prédéfinie
mm=ax.pcolormesh(lons_data, lats_data, moy_data,norm=norm_mean,transform=ccrs.PlateCarree(),cmap=colormap)
cbar=plt.colorbar(mm,orientation='vertical',shrink=0.7,drawedges='True')
#A COMPLETER :
cbar.set_label('',fontsize=17)
cbar.set_ticks(levels,labels=levels,fontsize=13)
"""

#A ADAPTER :
plt.title('',fontsize=25)
plt.suptitle('',fontsize=18)

#A COMPLETER/ADAPTER :
chemin_fig='' 
figname=chemin_fig+'.png'
plt.savefig(figname,dpi=200)
plt.close()

"""
The function of this is to set rcParams and define a bunch of functions which make figure plotting easy and consistent
"""


from posix import times_result
import matplotlib
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import matplotlib.font_manager as font_manager
from matplotlib import rcParams, rc
from mpl_toolkits.axes_grid1 import make_axes_locatable
from cycler import cycler

import numpy as np 
from datetime import datetime 
import os 

matplotlib.rcParams['pdf.fonttype'] = 42 #this is super weird, see http://phyletica.org/matplotlib-fonts/
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = 'Helvetica'
rcParams['figure.dpi']= 400
rcParams['axes.labelsize']=7
rcParams['axes.labelpad']=3
rcParams['axes.titlepad']=3
rcParams['axes.titlesize']=9
rcParams['axes.xmargin']=0
rcParams['axes.ymargin']=0
rcParams['axes.facecolor']=[1,1,1,0] 
rcParams['axes.edgecolor'] = 'darkgrey'
rcParams['axes.linewidth'] = 2
rcParams['lines.linewidth'] = 20
rcParams['xtick.major.width'] = 2
rcParams['xtick.color'] = 'darkgrey'
rcParams['ytick.major.width'] = 2
rcParams['ytick.color'] = 'darkgrey'
rcParams['xtick.labelsize']=7
rcParams['ytick.labelsize']=7
rcParams['grid.linewidth']=0.1
rcParams['legend.fontsize']=7
rcParams['lines.linewidth']=0.5
rcParams['lines.markersize'] = 1.5
rcParams['xtick.major.pad']=2
rcParams['xtick.minor.pad']=2
rcParams['ytick.major.pad']=2
rcParams['ytick.minor.pad']=2
rcParams['figure.titlesize']='medium'
rcParams['axes.prop_cycle']=cycler('color', ['#66c2a5','#fc8d62','#8da0cb','#e78ac3','#a6d854','#ffd92f','#e5c494','#b3b3b3'])
rcParams['image.cmap'] = 'inferno'

def saveFigure(fig,saveTitle="",specialLocation=None,figureDirectory=None,saveTypes=['pdf','svg']):
    """saves a figure by date (folder) and time (name) 
    Args:

        fig (matplotlib fig object): the figure to be saved
        saveTitle (str, optional): name to be saved as. Current time will be appended to this Defaults to "".
    """	
    #make global figure directory (in same directory as tomplotlib unless otherwise specificed)
    if figureDirectory is None: 
        figureDirectory = os.path.dirname(os.path.dirname(tomplotlib.__file__))
        figureDirectory = figureDirectory  + "/Figures/"
        if not os.path.isdir(figureDirectory):
            os.mkdir(figureDirectory)

    #make today-specific directory inside figure directory  
    today =  datetime.strftime(datetime.now(),'%y%m%d')
    if not os.path.isdir(figureDirectory + f"{today}/"):
        os.mkdir(figureDirectory + f"{today}/")
    
    filetypes = ['pdf','svg']
    for filetype in filetypes:
        figdir = figureDirectory + f"{today}/"
        now = datetime.strftime(datetime.now(),'%H%M')
        path_ = f"{figdir}{saveTitle}_{now}"
        path = path_
        i=1
        while True:
            if os.path.isfile(path+"." + filetype):
                path = path_+"_"+str(i)
                i+=1
            elif i >= 100: break
            else: break
        fig.savefig(path+"."+filetype,bbox_inches='tight')
    
    if specialLocation is not None: 
        fig.savefig(specialLocation,bbox_inches='tight')

    return path

def hideAxes(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['left'].set_color(rcParams['axes.edgecolor'])
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_color('none')        
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_color(rcParams['axes.edgecolor'])
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['top'].set_color('none')




if __name__ == "__main__": 
    x = np.linspace(-2*np.pi,2*np.pi,1000)
    y = np.sin(x) + np.random.normal(0,0.3,size=len(x))
    fig, ax = plt.subplots(figsize=(2,2))
    ax.scatter(x,y)
    ax.plot(x,np.sin(x))
    ax.set_xlabel("x / m")
    ax.set_ylabel("A dependent variable / a.u.")
    hideAxes(ax)
    saveFigure(fig)

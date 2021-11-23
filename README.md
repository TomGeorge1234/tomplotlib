# tomplotlib

Welcome to tomplotlib. My wrapper for matplotlib. 
This package will style your plots and defines some useful functions. 
<img src="/readmefigures/tomplotlib.png" width="600">

## Installation
To install, run
```
pip install git+https://github.com/TomGeorge1234/tomplotlib.git
```
Alternatively, clone this directory and then run:
```
python setup.py install 
```

## Importing 
Import ```tomplotlib``` into your code with: /
```
import tomplotlib.tomplotlib as tpl 
```
set's most of the required style parameters. 

## Usage
* ```tpl.xyAxes(ax)``` 
Tidies the axes, leaving only x and y axes at zero. 


* ```tpl.setColorScheme(colorscheme)``` sets the colour scheme
```
tpl.setColorscheme(colorscheme=1)
fig, ax = makeFigure(N=5)

tpl.setColorscheme(colorscheme=2)
fig, ax = makeFigure(N=5)

tpl.setColorscheme(colorscheme='Set3')
fig, ax = makeFigure(N=5)

tpl.setColorscheme(colorscheme=[[0.9,0.9,0.9],[0.75,0.75,0.75],[0.6,0.6,0.6],[0.45,0.45,0.45],[0.3,0.3,0.3],[0.15,0.15,0.15],[0,0,0]])
fig, ax = makeFigure(N=5)
```
You pass ```colorscheme``` as an ```int``` (schemes I have defined), as ```str``` (matplotlib schemes, see [here](https://matplotlib.org/stable/tutorials/colors/colormaps.html)) or as a ```list``` of colors (e.g. list of hexstrings). These will become C0, C1, C2...

<img src="/readmefigures/colorschemes.png">


* ```tpl.saveFigure(fig)```
This, in my opinion, is the most useful bit. By defining a figure directory (```tpl.figureDirectory = "where_to_save_my/Figures/"```), you can call ```tpl.saveFigure(fig, `figureName`)```. This will timestamp the figure and save it in the figure directory, inside another directory which is the todays days date. ```"./"``` is your current working directory so the default is set "./Figures/". By default images will be saved as `.pdf`s, `.png`s and `.svg`s

```
import tomplotlib.tomplotlib as tpl 
tpl.figureDirectory = "./Figures/"
fig, ax = makeFigure()
tpl.saveFigure(fig,figName)
```

## Edits 
If you wish to edit this code, go ahead! After editing you will need to make a new setup files, then reinstall. This can be done with: 
```
python setup.py sdist
python setup.py install
```
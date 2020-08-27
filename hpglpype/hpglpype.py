from typing import Tuple

import click
import vpype as vp
import numpy as np
#import ConfigParser #for plotter hard clips



@click.command()
@click.argument("output", type=click.File("w"))
@click.option(
    "-p",
    "--page-format",
    type=vp.PageSizeType(),
    default="tight",
    help="Set the page format.",
)
@click.option(
    "-l", "--landscape", is_flag=True, help="Use landscape orientation instead of portrait.",
)
@click.option(
    "-c", "--center", is_flag=True, help="Center the geometries within the SVG bounds.",
)



@vp.global_processor
def hpgl(
    vector_data: vp.VectorData,
    output,
    page_format: Tuple[float, float],
    landscape: bool,
    center: bool,
) -> vp.VectorData:
    """
    Insert documentation here (it will show up with `vpype hpgl --help`)
    ===HPGLpype by zxsq===
    this vpype plugin allows converting svg files to HPGL files
    compatible with vintage plotters such as those by HP and Roland.
    Pens are selected according to layer numbers, defaulting to pen 1.
    It was tested on an HP7475A, and may/may not misbehave on other models.
    ===command options===
    -PS  | --paper-size        Specify loaded paper size from the following list
        ================================
        ||          US Sizes  (inches)||
        ||A    US Letter      (8.5x11)||
        ||B    US Tabloid      (11x17)||
        ||L    US Legal       (8.5x14)||
        ||X    US Executive(7.25x10.5)||
        ||        Metric Sizes    (mm)||
        ||A6   ISO A6        (105x148)||
        ||A5   ISO A5        (148x210)||
        ||A4   ISO A4        (210x297)||
        ||A3   ISO A3        (297x420)||
        ================================
    -OL  | --origin_location   use either [center] or [corner] based on what your plotter uses
    
    """

    # TODO: <your code here - call 800-555-1212>
    ####### Care about options eg plotter home, paper orientation
    
    def plotUnit(line):
    #convert vpype pixels (96ppi) to plotter units (0.025mm)
    #[0.025 mm/pu] / [25.4 mm/in] = 0.0009842519685 in/pu
    #1 in / 0.0009842519685 in/pu = 1,016.0000000041 pu/in
    #1,016.0000000041 pu/in / [96 px/in] = 10.5833333334 pu/px
    ##plotter truncates to int when using pu anyways, so we round the conversion
           ##round(px val * 10.583333) = pu val
        PUConstant = 10.583333
        PUX = np.round(line.real * PUConstant)
        PUY = np.round(line.imag * PUConstant)
        plot = np.zeros((line.size,), dtype=complex)
        plot.real = PUX
        plot.imag = PUY
        #print("PLOT ", plot)
        return(plot)
    
    def hpglWrite(plotData):
    #write the actual line data to the hpgl file, runs once per line.
        workingX = 0
        workingY = 0
        #print("write data: ", plotData)
        output.write("PU") #move to 1st endpoint on line
        workingX = int(plotData[0].real) #int() to drop trailing .0
        workingY = int(plotData[0].imag)
        output.write("{},{}".format(workingX, workingY))
        output.write(";PD") #never need to PU to multiple points
        for i in range(1, plotData.size):
            workingX = int(plotData[i].real)
            workingY = int(plotData[i].imag)
            output.write("{},{}".format(workingX, workingY) )
            output.write("," if i < (plotData.size - 1) else ";")
            #write movement values, add commas between multiple
            ##points on same line and semicolons @ end of line
        return(0)
 
    def initFile():
        #initialize the output hpgl file
        output.write("IN;")
        return(0)
    
    def selPen(layer):
        #select pen via layer number
        output.write("SP{};".format(layer))
        return(0)
    
    initFile()
    for layer_id in sorted(vector_data.layers.keys()):
        selPen(layer_id)
        layer = vector_data.layers[layer_id]
        for line in layer:
            plotArr = plotUnit(line) #convert px to PU
            hpglWrite(plotArr) #write to file
    selPen(0); #put the pen away
    initFile(); #leave plotter in initialized state

    return vector_data


hpgl.help_group = "Plugins"



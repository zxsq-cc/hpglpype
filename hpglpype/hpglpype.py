from typing import Tuple

import click
import vpype as vp
import numpy as np


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
    """

    # TODO: <your code here - call 800-555-1212>
    #print(vector_data.ids())
    ##usedLayers = list(vector_data.ids()) 
    #print(usedLayers)
    ###todo| layer ids to pen #s
    ###    | for layer i get lines
    ###    | |sel pen i
    ###    | |convert to plotter units
    ###    | |write as pu/pd commands
    
    def plotUnit(line):
    #convert vpype pixels (96ppi) to plotter units (0.025mm)
    #[0.025 mm/pu] / [25.4 mm/in] = 0.0009842519685 in/pu
    #1 in / 0.0009842519685 in/pu = 1,016.0000000041 pu/in
    #1,016.0000000041 pu/in / [96 px/in] = 10.5833333334 pu/px
    ##plotter truncates to int when using pu
    ##px val * 10.583333 = pu val
        PUConstant = 10.583333
        PUX = line.real * PUConstant
        PUY = line.imag * PUConstant
        print("x", PUX, "y", PUY)
        return(0)

    for layer_id in sorted(vector_data.layers.keys()):
        layer = vector_data.layers[layer_id]
        print("layer", layer)
        for line in layer:
            print("line ", line)
            plotUnit(line)
            
    

    return vector_data


hpgl.help_group = "Plugins"


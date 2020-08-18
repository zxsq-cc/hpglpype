from typing import Tuple

import click
import vpype as vp


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

    # TODO: implement this...

    return vector_data


hpgl.help_group = "Plugins"
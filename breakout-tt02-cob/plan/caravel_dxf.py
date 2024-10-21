#!/usr/bin/env python3

from caravel_data import die_size, pads_top, pads_right, pads_bottom, pads_left
import ezdxf

doc = ezdxf.new(dxfversion="R2010")
msp = doc.modelspace()

for pads in pads_top, pads_right, pads_bottom, pads_left:
    for pad in pads:
        msp.add_point(pad)

doc.saveas("caravel.dxf")


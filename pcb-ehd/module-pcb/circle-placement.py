#!/usr/bin/python3

# call as ./circle-placment.py path-to-project/pcb.kicad_pcb

import math
import sys

sys.path.insert(1, '/usr/lib/kicad-nightly/lib/python3/dist-packages/')

from pcbnew import * 

pcb = LoadBoard(sys.argv[1])

for x in range(1,13):
	refdes = "D{0}".format(x)

	x_center = 100
	y_center = 100

	radius = 45

	angle = ((360 / 12 * (x-1)) - 90) % 360

	x_led = x_center + math.cos(math.radians(angle)) * radius
	y_led = y_center + math.sin(math.radians(angle)) * radius

	part = pcb.FindFootprintByReference(refdes)
	part.SetPosition(wxPoint(FromMM(x_led),FromMM(y_led)))
	part.SetOrientation((angle + 180) * -10)

	print("Refdes: {0}, \t X: {1}, \t Y: {2}, \t rot: {3}".format(refdes, round(x_led,2), round(y_led,2), 90 - ((x-1) * 30)))

Refresh()

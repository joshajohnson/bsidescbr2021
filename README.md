# BSidesCBR2021
Slides and Design Files for BSides Canberra 2021

## Contents:
- `slides-ehd` slides for my "Electronic Hardware Design" talk.
- `pcb-ehd` design files for my "Electronic Hardware Design" talk.
    - `pcb-ehd/integrated-pcb` is the fully integrated bow tie.
    - `pcb-ehd/module-pcb` is the circular PCB using a Feather and microphone breakout.
    - `pcb-ehd/parts-lib` are custom footprints used in the above projects.
- `pcb-sao-magpie` design files for the Magpie SAO.

## PCB Design Files
**NOTE:** Both of the `pcb-ehd` projects have major issues with footprints and layout. **DO NOT manufacture these designs.** The Magpie SAO can however be manufactured if desired.

The `pcb-ehd` files require a recent KiCad Nightly build to open, whereas the SAO can be opened in KiCad 5.

In each of the project folders, you will find the below files:

- `proj.kicad_pro` is the overall KiCad project (`.pro` for V5).
- `proj.kicad_sch` is the schematic (`.sch` for V5).
- `proj.kicad_pcb` is the physical layout.
- `outputs/schematic.pdf` is a PDF of the schematic.
- `outputs/assembly.html` is a "Human Pick and Place" file which will help you hand assemble the board.
- `outputs/bom.csv` is the bill of materials required to populate the boards. I have not fully specified the resistors and capacitors for the integrated PCB.
#!/bin/bash -ue

targets=()
files=()

targets+=("//mk2:mk2.kicad_pcb")
files+=("mk2/mk2.kicad_pcb")
targets+=("//mk2:mk2_plate_top.dxf")
files+=("mk2/mk2_plate_top.dxf")

targets+=("//mk2:mk2_routed")
files+=("mk2/mk2_routed.zip")

targets+=("//mk3:mk3.kicad_pcb")
files+=("mk3/mk3.kicad_pcb")
targets+=("//mk3:mk3_plate_top.dxf")
files+=("mk3/mk3_plate_top.dxf")
targets+=("//mk3:mk3_plate_bottom.dxf")
files+=("mk3/mk3_plate_bottom.dxf")

targets+=("//mk3/routed:mk3")
files+=("mk3/routed/mk3.tar")

bazelisk build ${targets[@]} $@
rm -rf $(bazelisk info workspace)/dist/*
for path in "${files[@]}"
do
    mkdir -p $(dirname $(bazelisk info workspace)/dist/$path)
    cp $(bazelisk info bazel-bin)/$path $(bazelisk info workspace)/dist/$path
done

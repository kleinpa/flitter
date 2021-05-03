#!/bin/bash -ue

targets=()
files=()

targets+=("//mk2:plate_top")
files+=("mk2/plate_top.dxf")

targets+=("//mk2:board_routed")
files+=("mk2/board_routed.zip")

targets+=("//mk3:plate_top")
files+=("mk3/plate_top.dxf")

targets+=("//mk3:plate_bottom")
files+=("mk3/plate_bottom.dxf")

targets+=("//mk3:board_kicad")
files+=("mk3/board.kicad_pcb")

bazelisk build ${targets[@]} $@
rm -rf $(bazelisk info workspace)/dist/*
for path in "${files[@]}"
do
    mkdir -p $(dirname $(bazelisk info workspace)/dist/$path)
    cp $(bazelisk info bazel-bin)/$path $(bazelisk info workspace)/dist/$path
done

import sys

from absl import app, flags

from kbtb.keyboard import save_keyboard
from kbtb.keyboard_pb2 import Keyboard, Position
from kbtb.layout import holes_between_keys, mirror_keys, rotate_keys, grid
from kbtb.outline import generate_outline_tight

FLAGS = flags.FLAGS
flags.DEFINE_string('output', None, 'Output path.')
flags.DEFINE_enum('format', 'bin', ['bin', 'text'], 'Protobuf output format.')


def layout():
    kb = Keyboard(
        name="quine-mk2",
        controller=Keyboard.CONTROLLER_PROMICRO,
        switch=Keyboard.SWITCH_CHERRY_MX,

        # Plate outline parameters
        hole_diameter=2.6,
    )

    pitch = 19.05
    column_offsets = [-1.0, 0.0, 5.0, 2.25, -4.8, -6.3]
    keys = [
        *(grid(x, 3, y_offset=column_offsets[x]) for x in range(6)),
        *(grid(x, 2, y_offset=column_offsets[x]) for x in range(6)),
        *(grid(x, 1, y_offset=column_offsets[x]) for x in range(6)),
        *(grid(x,
               arc_radius=90,
               x_offset=-0.65 * pitch,
               y_offset=column_offsets[1]) for x in range(3)),
    ]

    for key in mirror_keys(rotate_keys(keys, angle=45)):
        kb.keys.append(key)

    for hole in holes_between_keys(kb.keys,
                                   ((1, 12), (12, 25), (5, 16), (29, 38),
                                    (30, 39), (6, 19), (10, 23), (23, 34))):
        kb.hole_positions.append(hole)

    kb.controller_pose.CopyFrom(kb.keys[8].pose)

    # TODO: un-hardcode
    row_nets = (0, 7, 8, 9)
    col_nets = (17, 16, 15, 14, 13, 12, 11, 10, 6, 5, 4, 3)
    for i, key in enumerate(kb.keys):
        key.controller_pin_low = row_nets[i // 12]
        key.controller_pin_high = col_nets[(i % 12) +
                                           (3 if i // 12 == 3 else 0)]

    for x, y in generate_outline_tight(
            kb,
            outline_concave=80,
            outline_convex=1.5,
    ).simplify(0.001).coords:
        kb.outline_polygon.add(x=x, y=y)

    return kb


def main(argv):
    save_keyboard(layout(), FLAGS.output, FLAGS.format)


if __name__ == "__main__":
    app.run(main)

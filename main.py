from PIL import Image
import sys
import numpy


def getArg(idx, default: any = ""):
    return sys.argv[idx] if idx < len(sys.argv) and sys.argv[idx] != "-" else default


def getColor(color: list[int]) -> str | None:
    result = ""
    if color[3] == 0:
        return None
    for c in color[:3]:
        hex_val = hex(c)[2::]
        result += "0" + hex_val if len(hex_val) == 1 else hex_val
    return result


CHAR = '⬛'
HIDDEN_CHAR = '  '


def convert_img(in_path: str, out_path: str, scoreboard="display", left_align=False):
    img = Image.open(in_path)

    width, height = img.size

    data = list(img.convert("RGBA").getdata())
    data = numpy.array(data).reshape((width, height, 4)).tolist()

    out = ""

    for idx, row in enumerate(data):
        out += f'scoreboard players set line_{idx} {scoreboard} -{idx}\n'

        display = '['
        last_cell: list[int] = row[0]
        count = 0
        for cell in row:
            if cell == last_cell:
                count += 1
                continue

            color = getColor(last_cell)
            if color is None:
                display += f'{{"text":"{HIDDEN_CHAR * count}"}},'
            else:
                display += f'{{"text":"{CHAR * count}","color":"#{color}"}},'
            count = 1
            last_cell = cell

        color = getColor(last_cell)
        if color is None:
            display += f'{{"text":"{HIDDEN_CHAR * count}"}}]'
        else:
            display += f'{{"text":"{CHAR * count}","color":"#{color}"}}]'

        if left_align:
            out += f'scoreboard players display numberformat line_{idx} {scoreboard} blank\n'
            out += f'scoreboard players display name line_{idx} {scoreboard} {display}\n'
        else:
            out += f'scoreboard players display name line_{idx} {scoreboard} ""\n'
            out += f'scoreboard players display numberformat line_{idx} {scoreboard} fixed {display}\n'

    if out_path == "":
        print(out)
        exit(0)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)


if __name__ == '__main__':
    leftAlign: bool
    match getArg(4, "left").lower():
        case "right":
            leftAlign = False
        case "left":
            leftAlign = True
        case _:
            raise "Invalid alignment, expected 'left' or 'right'"
    convert_img(getArg(1), getArg(2, ""), getArg(3, "display"), leftAlign)

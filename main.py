from PIL import Image
import sys
import numpy


def getArg(idx, default: any = ""):
    return sys.argv[idx] if idx < len(sys.argv) and sys.argv[idx] != "-" else default


def getColor(color: list[int]) -> str:
    result = ""
    for c in color:
        hex_val = hex(c)[2::]
        result += "0" + hex_val if len(hex_val) == 1 else hex_val
    return result


img = Image.open(getArg(1))
outputFile = getArg(2, "")
char = getArg(3, "⬛")
scoreboard = getArg(4, "display")
leftAlign: bool
match getArg(5, "left").lower():
    case "right":
        leftAlign = False
    case "left":
        leftAlign = True
    case _:
        raise "Invalid alignment, expected 'left' or 'right'"



width, height = img.size

data = list(img.convert("RGB").getdata())
data = numpy.array(data).reshape((width, height, 3)).tolist()

out = ""

for idx, row in enumerate(data):
    out += f'scoreboard players set line_{idx} {scoreboard} -{idx}\n'

    display = '['
    last_cell: list[int] = row[0]
    count = 0
    color = ""
    for cell in row:
        if cell == last_cell:
            count += 1
            continue

        display += f'{{"text":"{char * count}","color":"#{getColor(last_cell)}"}},'
        count = 1
        last_cell = cell

    display += f'{{"text":"{char * count}","color":"#{getColor(last_cell)}"}}]'

    if leftAlign:
        out += f'scoreboard players display numberformat line_{idx} {scoreboard} blank\n'
        out += f'scoreboard players display name line_{idx} {scoreboard} {display}\n'
    else:
        out += f'scoreboard players display name line_{idx} {scoreboard} ""\n'
        out += f'scoreboard players display numberformat line_{idx} {scoreboard} fixed {display}\n'


if outputFile == "":
    print(out)
    exit(0)

with open(outputFile, "w", encoding="utf-8") as f:
    f.write(out)
    print("Wrote file")

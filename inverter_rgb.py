
def check_colors(colors: list):
    for color in colors:
        if not isinstance(color, int):
            raise Exception('Valor não e um numero')
        if color < 0 or color > 255:
            raise Exception('Valor da cor não esta entre 0 e 255')


def inverter_rgb(colors: tuple) -> tuple:
    red, green, blue = colors
    check_colors(colors=[red, green, blue])
    red = abs(255 - red)
    green = abs(255 - green)
    blue = abs(255 - blue)
    return red, green, blue

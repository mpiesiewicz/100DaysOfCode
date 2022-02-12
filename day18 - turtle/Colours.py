from colorgram import colorgram


class Colours:

    @staticmethod
    def colour_getter(image, number_of_colours):
        scan = colorgram.extract(image, number_of_colours)
        colours = []
        for colour in scan:
            red = colour.rgb.r
            green = colour.rgb.g
            blue = colour.rgb.b
            colours.append((red, green, blue))
        return colours

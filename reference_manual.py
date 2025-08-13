from constants import MAJOR_COLORS, MINOR_COLORS
from color_code_converter import get_pair_number_from_color

def generate_reference_manual():
    manual = "Color Coding Reference Manual:\n"
    manual += "===========================\n"
    manual += "ID | Major  | Minor\n"
    manual += "-------------------\n"
    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            pair_num = get_pair_number_from_color(major, minor)
            manual += f"{pair_num:2d} | {major:<6} | {minor}\n"
    return manual

def print_reference_manual():
    print(generate_reference_manual())
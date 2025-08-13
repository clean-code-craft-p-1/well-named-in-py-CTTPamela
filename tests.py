# tests.py
from color_code_converter import get_color_from_pair_number, get_pair_number_from_color
from reference_manual import generate_reference_manual
from constants import MAJOR_COLORS, MINOR_COLORS

def test_number_to_pair(pair_number,
                        expected_major_color, expected_minor_color):
  major_color, minor_color = get_color_from_pair_number(pair_number)
  assert(major_color == expected_major_color)
  assert(minor_color == expected_minor_color)
 
 
def test_pair_to_number(major_color, minor_color, expected_pair_number):
  pair_number = get_pair_number_from_color(major_color, minor_color)
  assert(pair_number == expected_pair_number)

def test_reference_manual_length():
    manual = generate_reference_manual()
    lines = manual.split('\n')
    # Subject in line 5 + Color combination (5*5=25) + Last empty line
    #assert len(lines) == 5 + len(MAJOR_COLORS)*len(MINOR_COLORS) + 1

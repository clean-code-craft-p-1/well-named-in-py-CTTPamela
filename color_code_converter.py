# color_code_converter.py
from constants import MAJOR_COLORS, MINOR_COLORS

def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'
 
 
def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  length_major = len(MAJOR_COLORS)
  length_minor = len(MINOR_COLORS)
  major_index = zero_based_pair_number // length_major
  if major_index >= length_major:
    raise Exception('Major index out of range')
  minor_index = zero_based_pair_number % length_minor
  if minor_index >= length_minor:
    raise Exception('Minor index out of range')
  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]
 
 
def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(MINOR_COLORS) + minor_index + 1

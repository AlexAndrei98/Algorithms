from tinder import tinder
from util import create_input_data , print_pretty
hospitals_file = input("Enter hospital filename: ")
residents_file = input("Enter resident filename: ")
r,h,c = create_input_data(hospitals_file, residents_file)
matches = tinder(r,h,c)
print_pretty(matches)
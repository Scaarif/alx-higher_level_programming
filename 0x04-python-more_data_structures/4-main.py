#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements
set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
set_3 = set()
c_set = only_diff_elements(set_1, set_2)
print(sorted(list(c_set)))

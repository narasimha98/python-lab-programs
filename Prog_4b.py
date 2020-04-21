#Consider the string 'brontosaurus'.
#Write Pythonic code that implements and
#returns the functionality of histogram using dictionaries for the given string.
#Also, write the function print_hist to print the keys
#and their values in alphabetical order from the values returned by the histogram function.


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

# OR

# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] = d[c] + 1
#     return d

def print_hist(h):
    key_list = sorted(h.keys())
    for key in key_list:
        print(key, h.get(key))

print_hist(histogram('brontosaurus'))

# Text Wrap
import textwrap
# elp on module textwrap:
#
# NAME
#     textwrap - Text wrapping and filling.
#
# CLASSES
#     builtins.object
#         TextWrapper
#
#     class TextWrapper(builtins.object)
#      |  TextWrapper(width=70, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, \
#         fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True, tabsize=8, *, max_lines=None, placeholder=' [...]')
    # wrap(text, width=70, **kwargs)
    #     Wrap a single paragraph of text, returning a list of wrapped lines.
    #
    #     Reformat the single paragraph in 'text' so it fits in lines of no
    #     more than 'width' columns, and return a list of wrapped lines.  By
    #     default, tabs in 'text' are expanded with string.expandtabs(), and
    #     all other whitespace characters (including newline) are converted to
    #     space.  See TextWrapper class for available keyword args to customize
    #     wrapping behaviour.

def wrap(string, max_width):
    # return textwrap.wrap(string, width=max_width))
    # Example: textwrap returns a list. Use str.join method to get string format
    # sadasfsdgadfasdasd
    # 3
    # ['sad', 'asf', 'sdg', 'adf', 'asd', 'asd']
    return "\n".join(textwrap.wrap(string, width=max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

"""
Ouput
I am a disco dancer, Ten tehn ten tehn
4
I am
a di
sco
danc
er,
Ten
tehn
ten
tehn
"""


# BLue Blood

# This is a change to test git commands

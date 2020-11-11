import textwrap

def wrap(string, max_width):
    result = []
    init = 0
    while init <= len(string):
        p = string[init:init+max_width]
        result.append(p)
        init = init + max_width

    return '\n'.join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
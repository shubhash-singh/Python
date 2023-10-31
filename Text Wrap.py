import textwrap

def wrap(string, max_width):
    str=""
    result = textwrap.wrap(string, width = max_width)
    for i in result:
        str+=i+"\n"
    return str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
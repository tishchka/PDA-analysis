import ply.lex as lex
import sys

tokens = [
    'INPUT_ALPHABET',
    'STACK_ALPHABET',
    'AUTOMATA_STATE',
    'BIND',
    'OR',
    'ENDL',
    'NULL',
    'EMPTY',
    'EPS',
    'COMMENT'
]

t_BIND = r'~'
t_OR = r'\|'
t_ENDL = r','
t_NULL = r'NULL'
t_EMPTY = r'EMPTY'
t_EPS = r'EPS'

t_ignore = " \t\r\f"


def drop_commas_and_backslash(s):
    return s.replace("\\" + '"', '"').replace("\\" + "'", "'") \
            .replace("\\" + '`', '`').replace("\\" + '<', '<') \
            .replace("\\" + '>', '>').replace("\\" + "\\", "\\")


def for_comments(s):
    s = s.replace("\n", " ")
    result = s.replace("<", "").replace(">", "")
    helper = []
    i = 0
    while i < len(s):
        if s[i] == '<':
            helper.append(('<', i))
        if s[i] == '>':
            result += "|" + s[helper[len(helper)-1][1]+1:i].replace("<", "").replace(">", "")
            helper = helper[:-1]
        i += 1
    if len(helper) > 0:
        result += "|" + s[helper[len(helper)-1][1]:i].replace("<", "").replace(">", "")
    return result


def t_INPUT_ALPHABET(t):
    r'\'.+?(?<!\\)\''
    t.value = drop_commas_and_backslash(t.value[1:-1])
    return t


def t_STACK_ALPHABET(t):
    r'\`.+?(?<!(?<!\\)\\)\`'
    t.value = drop_commas_and_backslash(t.value[1:-1])
    return t


def t_AUTOMATA_STATE(t):
    r'\".+?(?<!(?<!\\)\\)\"'
    t.value = drop_commas_and_backslash(t.value[1:-1])
    return t


def t_COMMENT(t):
    r'\<.*\> | \<.*(\n.*)+\>'
    t.value = for_comments(t.value[1:-1])
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character " + str(t.value[0]) + " in line " + str(t.lexer.lineno))
    t.lexer.skip(1)


def main():
    if len(sys.argv) > 1:
        filename = str(sys.argv[1])

        with open(filename, 'r') as code, open(filename + ".out", "w") as outfile:
            lexer = lex.lex()
            lexer.input("".join(code.readlines()))

            while True:
                tok = lexer.token()
                if not tok:
                    break
                print(tok, file=outfile)


if __name__ == "__main__":
    main()

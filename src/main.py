import json


data = json.load(open('settings/settings.json','r'))

keywords = ['print','set','type']
variables = {}
operands = '+-*/'
digits = '0123456789'
_literals = ' \'|'

def lexer(text):
    tok = ""
    string = ''
    iS = False
    tokens = ['SOF']
    for char in text:
        tok += char
        if tok in _literals or tok[-1:] in _literals:
            if tok == ' ' or tok[-1:] == ' ':
                if iS:
                    string += tok
                tok = ''
            elif tok == '\'':
                if iS:
                    tokens.append('<str:{}>'.format(string))
                    iS = False
                    string = ''
                else:
                    iS = True
                tok = ''
            elif tok == '|':
                tokens.append('ignore')
                tok = ''
        elif tok in keywords:
            tokens.append(tok)
            tok = ""
        else:
            if iS:
                string += tok
                tok = ""
    tokens.append('EOF')
    if data['Debug']:
        print(tokens)
    return tokens

def parser(toks):
    i = 0
    while i < len(toks):
        if toks[i] != 'EOF':
            if toks[i-1] != 'ignore':
                if toks[i] == 'type':
                    a = 1
                    if toks[i+1] == 'ignore':
                        a = 2
                    if toks[i+a] in keywords:
                        print('<key>')
                    else:
                        print(toks[i+a].split(':')[0]+'>')
                elif toks[i] == 'print':
                    print(toks[i+1][5:-1])
        i += 1

def main(text):
    parser(lexer(text))

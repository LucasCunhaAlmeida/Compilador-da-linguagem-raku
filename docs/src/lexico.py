import ply.lex as lex     #importa módulo ply.lex e o renomeia para lex

# Definindo Tokens e padroes
tokens = ['ADC','DIV','IGUAL_DP','MAIOR_IGL','ADC_DP','SUB','MOD','DIF','IGUAL','DECREMENTO','POW','MT','KMARK','LPAREN','RPAR','COMMA','STRING','FLOAT','INTEGER','BOOLEAN', 'COMMENT','ID','MULT', 'DIVI', 'MENOR','CONC', 'NEGAC','DIVIDE','LCM','LESSEQUAL', 'REPLICARSTRING','UNARYMINUS','SMARTMATCH']

id_reservados = { 
  'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'while': 'WHILE',
    'loop': 'LOOP',
    'next': 'NEXT',
    'last': 'LAST',
    'redo': 'REDO',
    'return': 'RETURN',
    'exit': 'EXIT',
    'break': 'BREAK',
    'my': 'MY',
    'our': 'OUR',
    'has': 'HAS',
    'state': 'STATE',
    'constant': 'CONSTANT',
    'let': 'LET',
    'sub': 'SUB',
    'multi': 'MULTI',
    'only': 'ONLY',
    'Any': 'ANY',
    'Mu': 'MU',
    'Nil': 'NIL',
    'True': 'TRUE',
    'False': 'FALSE',
    'Int': 'INT',
    'Str': 'STR',
    'Pair': 'PAIR',
    'List': 'LIST',
    'Map': 'MAP',
    'Set': 'SET',
    'Bag': 'BAG',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'xor': 'XOR',
    'require': 'REQUIRE',
    'need': 'NEED',
    'use': 'USE',
    'unit': 'UNIT',
    'import': 'IMPORT',
    'export': 'EXPORT',
}

# Adiciona os tokens das palavras reservadas à lista principal de tokens
tokens += list(id_reservados.values())
# Não foi realizado a implementação das seguintes tokens:
# # t_GDC = r'gdc'
# t_EQ = r'eq'
# t_NEQ = r'ne'  
# pois se forem utilizados, o lexer não irá reconhecer as strings como tokens fixos / palavras reservadas,  
# Que vai contra a ideia da linguagem Raku.

t_DIVIDE = r'/'
t_LCM = r'lcm'
t_LESSEQUAL = r'<='
t_REPLICARSTRING = r'x'
t_SMARTMATCH = r'~~'
t_MULT = r'\*'
t_DIVI = r'%%'
t_MENOR = r'<'
t_CONC = r'~'
t_NEGAC = r'!'
t_ADC = r'\+'
t_DIV = r'div'
t_IGUAL_DP = r'=='
t_MAIOR_IGL = r'>='
t_ADC_DP = r'\+\+'
t_SUB = r'-'
t_MOD = r'%'
t_DIF = r'!='
t_IGUAL = r'='
t_DECREMENTO = r'\-\-'
t_POW = r'\*\*'
t_MT = r'>'
t_LPAREN = r'\('
t_RPAR = r'\)'
t_COMMA = r','
t_KMARK = r'\?'
t_ignore = r' \t' # Ignora espaços, tabulações e quebras de linha

def t_UNARYMINUS(t):
  r'-"?\d+"?'
  return t

def t_STRING(t):
  r'\'[^\']*\'|\"[^\"]*\"'
  #r'\'[a-z0-9A-Z_]*\'|"[a-zA-Z0-9_]*"' # | -> pipe = ou
  # t.value = t.value[1:-1] # Retira as aspas da palavras
  return t

def t_BOOLEAN(t):
  r'true|false'
  t.value = t.value.lower() == 'true'
  return t

def t_FLOAT(t):
  r'[0-9]+\.[0-9]+'
  t.value = float(t.value)
  return t

def t_INTEGER(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t

def t_COMMENT(t):
  r'\#.*'
  return None  # Ignora comentários

def t_ID(t):
  r'[a-zA-Z_](?:[a-zA-Z0-9_]*([\'-](?!\d|\Z)[a-zA-Z_][a-zA-Z0-9_]*)?)*'
  t.type = id_reservados.get(t.value, 'ID')  # Verifica se é palavra reservada
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Caractere ilegal '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()  # Cria o analisador léxico
lexer.input("if while str False my our")  # Define a entrada do analisador léxico

# Realizando analise lexica
print('{:10s}{:10s}{:10s}{:10s}'.format("Token", "Lexema", "Linha", "Coluna"))
for tok in lexer:
  print('{:10s}{:10s}{:10s}{:10s}'.format(tok.type, tok.value, str(tok.lineno), str(tok.lexpos))) 

# def ID ( ){
import ply.lex as lex     #importa módulo ply.lex e o renomeia para lex

# Definindo Tokens e padroes
tokens = ['ADC','LIST','DIV','IGUAL_DP','MAIOR_IGL','ADC_DP','SUB','MOD','DIF','IGUAL',
          'DECREMENTO','POW','MAIOR','KMARK','LPAREN','RPAREN','COMMA','STRING','FLOAT',
          'INTEGER','BOOLEAN', 'COMMENT','ID','MULT', 'DIVI', 'MENOR','CONC', 'NEGAC',
          'DIVIDE','LCM','GCD','LESSEQUAL', 'REPLICARSTRING','UNARYMINUS','SMARTMATCH', 'PONTO', 
          'SETA','ABRE_CHAVE', 'FECHA_CHAVE', 'PONTO_VIRGULA', 'AND_S', 'OR_S', 'XOR_S', 'FUNCTION', 'ESCALAR']

id_reservados = { 
  'if': 'IF',
    'else': 'ELSE',
    'times': 'TIMES',
    'elsif': 'ELSIF',
    'while': 'WHILE',
    'loop': 'LOOP',
    'for': 'FOR',
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
    'Map': 'MAP',
    'Set': 'SET',
    'Bag': 'BAG',
    'and': 'AND',   # Tem que retirar?
    'or': 'OR',     # Tem que retirar?
    'not': 'NOT',   
    'xor': 'XOR',   # Tem que retirar?
    'require': 'REQUIRE',
    'need': 'NEED',
    'use': 'USE',
    'unit': 'UNIT',
    'import': 'IMPORT',
    'export': 'EXPORT',
    'push': 'PUSH',
    'unshift': 'UNSHIFT',
    'splice': 'SPLICE',
}

tokens += list(id_reservados.values())

t_LCM = r'lcm'
t_GCD = r'gcd'
t_AND_S = r'&&'
t_OR_S = r'\|\|'
t_XOR_S = r'\^\^'
t_PONTO_VIRGULA = r';'
t_ABRE_CHAVE = r'\{'
t_FECHA_CHAVE = r'\}'
t_SETA = r'->'
t_PONTO = r'\.'
t_DIVIDE = r'/'
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
t_MAIOR = r'>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_KMARK = r'\?'
t_ignore = ' \t' # Ignora espaços, tabulações e quebras de linha

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

def t_ESCALAR(t):
  r'\$[a-zA-Z_](?:[a-zA-Z0-9_]*([\'-](?!\d|\Z)[a-zA-Z_][a-zA-Z0-9_]*)?)*'
  t.type = id_reservados.get(t.value, 'ESCALAR')
  return t

def t_LIST(t):
  r'@[a-zA-Z_](?:[a-zA-Z0-9_]*([\'-](?!\d|\Z)[a-zA-Z_][a-zA-Z0-9_]*)?)*'
  t.type = id_reservados.get(t.value, 'LIST')
  return t

def t_FUNCTION(t):
    r'function'
    return t 
  
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Caractere ilegal '%s'" % t.value[0])
  t.lexer.skip(1)

def t_TIMES(t):
    r'\.times'
    return t

lexer = lex.lex()  # Cria o analisador léxico
lexer.input("if while str False my our ( )")  # Define a entrada do analisador léxico

# Realizando analise lexica
print('{:10s}{:10s}{:10s}{:10s}'.format("Token", "Lexema", "Linha", "Coluna"))
for tok in lexer:
  print('{:10s}{:10s}{:10s}{:10s}'.format(tok.type, tok.value, str(tok.lineno), str(tok.lexpos))) 

# def ID ( ){

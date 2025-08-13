import ply.yacc as yacc
import lexico as lex
tokens = lex.tokens

precedence = ( ## Adicionar as regras da operação aritimetica // Isso é muito importante
    ('left', 'OR_S', 'XOR_S'),
    ('left', 'AND_S'),
    ('left', 'IGUAL_DP', 'DIF'),
    ('left', 'MAIOR', 'MENOR', 'MAIOR_IGL','LESSEQUAL', 'SMARTMATCH'),
    ('right', 'NOT', 'NEGAC'),
)

def p_exp(p):
    '''exp : exp_tip
            
            | exp_logic
            | exp_comp'''
    pass

def p_parametros(p):
    '''parametros : ID
                  | ID COMMA parametros
                  | empty'''
    pass

# Operadores lógicos 
def p_exp_logic(p):
     '''exp_logic : exp AND_S exp
                  | exp OR_S exp
                  | exp XOR_S exp
                  | NOT exp
                  | NEGAC exp'''
     pass

# Operadores de comparação
def p_exp_comp(p):
    '''exp_comp : exp IGUAL_DP exp
                | exp DIF exp
                | exp MAIOR exp
                | exp MENOR exp
                | exp MAIOR_IGL exp
                | exp LESSEQUAL exp
                | exp SMARTMATCH exp'''
    pass

def p_exp_tip(p):
    '''exp_tip : INTEGER
           | FLOAT
           | STRING
           | ID'''
    pass

def p_error(p):
    print(f"Erro de Sintaxe: {p}")


#parte inicial das estruturas de repetição
def p_for(p):
    '''loop : FOR expr SETA ID ABRE_CHAVE comando FECHA_CHAVE''' 
    
def p_ponto_times (p):
    ''' loop : INTEGER PONTO TIMES SETA ID  ABRE_CHAVE comando FECHA_CHAVE '''

def p_while (p):
    ''' loop : WHILE ID LESSEQUAL INTEGER ABRE_CHAVE comando FECHA_CHAVE '''

def p_loop(p):
    '''loop : LOOP LPAREN instrucao PV instrucao PV instrucao RPAREN ABRE_CHAVE comando FECHA_CHAVE'''
    
def p_loop_sem_condicao(p):
    '''loop : LOOP ABRE_CHAVE comando FECHA_CHAVE'''

#Estrutura de uma função
def p_funcao(p):
    '''funcao : FUNCTION ID LPAREN parametros RPAREN ABRE_CHAVE comando FECHA_CHAVE'''

def p_funcao_sem_parametros(p):
    '''funcao : FUNCTION ID LPAREN RPAREN ABRE_CHAVE comando FECHA_CHAVE'''

# Condicionais
def p_condicional1(p):
    '''condicional : IF expressao bloco'''

def p_condicional2(p):
    '''condicional : IF expressao bloco ELSE bloco'''

def p_condicional3(p):
    '''condicional : IF expressao bloco ELSIF expressao bloco'''

def p_condicional4(p):
    '''condicional : IF expressao bloco lista_elsif ELSE bloco'''

def p_lista_esif1(p):
    ''''lista_elsif : ELSIF expressao bloco'''

def p_lista_esif2(p):
    ''''lista_elsif : lista_elsif ELSIF expressao bloco'''

def p_bloco_if1(p):
    '''bloco_if : ABRE_CHAVE declaracoes FECHA_CHAVE'''

def p_bloco_if2(p):
    '''bloco_if : declaracao'''

def p_declaracao1(p):
    '''declaracoes : declaracao'''

def p_declaracao2(p):
    '''declaracoes : declaracoes declaracao'''

def p_declaracao1(p):
    '''declaracao : atribuicao PONTO_VIRGULA'''

def p_declaracao2(p):
    '''declaracao : chamada_funcao PONTO_VIRGULA'''

def p_declaracao3(p):
    '''declaracao : condicional'''

def p_declaracao4(p):
    '''declaracao : loop'''

def p_declaracao5(p):
    '''declaracao : expressao PONTO_VIRGULA'''

def p_declaracao6(p):
    '''declaracao : bloco_if'''

parser = yacc.yacc()

if __name__ == "__main__":
    try:
        result = parser.parse("1 && 2 == aaa == '1' || 2")
        print("Parse ok:", result)
    except Exception as e:
        print("Falha ao fazer parse:", e)

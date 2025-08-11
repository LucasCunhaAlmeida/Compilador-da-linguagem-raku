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



parser = yacc.yacc()

if __name__ == "__main__":
    try:
        result = parser.parse("1 && 2 == aaa == '1' || 2")
        print("Parse ok:", result)
    except Exception as e:
        print("Falha ao fazer parse:", e)

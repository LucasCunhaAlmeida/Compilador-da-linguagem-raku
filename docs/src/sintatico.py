import ply.yacc as yacc
import lexico as lex
tokens = lex.tokens

precedence = ( ## Adicionar as regras da operação aritimetica // Isso é muito importante
    ('left', 'OR_S', 'XOR_S'),
    ('left', 'AND_S'),
    ('left', 'IGUAL_DP', 'DIF'),
    ('left', 'MAIOR', 'MENOR', 'MAIOR_IGL', 'LESSEQUAL', 'SMARTMATCH'),
)

def p_exp(p):
    '''exp : exp_tip
            
            | exp_logic
            | exp_comp'''
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

parser = yacc.yacc()

if __name__ == "__main__":
    try:
        result = parser.parse("1 && 2")
        print("Parse ok:", result)
    except Exception as e:
        print("Falha ao fazer parse:", e)
import ply.yacc as yacc
import lexico as lex
tokens = lex.tokens


def p_exp(p):
    '''exp : PONTO_VIRGULA
           | exp_2 '''
    p[0] = p[1]

def p_exp_2(p):
   '''exp_2 : or
            | xor
            | exp_3 '''
   p[0] = p[1]

def p_or(p):
   '''or : exp_2 OR_S exp_3'''
   pass

def p_xor(p):
   '''xor : exp_2 XOR_S exp_3'''
   pass

def p_exp_3(p):
   '''exp_3 : and
            | exp_4 '''
   p[0] = p[1]

def p_and(p):
   '''and : exp_3 AND_S exp_4'''
   pass

def p_exp_4(p):
   '''exp_4 : igual_dp
            | dif
            | maior
            | menor
            | maior_igual
            | menor_igual
            | smartmatch
            | exp_5 '''
   p[0] = p[1]

def p_igual_dp(p):
   '''igual_dp : exp_4 IGUAL_DP exp_5'''
   pass

def p_dif(p):
    '''dif : exp_4 DIF exp_5'''
    pass

def p_maior(p):
   '''maior : exp_4 MAIOR exp_5'''
   pass

def p_menor(p):
   '''menor : exp_4 MENOR exp_5'''
   pass

def p_maior_igual(p):
   '''maior_igual : exp_4 MAIOR_IGL exp_5'''
   pass

def p_menor_igual(p):
   '''menor_igual : exp_4 LESSEQUAL exp_5'''
   pass

def p_smartmatch(p):
   '''smartmatch : exp_4 SMARTMATCH exp_5'''
   pass

def p_exp_5(p):
    '''exp_5 : adicao
             | subtracao
             | conc
             | exp_6 '''
    p[0] = p[1]

def p_adicao(p):
   '''adicao : exp_5 ADC exp_6'''
   pass

def p_subtracao(p):
   '''subtracao : exp_5 SUB exp_6'''
   pass

def p_conc(p):
   '''conc : exp_5 CONC exp_6'''
   pass

def p_exp_6(p):
    '''exp_6 : mult
             | divide
             | div
             | divi
             | mod
             | lcm
             | gcd
             | exp_7'''
    p[0] = p[1]

def p_mult(p):
   '''mult : exp_6 MULT exp_7'''
   pass

def p_divide(p):
   '''divide : exp_6 DIVIDE exp_7'''
   pass

def p_div(p):
   '''div : exp_6 DIV exp_7'''
   pass

def p_divi(p):
   '''divi : exp_6 DIVI exp_7'''
   pass

def p_mod(p):
   '''mod : exp_6 MOD exp_7'''
   pass

def p_lcm(p):
   '''lcm : exp_6 LCM exp_7'''
   pass

def p_gcd(p):
   '''gcd : exp_6 GCD exp_7'''
   pass

def p_exp_7(p):
    '''exp_7 : pow
             | exp_8'''
    p[0] = p[1]

def p_pow(p):
   '''pow : exp_7 POW exp_8'''
   pass

def p_exp_8(p):
    '''exp_8 : not_op
             | not_s
             | exp_9 '''
    p[0] = p[1]

def p_not_op(p):
   '''not_op : NOT exp_8 '''
   pass

def p_not_s(p):
   '''not_s : NEGAC exp_8'''
   pass

def p_exp_9(p):
    '''exp_9 : unario
             | operando'''
    p[0] = p[1]

def p_unario(p):
 '''unario : prefixo_incremento 
           | posfixo_incremento
           | prefixo_decremento
           | posfixo_decremento '''
 p[0] = p[1]

def p_prefixo_incremento(p):
   '''prefixo_incremento : ADC_DP ID'''
   pass

def p_posfixo_incremento(p):
    '''posfixo_incremento : ID ADC_DP'''
    pass

def p_prefixo_decremento(p):
   '''prefixo_decremento : DECREMENTO ID'''
   pass

def p_posfixo_decremento(p):
    '''posfixo_decremento : ID DECREMENTO'''
    pass

def p_operando(p):
    '''operando : parenteses
                | chaves
                | tipo '''
    p[0] = p[1]

def p_parentese(p):
   '''parenteses : LPAREN exp RPAREN'''
   pass

def p_chaves(p):
   '''chaves : ABRE_CHAVE exp FECHA_CHAVE'''
   pass

# Tipo 

def p_tipo(p):
    '''tipo : inteiro
           | float
           | string
           | boolean
           | id'''
    p[0] = p[1]

def p_inteiro(p):
   '''inteiro : INT '''
   p[0] = p[1]

def p_float(p):
   '''float : FLOAT'''
   p[0] = p[1]

def p_string(p):
    '''string : STRING
              | STR'''
    p[0] = p[1]

def p_boolean(p):
   '''boolean : BOOLEAN'''
   p[0] = p[1]

def p_id(p):
   '''id : ID'''
   p[0] = p[1]

def p_error(p):
    print(f"Erro de Sintaxe: {p}")

# Declarações de variáveis escalares e listas
def p_declaracao_escalar(p):
  'declaracao_escalar : ESCALAR IGUAL valor'

def p_declaracao_lista(p):
  'declaracao_lista : LIST IGUAL lista_valores'

def p_valor(p):
  '''valor : INT
            | FLOAT
            | STRING
            | BOOLEAN'''

def p_lista_valores(p):
  '''lista_valores : lista_valores COMMA valor
                   | valor'''
# Talvez seja necessário mais algumas mudanças

#parte inicial das estruturas de repetição
#instrucao coloquei essa senquencia, depois vou verificar de novo q my $a = 0
#id coloquei como a variavel
def p_for(p):
    '''loop : FOR expr SETA ID ABRE_CHAVE comando FECHA_CHAVE''' 
    p[0] = loopFor(p[2], p[4], p[6])
    
def p_ponto_times (p):
    ''' loop : INTEGER PONTO TIMES SETA ID  ABRE_CHAVE comando FECHA_CHAVE '''
    p[0] = loopTimes(p[1], p[5], p[7])

def p_while (p):
    ''' loop : WHILE ID LESSEQUAL INTEGER ABRE_CHAVE comando FECHA_CHAVE '''
    p[0] = loopWhile(p[2], p[4], p[6])

def p_loop(p):
    '''loop : LOOP LPAREN instrucao PV instrucao PV instrucao RPAREN ABRE_CHAVE comando FECHA_CHAVE'''
    p[0] = loopRepeticao(p[3], p[5], p[7], p[9])

def p_loop_sem_condicao(p):
    '''loop : LOOP ABRE_CHAVE comando FECHA_CHAVE'''
    p[0] =  loopSemCondicao(p[3])

#Estrutura de uma função
def p_funcao(p):
    '''funcao : FUNCTION ID LPAREN parametros RPAREN ABRE_CHAVE comando FECHA_CHAVE'''
    p[0] = CompoundFuncao(p[4],p[7])

def p_funcao_sem_parametros(p):
    '''funcao : FUNCTION ID LPAREN RPAREN ABRE_CHAVE comando FECHA_CHAVE'''
    p[0] = CompoundFuncaoSemParametros(p[6])

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

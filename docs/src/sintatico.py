import ply.yacc as yacc
import lexico as lex
import sintaxeabstrata as sa
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
   p[0] = sa.ExpressaoOR(p[1], p[3])

def p_xor(p):
   '''xor : exp_2 XOR_S exp_3'''
   p[0] = sa.ExpressaoXOR(p[1], p[3])

def p_exp_3(p):
   '''exp_3 : and
            | exp_4 '''
   p[0] = p[1]

def p_and(p):
   '''and : exp_3 AND_S exp_4'''
   p[0] = sa.ExpressaoAND(p[1], p[3])

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
   p[0] = sa.ExpressaoIGUAL_DP(p[1], p[3])

def p_dif(p):
    '''dif : exp_4 DIF exp_5'''
    p[0] = sa.ExpressaoDIF(p[1], p[3])

def p_maior(p):
   '''maior : exp_4 MAIOR exp_5'''
   p[0] = sa.ExpressaoMAIOR(p[1], p[3])

def p_menor(p):
   '''menor : exp_4 MENOR exp_5'''
   p[0] = sa.ExpressaoMENOR(p[1], p[3])

def p_maior_igual(p):
   '''maior_igual : exp_4 MAIOR_IGL exp_5'''
   p[0] = sa.ExpressaoMAIOR_IGUAL(p[1], p[3])

def p_menor_igual(p):
   '''menor_igual : exp_4 LESSEQUAL exp_5'''
   p[0] = sa.ExpressaoMENOR_IGUAL(p[1], p[3])

def p_smartmatch(p):
   '''smartmatch : exp_4 SMARTMATCH exp_5'''
   p[0] = sa.ExpressaoSMARTMATCH(p[1], p[3])

def p_exp_5(p):
    '''exp_5 : adicao
             | subtracao
             | conc
             | exp_6 '''
    p[0] = p[1]

def p_adicao(p):
   '''adicao : exp_5 ADC exp_6'''
   p[0] = sa.ExpressaoADICAO(p[1], p[3])

def p_subtracao(p):
   '''subtracao : exp_5 SUB exp_6'''
   p[0] = sa.ExpressaoSUBTRACAO(p[1], p[3])

def p_conc(p):
   '''conc : exp_5 CONC exp_6'''
   p[0] = sa.ExpressaoCONCATENACAO(p[1], p[3])

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
   p[0] = sa.ExpressaoMULTIPLICACAO(p[1], p[3])

def p_divide(p):
   '''divide : exp_6 DIVIDE exp_7'''
   p[0] = sa.ExpressaoDIVISAO(p[1], p[3])

def p_div(p):
   '''div : exp_6 DIV exp_7'''
   p[0] = sa.ExpressaoDIVISAO_INTEIRA(p[1], p[3])

def p_divi(p):
   '''divi : exp_6 DIVI exp_7'''
   p[0] = sa.ExpressaoDIVISIBILIDADE(p[1], p[3])

def p_mod(p):
   '''mod : exp_6 MOD exp_7'''
   p[0] = sa.ExpressaoMOD(p[1], p[3])

def p_lcm(p):
   '''lcm : exp_6 LCM exp_7'''
   p[0] = sa.ExpressaoLCM(p[1], p[3])

def p_gcd(p):
   '''gcd : exp_6 GCD exp_7'''
   p[0] = sa.ExpressaoGCD(p[1], p[3])

def p_exp_7(p):
    '''exp_7 : pow
             | exp_8'''
    p[0] = p[1]

def p_pow(p):
   '''pow : exp_7 POW exp_8'''
   p[0] = sa.ExpressaoPOW(p[1], p[3])

def p_exp_8(p):
    '''exp_8 : not_op
             | not_s
             | exp_9 '''
    p[0] = p[1]

def p_not_op(p):
   '''not_op : NOT exp_8 '''
   p[0] = sa.ExpressaoNOT_OPERADOR(p[2])

def p_not_s(p):
   '''not_s : NEGAC exp_8'''
   p[0] = sa.Expressao_NOT_SIMBULO(p[2])

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
   p[0] = sa.Expressao_PREFIXO_INCREMENTO(p[2]) # ARQUI É 2 OU 1

def p_posfixo_incremento(p):
    '''posfixo_incremento : ID ADC_DP'''
    p[0] = sa.Expressao_POSFIXO_INCREMENTO(p[1]) 

def p_prefixo_decremento(p):
   '''prefixo_decremento : DECREMENTO ID'''
   p[0] = sa.Expressao_PREFIXO_DECREMENTO(p[2]) # AQUI É 2 OU 1

def p_posfixo_decremento(p):
    '''posfixo_decremento : ID DECREMENTO'''
    p[0] = sa.Expressao_POSFIXO_DECREMENTO(p[1]) 

def p_operando(p):
    '''operando : parenteses
                | tipo '''
    p[0] = p[1]

def p_parenteses(p):
   '''parenteses : LPAREN exp RPAREN'''
   p[0] = sa.Expressao_PARENTESES(p[2]) # PRO QUE ESTÁ DANDO ERRO DE SINTAXE

# Tipo 

def p_tipo(p):          # TEM QUE SER VALORES CONSTANTES
    '''tipo : inteiro
           | float
           | string
           | boolean
           | id'''
    p[0] = p[1]

def p_inteiro(p):
   '''inteiro : INTEGER
              | INT '''
   p[0] = sa.Expressao_VALOR(p[1], 'int')

def p_float(p):
   '''float : FLOAT'''
   p[0] = sa.Expressao_VALOR(p[1], 'float')

def p_string(p):
    '''string : STRING
              | STR'''
    p[0] = sa.Expressao_VALOR(p[1], 'str')

def p_boolean(p):
   '''boolean : BOOLEAN'''
   p[0] = sa.Expressao_VALOR(p[1], 'boolean')

def p_id(p):
   '''id : ID'''
   p[0] = sa.Expressao_VALOR(p[1], 'ID')

# ... (toda a sua gramática de expressões de p_exp até p_id está ótima) ...


def p_error(p):
    if p:
        print(f"Erro de Sintaxe no token '{p.value}' (tipo: {p.type}) na linha {p.lineno}")
    else:
        print("Erro de Sintaxe: Fim inesperado do arquivo.")

# --- DECLARAÇÕES DE VARIÁVEIS ---
def p_declaracao_escalar(p):
  '''declaracao : ESCALAR IGUAL valor PONTO_VIRGULA''' # Adicionado PONTO_VIRGULA e movido para 'declaracao'
  # Aqui você criaria um nó na AST para a declaração

def p_declaracao_lista(p):
  '''declaracao : LIST IGUAL lista_valores PONTO_VIRGULA''' # Adicionado PONTO_VIRGULA e movido para 'declaracao'
  # Aqui você criaria um nó na AST para a declaração

def p_valor_numerico(p):
  '''valor : INTEGER
           | FLOAT'''
  p[0] = p[1]

def p_valor_texto(p):
  '''valor : STRING
           | BOOLEAN'''
  p[0] = p[1]

def p_lista_valores_recursiva(p):
  '''lista_valores : lista_valores COMMA valor'''

def p_lista_valores_base(p):
  '''lista_valores : valor'''

# --- ESTRUTURAS DE REPETIÇÃO ---
def p_loop_for(p):
    '''loop : FOR exp_2 SETA ESCALAR ABRE_CHAVE comando FECHA_CHAVE''' 
    p[0] = sa.LoopFor(p[2], p[4], p[6])
    
def p_loop_times(p):
    # O nome da função não pode ter espaço. Usei 'loop_times'.
    '''loop : INTEGER PONTO TIMES SETA ESCALAR ABRE_CHAVE comando FECHA_CHAVE'''
    p[0] = sa.LoopTimes(p[1], p[5], p[7])

def p_loop_while(p):
    # Alterei para usar exp_2 para consistência
    '''loop : WHILE exp_2 ABRE_CHAVE comando FECHA_CHAVE'''
    p[0] = sa.LoopWhile(p[2], None, p[4])

def p_loop_loop(p):
    '''loop : LOOP LPAREN instrucao PONTO_VIRGULA instrucao PONTO_VIRGULA instrucao RPAREN ABRE_CHAVE comando FECHA_CHAVE'''
    p[0] = sa.LoopRepeticao(p[3], p[5], p[7], p[10])

def p_loop_sem_condicao(p):
    '''loop : LOOP ABRE_CHAVE comando FECHA_CHAVE'''
    p[0] = sa.LoopSemCondicao(p[3])

# --- FUNÇÕES ---
def p_funcao_com_params(p):
    '''funcao : FUNCTION ID LPAREN parametros RPAREN ABRE_CHAVE comando FECHA_CHAVE'''
    p[0] = sa.CompoundFuncao(p[2], p[4], p[7])

def p_funcao_sem_params(p):
    '''funcao : FUNCTION ID LPAREN RPAREN ABRE_CHAVE comando FECHA_CHAVE'''
    p[0] = sa.CompoundFuncaoSemParametros(p[2], p[6])

# --- REGRAS QUE FALTAVAM ---
# Definição de 'parametros'
def p_parametros_recursivo(p):
    '''parametros : parametros COMMA ID'''
def p_parametros_base(p):
    '''parametros : ID'''

# Definição de 'comando' como uma ou mais declarações
def p_comando(p):
    '''comando : declaracoes'''
    p[0] = p[1]

# Definição de 'instrucao' (usada no loop estilo C)
def p_instrucao_atribuicao(p):
    '''instrucao : atribuicao'''
    p[0] = p[1]
def p_instrucao_expressao(p):
    '''instrucao : exp_2'''
    p[0] = p[1]

# Definição de 'atribuicao'
def p_atribuicao(p):
    '''atribuicao : ID IGUAL exp_2'''

# Definição de 'chamada_funcao'
def p_chamada_funcao(p):
    # Adicione regras para parâmetros se necessário
    '''chamada_funcao : ID LPAREN RPAREN'''

# --- CONDICIONAIS (COM NOMES ÚNICOS) ---
def p_condicional_if(p):
    '''condicional : IF exp_2 bloco'''

def p_condicional_if_else(p):
    '''condicional : IF exp_2 bloco ELSE bloco'''

def p_condicional_if_elsif(p):
    '''condicional : IF exp_2 bloco lista_elsif'''

def p_condicional_if_elsif_else(p):
    '''condicional : IF exp_2 bloco lista_elsif ELSE bloco'''

def p_lista_elsif_base(p):
    '''lista_elsif : ELSIF exp_2 bloco'''

def p_lista_elsif_recursiva(p):
    '''lista_elsif : lista_elsif ELSIF exp_2 bloco'''

# --- ESTRUTURA DE BLOCOS E DECLARAÇÕES (COM NOMES ÚNICOS) ---
def p_bloco_chaves(p):
    '''bloco : ABRE_CHAVE declaracoes FECHA_CHAVE'''
    p[0] = p[2]

def p_bloco_declaracao_unica(p):
   '''bloco : declaracao'''
   p[0] = p[1]

def p_declaracoes_base(p):
    '''declaracoes : declaracao'''

def p_declaracoes_recursiva(p):
    '''declaracoes : declaracoes declaracao'''

def p_declaracao_de_atribuicao(p):
    '''declaracao : atribuicao PONTO_VIRGULA'''

def p_declaracao_de_chamada_funcao(p):
    '''declaracao : chamada_funcao PONTO_VIRGULA'''

def p_declaracao_de_condicional(p):
   '''declaracao : condicional'''

def p_declaracao_de_loop(p):
    '''declaracao : loop'''

def p_declaracao_de_expressao(p):
    '''declaracao : exp_2 PONTO_VIRGULA'''

def p_declaracao_de_bloco(p):
    '''declaracao : bloco'''

# CONSTRUÇÃO DO PARSER
parser = yacc.yacc()

if __name__ == "__main__":
    # Teste com uma string que usa a sua gramática
    # Exemplo: my $var = 10;
    # Exemplo: for 1..10 -> $i { }
    # A string que você estava usando para testar não parece ser válida para a gramática
    # data = "my $var = 10;"#
    data = "1 + 2 * (3 - 1)"
    print(f"Analisando a entrada: {data}")
    try:
        # É crucial passar o lexer para o parser
        result = parser.parse(data, lexer=lex.lexer, debug = True)
        print("Análise sintática bem-sucedida!")
        print("Resultado (Árvore Sintática Abstrata):", result)
    except Exception as e:
        print("Falha ao fazer a análise sintática:", e)

import ply.yacc as yacc
import lexico as lex
import sintaxeabstrata as sa
tokens = lex.tokens

def p_programa(p):
    '''programa : declaracoes'''
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
                | completo '''
    p[0] = p[1]

def p_parenteses(p):
   '''parenteses : LPAREN exp_2 RPAREN'''
   p[0] = sa.Expressao_PARENTESES(p[2]) # PRO QUE ESTÁ DANDO ERRO DE SINTAXE

# Tipo 
def p_completo(p):
   '''completo : tipo
               | escalar '''
   p[0] = p[1]

def p_tipo(p):
    '''tipo : inteiro
             | float
             | string
             | boolean  '''
    p[0] = p[1]

def p_tipo_opicional(p):
   '''tipo_opicional : tipo_opicional_int
                     | STR 
                     | empty'''
   p[0] = p[1]

def p_tipo_opicional_int(p):
   '''tipo_opicional_int : INT '''
   p[0] = sa.Expressao_TIPO('int')

def p_empty(p):
   '''empty : '''
   p[0] = []

def p_inteiro(p):
   '''inteiro : INTEGER '''
   p[0] = sa.Expressao_VALOR(p[1], 'int')

def p_float(p):
   '''float : FLOAT '''
   p[0] = sa.Expressao_VALOR(p[1], 'float')

def p_string(p):
    '''string : STRING '''
    p[0] = sa.Expressao_VALOR(p[1], 'str')

def p_boolean(p):
   '''boolean : BOOLEAN'''
   p[0] = sa.Expressao_VALOR(p[1], 'boolean')

def p_escalar(p):
   '''escalar : ESCALAR'''
   p[0] = sa.Expressao_VALOR(p[1], 'ESCALAR')

# ... (toda a sua gramática de expressões de p_exp até p_id está ótima) ...

def p_error(p):
    if p:
        print(f"Erro de Sintaxe no token '{p.value}' (tipo: {p.type}) na linha {p.lineno}")
    else:
        print("Erro de Sintaxe: Fim inesperado do arquivo.")

# --- DECLARAÇÕES DE VARIÁVEIS ---
def p_declaracao_escalar_MY(p):
  '''declaracao_escalar_MY : MY tipo_opicional ESCALAR IGUAL tipo PONTO_VIRGULA declaracoes_para_funcoes''' # Problema com o ponto e virgula
  pass

def p_declaracao_escalar_OUR(p):
  '''declaracao_escalar_OUR : OUR tipo_opicional ESCALAR IGUAL tipo PONTO_VIRGULA declaracoes_para_funcoes''' # Problema com o ponto e virgula
  pass

def p_declaracao_lista(p):
  '''declaracao_lista : LIST IGUAL lista_valores PONTO_VIRGULA declaracoes_para_funcoes'''
  pass

def p_declaracao_lista_my(p):
  '''declaracao_lista_MY : MY LIST IGUAL lista_valores PONTO_VIRGULA declaracoes_para_funcoes''' 
  pass

def p_declaracao_lista_our(p):
  '''declaracao_lista_OUR : OUR LIST IGUAL lista_valores PONTO_VIRGULA declaracoes_para_funcoes'''
  pass

  # Aqui você criaria um nó na AST para a declaração

def p_lista_valores(p):
   '''lista_valores : lista_valores COMMA tipo 
                    | lista_valores_base '''

def p_lista_valores_base(p):
  '''lista_valores_base : tipo'''
  pass

# --- ESTRUTURAS DE REPETIÇÃO ---
def p_loop_for(p):
    '''loop_for : FOR inteiro INTERPOLACAO inteiro SETA ESCALAR ABRE_CHAVE declaracoes FECHA_CHAVE declaracoes_para_funcoes''' 
    p[0] = sa.LoopFor(p[2], p[4], p[6])
    
def p_loop_times(p):
    # O nome da função não pode ter espaço. Usei 'loop_times'.
    '''loop_times : INTEGER TIMES SETA ESCALAR ABRE_CHAVE declaracoes FECHA_CHAVE declaracoes_para_funcoes'''
    p[0] = sa.LoopTimes(p[1], p[5], p[7])

def p_loop_while(p):
    # Alterei para usar exp_2 para consistência
    '''loop_while : WHILE exp_2 ABRE_CHAVE declaracoes FECHA_CHAVE declaracoes_para_funcoes'''
    p[0] = sa.LoopWhile(p[2], p[4])

def p_loop(p):
    # Renomeei para evitar conflito com p_loop_for, etc.
    '''loop : LOOP LPAREN atribuicao PONTO_VIRGULA exp_2 PONTO_VIRGULA exp_2 RPAREN ABRE_CHAVE declaracoes FECHA_CHAVE declaracoes_para_funcoes'''
    p[0] = sa.LoopRepeticao(p[3], p[5], p[7], p[10])

def p_loop_sem_condicao(p):
    '''loop_sem_condicao : LOOP ABRE_CHAVE declaracoes FECHA_CHAVE declaracoes_para_funcoes'''
    p[0] = sa.LoopSemCondicao(p[3])

# --- SAY ---

def p_say(p):
    '''say : SAY exp_2 PONTO_VIRGULA declaracoes_para_funcoes'''
    p[0] = p[2]  # ✅ Usar 'sa.SAY' em vez de 'sa.Say'

# --- FUNÇÕES ---

def p_funcao_com_params(p):
    '''funcao_com_params : FUNCTION ID LPAREN parametros RPAREN ABRE_CHAVE declaracoes_para_funcoes FECHA_CHAVE declaracoes'''
    p[0] = sa.CompoundFuncao(p[2], p[4], p[6])

def p_funcao_sem_params(p):
    '''funcao_sem_params : FUNCTION ID LPAREN RPAREN ABRE_CHAVE declaracoes_para_funcoes FECHA_CHAVE declaracoes'''
    p[0] = sa.CompoundFuncaoSemParametros(p[2], p[6])

# --- REGRAS QUE FALTAVAM ---
# Definição de 'parametros'

def p_parametros(p):
    '''parametros : ESCALAR
                  | parametros COMMA ESCALAR '''
    if len(p) == 2:
        p[0] = [p[1]] # -> Com um unico parametro
    else:
        p[0] = p[1] + [p[3]] # -> Com varios parametros

# Definição de 'atribuicao'
def p_atribuicao(p):
    '''atribuicao : ESCALAR IGUAL exp_2'''
    pass

# Definição de 'chamada_funcao'

def p_chamada_funcao(p):
    # Adicione regras para parâmetros se necessário
    '''chamada_funcao : ID LPAREN chamada_funcao_auxiliar RPAREN declaracoes'''
    p[0] = sa.CHAMADA_FUNCAO(p[1], p[3])

def p_chamada_funcao_sem_parametro(p):
    '''chamada_funcao_sem_parametro : ID LPAREN RPAREN declaracoes'''
    p[0] = sa.CHAMADA_FUNCAO_SEM_PARAMETRO(p[1])

def p_chamada_funcao_auxiliar(p):
    '''chamada_funcao_auxiliar : chamada_funcao_auxiliar COMMA completo
                               | completo ''' 
    if len(p) == 2:
        p[0] = [p[1]] # -> Com um unico parametro
    else:
        p[0] = p[1] + [p[3]] # -> Com varios parametros

# --- CONDICIONAIS (COM NOMES ÚNICOS) ---
def p_condicional_if(p):
    '''condicional : IF exp_2 bloco declaracoes'''

def p_condicional_if_else(p):
    '''condicional : IF exp_2 bloco ELSE bloco declaracoes'''

def p_condicional_if_elsif(p):
    '''condicional : IF exp_2 bloco lista_elsif declaracoes'''

def p_condicional_if_elsif_else(p):
    '''condicional : IF exp_2 bloco lista_elsif ELSE bloco declaracoes'''

def p_lista_elsif_base(p):
    '''lista_elsif : ELSIF exp_2 bloco'''

def p_lista_elsif_recursiva(p):
    '''lista_elsif : lista_elsif ELSIF exp_2 bloco'''

# --- ESTRUTURA DE BLOCOS E DECLARAÇÕES (COM NOMES ÚNICOS) ---
def p_bloco_chaves(p):
    '''bloco : ABRE_CHAVE declaracoes FECHA_CHAVE'''
    p[0] = p[2]

# Se pensar em mecher nessa função vai arrumar muito problema

# def p_bloco_declaracao_unica(p): 
#    '''bloco : declaracoes'''
#    p[0] = p[1]

def p_delaracoes(p):
    '''declaracoes : declaracao_de_funcao
                   | declaracoes_para_funcoes '''
    p[0] = p[1]

def p_declaracoes_para_funcoes(p):
    '''declaracoes_para_funcoes : declaracao_de_atribuicao
                        | say
                        | declaracao_de_chamada_funcao
                        | declaracao_de_condicional
                        | declaracao_loop
                        | declaracao_de_expressao 
                        | declaracao_bloco
                        | declaracao_escalar_MY
                        | declaracao_escalar_OUR
                        | declaracao_lista
                        | declaracao_lista_MY
                        | declaracao_lista_OUR
                        | empty '''
    p[0] = p[1]
    
def p_declaracao_de_atribuicao(p):
    '''declaracao_de_atribuicao : atribuicao PONTO_VIRGULA'''

def p_declaracao_de_funcao(p):
    '''declaracao_de_funcao : funcao_com_params 
                            | funcao_sem_params '''
    p[0] = p[1]

def p_declaracao_de_chamada_funcao(p):
    '''declaracao_de_chamada_funcao : chamada_funcao PONTO_VIRGULA
                                    | chamada_funcao_sem_parametro PONTO_VIRGULA'''
    p[0] = p[1]

def p_declaracao_de_condicional(p):
   '''declaracao_de_condicional : condicional'''

def p_declaracao_de_loop(p):
    '''declaracao_loop : loop
                       | loop_for
                       | loop_times 
                       | loop_while
                       | loop_sem_condicao '''

def p_declaracao_de_expressao(p):
    '''declaracao_de_expressao : exp_2 PONTO_VIRGULA'''

def p_declaracao_de_bloco(p):
    '''declaracao_bloco : bloco'''

# CONSTRUÇÃO DO PARSER

    # Teste com uma string que usa a sua gramática
    # Exemplo: my $var = 10;
    # Exemplo: for 1..10 -> $i { }
    # A string que você estava usando para testar não parece ser válida para a gramática
    # data = "my $var = 10;"#

# Teste nos outros computadores 

# parser = yacc.yacc()

# if __name__ == "__main__":
#     try:
#         result = parser.parse("my Int $var = 10; my Str $var = 10;")
#         print("Parse ok:", result)
#     except Exception as e:
#         print("Falha ao fazer parse:", e)

# Utilizando caminhos no linux

def main():

    caminho = "./main.raku"

    try:
        with open(caminho, "r", encoding="utf-8") as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho}' não encontrado.")
        sys.exit(1)

    # Cria o parser
    parser = yacc.yacc()  # parser já construído no sintaxe.py
    result = parser.parse(codigo, lexer=lex.lexer)

    print("\n=== Resultado do Parser ===")
    print(result)  # aqui você vai ver a AST retornada

if __name__ == "__main__":
    main()

import ply.yacc as yacc
import lexico as lex
import sintaxeabstrata as sa
import sys
import os
from visitor import visitor

tokens = lex.tokens

def p_programa(p):
    '''programa : lista_declaracoes'''
    p[0] = p[1]

def p_lista_declaracoes(p): 
    '''lista_declaracoes : lista_declaracoes declaracoes
                         | declaracoes'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_lista_declaracoes_para_funcoes(p): 
    '''lista_declaracoes_para_funcoes : lista_declaracoes declaracoes_para_funcoes
                                      | declaracoes_para_funcoes'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

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
   '''prefixo_incremento : ADC_DP escalar'''
   p[0] = sa.Expressao_PREFIXO_INCREMENTO(sa.Expressao_VALOR(p[2], 'ESCALAR'))

def p_posfixo_incremento(p):
    '''posfixo_incremento : escalar ADC_DP'''
    p[0] = sa.Expressao_POSFIXO_INCREMENTO(sa.Expressao_VALOR(p[1], 'ESCALAR')) 

def p_prefixo_decremento(p):
   '''prefixo_decremento : DECREMENTO escalar'''
   p[0] = sa.Expressao_PREFIXO_DECREMENTO(sa.Expressao_VALOR(p[2], 'ESCALAR'))

def p_posfixo_decremento(p):
    '''posfixo_decremento : escalar DECREMENTO'''
    p[0] = sa.Expressao_POSFIXO_DECREMENTO(sa.Expressao_VALOR(p[1], 'ESCALAR')) 

def p_operando(p):
    '''operando : parenteses
                | completo '''
    p[0] = p[1]

def p_parenteses(p):
   '''parenteses : LPAREN exp_2 RPAREN'''
   p[0] = sa.Expressao_PARENTESES(p[2])

# Tipo 
def p_completo(p):
   '''completo : tipo
               | chamada_funcao
               | chamada_funcao_sem_parametro
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
                     | tipo_opicional_str 
                     | empty'''
   p[0] = p[1]

def p_tipo_opicional_int(p):
   '''tipo_opicional_int : INT '''
   p[0] = sa.Expressao_TIPO('int')

def p_tipo_opicional_str(p):
   '''tipo_opicional_str : STR '''
   p[0] = sa.Expressao_TIPO('str')

def p_empty(p):
   '''empty : '''
   p[0] = None

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
  '''declaracao_escalar_MY : MY tipo_opicional ESCALAR IGUAL exp_2 PONTO_VIRGULA''' # Problema com o ponto e virgula
  p[0] = sa.DeclaracaoEscalarMY(p[2], p[3], p[5])

def p_declaracao_escalar_OUR(p):
  '''declaracao_escalar_OUR : OUR ESCALAR IGUAL exp_2 PONTO_VIRGULA''' # Problema com o ponto e virgula
  p[0] = sa.DeclaracaoEscalarOUR(p[2], p[4])

def p_declaracao_lista(p):
  '''declaracao_lista : LIST IGUAL lista_valores PONTO_VIRGULA'''
  p[0] = sa.DeclaracaoLista(p[1], p[3])

def p_declaracao_lista_my(p):
  '''declaracao_lista_MY : MY LIST IGUAL lista_valores PONTO_VIRGULA''' 
  p[0] = sa.DeclaracaoListaMY(p[2], p[4])

def p_declaracao_lista_our(p):
  '''declaracao_lista_OUR : OUR LIST IGUAL lista_valores PONTO_VIRGULA'''
  p[0] = sa.DeclaracaoListaOUR(p[2], p[4])

  # Aqui você criaria um nó na AST para a declaração

def p_lista_valores(p):
   '''lista_valores : lista_valores COMMA tipo 
                    | lista_valores_base '''
   if len(p) == 4:
        p[0] = p[1] + [p[3]]
   else:
        p[0] = p[1]

def p_lista_valores_base(p):
  '''lista_valores_base : tipo'''
  p[0] = [p[1]]

# --- ESTRUTURAS DE REPETIÇÃO ---

def p_loop_for(p):
    '''loop_for : FOR inteiro INTERPOLACAO inteiro SETA ESCALAR ABRE_CHAVE lista_declaracoes FECHA_CHAVE''' 
    p[0] = sa.LoopFor(p[2], p[4], p[6])

def p_loop_for_com_lista(p):
    '''loop_for_com_lista : FOR LIST SETA ESCALAR ABRE_CHAVE lista_declaracoes FECHA_CHAVE''' 
   # p[0] = sa.LoopFor(p[2], p[4])
    p[0] = sa.LoopFor(p[2], p[4], p[6])

def p_loop_while(p):
    # Alterei para usar exp_2 para consistência
    '''loop_while : WHILE exp_2 ABRE_CHAVE lista_declaracoes FECHA_CHAVE'''
    p[0] = sa.LoopWhile(p[2], p[4])

def p_loop(p):
    # Renomeei para evitar conflito com p_loop_for, etc.
    '''loop : LOOP LPAREN declaracao_escalar_MY exp_2 PONTO_VIRGULA atribuicao RPAREN ABRE_CHAVE lista_declaracoes FECHA_CHAVE '''
    p[0] = sa.LoopRepeticao(p[3], p[5], p[7], p[10])

def p_loop_sem_condicao(p):
    '''loop_sem_condicao : LOOP ABRE_CHAVE lista_declaracoes FECHA_CHAVE'''
    p[0] = sa.LoopSemCondicao(p[3])

# --- SAY ---

def p_say(p):
    '''say : SAY say_func PONTO_VIRGULA '''
    p[0] = p[2]

def p_say_func(p):
    '''say_func : exp_2
                | LIST'''
    p[0] = p[1]
# --- FUNÇÕES ---

def p_funcao_com_params(p):
    '''funcao_com_params : FUNCTION ID LPAREN parametros RPAREN ABRE_CHAVE lista_declaracoes_para_funcoes FECHA_CHAVE'''
    p[0] = sa.CompoundFuncao(p[2], p[4], p[6])

def p_funcao_sem_params(p):
    '''funcao_sem_params : FUNCTION ID LPAREN RPAREN ABRE_CHAVE lista_declaracoes_para_funcoes FECHA_CHAVE'''
    p[0] = sa.CompoundFuncaoSemParametros(p[2], p[6])

# --- REGRAS QUE FALTAVAM ---
# Definição de 'parametros'

def p_parametros(p):
    '''parametros : tipo_opicional ESCALAR
                  | parametros COMMA tipo_opicional ESCALAR '''
    if len(p) == 3:
        p[0] = [p[2]] # -> Com um unico parametro
    else:
        p[0] = p[1] + [p[4]] # -> Com varios parametros

# Definição de 'atribuicao'
def p_atribuicao(p):
    '''atribuicao : ESCALAR IGUAL exp_2'''
    p[0] = sa.Atribuicao(p[1], p[3])

# Definição de 'chamada_funcao'

def p_chamada_funcao(p):
    # Adicione regras para parâmetros se necessário
    '''chamada_funcao : ID LPAREN chamada_funcao_auxiliar RPAREN'''
    p[0] = sa.CHAMADA_FUNCAO(p[1], p[3])

def p_chamada_funcao_sem_parametro(p):
    '''chamada_funcao_sem_parametro : ID LPAREN RPAREN'''
    p[0] = sa.CHAMADA_FUNCAO_SEM_PARAMETRO(p[1])

def p_chamada_funcao_auxiliar(p):
    '''chamada_funcao_auxiliar : chamada_funcao_auxiliar COMMA exp_2
                               | exp_2 ''' 
    if len(p) == 2:
        p[0] = [p[1]] # -> Com um unico parametro
    else:
        p[0] = p[1] + [p[3]] # -> Com varios parametros

# --- CONDICIONAIS (COM NOMES ÚNICOS) ---
def p_condicional_if(p):
    '''condicional : IF exp_2 bloco'''
    p[0] = sa.CondicionalIf(p[2], p[3])

def p_condicional_if_else(p):
    '''condicional : IF exp_2 bloco ELSE bloco'''
    p[0] = sa.CondicionalIfElse(p[2], p[3], p[5])

def p_condicional_if_elsif(p):
    '''condicional : IF exp_2 bloco lista_elsif'''
    p[0] = sa.CondicionalIfElsif(p[2], p[3], p[4])

def p_condicional_if_elsif_else(p):
    '''condicional : IF exp_2 bloco lista_elsif ELSE bloco'''
    p[0] = sa.CondicionalIfElsifElse(p[2], p[3], p[4], p[6])

def p_lista_elsif_base(p):
    '''lista_elsif : ELSIF exp_2 bloco'''
    p[0] = [sa.Elsif(p[2], p[3])]

def p_lista_elsif_recursiva(p):
    '''lista_elsif : lista_elsif ELSIF exp_2 bloco'''
    p[0] = p[1] + [sa.Elsif(p[3], p[4])]

# --- ESTRUTURA DE BLOCOS E DECLARAÇÕES (COM NOMES ÚNICOS) ---
def p_bloco_chaves(p):
    '''bloco : ABRE_CHAVE lista_declaracoes FECHA_CHAVE'''
    p[0] = p[2]


def p_declaracoes(p):
    '''declaracoes : declaracoes_para_funcoes
                   | declaracao_multi
                   | declaracao_multi_sem_par
                   | declaracao_only
                   | declaracao_only_sem_par
                   | declaracao_de_funcao'''
    p[0] = p[1]

def p_declaracoes_para_funcoes(p):
    '''declaracoes_para_funcoes : declaracao_de_atribuicao
                        | say
                        | comentario
                        | declaracao_de_condicional
                        | declaracao_loop
                        | declaracao_de_expressao 
                        | declaracao_bloco
                        | declaracao_escalar_MY
                        | declaracao_escalar_OUR
                        | declaracao_lista
                        | declaracao_lista_MY
                        | declaracao_lista_OUR 
                        | declaracao_de_controle_de_fluxo
                        | declaracao_de_controle_de_escopo
                        | declaracao_de_controle_de_modularizacao
                        | declaracao_de_controle_de_lista'''
    p[0] = p[1]
    
def p_comentario(p):
    '''comentario : COMMENT '''
    p[0] = sa.Comentario(p[1])

def p_declaracao_de_atribuicao(p):
    '''declaracao_de_atribuicao : atribuicao PONTO_VIRGULA'''
    p[0] = p[1]

def p_declaracao_de_funcao(p):
    '''declaracao_de_funcao : funcao_com_params 
                            | funcao_sem_params '''
    p[0] = p[1]

def p_declaracao_de_condicional(p):
   '''declaracao_de_condicional : condicional'''
   p[0] = sa.DeclaracaoCondicional(p[1])

def p_declaracao_de_loop(p):
    '''declaracao_loop : loop
                       | loop_for
                       | loop_for_com_lista 
                       | loop_while
                       | loop_sem_condicao '''
    p[0] = sa.DeclaracaoLoop(p[1])

def p_declaracao_de_expressao(p):
    '''declaracao_de_expressao : exp_2 PONTO_VIRGULA'''
    p[0] = sa.DeclaracaoExpressao(p[1])

def p_declaracao_de_bloco(p):
    '''declaracao_bloco : bloco'''
    p[0] = sa.DeclaracaoBloco(p[1])

def p_declaracao_de_controle_de_fluxo(p):
    '''declaracao_de_controle_de_fluxo : declaracao_break 
                                       | declaracao_exit
                                       | declaracao_last
                                       | declaracao_next
                                       | declaracao_redo
                                       | declaracao_return '''
    p[0] = p[1]

def p_declaracao_de_controle_de_escopo(p):
    '''declaracao_de_controle_de_escopo : declaracao_constant 
                                        | declaracao_state '''
    p[0] = p[1]

def p_declaracao_de_controle_de_modularizacao(p):
    '''declaracao_de_controle_de_modularizacao : import
                                               | need
                                               | require
                                               | use '''
    p[0] = p[1]

def p_declaracao_de_controle_de_lista(p):
    '''declaracao_de_controle_de_lista : push 
                                       | unshift
                                       | splice '''
    p[0] = p[1]

# --- CONTROLE DE FLUXO ---

def p_break(p):
    '''declaracao_break : BREAK PONTO_VIRGULA'''
    p[0] = sa.Break()

def p_exit(p):
    '''declaracao_exit : EXIT exp_2 PONTO_VIRGULA'''
    p[0] = sa.Exit(p[2])

def p_last(p):
    '''declaracao_last : LAST PONTO_VIRGULA'''
    p[0] = sa.Last()

def p_next(p):
    '''declaracao_next : NEXT PONTO_VIRGULA'''
    p[0] = sa.Next()

def p_redo(p):
    '''declaracao_redo : REDO IF BOOLEAN PONTO_VIRGULA'''
    p[0] = sa.Redo()

def p_return(p):
    '''declaracao_return : RETURN exp_2 PONTO_VIRGULA'''
    p[0] = sa.Return(p[2])


 # --- DECLARAÇÕES E ESCOPO ---

def p_declaracao_constant(p):
    '''declaracao_constant : CONSTANT ESCALAR IGUAL exp_2 PONTO_VIRGULA'''
    p[0] = sa.Constant(p[2], p[4])

def p_declaracao_state(p):
    '''declaracao_state : STATE ESCALAR IGUAL exp_2 PONTO_VIRGULA'''
    p[0] = sa.State(p[2], p[4])

def p_declaracao_multi(p):
    '''declaracao_multi : MULTI ID LPAREN parametros RPAREN ABRE_CHAVE lista_declaracoes_para_funcoes FECHA_CHAVE'''
    p[0] = sa.Multi(p[2])

def p_declaracao_multi_sem_par(p):
    '''declaracao_multi_sem_par : MULTI ID LPAREN RPAREN ABRE_CHAVE lista_declaracoes_para_funcoes FECHA_CHAVE'''
    p[0] = sa.Multi(p[2])

def p_declaracao_only(p):
    '''declaracao_only : ONLY ID LPAREN parametros RPAREN ABRE_CHAVE lista_declaracoes_para_funcoes FECHA_CHAVE'''
    p[0] = sa.Only(p[2])

def p_declaracao_only_sem_par(p):
    '''declaracao_only_sem_par : ONLY ID LPAREN RPAREN ABRE_CHAVE lista_declaracoes_para_funcoes FECHA_CHAVE'''
    p[0] = sa.Only(p[2])


# --- IMPORTAÇÃO E MODULARIZAÇÃO ---

def p_import(p):
    '''import : IMPORT ID MENOR ID MAIOR PONTO_VIRGULA'''
    p[0] = sa.Import(p[2])

def p_need(p):
    '''need : NEED ID PONTO_VIRGULA'''
    p[0] = sa.Need(p[2])

def p_require(p):
    '''require : REQUIRE ID PONTO_VIRGULA'''
    p[0] = sa.Require(p[2])

def p_use(p):
    '''use : USE ID PONTO_VIRGULA'''
    p[0] = sa.Use(p[2])

# --- OPERAÇÕES EM LISTAS ---


def p_push(p):
    '''push : PUSH LIST COMMA lista_valores PONTO_VIRGULA'''
    p[0] = sa.Push(p[2], p[4])

def p_unshift(p):
    '''unshift : UNSHIFT LIST COMMA lista_valores PONTO_VIRGULA'''
    p[0] = sa.Unshift(p[2], p[4])

def p_splice(p):
    '''splice : SPLICE LIST COMMA lista_valores PONTO_VIRGULA'''
    p[0] = sa.Splice(p[2], p[4])


def main():

    # Caminho relativo
    caminho = os.path.join(os.path.dirname(__file__), "main.raku")

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


'''
    print("\n=== Visitando com Visitor ===")
    visitor = Visitor()
    result.accept(visitor)   # testando o visitor
'''

if __name__ == "__main__":
    main()

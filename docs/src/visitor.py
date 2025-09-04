from AbstractVisitor import abstractVisitor
import lexico
from sintatico import *
import ply.lex as lex

tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p


class Visitor(abstractVisitor):

# ------------------Funções-------------------------------
    def visitorCompoundFuncao(self, func):
        print(f"sub {func.id}({', '.join(func.parametros)}) {{")

        #func.comando.accept(self)
        if hasattr(func.comando, "accept"):
           func.comando.accept(self)
        else:
            print(func.comando)  

        print("}")

    def visitorCompoundFuncaoSemParametros(self, func):
        print(f"sub {func.id}() {{")
        #func.comando.accept(self)
        if hasattr(func.comando, "accept"):
           func.comando.accept(self)
        else:
            print(func.comando) 

        print("}")



# ------------------Repetição-------------------------------
    def visitorLoopFor(self, loop_for):
        print(f"for {loop_for.expr} -> {loop_for.id} {{")
        loop_for.comando.accept(self)
        print("}")

    def visitorLoopWhile(self, loop_while):
        print(f"while ({loop_while.limite}) {{")
        loop_while.comando.accept(self)
        print("}")

    def visitorLoopRepeticao(self, loop_repeticao):
        print(f"loop ({loop_repeticao.instrucao1}; {loop_repeticao.instrucao2}; {loop_repeticao.instrucao3}) {{")
        loop_repeticao.comando.accept(self)
        print("}")

    def visitorLoopSemCondicao(self, loop_sem_condicao):
        print("loop {")
        loop_sem_condicao.comando.accept(self)
        print("}")


#----------------------------------------------------Expressoes--------
    def visitorExpressaoOR(self, oor):
        print("(", end=""); oor.esquerda.accept(self); print(" or ", end=""); oor.direita.accept(self); print(")", end="")

    def visitorExpressaoXOR(self, xor):
        print("(", end=""); xor.esquerda.accept(self); print(" xor ", end=""); xor.direita.accept(self); print(")", end="")

    def visitorExpressaoAND(self, andd):
        print("(", end=""); andd.esquerda.accept(self); print(" and ", end=""); andd.direita.accept(self); print(")", end="")

    def visitorExpressaoIGUAL_DP(self, igual):
        print("(", end=""); igual.esquerda.accept(self); print(" == ", end=""); igual.direita.accept(self); print(")", end="")

    def visitorExpressaoDIF(self, dif):
        print("(", end=""); dif.esquerda.accept(self); print(" != ", end=""); dif.direita.accept(self); print(")", end="")

    def visitorExpressaoMAIOR(self, maior):
        print("(", end=""); maior.esquerda.accept(self); print(" > ", end=""); maior.direita.accept(self); print(")", end="")
    
    def visitorExpressaoMENOR(self, menor):
        print("(", end=""); menor.esquerda.accept(self); print(" < ", end=""); menor.direita.accept(self); print(")", end="")

    def visitorExpressaoMAIOR_IGUAL(self, igual):
        print("(", end=""); igual.esquerda.accept(self); print(" >= ", end=""); igual.direita.accept(self); print(")", end="")

    def visitorExpressaoMENOR_IGUAL(self, menorIgual):
        print("(", end=""); menorIgual.esquerda.accept(self); print(" <= ", end=""); menorIgual.direita.accept(self); print(")", end="")

    def visitorExpressaoSMARTMATCH(self, match):
        print("(", end=""); match.esquerda.accept(self); print(" ~~ ", end=""); match.direita.accept(self); print(")", end="")

    def visitorExpressaoADICAO(self, adicao):
        print("(", end=""); adicao.esquerda.accept(self); print(" + ", end=""); adicao.direita.accept(self); print(")", end="")

    def visitorExpressaoSUBTRACAO(self, subtacao):
        print("(", end=""); subtacao.esquerda.accept(self); print(" - ", end=""); subtacao.direita.accept(self); print(")", end="")

    def visitorExpressaoCONCATENACAO(self, concatenacao):
        print("(", end=""); concatenacao.esquerda.accept(self);print(" ~", end="");concatenacao.direita.accept(self); print(")", end="")


    def visitorExpressaoMULTIPLICACAO(self, mult):
        print("(", end=""); mult.esquerda.accept(self); print(" * ", end=""); mult.direita.accept(self); print(")", end="")

    def visitorExpressaoDIVISAO(self, div):
        print("(", end=""); div.esquerda.accept(self); print(" / ", end=""); div.direita.accept(self); print(")", end="")

    def visitorExpressaoDIVISAO_INTEIRA(self, diviInt):
        print("(", end=""); diviInt.esquerda.accept(self); print(" div ", end=""); diviInt.direita.accept(self); print(")", end="")

    def visitorExpressaoDIVISIBILIDADE(self, divi):
        print("(", end=""); divi.esquerda.accept(self); print(" % ", end=""); divi.direita.accept(self); print(")", end="")
     
    def visitorExpressaoMOD(self, mod):
        print("(", end=""); mod.esquerda.accept(self); print(" mod ", end=""); mod.direita.accept(self); print(")", end="")

    def visitorExpressaoLCM(self, lmc):
        print("lcm(", end=""); lmc.esquerda.accept(self); print(", ", end=""); lmc.direita.accept(self); print(")", end="")

    def visitorExpressaoGCD(self, gcd):
        print("gcd(", end=""); gcd.esquerda.accept(self); print(", ", end=""); gcd.direita.accept(self); print(")", end="")

    def visitorExpressaoPOW(self, pow):
        print("(", end=""); pow.esquerda.accept(self); print(" ** ", end=""); pow.direita.accept(self); print(")", end="")

    def visitorExpressaoNOT_OPERADOR(self, operador):
        print("not ", end=""); operador.operando.accept(self)

    def visitorExpressaoNOT_SIMBULO(self, simb):
        print("!", end=""); simb.operando.accept(self)

    def visitorExpressao_PREFIXO_INCREMENTO(self, increm):
        print("++", end=""); increm.operando.accept(self)

    def visitorExpressao_POSFIXO_INCREMENTO(self, increm):
        increm.operando.accept(self); print("++", end="")

    def visitorExpressao_PREFIXO_DECREMENTO(self, decrem):
        print("--", end=""); decrem.operando.accept(self)

    def visitorExpressao_POSFIXO_DECREMENTO(self, decrem):
        decrem.operando.accept(self); print("--", end="")

    def visitorExpressao_PARENTESES(self, parenteses):
        print("(", end=""); parenteses.expressao.accept(self); print(")", end="")

    def visitorExpressao_VALOR(self, valor):
        print(valor.valor, end="")

    def visitorExpressao_TIPO(self, tipo):
        print(tipo.tipo, end="")

    def visitorSAY(self, say):
        print("say ", end=""); say.exp.accept(self); print(";")

    def visitorPARAMETROS(self, param):
        param.escalar.accept(self)

    def visitorPARAMETROSMULT(self, param):
        param.escalar.accept(self)
        for p in param.outros_parametros:
            print(", ", end=""); p.accept(self)





# ------------------Chamada Funções-------------------------------
            
def visitorCHAMADA_FUNCAO(self, chamada):
    print(f"{chamada.id}(", end="")
    for i, arg in enumerate(chamada.args):
        if i > 0:
            print(", ", end="")
        arg.accept(self)
    print(");")

    def visitorCHAMADA_FUNCAO_SEM_PARAMETRO(self, chamada):
        print(f"{chamada.id}();")







      # ------------------Controle de Fluxo-------------------------------
    def visitorBreak(self, Break):
        print("break;")

    def visitorExit(self, exit):
        print("exit(", end=""); exit.exp.accept(self); print(");")

    def visitorLast(self, last):
        print("last;")

    def visitorNext(self, next):
        print("next;")

    def visitorRedo(self, redo):
        print("redo;")

    def visitorReturn(self, returnn):
        print("return ", end=""); returnn.exp.accept(self); print(";")  



# ------------------Declarações e Escopo-------------------------------
    def visitorConstant(self, constant):
        print(f"constant {constant.id} = {constant.valor};")

    def visitorState(self, state):
        print(f"state {state.id} = {state.valor};")


    def visitorMulti(self, multi):
        print(f"multi {multi.id}({', '.join(multi.parametros)}) {{")
        multi.comando.accept(self)
        print("}")

    def visitorOnly(self, only):
        print(f"only {only.id} {{")
        only.comando.accept(self)
        print("}")

    def visitorUnit(self, unit):
        print("unit;")

    # ------------------Importação/Modularização-------------------------------
    def visitorExport(self, export):
        print(f"export {export.id};")

    def visitorImport(self, importt):
        print(f"import {importt.id};")

    def visitorNeed(self, need):
        print(f"need {need.id};")

    def visitorRequire(self, require):
        print(f"require {require.id};")

    def visitorUse(self, use):
        print(f"use {use.id};")


    # ------------------Operações em Listas-------------------------------
    def visitorPush(self, push):
        print(f"push {push.escalar}, {', '.join(map(str, push.valores))};")

    def visitorUnshift(self, unshift):
        print(f"unshift {unshift.escalar}, {', '.join(map(str, unshift.valores))};")

    def visitorSplice(self, splice):
        print(f"splice {splice.escalar}, {splice.inicio}, {splice.quantidade};")

def main():
    f = open("main.raku", "r")
    lexer = lex.lex(module=lexico)
    lexer.input(f.read())
    parser = yacc.yacc(start='programa')
    result = parser.parse(debug=False)
    print("imprime o programa que foi passado como entrada")
    visitor = Visitor()
    result.accept(visitor)

    if isinstance(result, list):
      for node in result:
        if node is not None:
         node.accept(visitor)
    else:
     result.accept(visitor)

if __name__ == "__main__":
    main()

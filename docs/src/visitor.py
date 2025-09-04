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
    def visitCompoundFuncao(self, func):
        print(f"sub {func.id}({', '.join(func.parametros)}) {{")

        #func.comando.accept(self)
        if hasattr(func.comando, "accept"):
           func.comando.accept(self)
        else:
            print(func.comando)  

        print("}")

    def visitCompoundFuncaoSemParametros(self, func):
        print(f"sub {func.id}() {{")
        #func.comando.accept(self)
        if hasattr(func.comando, "accept"):
           func.comando.accept(self)
        else:
            print(func.comando) 

        print("}")



# ------------------Repetição-------------------------------
    def visitLoopFor(self, loop_for):
        print(f"for {loop_for.expr} -> {loop_for.id} {{")
        loop_for.comando.accept(self)
        print("}")

    def visitLoopTimes(self, loop_times):
        print(f"{loop_times.integer}.times -> {loop_times.id} {{")
        loop_times.comando.accept(self)
        print("}")

    def visitLoopWhile(self, loop_while):
        print(f"while ({loop_while.limite}) {{")
        loop_while.comando.accept(self)
        print("}")

    def visitLoopRepeticao(self, loop_repeticao):
        print(f"loop ({loop_repeticao.instrucao1}; {loop_repeticao.instrucao2}; {loop_repeticao.instrucao3}) {{")
        loop_repeticao.comando.accept(self)
        print("}")

    def visitLoopSemCondicao(self, loop_sem_condicao):
        print("loop {")
        loop_sem_condicao.comando.accept(self)
        print("}")


#----------------------------------------------------Expressoes--------
    def visitExpressaoOR(self, oor):
        print("(", end=""); oor.esquerda.accept(self); print(" or ", end=""); oor.direita.accept(self); print(")", end="")

    def visitExpressaoXOR(self, xor):
        print("(", end=""); xor.esquerda.accept(self); print(" xor ", end=""); xor.direita.accept(self); print(")", end="")

    def visitExpressaoAND(self, andd):
        print("(", end=""); andd.esquerda.accept(self); print(" and ", end=""); andd.direita.accept(self); print(")", end="")

    def visitExpressaoIGUAL_DP(self, igual):
        print("(", end=""); igual.esquerda.accept(self); print(" == ", end=""); igual.direita.accept(self); print(")", end="")

    def visitExpressaoDIF(self, dif):
        print("(", end=""); dif.esquerda.accept(self); print(" != ", end=""); dif.direita.accept(self); print(")", end="")

    def visitExpressaoMAIOR(self, maior):
        print("(", end=""); maior.esquerda.accept(self); print(" > ", end=""); maior.direita.accept(self); print(")", end="")
    
    def visitExpressaoMENOR(self, menor):
        print("(", end=""); menor.esquerda.accept(self); print(" < ", end=""); menor.direita.accept(self); print(")", end="")

    def visitExpressaoMAIOR_IGUAL(self, igual):
        print("(", end=""); igual.esquerda.accept(self); print(" >= ", end=""); igual.direita.accept(self); print(")", end="")

    def visitExpressaoMENOR_IGUAL(self, menorIgual):
        print("(", end=""); menorIgual.esquerda.accept(self); print(" <= ", end=""); menorIgual.direita.accept(self); print(")", end="")

    def visitExpressaoSMARTMATCH(self, match):
        print("(", end=""); match.esquerda.accept(self); print(" ~~ ", end=""); match.direita.accept(self); print(")", end="")

    def visitExpressaoADICAO(self, adicao):
        print("(", end=""); adicao.esquerda.accept(self); print(" + ", end=""); adicao.direita.accept(self); print(")", end="")

    def visitExpressaoSUBTRACAO(self, subtacao):
        print("(", end=""); subtacao.esquerda.accept(self); print(" - ", end=""); subtacao.direita.accept(self); print(")", end="")

    def visitExpressaoCONCATENACAO(self, concatenacao):
        print("(", end=""); concatenacao.esquerda.accept(self);print(" ~", end="");concatenacao.direita.accept(self); print(")", end="")


    def visitExpressaoMULTIPLICACAO(self, mult):
        print("(", end=""); mult.esquerda.accept(self); print(" * ", end=""); mult.direita.accept(self); print(")", end="")

    def visitExpressaoDIVISAO(self, div):
        print("(", end=""); div.esquerda.accept(self); print(" / ", end=""); div.direita.accept(self); print(")", end="")

    def visitExpressaoDIVISAO_INTEIRA(self, diviInt):
        print("(", end=""); diviInt.esquerda.accept(self); print(" div ", end=""); diviInt.direita.accept(self); print(")", end="")

    def visitExpressaoDIVISIBILIDADE(self, divi):
        print("(", end=""); divi.esquerda.accept(self); print(" % ", end=""); divi.direita.accept(self); print(")", end="")
     
    def visitExpressaoMOD(self, mod):
        print("(", end=""); mod.esquerda.accept(self); print(" mod ", end=""); mod.direita.accept(self); print(")", end="")

    def visitExpressaoLCM(self, lmc):
        print("lcm(", end=""); lmc.esquerda.accept(self); print(", ", end=""); lmc.direita.accept(self); print(")", end="")

    def visitExpressaoGCD(self, gcd):
        print("gcd(", end=""); gcd.esquerda.accept(self); print(", ", end=""); gcd.direita.accept(self); print(")", end="")

    def visitExpressaoPOW(self, pow):
        print("(", end=""); pow.esquerda.accept(self); print(" ** ", end=""); pow.direita.accept(self); print(")", end="")

    def visitExpressaoNOT_OPERADOR(self, operador):
        print("not ", end=""); operador.operando.accept(self)

    def visitExpressaoNOT_SIMBULO(self, simb):
        print("!", end=""); simb.operando.accept(self)

    def visitExpressao_PREFIXO_INCREMENTO(self, increm):
        print("++", end=""); increm.operando.accept(self)

    def visitExpressao_POSFIXO_INCREMENTO(self, increm):
        increm.operando.accept(self); print("++", end="")

    def visitExpressao_PREFIXO_DECREMENTO(self, decrem):
        print("--", end=""); decrem.operando.accept(self)

    def visitExpressao_POSFIXO_DECREMENTO(self, decrem):
        decrem.operando.accept(self); print("--", end="")

    def visitExpressao_PARENTESES(self, parenteses):
        print("(", end=""); parenteses.expressao.accept(self); print(")", end="")

    def visitExpressao_VALOR(self, valor):
        print(valor.valor, end="")

    def visitExpressao_TIPO(self, tipo):
        print(tipo.tipo, end="")

    def visitSAY(self, say):
        print("say ", end=""); say.exp.accept(self); print(";")

    def visitPARAMETROS(self, param):
        param.escalar.accept(self)

    def visitPARAMETROSMULT(self, param):
        param.escalar.accept(self)
        for p in param.outros_parametros:
            print(", ", end=""); p.accept(self)





# ------------------Chamada Funções-------------------------------
            
    def visitCHAMADA_FUNCAO(self, chamada):
        print(f"{chamada.id}({chamada.valor});")

    def visitCHAMADA_FUNCAO_SEM_PARAMETRO(self, chamada):
        print(f"{chamada.id}();")







      # ------------------Controle de Fluxo-------------------------------
    def visitBreak(self, breakk):
        print("break;")

    def visitExit(self, exit):
        print("exit(", end=""); exit.exp.accept(self); print(");")

    def visitLast(self, last):
        print("last;")

    def visitNext(self, next):
        print("next;")

    def visitRedo(self, redo):
        print("redo;")

    def visitReturn(self, returnn):
        print("return ", end=""); returnn.exp.accept(self); print(";")  



# ------------------Declarações e Escopo-------------------------------
    def visitConstant(self, constant):
        print(f"constant {constant.id} = {constant.valor};")

    def visitState(self, state):
        print(f"state {state.id} = {state.valor};")

    def visitLet(self, let):
        print(f"let {let.id} = {let.valor};")

    def visitMulti(self, multi):
        print(f"multi {multi.id}({', '.join(multi.parametros)}) {{")
        m.comando.accept(self)
        print("}")

    def visitOnly(self, only):
        print(f"only {only.id} {{")
        o.comando.accept(self)
        print("}")

    def visitUnit(self, unit):
        print("unit;")

    # ------------------Importação/Modularização-------------------------------
    def visitExport(self, export):
        print(f"export {export.id};")

    def visitImport(self, importt):
        print(f"import {importt.id};")

    def visitNeed(self, need):
        print(f"need {need.id};")

    def visitRequire(self, require):
        print(f"require {require.id};")

    def visitUse(self, use):
        print(f"use {use.id};")


    # ------------------Operações em Listas-------------------------------
    def visitPush(self, push):
        print(f"push {push.escalar}, {', '.join(map(str, push.valores))};")

    def visitUnshift(self, unshift):
        print(f"unshift {unshift.escalar}, {', '.join(map(str, unshift.valores))};")

    def visitSplice(self, splice):
        print(f"splice {splice.escalar}, {splice.inicio}, {splice.quantidade};")

def main():
    f = open("main.raku", "r")
    lexer = lex.lex(module=lexico)
    lexer.input(f.read())
    parser = yacc.yacc(start='programa')
    result = parser.parse(debug=False)
    print("imprime o programa que foi passado como entrada")
    visitor = Visitor()
    #result.accept(visitor)

    if isinstance(result, list):
      for node in result:
        if node is not None:
         node.accept(visitor)
    else:
     result.accept(visitor)

if __name__ == "__main__":
    main()














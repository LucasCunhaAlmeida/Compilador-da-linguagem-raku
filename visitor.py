from AbstractVisitor import abstractVisitor
import lexico
import os
from sintatico import *
import ply.lex as lex


tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p


class visitor(abstractVisitor):


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

    def visitDeclaracaoLoop(self, declaracao_loop):
        declaracao_loop.loop.accept(self)

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

    def visitLoopForLista(self, loop_for_lista):
        print(f"loop {loop_for_lista.escalar} in ", end="")
        loop_for_lista.lista.accept(self)

        print(" {")
    
        for comando in loop_for_lista.comandos:
            comando.accept(self)
    
        print("}")



#----------------------------------------------------Expressoes--------
    def visitExpressaoOR(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" or ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoXOR(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" xor ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoAND(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" and ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoIGUAL_DP(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" == ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoDIF(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" != ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoMAIOR(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" > ", end=""); expr.direita.accept(self); print(")", end="")
    
    def visitExpressaoMENOR(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" < ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoMAIOR_IGUAL(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" >= ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoMENOR_IGUAL(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" <= ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoSMARTMATCH(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" ~~ ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoADICAO(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" + ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoSUBTRACAO(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" - ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoCONCATENACAO(self, expr):
        print("(", end=""); expr.esquerda.accept(self);print(" ~", end="");expr.direita.accept(self); print(")", end="")


    def visitExpressaoMULTIPLICACAO(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" * ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoDIVISAO(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" / ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoDIVISAO_INTEIRA(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" div ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoDIVISIBILIDADE(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" % ", end=""); expr.direita.accept(self); print(")", end="")
     
    def visitExpressaoMOD(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" mod ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoLCM(self, expr):
        print("lcm(", end=""); expr.esquerda.accept(self); print(", ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoGCD(self, expr):
        print("gcd(", end=""); expr.esquerda.accept(self); print(", ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoPOW(self, expr):
        print("(", end=""); expr.esquerda.accept(self); print(" ** ", end=""); expr.direita.accept(self); print(")", end="")

    def visitExpressaoNOT_OPERADOR(self, expr):
        print("not ", end=""); expr.operando.accept(self)

    def visitExpressao_NOT_SIMBULO(self, expr):
        print("!", end=""); expr.operando.accept(self)

    def visitExpressao_PREFIXO_INCREMENTO(self, expr):
        print("++", end=""); expr.operando.accept(self)

    def visitExpressao_POSFIXO_INCREMENTO(self, expr):
        expr.operando.accept(self); print("++", end="")

    def visitExpressao_PREFIXO_DECREMENTO(self, expr):
        print("--", end=""); expr.operando.accept(self)

    def visitExpressao_POSFIXO_DECREMENTO(self, expr):
        expr.operando.accept(self); print("--", end="")

    def visitExpressao_PARENTESES(self, expr):
        print("(", end=""); expr.expressao.accept(self); print(")", end="")

    def visitExpressao_VALOR(self, expr):
        print(expr.valor, end="")

    def visitExpressao_TIPO(self, expr):
        print(expr.tipo, end="")

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
        print(f"{chamada.id}(", end="")
        for i, arg in enumerate(chamada.valor):
            if i > 0:
                print(", ", end="")
            arg.accept(self)
        print(");")

    def visitCHAMADA_FUNCAO_SEM_PARAMETRO(self, chamada):
        print(f"{chamada.id}();")



      # ------------------Controle de Fluxo-------------------------------
    def visitBreak(self, br):
        print("break;")

    def visitExit(self, ex):
        print("exit(", end=""); ex.exp.accept(self); print(");")

    def visitLast(self, l):
        print("last;")

    def visitNext(self, n):
        print("next;")

    def visitRedo(self, r):
        print("redo;")

    def visitReturn(self, r):
        print("return ", end=""); r.exp.accept(self); print(";")  



# ------------------Declarações e Escopo-------------------------------
    def visitConstant(self, c):
        print(f"constant {c.id} = {c.valor};")

    def visitState(self, s):
        print(f"state {s.id} = {s.valor};")

    def visitLet(self, l):
        print(f"let {l.id} = {l.valor};")

    def visitMulti(self, m):
        print(f"multi {m.id}({', '.join(m.parametros)}) {{")
        m.comando.accept(self)
        print("}")

    def visitOnly(self, o):
        print(f"only {o.id} {{")
        o.comando.accept(self)
        print("}")

    def visitDeclaracaoEscalarMY(self, declaracao):
        print(blank() + "my ", end="")
        if declaracao.tipo:
            declaracao.tipo.accept(self)
            print(" ", end="")
        
        print(f"{declaracao.escalar} = ", end="")
        declaracao.valor.accept(self)
        print(";")

    def visitDeclaracaoEscalarOUR(self, declaracao):
        print(blank() + "our ", end="")
        if declaracao.tipo:
            declaracao.tipo.accept(self)
            print(" ", end="")
        
        print(f"{declaracao.escalar} = ", end="")
        declaracao.valor.accept(self)
        print(";")

    def visitDeclaracaoLista(self, declaracao):
        print(" ", end="")

        print(f"{declaracao.lista} = (", end="")
        for i, v in enumerate(declaracao.valores):
            v.accept(self)
            if i < len(declaracao.valores) - 1:
                print(", ", end="")
        print(");")

    def visitDeclaracaoListaMY(self, declaracao):
        print("my ", end="")
        
        print(f"{declaracao.lista} = (", end="")
        for i, v in enumerate(declaracao.valores):
            v.accept(self)
            if i < len(declaracao.valores) - 1:
                print(", ", end="")
        print(");")
    
    def visitDeclaracaoListaOUR(self, declaracao):
        print("our ", end="")
        
        print(f"{declaracao.lista} = (", end="")
        for i, v in enumerate(declaracao.valores):
            v.accept(self)
            if i < len(declaracao.valores) - 1:
                print(", ", end="")
        print(");")

    # ------------------Importação/Modularização-------------------------------
    def visitExport(self, e):
        print(f"export {e.id};")

    def visitImport(self, i):
        print(f"import {i.id};")

    def visitNeed(self, n):
        print(f"need {n.id};")

    def visitRequire(self, r):
        print(f"require {r.id};")

    def visitUse(self, u):
        print(f"use {u.id};")


    # ------------------Operações em Listas-------------------------------
    def visitPush(self, p):
        print(f"push {p.escalar}, {', '.join(map(str, p.valores))};")

    def visitUnshift(self, u):
        print(f"unshift {u.escalar}, {', '.join(map(str, u.valores))};")

    def visitSplice(self, s):
        print(f"splice {s.escalar}, {s.inicio}, {s.quantidade};")

    # ------------------Condicionais-------------------------------
    def visitDeclaracaoCondicional(self, declaracao_condicional):
        declaracao_condicional.condicional.accept(self)

    def visitCondicionalIf(self, condicional_if):
        print("if (", end="")
        condicional_if.condicao.accept(self)  
        print(") {")
        for stmt in condicional_if.bloco:     
            if hasattr(stmt, "accept"):
                stmt.accept(self)
            else:
                print(stmt)
        print("}")

    def visitCondicionalIfElse(self, condicional_if_else):
        global tab
        self.visitCondicionalIfElse(condicional_if_else)
        
        print(" else {")
        tab += 2
        for declaracao in condicional_if_else.bloco_else:
            if hasattr(declaracao, "accept"):
                declaracao.accept(self)
        tab -= 2
        print(blank() + "}")

    def visitCondicionalIfElsif(self, condicional_if_elsif):
       
        self.visitCondicionalIfElsif(condicional_if_elsif)
        
        for elsif_node in condicional_if_elsif.elsifs:
            elsif_node.accept(self)

    def visitCondicionalIfElsifElse(self, condicional_if_elsif_else):
        global tab
        
        self.visitCondicionalIfElsifElse(condicional_if_elsif_else)

        print(" else {")
        tab += 2
        for declaracao in condicional_if_elsif_else.bloco_else:
            if hasattr(declaracao, "accept"):
                declaracao.accept(self)
        tab -= 2
        print(blank() + "}")

    def visitElsif(self, elsif):
        global tab
        print(" elsif ", end="")
        elsif.condicao.accept(self)
        print(" {")
        
        tab += 2
        for declaracao in elsif.bloco:
            if hasattr(declaracao, "accept"):
                declaracao.accept(self)
        tab -= 2
        print(blank() + "}", end="")

def main():
    f = open(os.path.join(os.path.dirname(__file__), "main.raku"))
    lexer = lex.lex(module=lexico)
    lexer.input(f.read())
    parser = yacc.yacc(start='programa')
    result = parser.parse(debug=False)
    print("imprime o programa que foi passado como entrada")
    visit = visitor()

    if result is not None:
        if isinstance(result, list):
            for node in result:
                if node is not None:
                    node.accept(visit)
        else:
            result.accept(visit)
    else:
        print("Erro: Parser retornou None")

if __name__ == "__main__":
    main()














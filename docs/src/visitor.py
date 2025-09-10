from abstractVisitor import abstractvisitor
import lexico
import sintatico
import ply.lex as lex
import os
import ply.yacc as yacc
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class visitor(abstractvisitor):

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
        
        if hasattr(func.comando, "accept"):
           func.comando.accept(self)
        else:
            print(func.comando) 

        print("}")



# ------------------Repetição-------------------------------
    def visitorDeclaracaoLoop(self, declaracao_loop):
        declaracao_loop.loop.accept(self)

    def visitorLoopFor(self, loop_for):
        print(f"for {loop_for.expr} -> {loop_for.id} {{")
        for comando in loop_for.comando:
            if hasattr(comando, "accept"):
                comando.accept(self)
            else:
                print(comando)
        print("}")
    
    def visitorLoopWhile(self, loop_while):
        print(f"while ({loop_while.limite}) {{")
        for comando in loop_while.comando:
            if hasattr(comando, "accept"):
                comando.accept(self)
            else:
                print(comando)
        print("}")

    def visitorLoopRepeticao(self, loop_repeticao):
        print(f"loop ({loop_repeticao.instrucao1}; {loop_repeticao.instrucao2}; {loop_repeticao.instrucao3}) {{")
        for comando in loop_repeticao.comando:
            if hasattr(comando, "accept"):
                comando.accept(self)
            else:
                print(comando)
        print("}")

    def visitorLoopSemCondicao(self, loop_sem_condicao):
        print("loop {")
        for comando in loop_sem_condicao.comando:
            if hasattr(comando, "accept"):
                comando.accept(self)
            else:
                print(comando)
        print("}")

    def visitorLoopForLista(self, loop_for_lista):
        print(f"loop {loop_for_lista.escalar} in ", end="")
        loop_for_lista.lista.accept(self)

        print(" {")
    
        for comando in loop_for_lista.comandos:
            comando.accept(self)
    
        print("}")

#----------------------------------------------------Expressoes--------
    def visitorExpressaoOR(self, oor):
        oor.esquerda.accept(self); print(" or ", end=""); oor.direita.accept(self)

    def visitorExpressaoXOR(self, xor):
        xor.esquerda.accept(self); print(" xor ", end=""); xor.direita.accept(self)

    def visitorExpressaoAND(self, andd):
        andd.esquerda.accept(self); print(" and ", end=""); andd.direita.accept(self)

    def visitorExpressaoIGUAL_DP(self, igual):
        igual.esquerda.accept(self); print(" == ", end=""); igual.direita.accept(self)

    def visitorExpressaoDIF(self, dif):
        dif.esquerda.accept(self); print(" != ", end=""); dif.direita.accept(self)

    def visitorExpressaoMAIOR(self, maior):
        maior.esquerda.accept(self); print(" > ", end=""); maior.direita.accept(self)
    
    def visitorExpressaoMENOR(self, menor):
        menor.esquerda.accept(self); print(" < ", end=""); menor.direita.accept(self)

    def visitorExpressaoMAIOR_IGUAL(self, igual):
        igual.esquerda.accept(self); print(" >= ", end=""); igual.direita.accept(self)

    def visitorExpressaoMENOR_IGUAL(self, menorIgual):
        menorIgual.esquerda.accept(self); print(" <= ", end=""); menorIgual.direita.accept(self)

    def visitorExpressaoSMARTMATCH(self, match):
        match.esquerda.accept(self); print(" ~~ ", end=""); match.direita.accept(self)

    def visitorExpressaoADICAO(self, adicao):
        adicao.esquerda.accept(self); print(" + ", end=""); adicao.direita.accept(self)

    def visitorExpressaoSUBTRACAO(self, subtacao):
        subtacao.esquerda.accept(self); print(" - ", end=""); subtacao.direita.accept(self)

    def visitorExpressaoCONCATENACAO(self, concatenacao):
        concatenacao.esquerda.accept(self);print(" ~", end="");concatenacao.direita.accept(self)


    def visitorExpressaoMULTIPLICACAO(self, mult):
        mult.esquerda.accept(self); print(" * ", end=""); mult.direita.accept(self)

    def visitorExpressaoDIVISAO(self, div):
        div.esquerda.accept(self); print(" / ", end=""); div.direita.accept(self)

    def visitorExpressaoDIVISAO_INTEIRA(self, diviInt):
        diviInt.esquerda.accept(self); print(" div ", end=""); diviInt.direita.accept(self)

    def visitorExpressaoDIVISIBILIDADE(self, divi):
        divi.esquerda.accept(self); print(" % ", end=""); divi.direita.accept(self)
     
    def visitorExpressaoMOD(self, mod):
        mod.esquerda.accept(self); print(" mod ", end=""); mod.direita.accept(self)

    def visitorExpressaoLCM(self, lmc):
        print("lcm(", end=""); lmc.esquerda.accept(self); print(", ", end=""); lmc.direita.accept(self); print(")", end="")

    def visitorExpressaoGCD(self, gcd):
        print("gcd(", end=""); gcd.esquerda.accept(self); print(", ", end=""); gcd.direita.accept(self); print(")", end="")

    def visitorExpressaoPOW(self, pow):
        pow.esquerda.accept(self); print(" ** ", end=""); pow.direita.accept(self)

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
        for i, arg in enumerate(chamada.valor):
            if i > 0:
                print(", ", end="")
            arg.accept(self)
        print(");")

    def visitorCHAMADA_FUNCAO_SEM_PARAMETRO(self, chamada):
        print(f"{chamada.id}();")


      # ------------------Controle de Fluxo-------------------------------
    def visitorBreak(self, Break):
        print("break;")
        pass

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
        for comando in multi.comando:
            if hasattr(comando, "accept"):
                comando.accept(self)
            else:
                print(comando)
        print("}")

    def visitorOnly(self, only):
        print(f"only {only.id} {{")
        for comando in only.comando:
            if hasattr(comando, "accept"):
                comando.accept(self)
            else:
                print(comando)
        print("\n}")

    def visitorDeclaracaoEscalarMY(self, declaracao):
        print(blank() + "my ", end="")
        if declaracao.tipo:
            declaracao.tipo.accept(self)
            print(" ", end="")
        
        print(f"{declaracao.escalar} = ", end="")
        declaracao.valor.accept(self)
        print(";")

    def visitorDeclaracaoEscalarOUR(self, declaracao):
        print(blank() + "our ", end="")
        if declaracao.tipo:
            declaracao.tipo.accept(self)
            print(" ", end="")
        
        print(f"{declaracao.escalar} = ", end="")
        declaracao.valor.accept(self)
        print(";")

    def visitorAtribuicao(self, atribuicao):
        print(blank() + f"{atribuicao.variavel} = ", end="")
        atribuicao.valor.accept(self)
        print(";")

    def visitorDeclaracaoLista(self, declaracao):
        print(" ", end="")
        if declaracao.tipo:
            declaracao.tipo.accept(self)
            print(" ", end="")

        print(f"{declaracao.lista} = (", end="")
        for i, v in enumerate(declaracao.valores):
            v.accept(self)
            if i < len(declaracao.valores) - 1:
                print(", ", end="")
        print(");")

    def visitorDeclaracaoListaMY(self, declaracao):
        print("my ", end="")
        if declaracao.tipo:
            declaracao.tipo.accept(self)
            print(" ", end="")

        print(f"{declaracao.lista} = (", end="")
        for i, v in enumerate(declaracao.valores):
            v.accept(self)
            if i < len(declaracao.valores) - 1:
                print(", ", end="")
        print(");")

    def visitorDeclaracaoListaOUR(self, declaracao):
        print("our ", end="")
        if declaracao.tipo:
            declaracao.tipo.accept(self)
            print(" ", end="")
        print(f"{declaracao.lista} = (", end="")
        for i, v in enumerate(declaracao.valores):
            v.accept(self)
            if i < len(declaracao.valores) - 1:
                print(", ", end="")
        print(");")

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
        print(f"push {push.escalar}, ", end="")
        for i, valor in enumerate(push.valores):
            if i > 0:
                print(", ", end="")
            if hasattr(valor, "accept"):
                valor.accept(self)
            else:
                print(valor, end="")
        print(";")

    def visitorUnshift(self, unshift):
        print(f"unshift {unshift.escalar}, ", end="")
        for i, valor in enumerate(unshift.valores):
            if i > 0:
                print(", ", end="")
            if hasattr(valor, "accept"):
                valor.accept(self)
            else:
                print(valor, end="")
        print(";")

    def visitorSplice(self, splice):
        print(f"splice {splice.escalar}, ", end="")
        for i, valor in enumerate(splice.quantidade):
            if i > 0:
                print(", ", end="")
            if hasattr(valor, "accept"):
                valor.accept(self)
            else:
                print(valor, end="")
        print(";")

    # ------------------Condicionais-------------------------------
    def visitorDeclaracaoCondicional(self, declaracao_condicional):
        declaracao_condicional.condicional.accept(self)

    def visitorDeclaracaoExpressao(self, declaracao_expressao):
        print(blank(), end="")
        declaracao_expressao.expressao.accept(self)
        print(";")

    def visitorDeclaracaoBloco(self, declaracao_bloco):
        for comando in declaracao_bloco.bloco:
            if hasattr(comando, "accept"):
                comando.accept(self)
            else:
                print(comando)

    def visitorCondicionalIf(self, condicional_if):
        print("if (", end="")
        condicional_if.condicao.accept(self)  
        print(") {")
        for stmt in condicional_if.bloco:     
            if hasattr(stmt, "accept"):
                stmt.accept(self)
            else:
                print(stmt)
        print("}")

    def visitorCondicionalIfElse(self, condicional_if_else):
        global tab
        # Chama o método base para o if, mas passa os atributos corretos
        print("if (", end="")
        condicional_if_else.condicao.accept(self)  
        print(") {")
        for stmt in condicional_if_else.bloco_if:     
            if hasattr(stmt, "accept"):
                stmt.accept(self)
            else:
                print(stmt)
        print("}")
        
        print(" else {")
        tab += 2
        for declaracao in condicional_if_else.bloco_else:
            if hasattr(declaracao, "accept"):
                declaracao.accept(self)
        tab -= 2
        print(blank() + "}")

    def visitorCondicionalIfElsif(self, condicional_if_elsif):
       
        print("if (", end="")
        condicional_if_elsif.condicao.accept(self)  
        print(") {")
        for stmt in condicional_if_elsif.bloco_if:     
            if hasattr(stmt, "accept"):
                stmt.accept(self)
            else:
                print(stmt)
        print("}")
        
        for elsif_node in condicional_if_elsif.elsifs:
            elsif_node.accept(self)

    def visitorCondicionalIfElsifElse(self, condicional_if_elsif_else):
        print("if (", end="")
        condicional_if_elsif_else.condicao.accept(self)  
        print(") {")
        
        for stmt in condicional_if_elsif_else.bloco_if:     
            if hasattr(stmt, "accept"):
                stmt.accept(self)
            else:
                print(stmt)
        
        print("}")
        
        for elsif_node in condicional_if_elsif_else.elsifs:
            elsif_node.accept(self)

        print(" else {")
        
        for declaracao in condicional_if_elsif_else.bloco_else:
            if hasattr(declaracao, "accept"):
                declaracao.accept(self)
        
        print("}")

    def visitorElsif(self, elsif):
        print(" elsif ", end="")
        elsif.condicao.accept(self)
        print(" {")
        
        for declaracao in elsif.bloco:
            if hasattr(declaracao, "accept"):
                declaracao.accept(self)
        
        print("}", end="")


def main():
    caminho = os.path.join(os.path.dirname(__file__), "main.raku")
    with open(caminho, "r", encoding="utf-8") as f:
        codigo = f.read()

    lexer = lexico.lexer
    parser = yacc.yacc(module=sintatico)
    result = parser.parse(codigo, lexer=lexer, debug=False)

    print("imprime o programa que foi passado como entrada")
    vis = visitor()

    if result is not None:
        if isinstance(result, list):
            for node in result:
                if node is not None:
                    if hasattr(node, "accept"):
                        node.accept(vis)
                    else:
                        print(node)
        else:
            if hasattr(result, "accept"):
                result.accept(vis)
            else:
                print(result)
    else:
        print("Erro: Parser retornou None")

if __name__ == "__main__":
    main()
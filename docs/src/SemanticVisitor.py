from AbstractVisitor import abstractvisitor
from SymbolTable import *
import lexico
import sintatico
import sintaxeabstrata as sa
import ply.lex as lex
import ply.yacc as yacc

# Tipos básicos
class Types:
    INT = 'int'
    FLOAT = 'float'
    BOOL = 'boolean'
    STR = 'str'
    LIST = 'list'
    ANY = 'any'
    VOID = 'void'

Number = [Types.INT, Types.FLOAT]

def coerce_numeric(a, b):
    if a == Types.FLOAT or b == Types.FLOAT:
        return Types.FLOAT
    if a == Types.INT and b == Types.INT:
        return Types.INT
    return None

#----------------------------Semantic Visitor----------------------------
class SemanticVisitor(abstractvisitor):
    def __init__(self):
        self.errors = 0
        beginScope("global")  # Garante que há um escopo global

    def report(self, msg):
        self.errors += 1
        print(f"[Semântico] Erro: {msg}")

#----------------------------Funções----------------------------
    def visitorCompoundFuncao(self, compoundFuncao):
        beginScope(compoundFuncao.id)
        if getattr(compoundFuncao, 'parametros', None):
            for p in compoundFuncao.parametros:
                addVar(p, Types.ANY)
        if hasattr(compoundFuncao, "comando") and hasattr(compoundFuncao.comando, "accept"):
            compoundFuncao.comando.accept(self)
        endScope()

    def visitorCompoundFuncaoSemParametros(self, compound):
        beginScope(compound.id)
        if hasattr(compound, "comando") and hasattr(compound.comando, "accept"):
            compound.comando.accept(self)
        endScope()

#----------------------------LOOPS----------------------------
    def visitorLoopFor(self, loopFor):
        beginScope(f"for_{getattr(loopFor, 'id', '')}")
        if getattr(loopFor, 'id', None):
            addVar(loopFor.id, Types.ANY)
        if getattr(loopFor, 'expr', None) and hasattr(loopFor.expr, "accept"):
            loopFor.expr.accept(self)
        if getattr(loopFor, 'comando', None) and hasattr(loopFor.comando, "accept"):
            loopFor.comando.accept(self)
        endScope()

    def visitorLoopWhile(self, loopWhile):
        beginScope("while")
        if getattr(loopWhile, 'limite', None) and hasattr(loopWhile.limite, "accept"):
            loopWhile.limite.accept(self)
        if getattr(loopWhile, 'comando', None) and hasattr(loopWhile.comando, "accept"):
            loopWhile.comando.accept(self)
        endScope()

    def visitorLoopRepeticao(self, loopRepeticao):
        beginScope("loop_repeticao")
        for instr in [getattr(loopRepeticao, 'instrucao1', None),
                      getattr(loopRepeticao, 'instrucao2', None),
                      getattr(loopRepeticao, 'instrucao3', None)]:
            if instr and hasattr(instr, "accept"):
                instr.accept(self)
        if getattr(loopRepeticao, 'comando', None) and hasattr(loopRepeticao.comando, "accept"):
            loopRepeticao.comando.accept(self)
        endScope()

    def visitorLoopSemCondicao(self, loopSemCondicao):
        beginScope("loop_sem_condicao")
        if getattr(loopSemCondicao, 'comando', None) and hasattr(loopSemCondicao.comando, "accept"):
            loopSemCondicao.comando.accept(self)
        endScope()
    
    def visitorDeclaracaoLoop(self, declaracaoLoop):
        if hasattr(declaracaoLoop.loop, "accept"):
            declaracaoLoop.loop.accept(self)

#----------------------------EXPRESSÕES----------------------------
    def visitorExpressaoOR(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoXOR(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoAND(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoIGUAL_DP(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoDIF(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoMAIOR(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoMENOR(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoMAIOR_IGUAL(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoMENOR_IGUAL(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoSMARTMATCH(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoADICAO(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoSUBTRACAO(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoCONCATENACAO(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoMULTIPLICACAO(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoDIVISAO(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoDIVISAO_INTEIRA(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoDIVISIBILIDADE(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoMOD(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoLCM(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoGCD(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoPOW(self, node):
        if hasattr(node, "esquerda") and hasattr(node.esquerda, "accept"):
            node.esquerda.accept(self)
        if hasattr(node, "direita") and hasattr(node.direita, "accept"):
            node.direita.accept(self)

    def visitorExpressaoNOT_OPERADOR(self, node):
        if hasattr(node, "valor") and hasattr(node.valor, "accept"):
            node.valor.accept(self)

    def visitorExpressaoNOT_SIMBULO(self, node):
        if hasattr(node, "valor") and hasattr(node.valor, "accept"):
            node.valor.accept(self)

    def visitorExpressao_PREFIXO_INCREMENTO(self, node):
        if hasattr(node, "valor") and hasattr(node.valor, "accept"):
            node.valor.accept(self)

    def visitorExpressao_POSFIXO_INCREMENTO(self, node):
        if hasattr(node, "valor") and hasattr(node.valor, "accept"):
            node.valor.accept(self)

    def visitorExpressao_PREFIXO_DECREMENTO(self, node):
        if hasattr(node, "valor") and hasattr(node.valor, "accept"):
            node.valor.accept(self)

    def visitorExpressao_POSFIXO_DECREMENTO(self, node):
        if hasattr(node, "valor") and hasattr(node.valor, "accept"):
            node.valor.accept(self)

    def visitorExpressao_PARENTESES(self, node):
        if hasattr(node, "valor") and hasattr(node.valor, "accept"):
            node.valor.accept(self)

    def visitorExpressao_VALOR(self, node):
        # literal, nada para visitar
        pass

    def visitorExpressao_TIPO(self, node):
        if hasattr(node, "valor") and hasattr(node.valor, "accept"):
            node.valor.accept(self)

#----------------------------DECLARAÇÕES----------------------------
    def visitorDeclaracaoEscalarMY(self, declaracao):
        if getattr(declaracao, 'escalar', None) in [None, ""]:
            self.report("Nome de variável escalar inválido.")
        else:
            addVar(declaracao.escalar, getattr(declaracao, 'tipo', Types.ANY))
        if getattr(declaracao, 'valor', None) and hasattr(declaracao.valor, "accept"):
            declaracao.valor.accept(self)

    def visitorDeclaracaoEscalarOUR(self, declaracao):
        if getattr(declaracao, 'escalar', None) in [None, ""]:
            self.report("Nome de variável escalar OUR inválido.")
        else:
            addVar(declaracao.escalar, getattr(declaracao, 'tipo', Types.ANY))
        if getattr(declaracao, 'valor', None) and hasattr(declaracao.valor, "accept"):
            declaracao.valor.accept(self)

    def visitorDeclaracaoLista(self, declaracao):
        if getattr(declaracao, 'lista', None) in [None, ""]:
            self.report("Nome de lista inválido.")
        else:
            addVar(declaracao.lista, Types.LIST)

    def visitorDeclaracaoListaMY(self, declaracao):
        if getattr(declaracao, 'lista', None) in [None, ""]:
            self.report("Nome de lista MY inválido.")
        else:
            addVar(declaracao.lista, Types.LIST)

    def visitorDeclaracaoListaOUR(self, declaracao):
        if getattr(declaracao, 'lista', None) in [None, ""]:
            self.report("Nome de lista OUR inválido.")
        else:
            addVar(declaracao.lista, Types.LIST)

    def visitorDeclaracaoExpressao(self, declaracao):
        if getattr(declaracao, 'expressao', None) and hasattr(declaracao.expressao, "accept"):
            declaracao.expressao.accept(self)

    def visitorDeclaracaoBloco(self, declaracao):
        if getattr(declaracao, 'bloco', None) and hasattr(declaracao.bloco, "accept"):
            declaracao.bloco.accept(self)

    def visitorComentario(self, comentario):
        pass

#----------------------------SAY----------------------------
    def visitorSAY(self, SAY):
        if getattr(SAY, 'valor', None) and hasattr(SAY.valor, "accept"):
            SAY.valor.accept(self)

#----------------------------CHAMADA DE FUNÇÃO E PARÂMETROS----------------------------
    def visitorPARAMETROS(self, PARAMETROS):
        if getattr(PARAMETROS, 'valor', None) and hasattr(PARAMETROS.valor, "accept"):
            PARAMETROS.valor.accept(self)

    def visitorPARAMETROSMULT(self, PARAMETROSMULT):
        for param in getattr(PARAMETROSMULT, 'valores', []):
            if hasattr(param, "accept"):
                param.accept(self)

    def visitorCHAMADA_FUNCAO(self, CHAMADA_FUNCAO):
        if getattr(CHAMADA_FUNCAO, 'parametros', None) and hasattr(CHAMADA_FUNCAO.parametros, "accept"):
            CHAMADA_FUNCAO.parametros.accept(self)

    def visitorCHAMADA_FUNCAO_SEM_PARAMETRO(self, CHAMADA_FUNCAO_SEM_PARAMETRO):
        pass

#----------------------------COMANDOS DE CONTROLE----------------------------
    def visitorBreak(self, Break):
        pass

    def visitorExit(self, Exit):
        pass

    def visitorLast(self, Last):
        pass

    def visitorNext(self, Next):
        pass

    def visitorRedo(self, Redo):
        pass

    def visitorReturn(self, Return):
        if getattr(Return, 'valor', None) and hasattr(Return.valor, "accept"):
            Return.valor.accept(self)

    def visitorConstant(self, Constant):
        pass

    def visitorState(self, State):
        pass

    def visitorMulti(self, Multi):
        pass

    def visitorOnly(self, Only):
        pass

    def visitorExport(self, Export):
        pass

    def visitorImport(self, Import):
        pass

    def visitorNeed(self, Need):
        pass

    def visitorRequire(self, Require):
        pass

    def visitorUse(self, Use):
        pass

    def visitorPush(self, Push):
        pass

    def visitorUnshift(self, Unshift):
        pass

    def visitorSplice(self, Splice):
        pass

#----------------------------CONDICIONAIS----------------------------
    def visitorCondicionalIf(self, cond):
        if getattr(cond, 'condicao', None) and hasattr(cond.condicao, "accept"):
            cond.condicao.accept(self)
        if getattr(cond, 'bloco_if', None) and hasattr(cond.bloco_if, "accept"):
            cond.bloco_if.accept(self)

    def visitorCondicionalIfElse(self, condicionalIfElse):
        if getattr(condicionalIfElse, 'condicao', None) and hasattr(condicionalIfElse.condicao, "accept"):
            condicionalIfElse.condicao.accept(self)
        if getattr(condicionalIfElse, 'bloco_if', None) and hasattr(condicionalIfElse.bloco_if, "accept"):
            condicionalIfElse.bloco_if.accept(self)
        if getattr(condicionalIfElse, 'bloco_else', None) and hasattr(condicionalIfElse.bloco_else, "accept"):
            condicionalIfElse.bloco_else.accept(self)

    def visitorCondicionalIfElsif(self, condicionalIfElsif):
        if getattr(condicionalIfElsif, 'condicao', None) and hasattr(condicionalIfElsif.condicao, "accept"):
            condicionalIfElsif.condicao.accept(self)
        if getattr(condicionalIfElsif, 'bloco_if', None) and hasattr(condicionalIfElsif.bloco_if, "accept"):
            condicionalIfElsif.bloco_if.accept(self)
        for elsif in getattr(condicionalIfElsif, 'elsifs', []):
            if hasattr(elsif, "accept"):
                elsif.accept(self)

    def visitorCondicionalIfElsifElse(self, condicionalIfElsifElse):
        if getattr(condicionalIfElsifElse, 'condicao', None) and hasattr(condicionalIfElsifElse.condicao, "accept"):
            condicionalIfElsifElse.condicao.accept(self)
        if getattr(condicionalIfElsifElse, 'bloco_if', None) and hasattr(condicionalIfElsifElse.bloco_if, "accept"):
            condicionalIfElsifElse.bloco_if.accept(self)
        for elsif in getattr(condicionalIfElsifElse, 'elsifs', []):
            if hasattr(elsif, "accept"):
                elsif.accept(self)
        if getattr(condicionalIfElsifElse, 'bloco_else', None) and hasattr(condicionalIfElsifElse.bloco_else, "accept"):
            condicionalIfElsifElse.bloco_else.accept(self)

    def visitorElsif(self, elsif):
        if getattr(elsif, 'condicao', None) and hasattr(elsif.condicao, "accept"):
            elsif.condicao.accept(self)
        if getattr(elsif, 'bloco', None) and hasattr(elsif.bloco, "accept"):
            elsif.bloco.accept(self)

    def visitorDeclaracaoCondicional(self, declaracaoCondicional):
        if getattr(declaracaoCondicional, 'condicao', None) and hasattr(declaracaoCondicional.condicao, "accept"):
            declaracaoCondicional.condicao.accept(self)

#----------------------------MAIN----------------------------

def main():
    with open("main.raku", "r", encoding="utf-8") as f:
        code = f.read()
    lexer = lex.lex(module=lexico)
    parser = yacc.yacc(module=sintatico)
    ast = parser.parse(code, lexer=lexer, debug=False)
    print("Checando semântica…")
    s = SemanticVisitor()
    if isinstance(ast, list):
        for node in ast:
            if hasattr(node, "accept"):
                node.accept(s)
    else:
        if hasattr(ast, "accept"):
            ast.accept(s)
    print(f"Foram encontrados {s.errors} erro(s) semântico(s).")

if __name__ == "__main__":
    main()

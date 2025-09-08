from abc import abstractmethod
from abc import ABCMeta

#Funções

class Funcao(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class CompoundFuncao(Funcao):
    def __init__(self, id, parametros, comando):
        self.id= id
        self.parametros = parametros
        self.comando = comando
    def accept(self, visitor):
        return visitor.visitCompoundFuncao(self)

class CompoundFuncaoSemParametros(Funcao):
    def __init__(self, id, comando):
        self.id= id
        self.comando = comando
    def accept(self, visitor):
        return visitor.visitCompoundFuncaoSemParametros(self)


    

class Loop(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class LoopFor(Loop):
    def __init__(self, expr, id, comando):
        self.expr = expr         
        self.id= id           
        self.comando = comando    
    
    def accept(self, visitor):
        return visitor.visitLoopFor(self)

class LoopWhile(Loop):
    def __init__(self, limite, comando):      
        self.limite = limite    
        self.comando = comando  
    
    def accept(self, visitor):
        return visitor.visitLoopWhile(self)

class LoopRepeticao(Loop):
    def __init__(self, instrucao1, instrucao2, instrucao3, comando):
        self.instrucao1 = instrucao1   
        self.instrucao2 = instrucao2   
        self.instrucao3 = instrucao3   
        self.comando = comando
    
    def accept(self, visitor):
        return visitor.visitLoopRepeticao(self)

class LoopSemCondicao(Loop):
    def __init__(self, comando):
        self.comando = comando
    
    def accept(self, visitor):
        return visitor.visitLoopSemCondicao(self)

# Operações

class Expressao(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpressaoOR(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoOR(self)

class ExpressaoXOR(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoXOR(self)

class ExpressaoAND(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoAND(self)

class ExpressaoIGUAL_DP(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoIGUAL_DP(self)

class ExpressaoDIF(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoDIF(self)
    
class ExpressaoMAIOR(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoMAIOR(self)
    
class ExpressaoMENOR(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoMAIOR(self)

class ExpressaoMAIOR_IGUAL(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoMAIOR(self)

class ExpressaoMENOR_IGUAL(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoMAIOR(self)

class ExpressaoSMARTMATCH(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoSMARTMATCH(self)
    
class ExpressaoADICAO(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoADICAO(self)

class ExpressaoSUBTRACAO(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoSUBTRACAO(self)    

class ExpressaoCONCATENACAO(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoCONCATENACAO(self)   

class ExpressaoMULTIPLICACAO(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoCONCATENACAO(self)   

class ExpressaoDIVISAO(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoDIVISAO(self)   

class ExpressaoDIVISAO_INTEIRA(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoDIVISAO_INTEIRA(self)

class ExpressaoDIVISIBILIDADE(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoDIVISIBILIDADE(self)

class ExpressaoMOD(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoMOD(self)  

class ExpressaoLCM(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoLCM(self)  

class ExpressaoGCD(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoGCD(self) 

class ExpressaoPOW(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitorExpressaoPOW(self)  

class ExpressaoNOT_OPERADOR(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitorNOT_OPERADOR(self)  

class Expressao_NOT_SIMBULO(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitorNOT_SIMBULO(self) 

class Expressao_PREFIXO_INCREMENTO(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitor_PREFIXO_INCREMENTO(self)
    
class Expressao_POSFIXO_INCREMENTO(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitor_POSFIXO_INCREMENTO(self)
    
class Expressao_PREFIXO_DECREMENTO(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitor_PREFIXO_DECREMENTO(self)
    
class Expressao_POSFIXO_DECREMENTO(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitor_POSFIXO_INCREMENTO(self)

class Expressao_PARENTESES(Expressao):
    def __init__(self, expressao):
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitor_PARENTESES(self)

class Expressao_VALOR(Expressao):
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

    def accept(self, visitor):
        return visitor.visitor_VALOR(self)

class Expressao_TIPO(Expressao):
    def __init__(self, tipo):
        self.tipo = tipo

    def accept(self, visitor):
        return visitor.visitor_TIPO(self)

class SAY(Expressao):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitor_SAY(self)

class PARAMETROS(Expressao):
    def __init__(self, escalar):
        self.escalar = escalar
    
    def accept(self, visitor):
        return visitor.visitor_PARAMETROS(self)

class PARAMETROSMULT(Expressao):
    def __init__(self, escalar, outros_parametros):
        self.escalar = escalar
        self.outros_parametros = outros_parametros

    def accept(self, visitor):
        return visitor.visitor_PARAMETROSMULT(self)

class CHAMADA_FUNCAO(Expressao):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor

    def accept(self, visitor):
        return visitor.visitor_CHAMADA_FUNCAO(self)
        
class CHAMADA_FUNCAO_SEM_PARAMETRO(Expressao):
    def __init__(self, id):
        self.id = id
        
    def accept(self, visitor):
        return visitor.visitor_CHAMADA_FUNCAO_SEM_PARAMETRO(self)

class Atribuicao(Expressao):
    def __init__(self, variavel, valor):
        self.variavel = variavel
        self.valor = valor
        
    def accept(self, visitor):
        return visitor.visitorAtribuicao(self)
# --- Comentario --- 

class Comentario():
    def __init__(self, comentario) -> None:
        self.comentario = comentario

    def accept(self, visitor):
        return visitor.visitorComentario(self)
    
# --- CONTROLE DE FLUXO ---

class Break(Expressao):
    def accept(self, visitor):
        return visitor.visitorBreak(self)

class Exit(Expressao):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitorExit(self)

class Last(Expressao):
    def accept(self, visitor):
        return visitor.visitorLast(self)

class Next(Expressao):
    def accept(self, visitor):
        return visitor.visitorNext(self)

class Redo(Expressao):
    def accept(self, visitor):
        return visitor.visitorRedo(self)

class Return(Expressao):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitorReturn(self)


 # --- DECLARAÇÕES E ESCOPO ---

class Constant(Expressao):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor
    def accept(self, visitor):
        return visitor.visitorConstant(self)

class State(Expressao):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor
    def accept(self, visitor):
        return visitor.visitorState(self)

class Multi(Expressao):
    def __init__(self, comando):
        self.comando = comando
    def accept(self, visitor):
        return visitor.visitorMulti(self)

class Only(Expressao):
    def __init__(self, comando):
        self.comando = comando
    def accept(self, visitor):
        return visitor.visitorOnly(self)
    
# --- IMPORTAÇÃO E MODULARIZAÇÃO ---

class Export(Expressao):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitorExport(self)

class Import(Expressao):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitorImport(self)

class Need(Expressao):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitorNeed(self)

class Require(Expressao):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitorRequire(self)

class Use(Expressao):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitorUse(self)
        
# --- OPERAÇÕES EM LISTAS ---

class Push(Expressao):
    def __init__(self, escalar, valores):
        self.escalar = escalar
        self.valores = valores
    def accept(self, visitor):
        return visitor.visitorPush(self)

class Unshift(Expressao):
    def __init__(self, escalar, valores):
        self.escalar = escalar
        self.valores = valores
    def accept(self, visitor):
        return visitor.visitorUnshift(self)

class Splice(Expressao):
    def __init__(self, escalar, quantidade):
        self.escalar = escalar
        self.quantidade = quantidade
    def accept(self, visitor):
        return visitor.visitorSplice(self)
    
class DeclaracaoEscalarMY:
    def __init__(self, tipo, escalar, valor):
        self.tipo = tipo
        self.escalar = escalar
        self.valor = valor
    def accept(self, visitor):
        return visitor.visitDeclaracaoEscalarMY(self)
    

class DeclaracaoEscalarOUR:
    def __init__(self, escalar, valor):
        self.escalar = escalar
        self.valor = valor
    def accept(self, visitor):
        return visitor.visitDeclaracaoEscalarOUR(self)

class DeclaracaoLista:
    def __init__(self, lista, valores):
        self.lista = lista
        self.valores = valores
    def accept(self, visitor):
        return visitor.visitDeclaracaoLista(self)
    
class DeclaracaoListaMY:
    def __init__(self, lista, valores):
        self.lista = lista
        self.valores = valores
    def accept(self, visitor):
        return visitor.visitDeclaracaoListaMY(self)
    
class DeclaracaoListaOUR:
    def __init__(self, lista, valores):
        self.lista = lista
        self.valores = valores
    def accept(self, visitor):
        return visitor.visitDeclaracaoListaOUR(self)
    
class LoopForLista(Loop):
    def __init__(self, lista, escalar, comandos):
        self.lista = lista
        self.escalar = escalar
        self.comandos = comandos
    def accept(self, visitor):
        return visitor.visitLoopForLista(self)
    
class CondicionalIf:
    def __init__(self, condicao, bloco):
        self.condicao = condicao
        self.bloco = bloco
    def accept(self, visitor):
        return visitor.visitCondicionalIf(self)

class CondicionalIfElse:
    def __init__(self, condicao, bloco_if, bloco_else):
        self.condicao = condicao
        self.bloco_if = bloco_if
        self.bloco_else = bloco_else
    def accept(self, visitor):
        return visitor.visitCondicionalIfElse(self)

class CondicionalIfElsif:
    def __init__(self, condicao, bloco_if, elsifs):
        self.condicao = condicao
        self.bloco_if = bloco_if
        self.elsifs = elsifs
    def accept(self, visitor):
        return visitor.visitCondicionalIfElsif(self)

class CondicionalIfElsifElse:
    def __init__(self, condicao, bloco_if, elsifs, bloco_else):
        self.condicao = condicao
        self.bloco_if = bloco_if
        self.elsifs = elsifs
        self.bloco_else = bloco_else
    def accept(self, visitor):
        return visitor.visitCondicionalIfElsifElse(self)

class Elsif:
    def __init__(self, condicao, bloco):
        self.condicao = condicao
        self.bloco = bloco
    def accept(self, visitor):
        return visitor.visitElsif(self)

class DeclaracaoCondicional:
    def __init__(self, condicional):
        self.condicional = condicional
    def accept(self, visitor):
        return visitor.visitDeclaracaoCondicional(self)

class DeclaracaoLoop:
    def __init__(self, loop):
        self.loop = loop
    def accept(self, visitor):
        return visitor.visitDeclaracaoLoop(self)

class DeclaracaoExpressao:
    def __init__(self, expressao):
        self.expressao = expressao
    def accept(self, visitor):
        return visitor.visitDeclaracaoExpressao(self)

class DeclaracaoBloco:
    def __init__(self, bloco):
        self.bloco = bloco
    def accept(self, visitor):
        return visitor.visitDeclaracaoBloco(self)
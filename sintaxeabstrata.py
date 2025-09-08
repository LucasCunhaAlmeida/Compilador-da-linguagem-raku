from abc import abstractmethod
from abc import ABCMeta

#Funções

#--------------------------função------------------------
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


    
#--------------------------     Repetição------------------------
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


class LoopTimes(Loop):
    def __init__(self, integer, id, comando):
        self.integer = integer
        self.id = id
        self.comando = comando
    
    def accept(self, visitor):
        return visitor.visitLoopTimes(self)

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

#--------------------------Expressões------------------------

class Expressao(metaclass = ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpressaoOR(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoOR(self)

class ExpressaoXOR(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoXOR(self)

class ExpressaoAND(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoAND(self)

class ExpressaoIGUAL_DP(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoIGUAL_DP(self)

class ExpressaoDIF(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoDIF(self)
    
class ExpressaoMAIOR(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoMAIOR(self)
    
class ExpressaoMENOR(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoMENOR(self)

class ExpressaoMAIOR_IGUAL(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoMAIOR(self)

class ExpressaoMENOR_IGUAL(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoMAIOR(self)

class ExpressaoSMARTMATCH(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoSMARTMATCH(self)
    
class ExpressaoADICAO(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoADICAO(self)

class ExpressaoSUBTRACAO(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoSUBTRACAO(self)    

class ExpressaoCONCATENACAO(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoCONCATENACAO(self)   

class ExpressaoMULTIPLICACAO(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoMULTIPLICACAO(self)   

class ExpressaoDIVISAO(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoDIVISAO(self)   

class ExpressaoDIVISAO_INTEIRA(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoDIVISAO_INTEIRA(self)

class ExpressaoDIVISIBILIDADE(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoDIVISIBILIDADE(self)

class ExpressaoMOD(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoMOD(self)  

class ExpressaoLCM(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoLCM(self)  

class ExpressaoGCD(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoGCD(self) 

class ExpressaoPOW(Expressao):
    def __init__(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def accept(self, visitor):
        return visitor.visitExpressaoPOW(self)  

class ExpressaoNOT_OPERADOR(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitExpressaoNOT_OPERADOR(self)  

class Expressao_NOT_SIMBULO(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitExpressao_NOT_SIMBULO(self) 

class Expressao_PREFIXO_INCREMENTO(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitExpressao_PREFIXO_INCREMENTO(self)
    
class Expressao_POSFIXO_INCREMENTO(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitExpressao_POSFIXO_INCREMENTO(self)
    
class Expressao_PREFIXO_DECREMENTO(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitExpressao_PREFIXO_DECREMENTO(self)
    
class Expressao_POSFIXO_DECREMENTO(Expressao):
    def __init__(self, operando):
        self.operando = operando

    def accept(self, visitor):
        return visitor.visitExpressao_POSFIXO_DECREMENTO(self)

class Expressao_PARENTESES(Expressao):
    def __init__(self, expressao):
        self.expressao = expressao

    def accept(self, visitor):
        return visitor.visitExpressao_PARENTESES(self)

class Expressao_VALOR(Expressao):
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo

    def accept(self, visitor):
        return visitor.visitExpressao_VALOR(self)

class Expressao_TIPO(Expressao):
    def __init__(self, tipo):
        self.tipo = tipo

    def accept(self, visitor):
        return visitor.visitExpressao_TIPO(self)

class SAY(Expressao):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitSAY(self)

class PARAMETROS(Expressao):
    def __init__(self, escalar):
        self.escalar = escalar
    
    def accept(self, visitor):
        return visitor.visitPARAMETROS(self)

class PARAMETROSMULT(Expressao):
    def __init__(self, escalar, outros_parametros):
        self.escalar = escalar
        self.outros_parametros = outros_parametros

    def accept(self, visitor):
        return visitor.visitPARAMETROSMULT(self)


# ------------------Chamada Funções-------------------------------
class CHAMADA_FUNCAO(Expressao):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor

    def accept(self, visitor):
        return visitor.visitCHAMADA_FUNCAO(self)
        
class CHAMADA_FUNCAO_SEM_PARAMETRO(Expressao):
    def __init__(self, id):
        self.id = id
        
    def accept(self, visitor):
        return visitor.visitCHAMADA_FUNCAO_SEM_PARAMETRO(self)




 # ------------------Controle de Fluxo-------------------------------

class Break(Expressao):
    def accept(self, visitor):
        return visitor.visitBreak(self)

class Exit(Expressao):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitExit(self)

class Last(Expressao):
    def accept(self, visitor):
        return visitor.visitLast(self)

class Next(Expressao):
    def accept(self, visitor):
        return visitor.visitNext(self)

class Redo(Expressao):
    def accept(self, visitor):
        return visitor.visitRedo(self)

class Return(Expressao):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitReturn(self)


 # --- DECLARAÇÕES E ESCOPO ---------------

class Constant(Expressao):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor
    def accept(self, visitor):
        return visitor.visitConstant(self)

class State(Expressao):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor
    def accept(self, visitor):
        return visitor.visitState(self)

class Let(Expressao):
    def __init__(self, id, valor):
        self.id = id
        self.valor = valor
    def accept(self, visitor):
        return visitor.visitLet(self)

class Multi(Expressao):
    def __init__(self, id, parametros, comando):
        self.id = id
        self.parametros = parametros
        self.comando = comando
    def accept(self, visitor):
        return visitor.visitMulti(self)

class Only(Expressao):
    def __init__(self, id, comando):
        self.id = id
        self.comando = comando
    def accept(self, visitor):
        return visitor.visitOnly(self)

class Unit(Expressao):
    def accept(self, visitor):
        return visitor.visitUnit(self)
    

    
# --- IMPORTAÇÃO E MODULARIZAÇÃO --------------------

class Export(Expressao):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitExport(self)

class Import(Expressao):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitImport(self)

class Need(Expressao):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitNeed(self)

class Require(Expressao):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitRequire(self)

class Use(Expressao):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitUse(self)
        
 # ------------------Operações em Listas-------------------------------

class Push(Expressao):
    def __init__(self, escalar, valores):
        self.escalar = escalar
        self.valores = valores
    def accept(self, visitor):
        return visitor.visitPush(self)

class Unshift(Expressao):
    def __init__(self, escalar, valores):
        self.escalar = escalar
        self.valores = valores
    def accept(self, visitor):
        return visitor.visitUnshift(self)

class Splice(Expressao):
    def __init__(self, escalar, inicio, quantidade):
        self.escalar = escalar
        self.inicio = inicio
        self.quantidade = quantidade
    def accept(self, visitor):
        return visitor.visitSplice(self)
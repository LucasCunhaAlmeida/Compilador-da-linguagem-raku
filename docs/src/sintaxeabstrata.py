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


class LoopTimes(Loop):
    def __init__(self, integer, id, comando):
        self.integer = integer
        self.id = id
        self.comando = comando
    
    def accept(self, visitor):
        return visitor.visitLoopTimes(self)

class LoopWhile(Loop):
    def __init__(self, id, limite, comando):
        self.id = id         
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

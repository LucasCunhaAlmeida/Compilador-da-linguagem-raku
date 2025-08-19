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
    def accept(self):
        pass

class CompoundFuncaoSemParametros(Funcao):
    def __init__(self, id, comando):
        self.id= id
        self.comando = comando
    def accept(self):
        pass

# Estruturas de Repetição

class Loop(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class LoopFor(Loop):
    def __init__(self, expr, id, comando):
        self.expr = expr         
        self.id= id           
        self.comando = comando    
    
    def accept(self):
        pass


class LoopTimes(Loop):
    def __init__(self, integer, id, comando):
        self.integer = integer
        self.id = id
        self.comando = comando
    
    def accept(self):
        pass


class LoopWhile(Loop):
    def __init__(self, id, limite, comando):
        self.id = id         
        self.limite = limite    
        self.comando = comando  
    
    def accept(self):
        pass

class LoopRepeticao(Loop):
    def __init__(self, instrucao1, instrucao2, instrucao3, comando):
        self.instrucao1 = instrucao1   
        self.instrucao2 = instrucao2   
        self.instrucao3 = instrucao3   
        self.comando = comando
    
    def accept(self):
        pass

class LoopSemCondicao(Loop):
    def __init__(self, comando):
        self.comando = comando
    
    def accept(self):
        pass

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

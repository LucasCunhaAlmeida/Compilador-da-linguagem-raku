from abc import abstractmethod
from abc import ABCMeta

class Funcao(metaclass=ABCMeta):
@abstractmethod
def accept(self):
pass

class CompoundFuncao(Funcao):
def __init__(self, parametros, comando):
self.parametros = parametros
self.comando = comando
def accept(self):
  pass

class CompoundFuncaoSemParametros(Funcao):
def __init__(self, comando):
self.comando = comando
def accept(self):
  pass

# Estruturas de Repetição

class Loop(metaclass=ABCMeta):
    @abstractmethod
    def accept(self):
        pass

class loopFor(Loop):
    def __init__(self, expr, id, comando):
        self.expr = expr         
        self.id= id           
        self.comando = comando    
    
    def accept(self):
        pass


class loopTimes(Loop):
    def __init__(self, integer, id, comando):
        self.integer = integer
        self.id = id
        self.comando = comando
    
    def accept(self):
        pass


class loopWhile(Loop):
    def __init__(self, id, limite, comando):
        self.id = id         
        self.limite = limite    
        self.comando = comando  
    
    def accept(self):
        pass

class loopRepeticao(Loop):
    def __init__(self, instrucao1, instrucao2, instrucao3, comando):
        self.instrucao1 = instrucao1   
        self.instrucao2 = instrucao2   
        self.instrucao3 = instrucao3   
        self.comando = comando
    
    def accept(self):
        pass

class loopSemCondicao(Loop):
    def __init__(self, comando):
        self.comando = comando
    
    def accept(self):
        pass







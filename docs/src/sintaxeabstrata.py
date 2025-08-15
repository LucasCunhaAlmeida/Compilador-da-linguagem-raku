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

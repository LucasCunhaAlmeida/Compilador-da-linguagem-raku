from abc import abstractmethod, ABCMeta

class abstractVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visitLoopFor(self, loopFor):
        pass

    @abstractmethod
    def visitLoopTimes(self, loopTimes):
        pass

    @abstractmethod
    def visitLoopWhile(self, loopWhile):
        pass

    @abstractmethod
    def visitLoopRepeticao(self, loopRepeticao):
        pass

    @abstractmethod
    def visitLoopSemCondicao(self, loopSemCondicao):
        pass

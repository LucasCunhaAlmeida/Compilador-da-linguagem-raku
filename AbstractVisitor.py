from abc import abstractmethod, ABCMeta

class abstractVisitor(metaclass=ABCMeta):


    @abstractmethod
    def visitCompoundFuncao(self, compoundFuncao):
        pass

    @abstractmethod
    def visitCompoundFuncaoSemParametros(self, CompoundFuncaoSemParametros):
        pass

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

    @abstractmethod
    def visitExpressaoOR(self, ExpressaoOR):
        pass
    
    @abstractmethod
    def visitExpressaoXOR(self, ExpressaoXOR):
        pass

    @abstractmethod
    def visitExpressaoAND(self, ExpressaoAND):
        pass

    @abstractmethod
    def visitExpressaoIGUAL_DP(self, ExpressaoIGUAL_DP):
        pass
    
    @abstractmethod
    def visitExpressaoDIF(self, ExpressaoDIF):
        pass

    @abstractmethod
    def visitExpressaoMAIOR(self, ExpressaoMAIOR):
        pass

    @abstractmethod
    def visitExpressaoMENOR(self, ExpressaoMENOR):
        pass

    @abstractmethod
    def visitExpressaoMAIOR_IGUAL(self, ExpressaoMAIOR_IGUAL):
        pass

    @abstractmethod
    def visitExpressaoMENOR_IGUAL(self, ExpressaoMENOR_IGUAL):
        pass

    @abstractmethod
    def visitExpressaoSMARTMATCH(self, ExpressaoSMARTMATCH):
        pass

    @abstractmethod
    def visitExpressaoADICAO(self, ExpressaoADICAO):
        pass
    
    @abstractmethod
    def visitExpressaoSUBTRACAO(self, ExpressaoSUBTRACAO):
        pass

    @abstractmethod
    def visitExpressaoCONCATENACAO(self, ExpressaoCONCATENACAO):
        pass

    @abstractmethod
    def visitExpressaoMULTIPLICACAO(self, ExpressaoMULTIPLICACAO):
        pass

    @abstractmethod
    def visitExpressaoDIVISAO(self, ExpressaoDIVISAO):
        pass

    @abstractmethod
    def visitExpressaoDIVISAO_INTEIRA(self, ExpressaoDIVISAO_INTEIRA):
        pass

    @abstractmethod
    def visitExpressaoDIVISIBILIDADE(self, ExpressaoDIVISIBILIDADE):
        pass

    @abstractmethod
    def visitExpressaoMOD(self, ExpressaoMOD):
        pass

    @abstractmethod
    def visitExpressaoLCM(self, ExpressaoLCM):
        pass

    @abstractmethod
    def visitExpressaoGCD(self, ExpressaoGCD):
        pass

    @abstractmethod
    def visitExpressaoPOW(self, ExpressaoPOW):
        pass

    @abstractmethod
    def visitExpressaoNOT_OPERADOR(self, ExpressaoNOT_OPERADOR):
        pass

    @abstractmethod
    def visitExpressao_NOT_SIMBULO(self, Expressao_NOT_SIMBULO):
        pass

    @abstractmethod
    def visitExpressao_PREFIXO_INCREMENTO(self, Expressao_PREFIXO_INCREMENTO):
        pass
    
    @abstractmethod
    def visitExpressao_POSFIXO_INCREMENTO(self, Expressao_POSFIXO_INCREMENTO):
        pass

    @abstractmethod
    def visitExpressao_PREFIXO_DECREMENTO(self, Expressao_PREFIXO_DECREMENTO):
        pass

    @abstractmethod
    def visitExpressao_POSFIXO_DECREMENTO(self, Expressao_POSFIXO_DECREMENTO):
        pass

    @abstractmethod
    def visitExpressao_PARENTESES(self, Expressao_PARENTESES):
        pass

    @abstractmethod
    def visitExpressao_VALOR(self, Expressao_VALOR):
        pass

    @abstractmethod
    def visitExpressao_TIPO(self, Expressao_TIPO):
        pass

    @abstractmethod
    def visitSAY(self, SAY):
        pass

    @abstractmethod
    def visitPARAMETROS(self, PARAMETROS):
        pass

    @abstractmethod
    def visitPARAMETROSMULT(self, PARAMETROSMULT):
        pass

    @abstractmethod
    def visitCHAMADA_FUNCAO(self, CHAMADA_FUNCAO):
        pass

    @abstractmethod
    def visitCHAMADA_FUNCAO_SEM_PARAMETRO(self, CHAMADA_FUNCAO_SEM_PARAMETRO):
        pass

    @abstractmethod
    def visitBreak(self, Break):
        pass

    @abstractmethod
    def visitExit(self, Exit):
        pass
    
    @abstractmethod
    def visitLast(self, Last):
        pass

    @abstractmethod
    def visitNext(self, Next):
        pass

    @abstractmethod
    def visitRedo(self, Redo):
        pass

    @abstractmethod
    def visitReturn(self, Return):
        pass

    @abstractmethod
    def visitConstant(self, Constant):
        pass

    @abstractmethod
    def visitState(self, State):
        pass

    @abstractmethod
    def visitLet(self, Let):
        pass

    @abstractmethod
    def visitMulti(self, Multi):
        pass

    @abstractmethod
    def visitOnly(self, Only):
        pass

    #@abstractmethod
    #def visitUnit(self, Unit):
        #pass

    @abstractmethod
    def visitExport(self, Export):
        pass
    
    @abstractmethod
    def visitImport(self, Import):
        pass
    
    @abstractmethod
    def visitNeed(self, Need):
        pass

    @abstractmethod
    def visitRequire(self, Require):
        pass

    @abstractmethod
    def visitUse(self, Use):
        pass

    @abstractmethod
    def visitPush(self, Push):
        pass

    @abstractmethod
    def visitUnshift(self, Unshift):
        pass

    @abstractmethod
    def visitSplice(self, Splice):
        pass
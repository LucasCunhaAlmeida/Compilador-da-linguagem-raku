from abc import abstractmethod, ABCMeta

class abstractvisitor(metaclass=ABCMeta):


    @abstractmethod
    def visitorCompoundFuncao(self, compoundFuncao):
        pass

    @abstractmethod
    def visitorCompoundFuncaoSemParametros(self, CompoundFuncaoSemParametros):
        pass

    @abstractmethod
    def visitorLoopFor(self, loopFor):
        pass

    @abstractmethod
    def visitorLoopWhile(self, loopWhile):
        pass

    @abstractmethod
    def visitorLoopRepeticao(self, loopRepeticao):
        pass

    @abstractmethod
    def visitorLoopSemCondicao(self, loopSemCondicao):
        pass

    @abstractmethod
    def visitorExpressaoOR(self, ExpressaoOR):
        pass
    
    @abstractmethod
    def visitorExpressaoXOR(self, ExpressaoXOR):
        pass

    @abstractmethod
    def visitorExpressaoAND(self, ExpressaoAND):
        pass

    @abstractmethod
    def visitorExpressaoIGUAL_DP(self, ExpressaoIGUAL_DP):
        pass
    
    @abstractmethod
    def visitorExpressaoDIF(self, ExpressaoDIF):
        pass

    @abstractmethod
    def visitorExpressaoMAIOR(self, ExpressaoMAIOR):
        pass

    @abstractmethod
    def visitorExpressaoMENOR(self, ExpressaoMENOR):
        pass

    @abstractmethod
    def visitorExpressaoMAIOR_IGUAL(self, ExpressaoMAIOR_IGUAL):
        pass

    @abstractmethod
    def visitorExpressaoMENOR_IGUAL(self, ExpressaoMENOR_IGUAL):
        pass

    @abstractmethod
    def visitorExpressaoSMARTMATCH(self, ExpressaoSMARTMATCH):
        pass

    @abstractmethod
    def visitorExpressaoADICAO(self, ExpressaoADICAO):
        pass
    
    @abstractmethod
    def visitorExpressaoSUBTRACAO(self, ExpressaoSUBTRACAO):
        pass

    @abstractmethod
    def visitorExpressaoCONCATENACAO(self, ExpressaoCONCATENACAO):
        pass

    @abstractmethod
    def visitorExpressaoMULTIPLICACAO(self, ExpressaoMULTIPLICACAO):
        pass

    @abstractmethod
    def visitorExpressaoDIVISAO(self, ExpressaoDIVISAO):
        pass

    @abstractmethod
    def visitorExpressaoDIVISAO_INTEIRA(self, ExpressaoDIVISAO_INTEIRA):
        pass

    @abstractmethod
    def visitorExpressaoDIVISIBILIDADE(self, ExpressaoDIVISIBILIDADE):
        pass

    @abstractmethod
    def visitorExpressaoMOD(self, ExpressaoMOD):
        pass

    @abstractmethod
    def visitorExpressaoLCM(self, ExpressaoLCM):
        pass

    @abstractmethod
    def visitorExpressaoGCD(self, ExpressaoGCD):
        pass

    @abstractmethod
    def visitorExpressaoPOW(self, ExpressaoPOW):
        pass

    @abstractmethod
    def visitorExpressaoNOT_OPERADOR(self, ExpressaoNOT_OPERADOR):
        pass

    @abstractmethod
    def visitorExpressaoNOT_SIMBULO(self, Expressao_NOT_SIMBULO):
        pass

    @abstractmethod
    def visitorExpressao_PREFIXO_INCREMENTO(self, Expressao_PREFIXO_INCREMENTO):
        pass
    
    @abstractmethod
    def visitorExpressao_POSFIXO_INCREMENTO(self, Expressao_POSFIXO_INCREMENTO):
        pass

    @abstractmethod
    def visitorExpressao_PREFIXO_DECREMENTO(self, Expressao_PREFIXO_DECREMENTO):
        pass

    @abstractmethod
    def visitorExpressao_POSFIXO_DECREMENTO(self, Expressao_POSFIXO_DECREMENTO):
        pass

    @abstractmethod
    def visitorExpressao_PARENTESES(self, Expressao_PARENTESES):
        pass

    @abstractmethod
    def visitorExpressao_VALOR(self, Expressao_VALOR):
        pass

    @abstractmethod
    def visitorExpressao_TIPO(self, Expressao_TIPO):
        pass

    @abstractmethod
    def visitorSAY(self, SAY):
        pass

    @abstractmethod
    def visitorPARAMETROS(self, PARAMETROS):
        pass

    @abstractmethod
    def visitorPARAMETROSMULT(self, PARAMETROSMULT):
        pass

    @abstractmethod
    def visitorCHAMADA_FUNCAO(self, CHAMADA_FUNCAO):
        pass

    @abstractmethod
    def visitorCHAMADA_FUNCAO_SEM_PARAMETRO(self, CHAMADA_FUNCAO_SEM_PARAMETRO):
        pass

    @abstractmethod
    def visitorBreak(self, Break):
        pass

    @abstractmethod
    def visitorExit(self, Exit):
        pass
    
    @abstractmethod
    def visitorLast(self, Last):
        pass

    @abstractmethod
    def visitorNext(self, Next):
        pass

    @abstractmethod
    def visitorRedo(self, Redo):
        pass

    @abstractmethod
    def visitorReturn(self, Return):
        pass

    @abstractmethod
    def visitorConstant(self, Constant):
        pass

    @abstractmethod
    def visitorState(self, State):
        pass

    @abstractmethod
    def visitorLet(self, Let):
        pass

    @abstractmethod
    def visitorMulti(self, Multi):
        pass

    @abstractmethod
    def visitorOnly(self, Only):
        pass

    @abstractmethod
    def visitorExport(self, Export):
        pass
    
    @abstractmethod
    def visitorImport(self, Import):
        pass
    
    @abstractmethod
    def visitorNeed(self, Need):
        pass

    @abstractmethod
    def visitorRequire(self, Require):
        pass

    @abstractmethod
    def visitorUse(self, Use):
        pass

    @abstractmethod
    def visitorPush(self, Push):
        pass

    @abstractmethod
    def visitorUnshift(self, Unshift):
        pass

    @abstractmethod
    def visitorSplice(self, Splice):
        pass
    
    @abstractmethod
    def visitorDeclaracaoCondicional(self, declaracaoCondicional):
        pass

    @abstractmethod
    def visitorCondicionalIf(self, condicionalIf):
        pass

    @abstractmethod
    def visitorCondicionalIfElse(self, condicionalIfElse):
        pass

    @abstractmethod
    def visitorCondicionalIfElsif(self, condicionalIfElsif):
        pass

    @abstractmethod
    def visitorCondicionalIfElsifElse(self, condicionalIfElsifElse):
        pass
        
    @abstractmethod
    def visitorElsif(self, elsif):
        pass

    @abstractmethod
    def  visitorDeclaracaoExpressao(self, node):
        pass
 
from abstractVisitor import abstractVisitor

class Visitor (abstractVisitor):

#for 1..5 -> $x { ... }
    def visitLoopFor(self, loop_for):
        print(f"for {loop_for.interger} .. {loop_for.interger} -> {loop_for.escalar} {{")
        loop_for.comando.accept(self)
        print("}")
    
#5.times -> $teste { ... }
    def visitLoopTimes(self, loop_times):
        print(f"{loop_times.integer}.times -> {loop_times.id} ", end="")
        loop_times.comando.accept(self)

#while ($teste <= 5) { ... }
    def visitLoopWhile(self, loop_while):
        print(f"while ({loop_while.escalar} <= {loop_while.interger}) ", end="")
        loop_while.comando.accept(self)   

#loop (my $a = 0; $a < 4; $a++) { ... }
    def visitLoopRepeticao(self, loop_repeticao):
        print(f"loop ({loop_repeticao.instrucao1}; {loop_repeticao.instrucao2}; {loop_repeticao.instrucao3}) ", end="")
        loop_repeticao.comando.accept(self)

#loop { ... }
    def visitLoopSemCondicao(self, loop_sem_condicao):
        print("loop: ", end="")
        loop_sem_condicao.comando.accept(self)

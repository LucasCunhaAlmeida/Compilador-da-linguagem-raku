# 🚀Linguagem Raku - Elementos Léxicos

## 1. Palavras reservadas
A linguagem de programação Raku possui uma ampla gama de palavra reservadas que abordam controle de fluxo, declaração de tipos, manipulação de objetos, regexes(expressões regulares), entre outros. Como não há uma lista definida das palavra reservadas nessa linguagem, a estruturação que será realizada nesse contexto lexico será organizada em categorias, das mais usadas para as palavras com propósitos específicos, para que possa ser possível uma melhor compreensão.

### 1.1 Palavras Reservadas mais comuns
Estas são amplamente utilizadas em programas Raku:

- Controle de Fluxo: `if`, `else`, `elsif`, `while`, `for`, `loop`, `next`, `last`, `redo`, `return`, `exit`, `BREAK`.

- Declaração de variáveis e escopo: `my`, `our`, `has`, `state`, `constant`, `let`

- Definição de sub-rotinas e métodos: `sub`, `multi`, `only`.

- Tipos e valores especiais: `Any`, `Mu`, `Nil`, `True`, `False`, `Int`, `Str`, `Pair`, `List`, `Map`, `Set`, `Bag`

- Operadores e metacaracteres: `and`, `or`, `not`, `xor`, `div`, `mod`, `eq`, `le`

### 1.2 Palavras Reservadas intermediárias
Estas são usadas em contextos mais específicos ou avançados:

- Fases de execução: `BEGIN`, `CHECK`, `INIT`, `START`, `FIRST`, `ENTER`, `LEAVE`, `KEEP`, `UNDO`, `NEXT`, `LAST`, `PRE`, `POST`, `END`, `CLOSE`, `TEMP`, `UNITCHECK`

- Declarações de importação e compilação: `use` (Verificar a usabilidade 'Seria um comando único?'), `require`, `need`, `import` (Verificar a usabilidade 'Seria um comando único?'), `export`, `unit`, `trusts`, `augment`, `supersede`

- Outros: `do`, `given`, `with`, `without`, `unless`, `until`, `repeat`, `redo`, `break`, `continue`, `return`, `fail`, `LEAVE`, `KEEP`, `UNDO`, `CONTROL`, `NEXT`, `REDO`, `BREAK`, `CONTINUE`
  
## 2. Operadores

### 2.1. Operadores comuns
A linguagem Raku possui diversos operadores, e os mais comuns serão listados logo abaixo.  
Observação: **Infix** refere-se a um **operador** que aparece entre dois **operandos**. Já o **Prefix** indica um **operador** que precede o **operando**. Por fim, o **Postfix** designa um **operador** que aparece após o **operando**. 
| Operador | Tipo     | Descrição                                      | Exemplo       | Resultado      |
|:----------:|:---------:|:------------------------------------------------:|:---------------:|:---------------:|
| +        | Infix   | Adição                                         | 1 + 2         | 3             |
| -        | Infix   | Subtração                                      | 3 - 1         | 2             |
| *        | Infix   | Multiplicação                                  | 3 * 2         | 6             |
| **       | Infix   | Potência                                       | 3 ** 2        | 9             |
| /        | Infix   | Divisão                                        | 3 / 2         | 1.5           |
| div      | Infix   | Divisão inteira (arredonda para baixo)        | 3 div 2       | 1             |
| %        | Infix   | Módulo                                        | 7 % 4         | 3             |
| %%       | Infix   | Divisibilidade                                | 6 %% 4        | False         |
| gcd      | Infix   | Máximo denominador comum (mdc)               | 6 gcd 9       | 3             |
| lcm      | Infix   | Menor múltiplo comum (mmc)                    | 6 lcm 9       | 18            |
| ==       | Infix   | Igualdade numérica                            | 9 == 7        | False         |
| !=       | Infix   | Diferente numérico                            | 9 != 7        | True          |
| <        | Infix   | Menor que                                     | 9 < 7         | False         |
| >        | Infix   | Maior que                                     | 9 > 7         | True          |
| <=       | Infix   | Menor ou igual a                              | 7 <= 7        | True          |
| >=       | Infix   | Maior ou igual a                              | 9 >= 7        | True          |
| eq       | Infix   | Igualdade de string                          | "João" eq "João" | True      |
| ne       | Infix   | Diferença de string                          | "João" ne "Joana" | True      |
| =        | Infix   | Atribuição                                    | my $var = 7   | Atribui o valor 7 à variável $var |
| ~        | Infix   | Concatenação de strings                      | "Oi " ~ "pessoal" | Oi pessoal |
| x        | Infix   | Replicação de strings                        | "Olá " x 3    | Olá Olá Olá   |
| ~~       | Infix   | Smart match (equivalência inteligente)       | "Raku" ~~ Str | True          |
| ++       | Prefix  | Incremento                                    | my $var = 2; ++$var; | 3 |
| ++       | Postfix | Incremento                                    | my $var = 2; $var++; | 2 |
| --       | Prefix  | Decremento                                    | my $var = 2; --$var; | 1 |
| --       | Postfix | Decremento                                    | my $var = 2; $var--; | 2 |
| +        | Prefix  | Força o operando para um valor numérico       | +"3"          | 3 |
| -        | Prefix  | Força o operando para um valor numérico e retorna sua negação | -"3" | -3 |
| ?        | Prefix  | Força o operando para um valor booleano       | ?0            | False |
| !        | Prefix  | Força o operando para um valor booleano e retorna sua negação | !4 | False |

### 2.2. Operadores Reversos  
Adicionar um `R` antes de qualquer operador tem o efeito de inverter seus operandos.

| Operação Normal | Resultado | Operador Reverso | Resultado |
|:--------------:|:---------:|:---------------:|:---------:|
| 2 / 3         | 0.666667  | 2 R/ 3          | 1.5       |
| 2 - 1         | 1         | 2 R- 1          | -1        |

### 2.3. Operadores de Redução  
Operadores de redução trabalham com listas de valores. Eles são formados colocando o operador entre colchetes `[]`.

| Operação Normal | Resultado | Operador de Redução | Resultado |
|:--------------:|:---------:|:------------------:|:---------:|
| 1 + 2 + 3 + 4 + 5 | 15      | [+] 1,2,3,4,5     | 15        |
| 1 * 2 * 3 * 4 * 5 | 120     | [*] 1,2,3,4,5     | 120       |

## 3.Delimitadores
Delimitadores são símbolos usados para definir limites em diferentes contextos dentro do código. Em Raku são usados da seguinte forma:

| Tipo de Delimitador         | Símbolos  | Utilização                                      | Exemplo                          |
|----------------------------|------------|--------------------------------------------------|----------------------------------|
| Final de comando           | `;`        | Indica o fim de uma instrução                    | `say "Olá, mundo!";`             |
| Parâmetros de função       | `,`        | Separa os parâmetros dentro de uma função        | `soma(1, 2, 3)`                  |
| Expressões e chamadas      | `()`       | Delimita expressões e chamadas de função         | `my $resultado = (2 + 3) * 4;`   |
| Blocos de comandos         | `{}`       | Agrupa instruções em um bloco de código          | `if $x > 0 { say "LFT" }`   |

## 4. Números
A linguagem Raku oferece suporte a diversos tipos numéricos como inteiros, números racionais, de ponto flutuante e complexos. Os inteiros (Int) não possuem limite de tamanho, permitindo cálculos com números extremamente grandes. Números racionais (Rat) são representados como frações exatas, evitando erros de arredondamento comuns em outras linguagens. Números de ponto flutuante (Num) são usados para aproximações de valores reais, enquanto números complexos (Complex) permitem operações com componentes imaginários.
Raku realiza conversões automáticas entre tipos quando necessário, mas também permite conversões explícitas usando métodos como .Int, .Rat, .Num e .Complex.

| Tipo    | Descrição                         | Exemplo              |
|:-------:|:----------------------------------|:---------------------|
| Int     | Inteiros sem limite de tamanho    | 1234567890123        |
| Rat     | Racional                          | 3/4, 0.5.Rat         |
| Num     | Ponto flutuante                   | 3.14, 2e10           |
| Complex | Número com parte imaginária       | 2+3i, Num.sqrt(-1)   |

## 5. Identificadores

Em Raku, os identificadores seguem estas regras:

- Devem começar com um caractere alfabético ou um sublinhado (`_`).
- Podem conter dígitos, mas não podem começar com um dígito.
- Podem incluir traços (`-`) ou apóstrofos (`'`), mas:
  - Não podem estar no início ou no final.
  - Devem ter um caractere alfabético à direita.

**Exemplos válidos:** `var1`, `var-one`, `var'one`, `var1_`, `_var`

**Exemplos inválidos:** `1var` (começa com dígito), `-var` (começa com traço), `var-` (termina com traço), `var-1` (número à direita do traço), `var'1` (número à direita do apóstrofo), `var1'` (termina com apóstrofo)


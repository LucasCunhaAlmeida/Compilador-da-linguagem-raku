# 🚀Linguagem Raku - Elementos Léxicos

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
| ..       | Infix   | Construtor de Sequências                      | 0..5          | Cria uma série de 0 a 5 |
| ..^      | Infix   | Construtor de Sequências                      | 0..^5         | Cria uma série de 0 a 4 |
| ^..      | Infix   | Construtor de Sequências                      | 0^..5         | Cria uma série de 1 a 5 |
| ^..^     | Infix   | Construtor de Sequências                      | 0^..^5        | Cria uma série de 1 a 4 |
| ^        | Prefix  | Construtor de Sequências                      | ^5            | Cria uma série de 0 a 4 |
| …​       | Infix   | Construtor de Listas Preguiçosas (Lazy Lists) | 0…​9999       | Retorna os elementos só quando pedido |


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

## 3. Delimitadores
Comandos em Raku utilizam ; como delimitador. Parâmetros de funções utilizam , como delimitador. Adicionalmente, Raku utiliza os delimitadores () para expressões e chamadas de função. Por fim, também são utilizados os delimitadores {} para blocos de comandos.

## 4. Números
A linguagem Raku oferece suporte a diversos tipos numéricos como inteiros, números racionais, de ponto flutuante e complexos. Os inteiros (Int) não possuem limite de tamanho, permitindo cálculos com números extremamente grandes. Números racionais (Rat) são representados como frações exatas, evitando erros de arredondamento comuns em outras linguagens. Números de ponto flutuante (Num) são usados para aproximações de valores reais, enquanto números complexos (Complex) permitem operações com componentes imaginários.
Raku realiza conversões automáticas entre tipos quando necessário, mas também permite conversões explícitas usando métodos como .Int, .Rat, .Num e .Complex.

| Tipo    | Descrição                         | Exemplo              |
|:-------:|:----------------------------------|:---------------------|
| Int     | Inteiros sem limite de tamanho    | 1234567890123        |
| Rat     | Racional                          | 3/4, 0.5.Rat         |
| Num     | Ponto flutuante                   | 3.14, 2e10           |
| Complex | Número com parte imaginária       | 2+3i, Num.sqrt(-1)   |

## 5. Erros
A Raku possui um sistema detalhado para tratamento de erros, incluindo erros de sintaxe (detectados durante a compilação), erros de tempo de execução (como variáveis não declaradas ou operações inválidas) e exceções (erros que podem ser capturados e tratados programaticamente).
As exceções em Raku são objetos que herdam da classe Exception e podem ser tratadas usando blocos try e CATCH e para lidar com erros, é recomendado capturar apenas exceções específicas, fornecer mensagens claras de erro e validar entradas antes de realizar operações críticas, o uso de tipos numéricos adequados e verificações explícitas pode prevenir muitos erros comuns em operações matemáticas.

Exemplo: Esse código trata de forma segura uma divisão por zero.
```raku
my $x = 0;
try {
    my $r = 10 / $x;
    CATCH {
        when X::Numeric::DivideByZero {
            say "Erro: divisão por zero!";
        }
    }
}


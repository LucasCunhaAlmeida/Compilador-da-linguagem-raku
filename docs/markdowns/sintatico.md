## 1. Como declarar uma função (Alanna)

## 2. Variaveis (Thiago)

### 2.1 Criação de uma variavel

### 2.2 Atribuição de variavel

## 3. Operações (Felipe e Lucas)
A linguagem Raku oferece uma ampla variedade de operadores, incluindo operadores lógicos, aritméticos e comparativos. Para representar os tipos de dados básicos e os identificadores que serão utilizados, define-se a seguinte produção sintática chamada **tip**: 
 ```    
 tip -> INTEGER
     | STRING
     | BOOLEAN
     | FLOAT
     | ID
```
Será utilizada também uma expressão chamada exp, responsável por combinar todas as operações válidas da linguagem, incluindo expressões lógicas (**exp_logic**), aritméticas (**Colocar Nome**), comparativas (**exp_comp**) e os próprios tipos (**tip**):
```
exp -> "Colocar Nome"
    | exp_logic
    | exp_comp
    | tip
```
### 3.1 Aritmeticas

### 3.2 Lógicas
  A linguagem Raku oferece suporte completo a operações lógicas utilizando os operadores **and**, **or**, **xor**, além das formas de negação **not** e **!**.

  Esses operadores seguem o modelo de avaliação baseada em **truthy** e **falsy**, ou seja, qualquer tipo de valor pode ser utilizado como condição lógica. Isso permite que inteiros, strings, booleanos, floats e identificadores (variáveis) sejam avaliados diretamente em expressões lógicas, sendo eles transformado implicitamente em valores booleanos durante as operações lógicas.

```
exp_logic → tip "and" exp
     | tip "or" exp
     | tip "xor" exp
     | "not" exp
     | "!" exp
```

### 3.3 Comparação
  A linguagem Raku oferece uma variedade de operadores de comparação, que funcionam com diferente tipos de dados como Integer, Float, String e Boolean. Os operadores de comparação são constituidos de Igualdade (**==**), Diferença (**!=**), Maior ou Igual (**>=**), Maior (**>**), Menor ou Igual (**<=**), Menor (**<**) e o Smart Match (**~~**).

```
exp_comp → tip "==" exp
         | tip "!=" exp
         | tip ">=" exp
         | tip "<=" exp
         | tip ">"  exp
         | tip "<"  exp
         | tip "~~" exp
```
## 4. Estruturas de repetição (Hevellyn)

## 5. Estruturas condicionais (Lorena)


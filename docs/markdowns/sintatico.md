## Como declarar uma função
Raku permite a declaração de funções utilizando a palavra-chave sub. Uma função pode ou não ter parâmetros, e os parâmetros são declarados dentro de parênteses, podendo ter tipos opcionais.

Sintaxe básica para declarar funções em Raku:

```raku
# Sem parâmetros
sub ola() {
    say "Oi!";
}

# Com um parâmetro
sub dobro($x) {
    return $x * 2;
}

# Com dois parâmetros
sub soma($a, $b) {
    return $a + $b;
}
```


#### Regras Sintáticas

A declaração de funções segue a forma:

```raku
function_decl → "sub" ID "(" param_list? ")" block
param_list    → param ("," param)*
param         → type? "$"ID
type          → ID
block         → "{" statement* "}"
```

sub: palavra-chave usada para definir funções.

ID: identificador do nome da função.

param_list: lista opcional de parâmetros.

type: tipo opcional do parâmetro (como Int, Str, etc.).

block: corpo da função delimitado por {}.

# Variáveis 
As variáveis servem para armazenar informações (como números, textos, listas, etc.) que podem ser usadas, alteradas e reutilizadas ao longo do código.
## Declaração de variáveis
Você pode declarar variáveis com:

`my`: escopo léxico (local).

`our`: escopo global compartilhado.

`state`: lembra o valor entre chamadas de função.
```

my $x = 10;       # variável local
our $y = 20;      # variável global
state $contador = 0;  # mantém valor entre chamadas

```

## Tipos de variáveis 
### 1 - Escalar(`$`): 
Usado para armazenar um único valor (inteiro, string, etc.).
```
my $nome = "Thiago"; 
my $idade = 20;
say "Nome: $nome, Idade: $idade";

```

### 2 - Lista(`@`):
Usado para armazena uma lista ordenada de valores (semelhante a arrays em outras linguagens).

```

my @unidades = <unidade1 unidade2 unidade3>;
say @unidades[0]; #Imprime unidade1

``` 

## Tipagem opcional 
Você pode (opcionalmente) especificar tipos para variáveis:
```
my Int $idade = 20;
my Str $nome = "Thiago";

```

## Operações
No raku as operações sao compostas por varias estuturações, mas por limites de tempo iremos abordar as segintes expressões: expressões Aritimeticas (exp_metic), expressões Logicas (exp_logic) e expressões de Comparação (exp_comp), sendo elas compostas da seguinte forma:

```
exp → exp_metic
     | exp_logic
     | exp_comp
     | exp_tip
```

Os valores que se pode ser atribuido aos valores de um expressão em raku são como inteiro, float e string, sendo que também é possivel a obtenção de valor por meio de um identificador/variavel, isso é representado por meior dessa gramatica:

```
exp_tip → INTEGER
     | FLOAT
     | STRING
     | ID
```
### Aritmeticas

Raku oferece suporte completo às operações aritméticas básicas.

```
exp_metic → exp "+" exp
     | exp "-" exp
     | exp "*" exp
     | exp "/" exp
```

Abaixo estão exemplos de como utilizá-las:

```raku
# Soma
my Int $a = 10;
my Int $b = 5;
say $a + $b;  # Saída: 15

# Subtração
say $a - $b;  # Saída: 5

# Multiplicação
say $a * $b;  # Saída: 50

# Divisão (retorna Rat por padrão)
say $a / $b;  # Saída: 2.0

# Divisão inteira
say $a div $b;  # Saída: 2

# Módulo (resto da divisão)
say $a % $b;  # Saída: 0

# Exponenciação
say $a ** 2;  # Saída: 100

# Incremento e decremento
$a++;  # $a agora é 11
$b--;  # $b agora é 4
say $a, ", ", $b;
```

### 3.2 Lógicas
  A linguagem Raku oferece suporte completo a operações lógicas utilizando os operadores **&&**, **||**, **^^**, além das formas de negação **not** e **!**.

  Esses operadores seguem o modelo de avaliação baseada em **truthy** e **falsy**, ou seja, qualquer tipo de valor pode ser utilizado como condição lógica. Isso permite que inteiros, strings, booleanos, floats e identificadores (variáveis) sejam avaliados diretamente em expressões lógicas, sendo eles transformado implicitamente em valores booleanos durante as operações lógicas.

```
exp_logic → exp "&&" exp
     | exp "||" exp
     | exp "^^" exp
     | "not" exp
     | "!" exp
```
Exemplos no código:

````
# Operador AND
my Bool $a = True;
my Bool $b = False;
say $a && $b;  # Saída: False

# Operador OR
say $a || $b;  # Saída: True

# Operador XOR
say $a ^^ $b;  # Saída: True

# Negação com 'not'
say not $a;    # Saída: False

# Negação com '!'
say !$b;       # Saída: True

# Avaliação de inteiros como booleanos
my Int $x = 0;
my Int $y = 10;
say $x || $y;  # Saída: 10 (0 é falsy, 10 é truthy)

# Avaliação de strings como booleanos
my Str $nome = "";
say !$nome;    # Saída: True (string vazia é falsy)
````

### 3.3 Comparação
  A linguagem Raku oferece uma variedade de operadores de comparação, que funcionam com diferente tipos de dados como Integer, Float, String e Boolean. Os operadores de comparação são constituidos de Igualdade (**==**), Diferença (**!=**), Maior ou Igual (**>=**), Maior (**>**), Menor ou Igual (**<=**), Menor (**<**) e o Smart Match (**~~**).

```
exp_comp → exp "==" exp
         | exp "!=" exp
         | exp ">=" exp
         | exp "<=" exp
         | exp ">"  exp
         | exp "<"  exp
         | exp "~~" exp
```

### Exemplos de código

```
my Int $a = 10;
my Int $b = 20;

say $a == $b;  # False
say $a != $b;  # True
say $a < $b;   # True
say $b >= $a;  # True

# Comparando strings
my Str $nome1 = "Lucas";
my Str $nome2 = "lucas";

say $nome1 eq $nome2;  # False (case-sensitive)
say $nome1.lc eq $nome2.lc;  # True (após lowercase)

# Smart Match (~~)
say $a ~~ Int;     # True (verifica tipo)
say $nome1 ~~ /Luc/;  # True (regex match)
```

# Estruturas de repetição
As estruturas de repetição são blocos de código que executam repetidamente até que uma condição seja atendida ou até que todos os elementos de uma sequência sejam percorridos. Assim como em outras linguagens com as quais estamos mais familiarizados, em Raku os loops permitem iterar sobre listas, ranges, hashes, ou repetir instruções.

## Tipos de repetição:
### 1 - For:
Ele é usado principamente para percorrer listas, arrays e hashs. Lida bem quando precisa percorrer elementos de uma sequência
```
#Imprime de 1 a 10:
for 1..10 -> $x {
    say "Número: $x";
}

#Percorre lista:
my @materias = ("LFT", "SO", "OAC");
for @materias -> $materia {
    say "A matéria que eu mais gosto é  $materias";
}

```
### 2 - .times:
Ele é uma forma simples de repetir um bloco N vezes, muito útil para repetições fixas porém não itera sobre listas, arrays ou hashes. Apenas repete o bloco baseado em um número inteiro. 
```
#Repete 10 vezes o bloco:
10.times -> $x {
    say "Contando de 1 a 10:";
    say $x + 1;
}
```

### 3 - While:
Ele é útil quando você quer repetir algo até atingir um limite.
```
my $sintatico = 1;
while $sintatico <= 5 {
    say "Exemplo de repetição com while: $sintatico";
    $sintatico++;
}
```
### 4 - Loop:
Estrutura de repetição com controle manual semelhante ao estilo que já conhecemos em C
```
loop (my $a = 0; $a < 4; $a++) {
    say "Repetição com loop estilo C: $a";
}
```

### 5 - Loop sem condição:
Estrutura de repetição sem controle e precisa ser interrompido manualmente (Ctrl+C)
```
loop {
    say "infinitamente rodando...";
    sleep 2; # para dar uma pausa
}
```

## Estruturas condicionais

Aqui... Estrutura condicional Raku

condicional -> IF expressão bloco
		| IF expressão bloco ELSE bloco
		| IF expressão bloco ELSIF expressão bloco
		| IF expressão bloco lista_elsif ELSE bloco
		
lista_elsif -> ELSIF expressao bloco
                | lista_elsif ELSIF expressao bloco	

bloco -> ACHAVE declarações FCHAVE
	   | declaração

declarações -> declaração
		| declarações declaração

declaração -> atribuição PONTO_VIRGULA
               | chamada função PONTO_VIRGULA
               | condicional
               | laco
               | expressão PONTO_VIRGULA
               | bloco


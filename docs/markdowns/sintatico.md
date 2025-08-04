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

### 3 - Hash(`%`):
Usado para armazena pares chave/valor (semelhante a dicionários ou mapas).
```

my %pessoa = nome => "Thiago", idade => 20;
say %pessoa<nome>;

```

## Tipagem opcional 
Você pode (opcionalmente) especificar tipos para variáveis:
```
my Int $idade = 20;
my Str $nome = "Thiago";

```

## Operações (Felipe e Lucas)

### Aritmeticas

### Lógicas

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
    say "Ezemplo de repetição com while: $sintatico";
    $sintatico++;
}
```

### 3 - While:
Ele é útil quando você quer repetir algo até atingir um limite.
```
my $sintatico = 1;
while $sintatico <= 5 {
    say "Ezemplo de repetição com while: $sintatico";
    $sintatico++;
}
```

## Estruturas condicionais (Lorena)


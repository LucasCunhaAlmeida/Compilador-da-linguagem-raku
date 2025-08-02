## Como declarar uma função (Alanna)
Raku permite a declaração de funções utilizando a palavra-chave sub. Uma função pode ou não ter parâmetros, e os parâmetros são declarados dentro de parênteses, podendo ter tipos opcionais.

Sintaxe básica para declarar funções em Raku:

#### Exemplos:

#### Exemplos:

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

Regras Sintáticas

A declaração de funções segue a forma:

function_decl → "sub" ID "(" param_list? ")" block
param_list    → param ("," param)*
param         → type? "$"ID
type          → ID
block         → "{" statement* "}"

sub: palavra-chave usada para definir funções.
ID: identificador do nome da função.
param_list: lista opcional de parâmetros.
type: tipo opcional do parâmetro (como Int, Str, etc.).
block: corpo da função delimitado por {}.


## Variaveis (Thiago)

### Criação de uma variavel

### Atribuição de variavel

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

## Estruturas condicionais (Lorena)


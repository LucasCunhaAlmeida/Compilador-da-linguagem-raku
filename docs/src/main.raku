# Declarações de variáveis escalares

my Int $a = -20;
my Int $b = 20;
our Str $nome = "Felipe";

# Variáveis para o loop

my Int $d = 0;
my Int $v = 0;
my Int $k = 0;

# Lista;

my @lista = 1, 2, 3, 4, 5;

# Condicional simples

if $a < $b {
    say 'a é menor que b';
}
elsif $a == $b {
    say '12';
}
else {
    $a = 3 - 4;
}

# Condicional Complexa

if $a < $b {
    if $b < 100 {
        say "b é menor que 100";
    }
    else {
        say "b é maior ou igual a 100";
    }
}
elsif $a == $b {
    say "a é igual a b";
}
else {
    say "a é maior que b";
}

# Expressões com operadores lógicos

if ($a < $b) && ($b < 50) {
    say "a é menor que b e b < 50";
}

if ($a < $b) || ($b > 100) {
    say "a < b ou b > 100";
}

say "123"; 

# Loop for com listas

for @lista -> $elem {
    say "Elemento da lista: " ~ $elem;
}

# Estrutura de repetição for
say "Iteração: " ~ $i;

for 1..5 -> $i {
    say "Iteração: " ~ $i;
}

# Estrutura de repetição times
5.times -> $j {
    say "Times loop: " ~ $j;
}

# Estrutura de repetição while
while $a < 50 {
  say "Novo valor de a: " ~ $a;
  $a = $a + 5;
}

# ===========================
# # Função
# ===========================
sub soma($x, $y) {
    say "Resultado da soma: " ~ ($x + $y);
    $a = $a + 5;
}

sub saudacao() {
    say "Olá, " ~ $nome ~ "!";
    $a = $a + 5;
}

# # Chamadas de função

saudacao();
soma(15, 30);

# ===========================
# Expressões com operadores
# ===========================

my Int $c = ($a * $b) % 7;
say "Valor de c: " ~ $c;

# ===========================
# Loop estilo C
# ===========================

loop (my Int $a = 0; $d < 3; $v = $v + 1) {
     say "Loop estilo C, k = " ~ $k;
     $k = $k + 1;
}

# ===========================
# Função recursiva
# ===========================

sub fatorial($n) {
    if $n <= 1 {
        return 1;
    }
    else {
       return $n * fatorial($n - 1);
    }
}

say "Fatorial de 5: " ~ fatorial(5);

# ===========================
# Testes de controle de fluxo
# ===========================

for 1..3 -> $i {
    if $i == 2 {
        next;        # Deve pular a iteração
    }
    if $i == 3 {
        last;        # Deve sair do loop
    }
    say "Valor do i: $i";
}

redo if False;       # Deve repetir a instrução anterior (não roda pois False)

exit(0);             
return 42;           # Retorna valor (só válido dentro de função normalmente)
break;               

# ===========================
# Testes com constantes e variáveis especiais
# ===========================

constant $PI = 3.14159;
say "Valor de PI: " ~ $PI;

state $contador = 0;
$contador++;
say "Valor persistente de contador: $contador";

let $x = 10;  
say "Valor de x com let: $x";

# ===========================
# Testes de multi-funções
# ===========================

multi sub soma(Int $a, Int $b) {
    $a + $b
}
multi sub soma(Str $a, Str $b) {
    $a ~ $b
}

say soma(2, 3);
say soma("Olá, ", "Felipe");

# ===========================
# Testes de only
# ===========================

only sub saudacao() {
    say "Função exclusiva saudacao";
}
saudacao();

# ===========================
# Testes de import, need, require, use
# ===========================

use Utils;         
need Utils;        
require Utils;     
import Utils <ola>; 

ola("Felipe");

# ===========================
# Testes com arrays e operações
# ===========================

my @lista = 'a', 'b', 'c';
push @lista, "d";
say @lista;

unshift @lista, "z";
say @lista;

splice @lista, 1, 2, 'x', 'y';
say @lista;


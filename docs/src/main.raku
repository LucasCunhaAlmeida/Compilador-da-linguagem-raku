# Declarações de variáveis escalares

my Int $a = -20;
my Int $b = 20;
our $nome = "Felipe";

# Variáveis para o loop

my Int $d = 0;
my Int $v = 0;
my Int $k = 0;
my $j = 1;
my $i = 1;

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

# Estrutura de repetição while
while $a < 50 {
  say "Novo valor de a: " ~ $a;
  $a = $a + 5;
}

# ===========================
# # Função
# ===========================
multi soma($x, $y) {
    say "Resultado da soma: " ~ ($x + $y);
    $a = $a + 5;
}

soma(15, 30);

# ===========================
# Expressões com operadores
# ===========================

my Int $c = ($a * $b) % 7;
say "Valor de c: " ~ $c;

# ===========================
# Loop estilo C
# ===========================

# loop ($a = 0; $d < 3; $v = $v + 1) {
#      say "Loop estilo C, k = " ~ $k;
#      $k = $k + 1;
# }

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
        next;  # pular iteração
    }
    if $i == 3 {
        last;  # sair do loop
    }
    say "Valor do i: $i";
}

# redo só dentro de loop
loop {
    say "Exemplo redo";
    redo if False;  # OK, mas não repete
    last;
}

exit(0);

# return 42 só dentro de sub
sub teste-retorno() { return 42; }
say teste-retorno();            

# ===========================
# Testes com constantes e variáveis especiais
# ===========================

constant $PI = 3.14159;
say "Valor de PI: " ~ $PI;

state $contador = 0;
$contador++;
say "Valor persistente de contador: $contador";

my $x = 10;  
say "Valor de x com my: $x";

# ===========================
# Testes de multi-funções
# ===========================


multi soma(Int $valor, Int $valor1) {
    return $valor + $valor1;
}

multi soma() {
    return 12;
}

multi soma(Str $nome, Str $nome2) {
    return $nome ~ $nome2;
}

say soma(2, 3);
say soma("Olá, ", "Felipe");

# ===========================
# Testes de only
# ===========================

only saudacao() {
    say "Função exclusiva saudacao";
}
saudacao();

# # ===========================
# # Testes com arrays e operações
# # ===========================

my @lista1 = 'a', 'b', 'c';
push @lista1, "d";
say @lista1;

unshift @lista1, "z";
say @lista1;

splice @lista1, 1, 2, 'x', 'y';
say @lista1;


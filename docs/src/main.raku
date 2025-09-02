# Declarações de variáveis escalares
my Int $a = -20;
my Int $b = 20;
our Str $nome = "Felipe";

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
    3 - 4;
}

say "123"; 

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

# # Função com parâmetros
sub soma($x, $y) {
    say "Resultado da soma: " ~ ($x + $y);
    $a = $a + 5;
}

# # Função sem parâmetros
sub saudacao() {
    say "Olá, " ~ $nome ~ "!";
    $a = $a + 5;
}

# # Chamadas de função
saudacao();
soma(15, 30);

# Expressões com operadores
my Int $c = ($a * $b) % 7;
say "Valor de c: " ~ $c;

# Loop estilo C
loop (my Int $a = 0; $d < 3; $v = $v + 1) {
    say "Loop estilo C, k = " ~ $k;
}

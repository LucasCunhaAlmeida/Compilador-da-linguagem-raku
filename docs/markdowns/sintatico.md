## Como declarar uma função (Alanna)

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


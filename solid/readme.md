
# Princípios Solid


## S - Single Responsibility

Uma classe deve ter apenas uma razão para mudar.

A classe deve apenas realizar uma função dentro da aplicação e essa função deverá ser encapsulada (escondida) dentro da classe.

Objetivo : Reduzir o acoplamento e complexidade.

Frases de efeito:

- Evita classes muito grandes
- Prefira pequenas partes à grandes acoplamentos
- Uma alteração em uma classe que faz mais de uma coisa é mais complexa que uma que tem uma única responsabilidade

## O - Open/Close

As classes devem ser abertas para extensão mas fechadas para modificação

Frases de efeito:

- Uma classe aberta possibilita herança e sobrescrita da mesma
- Se uma classe já foi concluída é melhor relizar alterações por meio de subclasses
- Uma classe com bug não pode ser considerada concluída e deverá ser alterada diretamente
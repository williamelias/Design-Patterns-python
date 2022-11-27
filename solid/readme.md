
# Princípios Solid


## S - Single Responsibility

**código presente em** : [code](single_responsability.py)

Frase de efeito: Uma classe deve ter apenas uma razão para mudar.
A classe deve apenas realizar uma função dentro da aplicação e essa função deverá ser encapsulada (escondida) dentro da classe.

Objetivo : Reduzir o acoplamento e complexidade.

Frases Auxiliares:

- Evita classes muito grandes
- Prefira pequenas partes à grandes acoplamentos
- Uma alteração em uma classe que faz mais de uma coisa é mais complexa que uma que tem uma única responsabilidade

<hr>

## O - Open/Close

**código presente em** : [code](open_close.py)

Frases de efeito: As classes devem ser abertas para extensão mas fechadas para modificação

Frases Auxiliares:

- Uma classe aberta possibilita herança e sobrescrita da mesma
- Se uma classe já foi concluída é melhor relizar alterações por meio de subclasses
- Uma classe com bug não pode ser considerada concluída e deverá ser alterada diretamente

## L - Liskov Substitution Principle

**código presente em** : [code](liskov.py)

Frase de efeito: Quando estendendo  uma classe, lembre-se que você deve ser capaz de passar objetos da subclasse em lugar de objetos da classe mãe sem quebrar o código cliente.

Requerimentos para implementar Liskov 

- Os tipos de parâmetros em um método de uma subclase deve coincidir ou serem mais abstratos que os tipos de parâmetros nos métodos da superclasse
- O tipo de retorno de um método da subclasse deve coincidir com o tipo de retorno do método da superclasse
- Um método em uma subclase não deve lançar tipos de exceção que não são esperados que método base lançaria
- Uma subclasse não deve fortalecer pré-condições
- Uma subclasse não deveria enfraquecer pós-condições
- Invariantes de uma superclasse devem ser preservados
- Uma subclasse não deve mudar valores de campos privados da superclasse
    - No lugar de sobrescrever ou alterar valores, devemos optar por criar novos métodos

## I - Interface Segregation Principle

**código presente em** : [code](interface_segregation.py)

Frase de efeito: Clientes não devem ser forçados a depender de métodos que não usam

Frases Auxiliares:

- Devemos prezar por classes mais enxutas e pela segregação para que o cliente use somente o necessário.
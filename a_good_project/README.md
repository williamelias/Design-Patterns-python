# Características de um bom projeto

Nesse tópico iremos abordar algumas premissas a serem seguidas e situações a serem evitadas, em relação a aquitetura de projetos.

<hr>


**Reutiliação de código**

Um projeto deve focar na redução de custo e de tempo de produção do mesmo e essas variantes podem ter relação direta com a reutilização de código.
Ela é uma "amiga dos projetos/desenvolvedores", digo entre aspas pois não é tão simples criar módulos/classes que não estejam acopladas a um contexto específico.

**Extensibilidade**

"Mudança é a única constante na vida de um programador" (by Mergulho nos padrões de projeto,pág. 39)

Um projeto sem mudança provavelmente é um projeto deixado de lado, pois existem vários motivos para mudanças , seja a curto, médio ou longo prazo:

- Manter as bibliotecas e tecnologias atualizadas na melhor versão possível
- Alterações de design de interfaces solicitadas por clientes ou por seguir o momento atual do mercado
- Bugs encontrados por clientes
- Melhoria na codificação/arquitetura do projeto
- Solicitações de evolução e criação de novas funcionalidades 

<hr>

# Princípios de Projeto

**Encapsule o que varia**

- Identique aspectos que mudam e separe-os dos que não mudam

objetivo: Minimizar efeitos causados por mudanças

Tipos:

- Encapsulamento a nível de método
- Encapsulamente a nível de classe

**Programe para um interface, não para um implementação**

"Dependa de abstrações, não de classes concretas" (by Mergulho no padrão de projetos, pag 47)

Ao se programar para uma classe concreta você gera um nível de acomplamento que poderá dificultar alterações.

Quando for definir uma interface, se pergunte:

-> Quais métodos eu irei usar daquele objeto na minha classe?
    - Após decidir, descreva esses métodos numa interface ou classe abstrata.
    - Faça a classe que era uma dependência implementar essa interface
    - Agora faça a dependência entre a interface no lugar da classe concreta

**Prefira composição sobre herança**

Quando temos um projeto em que há heranças de mais, não conseguimos realizar as seguintes ações:

-> Uma subclasse não pode reduzir a interface da superclasse.
-> Quando sobrescrevemos métodos precisamos conferir se o comportamente é compatível com o da superclasse
-> A herança quebra o encapsulamento da superclasse
-> Há um grande acomplamento entre a subclasse e superclasse
-> Tentar reutilizar código via herança, poderá gerar heranças paralelas
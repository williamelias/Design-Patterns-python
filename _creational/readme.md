
# Padrões Presentes

- Factory Method

- Abstract Factory

- Builder

<hr>

## Factoy method

Fornece uma interface para criar objetos em uma superclasse, permitindo que as subclasses alterem o tipo de objetos que são criados.

**Aplicabilidade**: Usado quando não soubermos de antemão os tipos e dependências exatas dos objetos a interagir.

<hr>

**Prós**:

- Evita acoplamentos entre o criador e o produto
- Aplica o princípio S (Single responsability) do SOLID
- Aplica o princípio O (open/closed) do SOLID

**Contras**:

- O código pode se tornar complicado pela necessidade de intruduzir muitas subclasses

<hr>

**Padrões relacionados** : Abstract factory, Prototype, Template Method e Builder

<hr>

**Diagrama UML**

!['factory_method'](/_creational/factory_method/factory.png)

<hr>

## Abstract Factory

Permite criar famílias de objetos sem ter que especificar suas classes concretas.

**Aplicabilidade**: Usado quando devemos interagir com diversas famílas de produtos sem interação com classes concretas, permitindo uma futura escalabilidade

<hr>

**Prós**:

- Todos produtos são compatíveis entre si
- Sem vínculo forte com classes concretas
- Aplicação do princípio S (single responsability) do SOLID
- Aplica o princípio O (open/closed) do SOLID

**Contras**:

- O código pode se tornar complexo pois a cada novo produto ou fábrica uma interface deverá ser criada, além das classes concretas

<hr>

**Padrões relacionados** : Abstract factory, Prototype e Builder

<hr>

**Diagrama UML**

!['abs_method'](/_creational/abstract_factory/abs_factory.png)

<hr>

## Builder

Permite criar objetos complexos passo a passo - com um mesmo código é possível construir diferentes tipos e representações
Esse design pattern só se torna útils quando temos objetos que requerem configuração extensiva.
Ao contrário de outros padrões de projeto, o builder possibilita criar objetos de interfaces diferentes.
Esse padrão permite que você execute etapas não sequenciais e somente quando quiser busque o objeto gerado,diferentemente dos outros padrões que retornam o objeto imediatamente.

**Aplicabilidade**:  Use-o para se livrar de um construtor telescópico

<hr>

**Prós**:

- Você tem total controle das etapas de construção de um objeto, podendo: adiár etapas, pular e executar em sequência.
- Haverá uma boa reutilização de código
- Aplicamos o princípio S (Single responsability)

**Contras**:

- O nível de complexidade de código aumenta, pois temos que criar várias classes e interfaces .

<hr>

**Padrões relacionados** : Abstract factory, Bridge, Composite e Builder

<hr>

**Diagrama UML**

!['abs_method'](/_creational/builder/with_builder.png)
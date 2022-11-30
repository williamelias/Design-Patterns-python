
# Padrões Presentes

- Factory Method

- Abstract Factory

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

!['factory_method'](/creational/factory_method/factory.png)

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

!['abs_method'](/creational/abstract_factory/abs_factory.png)
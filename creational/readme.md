
# Factoy method

Fornece uma interface para criar objetos em uma superclasse, permitindo que as subclasses alterem o tipo de objetos que são criados.

**Aplicabilidade**: Usado quando não soubermos de antemão os tipos e dependências exatas dos objetos a interagir.

<hr>

**Prós**:

- Evita acoplamentos entre o criador e o produto
- Aplica o princípio S (Single responsability) do Sólid
- Aplica o princípio O (open/closed)

**Contras**:

- O código pode se tornar complicado pela necessidade de intruduzir muitas subclasses

<hr>

**Padrões relacionados** : Abstract factory, Prototype, Template Method e Builder

!['factory_method'](/factory_method/factory.png)
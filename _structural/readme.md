
# Padrões Presentes

- Adapter

<hr>

## Adapter

Permite a colaboração de objetos de interfaces compatíveis.
Converte a interface de um objeto para que outro objeto possa entendê-lo
Um adapter encobre toda complexidade da adaptação e o objeto encobrido não sabe do adaptador.

### Estruturas possíveis

- **Adaptador de Objeto**
    - Usa composição de objeto
    - Ele implementa a interface de um objeto e encobre o outro

- **Adaptador de Classe**
  
    - Usa herança
    - Necessário usar uma linguagem de programção que suporte heranças múltiplas

**Aplicabilidade**: Utilize quando você tiver uma classe existente que não tem uma interface compatível com o resto do código.

<hr>

**Prós**:

- Usando a **composição** diminui o acoplamento, pois o cliente não interage diretamente com a classe de terceiros
- Utiliza do princípio S (Single responsability)
- Utiliza do princípio O (Open/closed)


**Contras**:

- Por conta do uso de interfaces ou heranças a complexidade do código aumenta

<hr>

**Padrões relacionados** : Bridge, Decorator, Proxy e Facade

<hr>

**Diagramas UML**

**Usando composição**

!['adapter_1'](/_structural/adapter/with_composition.png)

<hr>

**Usando Herança**

!['adapter_2'](/_structural/adapter/with_inheritance.png)

<hr>
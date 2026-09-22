:description: Information Management Guidebook Glossary


Glossary
========


.. glossary::


    Associative Entity
      Associates the instances of one or more entity types. They also contain attributes that are unique to the relationship between those entity instances.


    Attribute
      A particular property that describes the entity. It's the characteristics of either an entity, a many-to-many relationship, or a one-to-one relationship.


    Binary Relationship
      A relationship that has a degree of 2, meaning it connects exactly two different entity types or sets.


    Composite Attribute
      Attribute that can be divided into smaller sub-parts, each with its own independent meaning.


    Conceptual ERD
      A high-level visual blueprint that maps out core business concepts and how they relate to one another, completely ignoring technical database details.


    Data
      Consists of unorganized numbers, symbols, or observations lacking explicit context or meaning on their own.

      Raw, unorganized, and unprocessed facts or figures.


    Data Properties
      Refers to the characteristics, attributes, or rules that define a specific piece of data.


    Derived Attribute
      Attributes whose value is not stored directly in the database, but instead calculated or derived from other stored attributes or system values.


    DIKW Hierarchy
      A structural framework used to explain how raw, unorganized facts are progressively transformed into valuable, actionable insights for decision-making.


    Entity
      A real-world item or concept that exists on its own. They are equivalent to database tables in a relational database, with each row of the table representing an instance of that entity. Entities are objects or concepts that represent important data. They are typically nouns (customer, supervisor, location, or promotion).


    Entity Cardinality
      The number of instances of one entity that can, or must, be associated with each instance of another entity.


    Entity-Relationship Diagram
      A data modeling technique that graphically illustrates an information system's entities and the relationships between those entities. It's a conceptual and representational model of data used to represent the entity framework infrastructure.


    Foreign Key
      An attribute or group of attributes in one table that links to the primary key of another table, establishing a relationship between them.


    Identifier Attribute
      Used to represent primary key. An attribute (or combination of attributes) that uniquely identifies individual instances of an entity type.


    Information
      Processed and organized data that provides explicit meaning, clarity, and directly supports decision-making.

      Processed data equipped with context, structure, and meaning.


    Information Management
      A core course covering how organizations collect, store, process, and secure data. It bridges raw computer hardware with business decision-making.


    Knowledge
      Applied information combined with domain expertise and understanding.


    Logical ERD
      An abstract representation of an organization's data requirements. It focuses on the structure and relationships of data, independent of any technical constraints or specific database technologies. Logical models are primarily concerned with **what** data is needed and **how** it relates, rather than **how** it will be stored or accessed.


    Many-to-Many Cardinality
      Entities on both sides of the relationship can have many related entities on the other side.


    Maximum Cardinality
      The **greatest** number of times an instance of one entity can participate in a relationship with another entity.


    Minimum Cardinality
      The **fewest** number of times an instance must participate in a relationship, showing whether the relationship is optional or mandatory.


    Multivalued Attribute
      Attributes that are capable of taking in more than one value.


    One-to-One Cardinality
      Each entity in the relationship will have exactly one related entity.


    One-to-Many Cardinality
      An entity on one side of the relationship can have many related entities, but an entity on the other side will have a maximum of one related entity.


    Partial Key
      An attribute that uniquely identifies weak entity instances only when combined with the primary key of a related strong (owner) entity.


    Physical ERD
      Translates the logical model into a complete implementation within a specific database system. It addresses technical considerations, such as storage formats, indexing, data types, and security mechanisms, ensuring that the database performs efficiently and securely in the real world.


    Primary Key
      A specific attribute or set of attributes that uniquely identifies every single record or row within an entity.


    Relationship
      The association that describes the interaction between entities.


    Strong Entity
      Exists independently from other entity types. They always possess one or more attributes that uniquely distinguish each occurence of the entity.


    Strong Relationship
      A connection between two independent strong entities where each entity has its own primary key.


    Ternary Relationship
      A single diamond-shaped conenction that links three distinct entity types together. It is used when a normal two-way (binary) link cannot correctly show how all three things depend on each other at the same time.


    Unary Relationhsip
      An association where a single entity type relates to instances of itself, giving it a degree of 1.


    Weak Entity
      Depends on some other entity type. They don't possess unique attributes (also known as a **primary key**) and have no meaning in the diagram without depending on another entity. This other entity is known as the **owner**.


    Weak Relationship
      Or **identifying relationship**; are connections that exist between a weak entity type and its owner.


    Wisdom
      Strategic synthesis combining knowledge and judgment for ethical, long-term action.
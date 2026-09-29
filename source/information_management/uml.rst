:description: Unified Modeling Language (UML) is a widely adopted stsandard for visualizing, specifying, constructing, and documenting the artifacts of software systems. UML provides a set of graphic notation techniques to create abstract models of systems, which can be used for both software and information management contexts.


Unified Modeling Language
=========================

The **Unified Modeling Language (UML)** is a widely adopted stsandard for visualizing, specifying, constructing, and documenting the artifacts of software systems. UML provides a set of graphic notation techniques to create abstract models of systems, which can be used for both software and information management contexts.

UML assists in bridging the gap between conceptual design and implementation by offering a common lagnuage for stakeholders, analysts, designers, and devleopers. Through its visual diagrams, it enables clear communication of system structure and behavior, making it easier to analyze requirements and design robust solutions.

UML's flexibility allows it to be applied across a range of domains, from database design to process modelling and enterprise architecture. In information management, UML helps to clarify data flows, relationships, and system interactions, supporting both technical and non-technical stakeholders in understanding system dynamics.


Standard UML Models
+++++++++++++++++++

UML comprises several types of diagrams, each serving a distinct purpose in modelling information systems. These diagrams can be broadly grouped into **structural diagrams** (which show the static aspects of a system) and **behavioral diagrams** (which show the dynamic aspects).

In information management system, diagrams are used to **model**, **analyze**, and **communicate** how data and processes behave in an information system. Unified Modeling Langauge provides several diagram types, each focusing on different aspects of the system. Together, they help ensure that database and system designs are consistent, reliable, and aligned with user requirements.


.. grid:: 1
    :gutter: 3


    .. grid-item-card:: Class Diagram
        
        Describes the static structure of a system, including classes, attributes, operations, and relationships.

        Models the *static structure* of a system: its classes, attributes, operations, and relationships. It is particularly important for information maangement because it closely relates to **database schema design**.


        .. grid:: 1
            :class-row: surface
            :gutter: 3


            .. grid-item-card:: Classes

                Represent key entities (e.g. ``Book``, ``Member``, ``Loan``).


            .. grid-item-card:: Attributes

                Data stored in such class (e.g. ``title``, ``author``, ``dueDate``).


            .. grid-item-card:: Operations

                Functions or methods (e.g. ``calculateFine()``, ``updateStatus()``).

            
            .. grid-item-card:: Relationships

                Associations, aggregations, compositions, and inheritance between classes.


        .. admonition:: Example
            :class: hint

            Modelling the entities and relationships in a university database, such as ``Student``, ``Course``, and ``Enrolment``.


        .. admonition:: Example
            :class: hint

            **Library Domain Classes**:

            - **Book**: ``bookId``, ``title``, ``author``, ``status``

            - **Member**: ``memberId``, ``name``, ``email``

            - **Loan**: ``loanId``, ``loanDate``, ``dueDate``

            - Relationships:

              - ``Member`` "has many" ``Loans``

              - ``Book`` "is loaned in" ``Loans``


    .. grid-item-card:: Use-Case Diagram
        
        Illustrates the functionality provided by a system in terms of actors and their interactions with use-cases.

        It shows the *functional requirements* of a system from the perspective of its users (called **actors**). It answers the question: *"What should the system do?"*


        .. grid:: 1
            :class-row: surface
            :gutter: 3


            .. grid-item-card:: Actors

                External entities that interact with the system (e.g. ``Customer``, ``Admin``).


            .. grid-item-card:: Use-Cases

                Goals or tasks the actors perform using the system (e.g. Place oder, Update inventory).


            .. grid-item-card:: Relationships

                Includes, extends, and associations between actors and use-cases.


        .. admonition:: Example
            :class: hint

            Showing how a library member interacts with a library sytem to borrow books or pay fines.


        .. admonition:: Example
            :class: hint

            **Online Library System**:

            - Actors: ``Student``, ``Librarian``

            - Use-cases: Search books, Borrow book, Return book, Manage catalog

            - ``Student`` → Search books, Borrow book, Return book

            - ``Librarian`` → Manage catalog, Approve membership


    .. grid-item-card:: Sequence Diagram

        Shows how objects interact in a particular scenario of a use-case, focusing on the sequence of messages exchanged.

        Models the *time-ordered interaction* between objects or components. It is useful for analyzing how data flows through the system during a specific scenario.

        - Shows objects (e.g. user, web application, database).

        - Displays messages exchanged over time (e.g. requests, responses).

        - Helps identify potential performance and reliability issues in process flows.


        .. admonition:: Example
            :class: hint

            Modelling the steps involved when a customer places an online order, including interactions between customer, shopping cart, and payment gateway.


        .. admonition:: Example
            :class: hint

            **Borrow Book Scenario**:

            - Student → Library system: ``requestBook(bookId)``

            - Library system → Database: ``checkAvailability(bookId)``

            - Database → Library system: ``availabilityStatus``

            - Library system → Student: ``confirmBorrow`` / ``rejectBorrow``


    .. grid-item-card:: Activity Diagram

        Represents workflows of stepwise activities and actions, supporting modelling of business and operational processes.

        Represents the *workflow* or *business process* in terms of activities, decisions, and parallel flows. It is useful for modeling how information is processed and transformed.
        
        - Shows activities (tasks), decision points, and start/end nodes.

        - Can represent parallel processes (e.g. two checks happening at the same time).

        - Supports analysis of efficiency and bottlenecks in processes.


        .. admonition:: Example
            :class: hint

            Diagramming the process of onboarding a new employee, from document submission to training allocation.


        .. admonition:: Example
            :class: hint

            **User Registration Process**:

            - Start → Fill registration form → Validate data

            - Decision: *"Data valid?"*

              - If yes → Create user record → Send confirmation email → End

              - If no → Show error message → Return to Fill registration form


    .. grid-item-card:: State Machine Diagram

        Depicts the states of an object and transitions triggered by events.

        Models the *states of an object* and the events that cause transitions between those states. It is valuable for understanding how data entities change over time.

        - Focuses on a single entity (e.g. ``Order``, ``Membership``, ``Ticket``).
        
        - Shows states (e.g. ``Pending``, ``Approved``, ``Cancelled``).

        - Shows events or triggers that cause state changes (e.g. ``payment``, ``received``, ``request cancelled``).


        .. admonition:: Example
            :class: hint

            Modelling the lifecycle of a loan application, from submission to approval, rejection, or withdrawal.


        .. admonition:: Example
            :class: hint

            **Library Membership State**:

            - States: ``Applied`` → ``Active`` → ``Suspended`` → ``Terminated``

            - Transitions:

              - ``Applied`` → ``Active`` (after approval)

              - ``Active`` → ``Suspended`` (after overdue fines)

              - ``Suspended`` → ``Active`` (after fines paid)

              - ``Active`` / ``Suspended`` → ``Terminated`` (on request or policy)


    .. grid-item-card:: Component Diagram

        Models the physical aspects of a system, such as software components, their organization, and dependencies.

        Shows the *high-level structure* of the system in terms of software components and their dependencies. It is useful for analyzing scalability, reliability, and maintainability.


        .. grid:: 1
            :class-row: surface
            :gutter: 3


            .. grid-item-card:: Components

                Logical modules (e.g. User interface, Business logic, Database service).


            .. grid-item-card:: Interfaces

                Services provided or required by components.


            .. grid-item-card:: Dependencies

                How components interact and rely on each other.


        .. admonition:: Example
            :class: hint

            Illustrating the major modules of a hospital management system, such as patient records, billing, and scheduling.


        .. admonition:: Example
            :class: hint

            **Information Management System Components**:

            - Web client component (browser-based interface)

            - Application server component (handles business rules and queries)

            - Database component (stores and manages data)

            - Reporting component (generates analytical reports)

            - Dependencies: Web client → Application server → Database; Application Server → Reporting component


Integrating Diagrams
++++++++++++++++++++

These diagrams complement each other in designing robust information systems:

- **Use-Case Diagrams** capture functional requirements.

- **Class Diagrams** defien the data structure and support database schema design.

- **Sequence** and **Activity Diagrams** detail how information is processed.

- **State Machine Diagrams** track changes in data entities over time.

- **Component Diagrams** show the structural organization of the system.

Using these models together supports the design of database systems that are **efficient**, **secure**, and **aligned with user needs**, and provides a clear basis for implementing queries and operations on the underlying data.


UML Patterns
++++++++++++

Patterns in UML are reusable solutions to commonly occurring problems in software design and information management. They help standardize approachees, improve system quality, and facilitate communication among stakeholders. By applying UML patterns, designers can leverage proven strategies to address issues such as object creation, system organization, and interaction management.

UML patterns can be categorized into **structural patterns** (which deal with object composition), **behavioral patterns** (which focus on object communication), and **creational patterns** (which manage object creation).


.. grid:: 1
    :gutter: 3


    .. grid-item-card:: Singleton

        Ensures a class has only one instance and provides a global point of access.


        .. admonition:: Typical Application
            :class: tip

            Configuration managers, logging systems.


        .. admonition:: Example
            :class: hint

            A system-wide settings manager for a government portal, ensuring all modules access the same configuration.


        .. figure:: https://refactoring.guru/images/patterns/content/singleton/singleton-comic-1-en.png?id=157509c5693a657ba465c7a9d58a7c25
            :align: center
            :width: 80%


    .. grid-item-card:: Factory

        Creates objects without specifying the exact class of object to be created.


        .. admonition:: Typical Application
            :class: tip

            Object creation frameworks, database connections.


        .. admonition:: Example
            :class: hint

            A document management system that generates different types of documents (PDF, Word, Excel) based on user selection.


        .. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20260407144147401428/notificationfactory.webp
            :align: center
            :width: 80%


    .. grid-item-card:: Observer

        Defines a one-to-many dependency so that when one object changes state, all its dependents are notified.


        .. admonition:: Typical Application
            :class: tip

            Event handling systems, notification services.


        .. admonition:: Example
            :class: hint

            In an e-commerce platform, customers are notified when a product they are watching is back in stock.


        .. figure:: https://media.geeksforgeeks.org/wp-content/uploads/20250911164921062949/observer-design-Pattern.webp
            :align: center
            :width: 80%


    .. grid-item-card:: Strategy

        Enables selecting an algorithm's behavior at runtime.


        .. admonition:: Typical Application
            :class: tip

            Sorting routines, payment processing systems.


        .. admonition:: Example
            :class: hint

            A payroll system that selects different tax calculation strategies based on employee type.


        .. figure:: https://upload.wikimedia.org/wikipedia/commons/3/39/Strategy_Pattern_in_UML.png?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail_unscaled
            :align: center
            :width: 80%


    .. grid-item-card:: Composite

        Composes objects into tree structures to represent part-whole hierarchies.


        .. admonition:: Typical Application
            :class: tip

            File systems, organizational charts.


        .. admonition:: Example
            :class: hint

            Modelling a university's organizational structure, where faculties contain departments, which contain staff members.


        .. figure:: https://refactoring.guru/images/patterns/diagrams/composite/problem-en.png?id=3320d7ddc5bdc3e43752bb4393710794
            :align: center
            :width: 80%


Applying UML Patterns
+++++++++++++++++++++

In information management, UML patterns can be leveraged to model data structures, workflows, and business rules. For example, the **Composite Pattern** is useful for representing hierarchical relationships in organizational data, while the **Observer Pattern** can facilitate event-driven updates in distributed information systems.


.. admonition:: Example
    :class: hint

    Consider a hospital information management system:

    - The **Composite Pattern** could be used to model the organizational hierarchy, where a hospital contains multiple departments, each department contains wards, and each ward contains beds and patients.

    - The **Observer Pattern** could be used for alerting staff when a patient's vital signs reach critical levels, ensuring timely responses.

    - The **Strategy Pattern** might be useful for implementing different billing strategies depending on patient insurance types.
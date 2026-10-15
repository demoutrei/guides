Database Normalization
======================

**Database normalization** is an important process in relational database design aimed at organizing data to minimize redundancy, enhance data integrity, and improve database efficiency. It is a systematic process used in relational database design to organize data efficiently by dividing large, complex tables into smaller, related tables. The main motive of this is to confirm redundancy of data (duplicate data) is minimal and unwanted attributes such as insertion, update, and deletion anomalies avoided. Normalization does this through a set of rules known as the normal forms each having distinct requirements that narrow down how the database would be designed.

.. admonition:: Key Takeaways
    :class: tip

    Database normalization is a step by step approach to structuring data in a way that reduces redundancy and preserves data integrity.

    The process is organized into a series of normal forms, each designed to resolve specific types of anomalies and structural problems.

    Applying normalization helps prevent insertion, update, and deletion anomalies, leading to more consistent and maintainable databases.

.. admonition:: Prerequisites
    :class: important

    Before diving into this guide on database normalization, you should have a basic understanding of:

    - **Relational databases**: Familiarity with tables, rows, and columns.
    - **SQL basics**: Knowing how to write simple ``SELECT``, ``INSERT``, and ``JOIN`` queries.
    - **Primary and foreign keys**: Understanding how keys are used to uniquely identify records and establish relationships.
    - **Data types**: Awareness of common data types like ``INT``, ``VARCHAR``, and ``DATE``.

    While this guide explains normalization in detail with examples, having this foundational knowledge will help you follow along more effectively and apply concepts in real-world scenarios.


Objectives
++++++++++

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: Eliminate Data Redundancy

        By breaking data into logical tables and removing duplicate information, normalization helps us make sure that each piece of data is stored only once. This reduces storage requirements nad prevents inconsistencies.
      
    .. grid-item-card:: Confirming Data Integrity

        Normalization enforces data consistency by establishing clear relationships and dependencies between tables. This maintains accurate and reliable data throughout the database.

    .. grid-item-card:: Prevent Anomalies

        Proper normalization prevents common data anomalies:

        .. grid:: 1
            :class-row: surface
            :gutter: 3

            .. grid-item-card:: Insertion Anomaly

                Difficulty adding new data due to missing other data.

            .. grid-item-card:: Update Anomaly

                Inconsistencies that arise when updating data in multiple places.

            .. grid-item-card:: Deletion Anomaly

                Unintended loss of data due to deletion of other data.

    .. grid-item-card:: Optimize Query Performance

        Well-structured tables can improve the efficiency of queries, especially for updates and maintenance, by reducing the amount of data processed.


Requirements of Database Normalization
++++++++++++++++++++++++++++++++++++++

It plays a foundational role in cofirming that databases are not just collections of tables, but well-structured systems capable of handling growth, change, and complexity over time. By applying normalization, organizations can avoid a wide range of data-related issues while providing consistency and performance acrross applications. This also applies to statistical and scientific environments.

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: Consistency and Accuracy

        Without normalization, the same data may be stored in multiple places, leading to inconsistencies and errors. Normalization ensures that updates to date are reflected everywhere, maintaining accuracy is one of the primary benefits of database normalization.

    .. grid-item-card:: Efficient Data Management

        Normalized databases are easier to maintain and modify. Changes to the database structure or data can be made with minimal risk of introducing errors.

    .. grid-item-card:: Scalability

        As databases grow, normalized structures make it easier to scale and adapt to new requirements without major redesigns.

    .. grid-item-card:: Data Integrity Enforcement

        By defining clear relationships and constraints, normalization helps enforce business rules and data integrity automatically.

    .. grid-item-card:: Reduced Storage Costs

        Eliminating redundant data reduces the amount of storage required, which can be significant in large databases.


Features
++++++++

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: Atomicity

        Data is broken down into smallest meaningful units, ensuring that each field contains only one value (no repeating groups or arrays).

    .. grid-item-card:: Logical Table Structure

        Data is organized into logical tables based on relationships and dependencies, making the database easier to understand and manage.

    .. grid-item-card:: Use of Keys
        
        Primary keys, foreign keys, and candidate keys are used to uniquely identify records and establish relationships between tables.

    .. grid-item-card:: Hierarchical Normal Forms

        The process follows a hierarchy of normal forms, each with stricter requirements to further reduce redundancy and dependency.

    .. grid-item-card:: Referential Integrity

        Relationships between tables are maintained through foreign key constraints, ensuring that related data remains consistent.

    .. grid-item-card:: Flexibility and Extensibility

        Normalized databases can be easily extended or modified to accommodate new data types or relationships without major restructuring.


Types of Normal Forms
+++++++++++++++++++++

Database normalization is structured around a series of increasingly strict rules called **normal forms**. Each normal form addresses specific types of redundancy and dependency issues, guiding you toward a more robust and maintainable relational schema.

First Normal Form
^^^^^^^^^^^^^^^^^

Initial state in the process of database normalization. It ensures taht each column in a table contains only atomic, indivisible values, and that each row is uniquely identifiable. By removing repeating groups and multi-valued attributes, it lays the groundwork for a more organized and consistent database structure. This makes querying, updating, and maintaing data more efficient and reliable, and ith helps avoid redundancy right from the beginning of the database design.

**Rule Enforced**: Atomicity

**Problem Solved**: Repeating/multi-valued data

**Dependency Focus**: None

.. admonition:: Key Requirements
    :class: important

    All columns must contain atomic values (no lists, sets, or composite fields).

    Each row is unique (typically enforced by a primary key).

    No repeating groups or arrays within a row.

    Each column contains values of a single data type.

.. admonition:: Key Takeaways
    :class: tip

    1NF requires that each field in a table contains only one value (atomicity).

    Repeating groups and arrays are eliminated by creating separate rows for each value.

    This transformation lays the foundation for the further normalization steps by ensuring a consistent and logical table structure.

.. admonition:: Key Benefits
    :class: tip

    Simplifies data retrieval.

    Establishes a baseline structure.

.. admonition:: Example
    :class: hint

    Suppose you have a table tracking customer purchases, where the "Purchased Products" column contains a comma-separated list of products:

    .. tabs::

        .. tab:: Data Table

            .. csv-table:: Purchases
                :header: CustomerID, CustomerName, PurchasedProducts
                :class: sphinx-datatable

                101, John Doe, "Laptop, Mouse"
                102, Jane Smith, Tablet
                103, Alice Brown, "Keyboard, Monitor, Pen"

        .. code-tab:: sql

            CREATE TABLE Purchases (
              CustomerID INT,
              CustomerName VARCHAR(100),
              PurchasedProducts VARCHAR(255) -- Comma-separated values
            );

    .. grid:: 1
        :gutter: 3

        .. grid-item-card:: Why is this not in 1NF?

            - Non-atomic values
                "Purchased Products" contains multiple items per cell.

            - Querying and updating are complex
                Searching for customers who bought "Mouse" requires string parsing.

            - Data integrity risks
                No way to enforce referential integrity between products and customers.

            - Inconsistent data entry.
                Different delimiters or typos can creep in.

        .. grid-item-card:: Real-World Impact

            - Reporting (e.g. "Who bought a Laptop?") is error-prone.

            - Updates (e.g. renaming "Mouse", to "Wireless Mouse") are tedious and unreliable.

            - Referential integrity cannot be enforced.

        .. grid-item-card:: Real-World Issues

            Reporting challenges
              Generating reports such as "How many customers bought a Laptop?" becomes complicated, as you canot simply filter a column for "Laptop", you must parse the string.

            Update anomalies
              If a product name changes (e.g. "Mouse" to "Wireless Mouse"), you must update every occurrence in every cell, increasing the risk of missing some entries.

            Data integrity risks
              There is no way to enforce referential integrity between products and customers, which can lead to orphaned or inconsistent data.

        .. grid-item-card:: Problems with the Unnormalized Table

            Non-atomic values
              The "Purchased Products" column contains multiple items in a single cell, making it difficult to query or update individual products.

            Data redundancy and inconsistency
              If a customer purchases more products, the list grows, increasing the risk of inconsistency data entry (e.g. different delimiters, typos).

            Difficulties in searching and reporting
              Queries to find all customers who purchased a specific product become complex and ineffiicent.

        .. grid-item-card:: Transformation Steps

            1. Identify columns with non-atomic values.
                In this case, "Purchased Products" contains multiple values.

            2. Split the multi-valued column into separate rows.
                Each product purchased by a customer should be represented as a separate row, ensuring that every field contains only a single value.

        .. grid-item-card:: Transformed Table in 1NF

            .. tabs::

                .. tab:: Data Table

                    .. csv-table:: CustomerProducts
                        :class: sphinx-datatable
                        :header: CustomerID, CustomerName, Product

                        101, John Doe, Laptop
                        101, John Doe, Mouse
                        102, Jane Smith, Tablet
                        103, Alice Brown, Keyboard
                        103, Alice Brown, Monitor
                        103, Alice Brown, Pen

                .. code-tab:: sql

                    CREATE TABLE CustomerProducts (
                      CustomerID INT,
                      CustomerName VARCHAR(100),
                      Product VARCHAR(100)
                    );

            **Explanation**:

            - Each row now represents a single product purchased by a customer.
            - All columns contain atomic values (no lists or sets).
            - The table can be easily queries, updated, and maintained. For example, finding all customers who purchased "Mouse" is now straightforward.


Second Normal Form
^^^^^^^^^^^^^^^^^^

A table is in 2NF if it is in 1NF and every non-prime attribute (i.e. non-primary key attribute) is fully functionally dependent on the entire primary key. This addresses **partial dependencies**, where a non-key attribute depends only on part of a composite key.

.. admonition:: Example
    :class: hint

    .. grid:: 1
        :gutter: 3

        .. grid-item-card:: Transformation to 2NF

            .. grid:: 1
                :class-row: surface
                :gutter: 3

                .. grid-item-card:: 1NF Table

                    .. tabs::

                        .. tab:: Data Table

                            .. csv-table:: Orders
                                :class: sphinx-datatable
                                :header: OrderID, CustomerID, CustomerName, Product

                                201, 101, John Doe, Laptop
                                202, 101, John Doe, Mouse
                                203, 102, Jane Smith, Tablet

                        .. code-tab:: sql

                            CREATE TABLE Orders(
                              OrderID INT PRIMARY KEY,
                              CustomerID INT REFERENCES Customers(CustomerID),
                              CustomerName VARCHAR(100),
                              Product VARCHAR(100)
                            );

                    Issue:
                      "Customer Name" depends only on "Customer ID", not the full primary key ("Order ID", "Customer ID"). This is a partial dependency.

                .. grid-item-card:: Normalization to 2NF

                    Separate customer information into its own table.

                    .. tabs::

                        .. tab:: Data Table

                            .. csv-table:: Orders
                                :class: sphinx-datatable
                                :header: OrderID, CustomerID, Product

                                201, 101, Laptop
                                202, 101, Mouse
                                203, 102, Tablet

                        .. code-tab:: sql

                            CREATE TABLE Orders (
                              OrderID INT PRIMARY KEY,
                              CustomerID INT REFERENCES Customers(CustomerID),
                              Product VARCHAR(100)
                            );
                            
                    .. tabs::

                        .. tab:: Data Table

                            .. csv-table:: Customers
                                :class: sphinx-datatable
                                :header: CustomerID, CustomerName

                                101, John Doe
                                102, Jane Smith

                        .. code-tab:: sql

                            CREATE TABLE Customers (
                              CustomerID INT PRIMARY KEY,
                              CustomerName VARCHAR(100)
                            );

        .. grid-item-card:: Benefits

            - Eliminates redundancy of customer details.

            - Simplifies data maintenance and updates.

            By moving ``CustomerName`` into a separate ``Customers`` table, we ensure it's only dependent on ``CustomerID`` and eliminate partial dependency on a composite key.


Third Normal Form
^^^^^^^^^^^^^^^^^

A table is in 3NF if it is in 2NF and all the attributes are functionally dependent only on the primary key, there are not **transitive dependencies** (i.e. non-key attributes depending on other non-key attributes).

.. admonition:: Example
    :class: hint

    .. grid:: 1
        :gutter: 3

        .. grid-item-card:: Transformation to 3NF

            .. grid:: 1
                :class-row: surface
                :gutter: 3

                .. grid-item-card:: 2NF Table

                    .. tabs::

                        .. tab:: Data Table

                            .. csv-table:: Orders
                                :class: sphinx-datatable
                                :header: OrderID, CustomerID, Product, Supplier

                                201, 101, Laptop, HP
                                202, 101, Mouse, Logitech
                                203, 102, Tablet, Apple
                        
                        .. code-tab:: sql

                            CREATE TABLE Orders (
                              OrderID INT PRIMARY KEY,
                              CustomerID INT,
                              Product VARCHAR(100),
                              Supplier VARCHAR(100)
                            );

                    Issue
                      "Supplier" depends on "Product", not directly on the primary key.

                .. grid-item-card:: Normalization to 3NF

                    Move product and supplier information to separate tables.

                    .. tabs::

                        .. tab:: Data Table

                            .. csv-table:: Orders
                                :class: sphinx-datatable
                                :header: OrderID, CustomerID, ProductID

                                201, 101, 301
                                202, 101, 302
                                203, 102, 303

                        .. code-tab:: sql

                            CREATE TABLE Orders (
                              OrderID INT PRIMARY KEY,
                              CustomerID INT REFERENCES Customers(CustomerID),
                              ProductID INT REFERENCES Products(ProductID)
                            );

                    .. tabs::

                        .. tab:: Data Table

                            .. csv-table:: Products
                                :class: sphinx-datatable
                                :header: ProductID, ProductName, SupplierID

                                301, Laptop, 401
                                302, Mouse, 402
                                303, Tablet, 403

                        .. code-tab:: sql

                            CREATE TABLE Products (
                              ProductID INT PRIMARY KEY,
                              ProductName VARCHAR(100),
                              SupplierID INT REFERENCES Suppliers(SupplierID)
                            );

                    .. tabs::

                        .. tab:: Data Table

                            .. csv-table:: Suppliers
                                :class: sphinx-datatable
                                :header: SupplierID, SupplierName

                                401, HP
                                402, Logitech
                                403, Apple

                        .. code-tab:: sql

                            CREATE TABLE Suppliers(
                              SupplierID INT PRIMARY KEY,
                              SupplierName VARCHAR(100)
                            );

        .. grid-item-card:: Benefits

            Removes transitive dependencies.

            Reduces data duplication.

            Improves data integrity and maintainability.
        
    This transformation improves maintainability and aligns with best practices for how to normalize a database effectively.

    Since ``Supplier`` depends on ``Product`` and not directly on the primary key (``OrderID``), we isolate it into a new ``Suppliers`` table and reference it via the ``Products`` table. This removes transitive dependencies and aligns with 3NF rules.


Boyce-Codd Normal Form
^^^^^^^^^^^^^^^^^^^^^^

BCNF is a stricter version of 3NF. A table is in BCNF if, for every non-trivial functional dependency X → Y, X is a superkey. In other words, every determinant must be a candidate key.

.. admonition:: When is BCNF Needed?
    :class: tip

    BCNF addresses certain edge cases where 3NF does not eliminate all redundancy, particularly when there are overlapping candidate keys or complex dependencies.

.. admonition:: Example
    :class: hint

    Suppose we have a university database that tracks which students are enrolled in which courses, adn who teaches each course. The initial table structure is as follows:

    .. tabs::

        .. tab:: Data Table

            .. csv-table:: StudentCourses
                :class: sphinx-datatable
                :header: StudentID, Course, Instructor

                1, Math, Dr. Smith
                2, Math, Dr. Smith
                3, History, Dr. Jones
                4, History, Dr. Jones

        .. code-tab:: sql

            CREATE TABLE StudentCourses (
              StudentID INT PRIMARY KEY,
              Course VARCHAR(100),
              Instructor VARCHAR(100)
            );

    .. admonition:: Functional Dependencies in the Table

        1. ``(StudentID, Course)`` → ``Instructor``
            Each unique combination of student and course determines the instructor for that course.

        2. ``Course`` → ``Instructor``
            Each course is always taught by the same instructor.

    .. admonition:: Candidate Keys

        The only candidate key in this table is the cmposite key ``(StudentID, Course)``, since both are needed to uniquely identify a row.

    .. admonition:: Why is this Table in 3NF?
        :class: tip

        All non-prime attributes (``Instructor``) are fully functionally dependent on the candidate key ``(StudentID, Course)``.

        There are no transitive dependencies (i.e. no non-prime attribute depends on another non-prime attribute through the candidate key).

    .. admonition:: Why is this Table NOT in BCNF?
        :class: tip

        The functional dependency ``Course`` → Instructor exists, but ``Course`` is not a superkey (it does not uniquely identify a row in the table).

        BCNF requires that for every non-trivial functional dependency X → Y, X must be a superkey. Here, ``Course`` is not a superkey, so this violates BCNF.

    .. admonition:: How to Normalize to BCNF

        To resolve the BCNF violation, we need to decompose the table so that every determinant is a candidate key in its respective table. This is done by splitting the original table into two separate tables.

        .. tabs::

            .. tab:: Data Table

                .. csv-table:: StudentCourses
                    :class: sphinx-datatable
                    :header: StudentID, Course

                    1, Math
                    2, Math
                    3, History
                    4, History

            .. code-tab:: sql

                CREATE TABLE StudentCourses(
                  StudentID INT PRIMARY KEY,
                  Course VARCHAR(100) REFERENCES CourseInstructors(Course)
                );

        .. tabs::

            .. tab:: Data Table

                .. csv-table:: CourseInstructors
                    :class: sphinx-datatable
                    :header: Course, Instructor

                    Math, Dr. Smith
                    History, Dr. Jones

            .. code-tab:: sql

                CREATE TABLE CourseInstructors(
                  Course VARCHAR(100) PRIMARY KEY,
                  Instructor VARCHAR(100)
                );

    .. admonition:: Resulting Structure and Benefits

        All functional dependencies in both tables have determinants that are candidate keys, so both tables are in BCNF.
        
        Data redundancy is reduced: the instructor for each course is stored only once, rather than repeated for every student enrolled in the course.

        Updates are easier and less error-prone: if an instructor changes for a course, you only need to update one row in the ``CourseInstructors`` table.


Normalization versus Denormalization
++++++++++++++++++++++++++++++++++++


Pros and Cons
^^^^^^^^^^^^^

Understanding the trade-offs between normalization and denormalization is crucial for designing databases that are both performant and maintainable.

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: Advantages

        +----------------+----------------------------------+---------------------------------+
        | Aspect         | Normalization                    | Denormalization                 |
        +================+==================================+=================================+
        | Data Integrity | Ensures consistency by           | May compromise integrity due to |
        |                | reducing redundancy and          | data duplication.               |
        |                | enforcing relationships.         |                                 |
        +----------------+----------------------------------+---------------------------------+
        | Efficient      | Easier to maintain and update    | Requires updating in multiple   |
        | Updates        | individual data points           | places, increasing maintenance  |
        |                |                                  | burden.                         |
        +----------------+----------------------------------+---------------------------------+
        | Clear          | Clarifies data structure through | Can obscure logical data        |
        | Relationships  | foreign keys and normalization   | relationships due to flattened  |
        |                | rules.                           | design.                         |
        +----------------+----------------------------------+---------------------------------+
        | Storage        | Reduces storage by eliminating   | Consumes more space due to      |
        | Optimization   | duplicate data.                  | repeated data.                  |
        +----------------+----------------------------------+---------------------------------+
        | Scalability    | Easier to evolve schema without  | Risk of inconsistency increases |
        |                | risking inconsistency.           | as system scales.               |
        +----------------+----------------------------------+---------------------------------+

    .. grid-item-card:: Disadvantages

        +-----------------+---------------------------------+-----------------------------------+
        | Aspect          | Normalization                   | Denormalization                   |
        +=================+=================================+===================================+
        | Query           | Requires joins across multiple  | Simpler queries due to flat       |
        | Complexity      | tables, increasing query        | structure.                        |
        |                 | complexity.                     |                                   |
        +-----------------+---------------------------------+-----------------------------------+
        | Performance     | Slower reads in complex         | Faster read performance with      |
        | Overhead        | queries due to multiple joins.  | reduced need for joins.           |
        +-----------------+---------------------------------+-----------------------------------+
        | Development     | Requires thoughful schema       | Quicker setup for specific        |
        | Time            | design and maintenance.         | reporting or analytic needs.      |
        +-----------------+---------------------------------+-----------------------------------+
        | Flexibility for | Less suited for ad-hoc          | Better aligned with analytics use |
        | BI/Analytics    | reporting; requires views or    | cases due to consolidated data.   |
        |                 | intermediate layers.            |                                   |
        +-----------------+---------------------------------+-----------------------------------+
        | Risk of         | Minimal if properly normalized. | Higher chance of anomalies        |
        | Anomalies       |                                 | from data duplication and         |
        |                 |                                 | inconsistency.                    |
        +-----------------+---------------------------------+-----------------------------------+


What's Best for Performance?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When designing a database, it's important to balance data integrity with system performance. Normalization improves consistency and reduces redundancy, but can introduce complexity and slow down queries due to the need for joins. Denormalization, on the other hand, can speed up data retrieval and simplify reporting, but increases the risk of data anomalies and requires more storage. Understanding these trade-offs helps you choose the right approach for your application's specific needs and workload patterns.


Join Performance versus Flat Tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Normalized databases stored related data in separate tables, which means retrieving information often requires joining these tables together. This structure assists in ensuring the constancy and integrity of data but may slacken the speed of querying particularly in case of intricate queries or data sets of significant sizes.

Denormalized databases on the other hand contain related data in the same table and hence, require fewer tables. This can speed up the read operations, but this would multiply the storage needs and the possibility of duplicating or non-consistent data.


.. admonition:: When Should We Consider Denormalization?
    :class: tip

    Normalization is generally best during the initial design of a database. However, denormalization can be helpful in situations where performance is critical or the workload is heavily focused on reading data. Common scenarios where denormalization is advantageous include:

    - **Analytics and business intelligence (BI) platforms** that need to quickly aggregate data across wide tables.

    - **Content delivery systems** that use denormalized cache layers to speed up response times.

    - **Data warehouses** where historical data snapshots and simplified queries are more important than frequent updates.

    .. important::

        Before denormalizing, always weigh the potential performance improvements against the increased risk of data duplication and the added complexity of maintaining consistency.


Role of Normalization in AI, Big Data, and NoSQL
++++++++++++++++++++++++++++++++++++++++++++++++

With the rise of AI, real-time analytics, and distributed systems, the approach to normalization is changing. While traditional relational databases (RDBMS) still benefit from strict normalization, modern data systems often use a mix of normalized and denormalized structures:

- **Big Data platforms** (like Hadoop and Spark) typically use denormalized, wide-column formats to improve performance and enable parallel processing.

- **NoSQL databases** (such as MongoDB and Cassandra) focus on flexible schemas and high performance, often avoiding strict normalization.

- **AI and machine learning pipelines** prefer denormalized datasets to reduce preprocessing and speed up model training.

Even as these new technologies emerge, understanding normalization remains important, especially when building core relational systems or preparing data for downstream processes. Many modern architectures use normalized databases for core storage, then create denormalized layers or views to optimize performance for specific use cases.


Frequently Asked Questions
++++++++++++++++++++++++++

.. grid:: 1
    :gutter: 3

    .. grid-item-card:: What is 1NF, 2NF, and 3NF in database normalization?

        These are the first three stages of database normalization. 1NF removes repeating groups and ensures atomicity; 2NF builds on this by eliminating partial dependencies, meaning every non-key attribute must depend on the entire primary key; 3NF removes transitive dependencies, ensuring non-key attributes only depend on primary keys. Each stage progressively refines the data model, reeducing redundancy and improving data consistency. Understanding these forms is crucial for creating scalable, maintainable relational database schemas.

    .. grid-item-card:: What is normalization in a database, and why is it important?

        Normalization is a database design technique that structures data to reduce duplication and improve data integrity. By organizing data into related tables and applying rules (normal forms), it prevents anomalies during data insertion, updates, and deletions. Normalization also makes querying more efficient and ensures logical data grouping. It's especially important in relational databases where accuracy and consistency are critical. For systems handling large volumes of transactions or frequent updates, normalization is foundational for performance and reliability.

    .. grid-item-card:: What are the rules of database normalization?

        Normalization follows a hierarchy of normal forms 1NF, 2NF, 3NF, and BCNF each with stricter rules. 1NF requires atomic values and unique rows; 2NF requires full functional dependency on the primary key; 3NF eliminates transitive dependencies; BCNF ensures that every determinant is a candidate key. These rules aim to eliminate redundancy, ensure data integrity, and optimize storage. Proper application of these rules results in more reliable, maintainable, and scalable database schemas.

    .. grid-item-card:: How do you normalize a database using SQL?

        Normalizing a database in SQL involves decomposing large tables into smaller ones and establishing foreign key relationships. For exmaple, to convert a table with customer and order into 2NF, you'd separate customer details into one table and orders into another, linking them with a foreign key. Use SQL ``CREATE TABLE``, ``INSERT``, and ``FOREIGN KEY`` constraints to maintain referential integrity. Normalization typically involves restructuring existing data with careful planning to avoid loss or inconsistency during transformation.

    .. grid-item-card:: What are the benefits and drawbacks of normalization?

        Advantages of normalization are less data redundancy, data integrity, and easy updates. It makes sure that modification done at a certain point is reproduced in other connected documents in an appropriate way. Its advantages, however, are that it has an overhead performance with regards to join and that it is very complex to write queries especially in highly normalized databases.

        Denormalization can be more preferable in high-read situations such as analytics dashboards. The rationale to normalize should, therefore, follow the needs of use cases, performance requirements, and maintenance.

    .. grid-item-card:: What is the difference between normalization and denormalization?

        Normalization breaks down data into smaller, related tables to reduce redundancy and improve consistency; denormalization, on the other hand, combines related data into fewer tables to speed up read operations and simplify queries. While normalization improves data integrity and is ideal for transaction-heavy systems, denormalization is often used in read-heavy systems like reporting tools. The choice depends on the trade-off between write efficiency and read performance.

    .. grid-item-card:: When should I denormalize a database instead of normalizing it?

        Denormalization is suitable when read performance is critical and the data doesn't change frequently. Use it in analytics, reporting, or caching layers where real-time joins would impact speed. Also, in NoSQL or big data environments, denormalizing aligns with the storage and access patterns. However, it should be approached cautiously since it increases data duplication and the risk of inconsistency. In many systems, a hybrid model using both normalized core tables and denormalized views or summaries works best.

    .. grid-item-card:: Is normalization still relevant for modern databases and AI applications?

        Yes, normalization remains essential, especially for transactional systems and data integrity-focused applications. In AI and big data contexts, normalized structures are often used as the source of truth before being transformed into denormalized datasets for training or analysis. Even in NoSQL and distributed systems, understanding normalization helps in modeling relationships and verifying consistency at the design level. While modern workloads may relax strict normalization, its principles are foundational for long-term data quality and manageability.
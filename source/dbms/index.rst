DBMS GuideBook
==============


A **database** is an organized collection of digital data or information stored electronically in a computer system. It allows users to store, manage, update, and retrieve information quickly. Think of it as a smart, high-capacity digital filing cabinet managed by software called a Database Management System (DBMS).


**Database management system** is a software system that manages, stores, and retrieves data efficiently in a structured format. DBMS acts as a bridge between a central database and multiple clients, including apps and users.

- A DBMS connects the central database with multiple clients (applications and users).
- It allows users to create, update, and query databases efficiently.
- Ensures data integrity, consistency, and security across multiple users and applications.
- Reduces data redundancy and inconsistency through centralized control.
- Supports concurrent data access, transaction management, and automatic backups.
- Uses APIs to handle data requests, ensuring secure and efficient access.


Problems with Traditional File-Based Systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before the introduction of modern DBMS, data was managed using basic file systems on hard drives. While this approach allowed user to store, retrieve and update files as needed it came with numerous challenges:


.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: :octicon:`database` Data Redundancy

        Duplicate entries across files.


    .. grid-item-card:: :octicon:`alert` Inconsistency

        Conflicting or outdated information.


    .. grid-item-card:: :octicon:`passkey-fill` Difficult Access

        Manual file search required.


    .. grid-item-card:: :octicon:`shield-slash` Poor Security
        
        No control over data access.


    .. grid-item-card:: :octicon:`people` Lack of Multi-User Support

        No support for collaboration.


    .. grid-item-card:: :octicon:`rows` No Backup/Recovery

        Data loss was often permanent.

A university file-based system storing data in separate files (e.g. Academics, Results, Hostels) often faced these problems.


Components of DBMS Applications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Any DBMS based application is made up of six key components that work together to handle data effectively.


.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: :octicon:`cpu` Hardware

        Physical devices like servers, disks, input-output devices. Stores and processes data; interfaces between real-world inputs and digital systems.

        
        .. admonition:: Examples
            :class: hint

            Personal computer, hard disk, RAM, network devices used for DBMS operations.


    .. grid-item-card:: :octicon:`terminal` Software

        Actual DBMS software like `MySQL`_, `Oracle`_, `PostgreSQL`_. Includes the database engine, OS, network software, and application tools. Translates database access languages into operations.


    .. grid-item-card:: :octicon:`file` Data

        Raw facts stored in structured or unstructured formats.

        Operational Data
            Actual user data (e.g. name, age).

        Metadata
            Data about data (e.g. storage time, size, data type).

        Core reason DBMS exists is to manage and store data efficiently.


    .. grid-item-card:: :octicon:`list-ordered` Procedures

        Instructions and rules for using DBMS effectively. Covers setup, login/logout, data validation, backup, access control, and report generation. Helps ensure consistent and secure use of the system.


    .. grid-item-card:: :octicon:`code-square` Database Access Language

        Used to interact with the database (create, read, update, delete).

        Data Definition Language
            ``CREATE``, ``ALTER``, ``DROP``

        Data Manipulation Language
            ``INSERT``, ``UPDATE``, ``DELETE``

        .. admonition:: Examples
            :class: hint

            SQL, `MyAccess`_, `Oracle`_ `PL/SQL`_.


    .. grid-item-card:: :octicon:`people` People

        Users interacting with DBMS at different levels:

        Database Administrators
            Manage security, performance, user access.

        Developers
            Build applications using the database.

        End-Users
            Use applications to access the database (e.g. students, employees).


Types of DBMS
^^^^^^^^^^^^^

There are several types of DBMS, each tailored to different data structures, scalability requirements and application needs. The most common types are as follows:


Relational Database Management System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RDBMS organizes data into tables (relations) composed of rows and columns. Uses primary keys to uniquely identify rows and foreign keys to establish relationships between tables. Queries are written in **Structured Query Language** (SQL), which allows for efficient data manipulation and retrieval.


.. admonition:: Examples
    :class: hint

    `MySQL`_, `Oracle`_, `Microsoft SQL Server`_, and `PostgreSQL`_.


NoSQL DBMS
~~~~~~~~~~

They are designed to handle large-scale data and provide high performance for scenarios where relational models might be restrictive. They store data in various non-relational formats such as key-value pairs, documents, graphs, or columns. These flexible data models enable rapid scaling and are well-suited for unstructured or semi-structured data.

.. admonition:: Examples
    :class: hint

    `MongoDB`_, `Cassandra`_, `DynamoDB`_, and `Redis`_.


Object-Oriented DBMS
~~~~~~~~~~~~~~~~~~~~

OODBMS integrates object-oriented programming concepts into the database environment allowing data to be stored as objects. Supports complex data types and relationships, making it ideal for applications requiring advanced data modeling and real-world simulations.


.. admonition:: Examples
    :class: hint

    `ObjectDB`_, db4o.


Hierarchical Database
~~~~~~~~~~~~~~~~~~~~~

Organizes data in a tree-like structure, where a record (node) has a single parent and have multiple children. This model is similar to a file system with folders and subfolders. It is efficient for storing data with a clear hierarchy, such as organizational charts or file directories. Navigation is fast and predictable due to the fixed structure. It lacks flexibility and is difficult to restructure or handle complex many-to-many relationships.


.. admonition:: Examples
    :class: hint

    IBM Information Management System (`IMS`_).


Network Database
~~~~~~~~~~~~~~~~

It uses a graph-like model to allow more complex relationships between entities. Unlike the hierarchical model, it permits each child to have multiple parents, enabling many-to-many relationships. Data is represented using records and sets, where sets define the relationships. It is more flexible than the hierarchical model and better suited for applications with complex data linkages.


.. admonition:: Examples
    :class: hint

    Integrated Data Store (`IDS`_), `TurboIMAGE`_.


Cloud-Based Database
~~~~~~~~~~~~~~~~~~~~

They are hosted on cloud computing platforms like `AWS`_, `Azure`_, or `Google Cloud`_. They offer on-demand scalability, high availability, automatic backups, and remote accessibility. These databases can be relational (SQL) or non-relational (NoSQL) and are maintained by cloud service providers, reducing administrative overhead. They support modern application requirements, including distributed access and real-time analytics.

.. admonition:: Examples
    :class: hint

    `Amazon RDS`_, `MongoDB Atlas`_, `Google BigQuery`_.


Database Languages
^^^^^^^^^^^^^^^^^^

Database languages are specialized sets of commands and instructions used to define, manipulate and control data within a database. Each language type plays a distinct role in database management, ensuring efficient storage, retrieval and security of data.


Types of DBMS Language
~~~~~~~~~~~~~~~~~~~~~~

.. grid:: 1
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: Data Definition Language (DDL)

        Deals with database schemas and descriptions, of how the data should reside in the database.

        CREATE
            To create a database and its objects (e.g. table, index, views, store procedure, function, and triggers).

        ALTER
            Alters the structure of the existing database.

        DROP
            Delete objects from the database.

        TRUNCATE
            Remove all records from a table, including all spaces allocated for the records are removed.

        COMMENT
            Add comments to the data dictionary.

        RENAME
            Rename an object.


    .. grid-item-card:: Data Manipulation Language (DML)

        Focuses on manipulating the data stored in the database, enabling users to retrieve, add, update and delete data.

        INSERT
            Insert data into a table.

        UPDATE
            Updates existing data within a table.

        DELETE
            Delete all records from a database table.

        MERGE
            UPSERT operation (insert or update).

        CALL
            Call a `PL/SQL`_ or Java subprogram.

        EXPLAIN PLAN
            Interpretation of the data access path.

        LOCK TABLE
            Concurrency control.


    .. grid-item-card:: Data Control Language (DCL)

        Commands manage access permissions, ensuring data security, by controlling who can perform certain actions on the database.

        GRANT
            Provides specific privileges to a user (e.g. ``SELECT``, ``INSERT``).

        REVOKE
            Removes previously granted permissions from a user.


    .. grid-item-card:: Transaction Control Language (TCL)

        Commands oversee transactional data to maintain consistency, reliability, and atomicity.

        ROLLBACK
            Undoes changes made during a transaction.

        COMMIT
            Saves all changes made during a transaction.

        SAVEPOINT
            Sets a point within a transaction to which one can later roll back.


    .. grid-item-card:: Data Query Language (DQL)

        A subset of SQL to retrieve data from a database without modifying it. Its main command is ``SELECT``, which allows users to fetch specific information based on their requirements.


Applications of DBMS
^^^^^^^^^^^^^^^^^^^^

- **Banking**: Manage accounts and transactions
- **E-commerce**: Tracks products, orders, and customers.
- Library systems
- Payroll systems
- **Healthcare**: Stores patient records and diagnoses.
- **Social media**: Manages user profiles and interactions.
- Online shopping
- **Education**: Handles student grades and schedules.
- Human resources
- Research
- Inventory MS
- **Data science**: Supports analytics and predictions.


.. toctree::
    :maxdepth: 1
    :caption: Topics

    getting-started


.. _Amazon RDS: https://aws.amazon.com/rds/
.. _AWS: https://aws.amazon.com/
.. _Azure: https://azure.microsoft.com/en-us
.. _Cassandra: https://cassandra.apache.org/_/index.html
.. _DynamoDB: https://aws.amazon.com/dynamodb/
.. _Google BigQuery: https://cloud.google.com/bigquery
.. _Google Cloud: https://cloud.google.com/
.. _IDS: https://en.wikipedia.org/wiki/Integrated_Data_Store
.. _IMS: https://www.ibm.com/products/ims
.. _Microsoft SQL Server: https://www.microsoft.com/en-us/sql-server
.. _MongoDB: https://www.mongodb.com/
.. _MongoDB Atlas: https://www.mongodb.com/products/platform/atlas-database
.. _MyAccess: https://myaccess.microsoft.com/
.. _MySQL: https://www.mysql.com/
.. _ObjectDB: https://www.objectdb.com/
.. _Oracle: https://oracle.com
.. _PL/SQL: https://www.oracle.com/asean/database/technologies/appdev/plsql.html
.. _PostgreSQL: https://postgresql.org
.. _Redis: https://redis.io/
.. _TurboIMAGE: https://en.wikipedia.org/wiki/TurboIMAGE
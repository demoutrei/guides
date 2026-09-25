Information and Data Management Fundamentals
============================================


.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: Data

        Consists of unorganized numbers, symbols, or observations lacking explicit context or meaning on their own.

        Examples
          1. 102.4
          2. 3.14
          3. 9.81
          4. 8 billion


    .. grid-item-card:: Information

        Processed and organized data that provides explicit meaning, clarity, and directly supports decision-making.

        Examples
          1. Temperature: 102.4 Fahrenheit
          2. Pi value: 3.14
          3. Gravitational acceleration: 9.81 m/s
          4. Human population: 8 billion


The DIKW Hierarchy
^^^^^^^^^^^^^^^^^^

The **DIKW Hierarchy** is a structural framework used to explain how raw, unorganized facts are progressively transformed into valuable, actionable insights for decision-making.

+-----------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Level           | Description                                                                         | Example                                                                                    |
+=================+=====================================================================================+============================================================================================+
| **Data**        | Raw, unorganized, and unprocessed facts or figures.                                 | 102.4                                                                                      |
+-----------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| **Information** | Processed data equipped with context, structure, and meaning.                       | Patient body temperature is recorded as 102.4 Fahrenheit.                                  |
+-----------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| **Knowledge**   | Applied information combined with domain expertise and understanding.               | Understanding that 102.4 Fahrenheit indicates a high fever requiring medical intervention. |
+-----------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| **Wisdom**      | Strategic synthesis combining knowledge and judgment for ethical, long-term action. | Establishing automated fever triage protocols across clinical operations.                  |
+-----------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+


Primary Objectives of Data Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: Data Quality

        Eliminating duplicate records, resolving system inconsistencies, and maintaining clean, high-integrity data stores; the degree to which a dataset meets established criteria for accuracy, completeness, consistency, timeliness, validity, and uniqueness, making fit for its intended use in decision-making analysis.


    .. grid-item-card:: Efficiency

        Automating routine data workflows to deliver relevant information with minimal operation friction; to store, access, process, and update data using the least amount of system resources---such as CPU time, memory, storage space, and network bandwidth---while maintaining fast response times and high accuracy.


    .. grid-item-card:: Compliance

        Protecting data assets via encryption, `Role-Based Access Control (RBAC)`_, and regulatory standards (`GDPR`_, `HIPAA`_); to ensure an organization handles digital assets strictly within legal, regulatory, and ethical boundaries. It defines the systematic adherence to external laws and internal policies protecting data security and privacy.


    .. grid-item-card:: Strategic Alignment

        Empowering teams and executive leadership to leverage business intelligence for competitive advantage; to ensure that all data policies, storage systems, and governance frameworks directly support and drive the overarching goals of the organization. It connects technical data operations with business outcomes to maximize value and minimize waste.


Key Lifecycle Stages
^^^^^^^^^^^^^^^^^^^^

1. Collection & Capture
    Ingesting raw data via standardized forms, APIs, IoT sensors, and direct user entry.

2. Storage & Processing
    Organizing structured data in relational SQL, document stores, or cloud warehouses.
    
3. Organization & Retrieval
    Applying metadata tags, indexing, and cataloging for rapid and accurate querying.

4. Governance & Safeguard
    Managing access policies, audit trails, and executing secure archival or disposal.


Data Properties
^^^^^^^^^^^^^^^

Data properties refer to the characteristics, attributes, or rules that define a specific piece of data. The three essential pillars determining data utility and organizational value: `Quality <#dimensions-of-data-quality>`_, `Accuracy <#data-accuracy-controls>`_, and `Timeliness <#data-timeliness-operational-impact>`_.


Dimensions of Data Quality
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. grid:: 1 2 2 2
    :class-row: surface
    :gutter: 3


    .. grid-item-card:: Completeness

        All required data is present. Missing contact numbers or addresses reduce utility for marketing or support.

    
    .. grid-item-card:: Consistency

        Absence of contradictions. Conflicting birthdates across systems create confusion and system errors.


    .. grid-item-card:: Relevance

        Data pertains directly to the task. Collecting non-pertinent facts adds noise without adding business value.


    .. grid-item-card:: Reliability

        Sourced from trustworthy origins and verifiable (e.g. financial figures drawn from audited statements).


Data Accuracy & Controls
~~~~~~~~~~~~~~~~~~~~~~~~

Data accuracy reflects how correctly data represents real-world entities. Inaccurate data leads to misinformed actions---such as a recorded exam score of 85 instead of 58, or stockout errors in retail.

.. admonition:: Techniques to Improve Accuracy
    :class: tip

    **Validation & Verification**
      Cross-checking sales figures against receipts and transactions.

    **Input Controls**
      Using constrained drop-down menus to eliminate typographical mistakes.

    **Authoritative Cross-Referencing**
      Verifying addresses against postal databases.


Data Timeliness & Operational Impact
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data must be available when decisions occur. Outdated data causes missed opportunities or catastrophic miscalculations.

.. admonition:: Examples
    :class: hint

    **Emergency Services**: Real-time bushfire locations and weather data save lives.

    **Commercial Business**: Fresh sales reports allow rapid adaptation of marketing strategies.

    **Public Health**: Rapid disease reporting enables timely epidemic intervention.


Lifecycle Alignment
^^^^^^^^^^^^^^^^^^^

1. Collection Stage
    Use standardized forms and entry validation to prevent missing or irrelevant data from entering systems.

2. Organization & Modeling
    Implement relational database keys and unique identifiers to prevent record duplication and guarantee consistency.

3. Transformation Stage
    Clean and standardize raw inputs (e.g. date formats) without compromising factual underlying integrity.

4. Presentation Stage
    Design dashboards that highlight current, real-time data tailored to executive decision-making needs.

5. Safety & Security
    Protect data against unauthorized alterations using access controls and encryption to maintain accuracy.


.. _Role-Based Access Control (RBAC): https://www.ibm.com/think/topics/rbac
.. _GDPR: https://gdpr-info.eu/
.. _HIPAA: https://compliancy-group.com/what-is-hipaa-compliance/
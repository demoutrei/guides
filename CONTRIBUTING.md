# Contributing to demoutrei/guides

This repository is open for contributions.


## How can I contribute?


### Pull Requests

Fork the repository, and create a branch of `contrib/<username>`. Append your contribution and ensure that it follows our style standards. Before you issue a PR, make sure it builds with no exceptions or warnings.


### Others

You are recommended to open a Discussion for topics you want to talk about, or something to clarify with; or an Issue regarding something that's already deployed in the guidebooks.


## Style Standards

This project utilizes Sphinx, a documentation generator in Python3.


### Admonitions

At most times, admonitions are generated with the `.. admonition::` directive instead, followed by the admonition title. Its class may vary on what it wants to portray:

- **tip**: Additional useful information regarding that topic.
- **hint**: Examples and alike.

*Unlisted admonition classes will remained used as they are by definition.**


### Links

For a cleaner/readable source code, hyperlinks must be written in **reference** or **targeted form**. Its directives must be placed at the bottom-most part of the source code/file.

```
Ths is a reference_. Works for `multiple words`_ too.

.. _reference: https://google.com
.. _multiple words: https://example.com
```


### Glossary

When a word or terminology is used in a page, and it conveys a different meaning than its conceptual/logical meaning, then that term must be added to the page's glossary section.

```
[...] :term:`language` [...]

.. glossary::

  Language
    A formal system of rules, vocabulary, and grammatical structures used to write instructions that a computer can understand and execute
```

*You may also append a term/noun in the glossary if you simply want to add additional information in regards that matter.*
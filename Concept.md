# Concept: Python for STEM (Science, Technology, Engineering, Mathematics) Scientists
## Brief
This series of talks is aimed at scientists with basic knowledge of the Python programming language who want to learn about more Python-related tools and techniques in order to write better codes for their research projects.

Each session will begin with a 60..90 minute frontal style presentation of packages, tools and programming techniques in Python. After that, I hope to engage in informal discussions about the research questions and coding problems of the participants, which shall influence the choice, order and depth of the presented ideas in the series. That means there is a prepared set of topics to present and discuss. However, the entire scope of the series is somewhat fluid and can adapt to the needs and wishes of the participants, if shared by a sufficiently large portion of them.

I will begin by presenting a number of useful packages and code patterns. See below for a choice of topics we can cover.

There will be no exam or exercise session.

Sessions will often be stand-alone presentations of a single concept, so missing out on some talks should not greatly affect the overall success in this course. If participants indicate greater interest in some aspects, some sessions might require familiarity with topics presented earlier in the series. In doubt, contact me to find out about the next session's topics and requirements.


## Prerequisites
Anyone with a basic knowledge of programming in Python is welcome. In particular, this includes students, graduate and PhD students, employees of UR and guests.

The examples used will often be inspired from problems in physics, so familiarity with linear algebra and analysis is desired. The primary focus will be on the programming aspects, so non-STEM scientists should be able to profit from this series of talks, too, albeit some sessions might be challenging to them.

In the workshop/open discussion part of the sessions, bringing your own computer will facilitate discussions. I recommend an up-to-date installation of a Python 3 interpreter along with an IDE of your choice.

I will be bringing my dog to the talks. Please contact me if you are allergic or otherwise impaired by the presence of a dog.

I will be speaking English unless all participants feel comfortable with German. I understand German, English and French, and can translate to English if you prefer to speak in your mother tongue.


## Topics we *can* cover
The below list of topics is a non-exhaustive list of what I feel capable of explaining. Not all of them fill an entire session, but some of them could fill an entire series of talks. That means, the below list is meant as a basis for discussions. If no input/feedback from participants reaches me, I'll select topics from the list below.

* Refreshing Python Basics
    + Built-in data types
    + Classes and Inheritance
    + Magic Methods
    + Modules and structuring code
    + Conventions and style guides
    + Exception Handling

* Advanced Python Concepts
    + Generators and Lazy Evaluation
    + Iterators
    + Decorators
    + Metaclasses
    + Introspection and Metaprogramming
    + Type annotations

* Python Packages
    + Handling input parameters
        - argparse -- writing command line based programs
        - configparser -- dealing with settings files

    + Numerics
        - numpy -- fast operations on (multidimensional) arrays
        - pandas -- data analysis on large data series in tabular format (based on numpy)
        - scipy -- implementations of common mathematical techniques such as Fourier Transform, integration, finding extremal values, ...
        - tensorflow and keras -- machine learning

    + Data Exchange File Formats
        - pickle -- a Python-internal format for quick reuse in other Python projects
        - json -- a human readable format, apt for exchange with other (non-)Python projects
        - toml -- a human readable format, apt for exchange with other (non-)Python projects
        - csv -- a human readable tabular format, apt to be loaded in spreadsheet programs like MS Excel or Libre Office Calc
        - xml -- an arguably human readable format for complex structured text-based information

    + Concurrency
        - threading -- "multitasking in a single processor"
        - multiprocessing -- using multiple processors at once
        - asyncio -- another multitasking paradigm

    + Interaction with the environment outside of the Python Script
        - subprocess -- executing other programs from within a Python script and working with their output
        - os -- foo
        - glob -- foo

    + Internet and networking
        - urllib -- downloading information from the web into memory
        - ftplib -- communication with a fileserver over the FTP protocol
        - imaplib -- sending and receiving email (the more modern protocol)Beginning
        - poplib -- sending and receiving email (the older and hardly any more in use protocol)Beginning

    + Time
        - timeit -- measuring execution time
        - time -- measuring time in general, working with time differences

    + Visualization
        - matplotlib -- the default visualization library
        - seaborn -- based on matplotlib and pandas, allows a more convenient way of defining plots
        - pillow -- work directly with images

    + Misc
        - tkinter -- graphical user interfaces
        - itertools -- foo
        - functools -- foo
        - unittest -- foo
        - sys -- foo
        - re -- RegExes: Pattern matching in strings
        - collections -- foo
        - pprint -- foo
        - graphlib -- foo

* General concepts in IT
    + Text representation in memory/encoding, Unicode and UTF
    + File System Features
    + Big O notation
    + git, github and gitlab -- version control and backups
    + IDEs -- QtCreator for Python, IntelliJ, Eclipse, Spyder


## Example Curriculum
The following selection from the topics above is based on my personal experience (things I use often or wished I'd have known about them earlier)

* Structuring a project
    - Example Simulation: particle in a potential landscape
    - Modelling reality in data structures
    - Encapsulation in classes and modules
    - Inheritance and composition
    - Deciding Input- and Output-Format

* Writing fast code
    - Code analysis, Big-O notation
    - Profiling
    - numpy
    -

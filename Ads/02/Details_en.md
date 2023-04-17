# Python Booster Pack
This four-session class aims to explain and demonstrate advanced concepts in Python specifically for use in scientific context. The sessions will be classic presentations of ca. 90 minutes each. Optionally, participants may engage in informal discussions about any programming related topics that come to mind, including problems with their current research projects.

The prepared sessions are stand-alone, meaning missing out on one presentation should not prevent you from joining a subsequent one.

## Syllabus
Below you'll find a summary of the four sessions of this series.

### Project Design and Encapsulation
Scientific simulations tend to be rather complex and comprise of many layers of interacting systems. In this session we will discuss how to transform a web of physical interactions into maintainable (i.e. well understandable) code by leveraging Python's classes and modules. We will explore this given an example code simulating N non-interacting particles in an arbitrary potential.

### Introduction To Metaprogramming
In Python you can change the behavior or your code at runtime. While this sounds like a recipe for unreadable code, it actually allows to make work a lot easier, especially when using some features built directly into the language. In this session, the concept of *decorators* is presented along with a look "under the hood" of Python. We will gain a deeper understanding of how Python handles our code and how to use that to increase both, how fast we can create code and how fast that code runs.

### Iterators and the Lazy Evaluation Paradigm
When Python runs an ordinary for loop, a lot is happening behind the scenes. We will analyze both, the what and the why and bring that newly gained knowledge to use by optimizing our money-to-sweets conversion rate. We will also understand the command *yield*, generator expressions and have a look into functional programming.


### Parallelism and Multiprocessing
When brute force doesn't help, you're not using enough of it. Some problems in scientific computing can only be solved by raw computing power. Modern computers usually have several CPUs that work independently from the others. In this lecture, we will learn to use the *multiprocessing* module which allows us to run multiple parts of a simulation in parallel. We start with some vocabulary that will allow you to understand online resources (regardless of the language you are working in) before focussing on the implementation in Python.


## Prerequisites
Anyone with a basic knowledge of programming in Python is welcome. In particular, this includes students, graduate and PhD students, employees of UR and guests.

The examples used will often be inspired from problems in physics, so familiarity with linear algebra and analysis is desired. The primary focus will be on the programming aspects, so non-STEM scientists should be able to profit from this series of talks, too, albeit some sessions might be challenging to them.

In the workshop/open discussion part of the sessions, bringing your own computer will facilitate discussions. I recommend an up-to-date installation of a Python 3 interpreter along with an IDE of your choice.

I will be bringing my dog to the talks. Please contact me if you are allergic or otherwise impaired by the presence of a dog.

I will be speaking English unless all participants feel comfortable with German. I understand German, English and French, and can translate to English if you prefer to speak in your mother tongue.

## Outlook
If sufficiently many participants are interested, the series can be extended. Details will be discussed in class; the goal is to find a compromise that suits most if not all participants. Topics we can cover include, but are not limited to:

* Efficiency

    How do we recognize and eventually write code that works fast?<br>
    Why does Python code (usually) run slower than C code and how do we get by this barrier?

* Numerics Miniseries

    In three sessions, we will discuss derivatives, integrals, (partial) differential equations, Fourier transformation and noise removal using numpy and scipy.

* More Metaprogramming

    Type hints and annotations are concepts that do not (usually) affect how a code runs but allows other tools to find bugs for us and make our lives as coders easier.
    I will show some of these tools and how these metadata together with decorators can have a truly noteworthy impact on how we write code.

* Handling Constants and Parameters

    Often, the same code needs to be run with only a few parameters changed (e.g. strength of a magnetic field).
    We will discuss code patterns that allow you to make such changes easily and without crawling around in the guts of your own code.
    At the same time we will look at code organization again.

* Whatever you ask for

    My aim is specifically to help you with your real-world problems.
    If you've heard about about some concept but didn't find the time to read into it, I can try to put together a few slides about that.

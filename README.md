# Kappa Gone


Twitch spam remover or compressor for a less chat-intrusive viewing experience
while staying in the loop.

The thrill of the Twitch chat flying past a viewers eyes as a game roars on can
be an incredibly fun addition to the viewing experience; however, sometimes its
intensity can be quite distracting from the main point of the stream. Turning
off the chat in its entirety could be a solution, but seeing what fellow viewers
have to say about a situation is something many people look forward to.

This extension provides an intuitive and useful alternative to hiding the chat
in its entirety when the distraction is unwanted: the extension will
intelligently group similar spam messages together and display them to the
user in a more intuitive manner that still reflects the same information but
makes space for more unique ideas and chat messages to not get lost in the sea
of spam.

## Table of Contents
* [Key Features](#key-features)
* [Usage](#usage)
   * [Installation](#installation)
   * [Overview](#overview)
* [Development](#development)
   * [Getting Started](#getting-started)
   * [Testing](#testing)
      * [Running Tests](#running-tests)
      * [Writing Tests](#writing-tests)

## Key Features
Some of the key features of Kappa Gone are as follows:
* Understands the context of what will most likely be spammed into the given
chat.
* Provides the option to reduce (to a customizable degree) or entirely remove
Twitch spam chat messages.
* Intuitively groups similar spam messages to improve detection of slight
variations of the same spam messages.
* Logically represents removed messages so that the scale and variation can
easily be inferred.
* Provides minimal chat intrusion into the viewing experience while also keeping
the viewer in the loop with what the chat is saying.


## Usage
This section has not yet been written

### Installation
This subsection has not yet been written.

### Overview
This subsection has not yet been written.


## Development
### Getting Started
Getting started with helping Kappa Gone development is quite simple.
1. Fork this repository then clone it.
1. Move into the directory where you cloned the repository.
1. Install the development package using `pip install -e ".[style]"`.
1. Make changes.
1. Run existing tests and write tests if required (see [Testing](#testing)).

### Testing
Running and writing tests is quite easy in the current development and testing
workflow.

##### Running Tests
1. Install [tox](https://tox.readthedocs.io/en/latest/) using `pip install tox`.
1. Execute `tox` to run all the tests in a separate environment.

##### Writing Tests
1. Navigate to the `test` directory.
1. Create a subdirectory if a new major area of the extension is to be tested.
1. Create a file if a new aspect of a part of the extension is to be tested.
1. Write the test following the conventions of the other test files.

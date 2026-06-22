# Temperature Converter

A simple Python Temperature Converter project built as part of my Python learning journey.

This repository contains **two versions** of the same project to demonstrate my progress in software design and programming concepts.

## Project Goal

The application converts temperatures between:

* Celsius (C)
* Fahrenheit (F)
* Kelvin (K)

It validates user input and performs the appropriate temperature conversion based on the selected units.

---

## Repository Structure

```
temperature-converter/
│
├── procedural-version/
│   └── main.py
│
├── oop-version/
│   ├── ConverterUI
│   └── temperatureconverter.py
│
└── README.md
```

### 1. Procedural Version

The first version was built using procedural programming.

Features:

* User input validation
* Temperature conversion logic
* Loops and conditional statements
* Error handling using try/except
* Basic command-line interaction

This version helped me practice:

* Variables
* Functions
* Loops
* Conditional logic
* Exception handling

---

### 2. OOP Version

After completing the procedural version, I refactored the project using Object-Oriented Programming (OOP).

Features:

* Dedicated `TemperatureConverter` class
* Separation of conversion logic from user interaction
* Cleaner project structure
* Reusable conversion methods
* Conversion history tracking
* Formatted history output using PrettyTable
* Multiple conversions in a single session

This version helped me practice:

* Classes and objects
* Constructors (`__init__`)
* Instance attributes
* Code organization
* Separation of concerns
* Modular programming

---

## Example Features

* Convert Celsius to Fahrenheit
* Convert Celsius to Kelvin
* Convert Fahrenheit to Celsius
* Convert Fahrenheit to Kelvin
* Convert Kelvin to Celsius
* Convert Kelvin to Fahrenheit
* Input validation for temperature values
* Input validation for units
* Conversion history display

---

## Technologies Used

* Python
* PrettyTable

---

## What I Learned

Through this project I learned:

* How to validate user input effectively
* The difference between procedural and object-oriented programming
* How to separate business logic from user interaction
* How to organize code into multiple files
* How to build reusable classes
* How to improve a project through refactoring

---

## Future Improvements

Possible future enhancements:

* GUI version using Tkinter
* Unit testing
* Support for additional temperature scales
* File-based conversion history
* More advanced OOP design

---


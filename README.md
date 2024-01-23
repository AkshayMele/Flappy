# Flappy Bird Game in Python using Pygame

![Flappy Bird](assets/Flappy.png)

## Description

This is a simple implementation of the classic Flappy Bird game using Python and the Pygame library. The game features a bird that the player can control to navigate through pipes while avoiding collisions with the ground and pipes.

## Requirements

- Python 3.x
- Pygame library

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/AkshayMele/Flappy.git
   
2. Install the required dependencies:

   ```bash
   pip install pygame
   
3. Run the game:

   ```bash
   python flappy.py

### TABLE OF CONTENTS 

- Git
- UML
- Requirements Engneering
- Analysis
- DDD
- Metrics
- Clean Code Development
- Build Management
- Unit tests
- IDE
- Functional Programming 

### 1. Git
Usage of GitHub for the whole project time

Commit History: https://github.com/AkshayMele/Flappy/commits

### 2. UML 
UML Diagrams used for the development of the code

+ [Dynamic-Activity diagram](https://github.com/AkshayMele/Flappy/blob/main/Docs/UML/Activity%20Diagram.png)
+ [Class Diagram](https://github.com/AkshayMele/Flappy/blob/main/Docs/UML/Class%20Diagram.png)
+ [Deployment Diagram](https://github.com/AkshayMele/Flappy/blob/main/Docs/UML/Class%20Diagram.png)
+ [User Case Diagram](https://github.com/AkshayMele/Flappy/blob/main/Docs/UML/Use_case_diagram.png)

Files: https://github.com/AkshayMele/Flappy/tree/main/Docs/UML

### 3. Requirements Engineering
Two variants are used and by mapping requirements in 2 different tools.

- Self-made version
  - Trello: https://trello.com/b/XsBRYYyo/flappy

  
- Professional version
  - Jira: https://akshay326.atlassian.net/jira/software/projects/FLAPPY/boards/2
  - Incase there is access with Jira, I'm attaching the [screenshot](https://github.com/AkshayMele/Flappy/blob/main/Docs/Jira.png) of the page.

### 4. Analysis
[Checklists and Analysis](https://github.com/AkshayMele/Flappy/blob/main/Docs/Analysis.pdf)

### 5. DDD
Creation with Miro For:
+ [Event Storming Chart](https://github.com/AkshayMele/Flappy/blob/main/Docs/DDD/DDD_Event_Storming.png)
+ [Core Domain Chart](https://github.com/AkshayMele/Flappy/blob/main/Docs/DDD/DDD_core_domain_chart.png)
+ [Domain Relations Chart](https://github.com/AkshayMele/Flappy/blob/main/Docs/DDD/DDD_domain_relation_chart.png)

Find all the images here : https://github.com/AkshayMele/Flappy/tree/main/Docs/DDD

### 6. Metrics

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=AkshayMele_Flappy&metric=bugs)](https://sonarcloud.io/summary/new_code?id=AkshayMele_Flappy)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=AkshayMele_Flappy&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=AkshayMele_Flappy)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=AkshayMele_Flappy&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=AkshayMele_Flappy)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=AkshayMele_Flappy&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=AkshayMele_Flappy)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=AkshayMele_Flappy&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=AkshayMele_Flappy)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=AkshayMele_Flappy&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=AkshayMele_Flappy)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=AkshayMele_Flappy&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=AkshayMele_Flappy)

### 7. Clean Code Development
[Clean Code Development - Documentation](https://github.com/AkshayMele/Flappy/blob/f2b28cccad782e8c5504af1107e007093005c143/Docs/Clean%20Code%20Development.md)

### 8.Build Management

Using Pybuilder to build the Project which enables us to install and import as a package for usage in other projects

→ With Pybuilder: Find files [here](https://github.com/AkshayMele/Flappy/tree/main/target)

### 9. Unit tests

I have conducted 3 unit tets each of them testing different fucntionalities of the code
+ [Test bird movement](https://github.com/AkshayMele/Flappy/blob/main/tests/test_bird.py)
+ [Test collision detection](https://github.com/AkshayMele/Flappy/blob/main/tests/test_collision_detection.py)
+ [Test pipe spawning](https://github.com/AkshayMele/Flappy/blob/main/tests/test_pipe.py)
+ 
### 10. IDE

#### Visual Studio Code is used for the develoment of this project

&rarr; *Build-in*:
+ ``` F5``` (Debug)
+ ``` Shift + Alt + A ```(Toggle block comment)
+ ``` Ctrl + F ``` (To Find in the Script)
+ ``` Ctrl + C/ Ctrl + V``` (Copy/paste)
+ ```Shift+ Alt + Arrow UP/DOWN``` (To Copy line(s) up or down)
+ ```Ctrl + Z / Ctrl + Y``` (To Undo/Redo)
+ ```Ctrl + /``` ( Comment/Uncomment selection)

&rarr; *Custom Key Shortcuts used*:

-``` Ctrl + Shift + / ``` (Add line comment)

### 11. Functional Programming

I have created a small [Weather APP](https://github.com/AkshayMele/Flappy/blob/main/Weather/weather.py) to demonstrate fucntional programming.

&rarr; [Only final data structure used in the code]()

&rarr; [Side effect free functions](https://github.com/AkshayMele/Flappy/blob/main/Weather/weather.py#L13C1-L13C79)

&rarr; [Usage of anonymous and Closure Function](https://github.com/AkshayMele/Flappy/blob/main/Weather/weather.py#L26)

&rarr; [Use of higher-order function as parameters and return values](https://github.com/AkshayMele/Flappy/blob/main/Weather/weather.py#L3C1-L3C62)

&rarr; [Functions as parameters and return values](https://github.com/AkshayMele/Flappy/blob/main/Weather/weather.py#L22)

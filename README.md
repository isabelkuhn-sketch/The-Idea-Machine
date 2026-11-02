# The Idea Machine
> Interactive coded artworks inspired by Sol LeWitt's Wall Drawings 935 and 936

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Creator](#creator)
<!-- * [License](#license) -->


## General Information
- This Prototype Project is an artistic challenge that follows the concept and design of Sol LeWitt's instruction-based art.
- In this project, I translated two of LeWitt's works: [Wall Drawing 935](https://www.sfmoma.org/artwork/2000.462/) and [Wall Drawing 936](https://www.sfmoma.org/artwork/2000.463/).
- I designed this project to be a contemporary interpretation of [LeWitt's artistic concept](https://www.sfmoma.org/artist/Sol_LeWitt/?showall=1), where instead of being carried out by another artist, code carries out the instructions to generate the artwork. The repeatable and variable nature of the code aligns with the repetition and variance of LeWitt's works.
- The purpose of this project is to explore how artistic concepts and sketches can be digitally generated and contain elements of interactivity.
- I created a pastel colour palette for both artworks that reflect my personal taste and choice. This can be varied by anyone replicating the code to reflect their own personal taste and choice.  

## Technologies Used
- Processing version 4.5.6 using Python Mode

## Features
- Both artworks have a 1200 x 800 canvas size, black background, four boxed sections with colourful geometric shapes.
- Both have interactive components.
- They differ in type of shapes and interactivity.  

**Wall Drawing 935**
  - Straight vertical, horizontal, and diagonal stripes.
  - Pressing the mouse moves all the colours along by one step with each click and cycles through the 11 colours in the list.  

**Wall Drawing 936**
  - Curved stripes expanding in varying directions.
  - Mouse movement alters the width of the stripe and rotates through the six colours in the list.
  - Pressing the mouse increases the stripe width while held down.

## Screenshots
### Wall Drawing 935
First Generated
<img width="1196" height="817" alt="first produced 2" src="https://github.com/user-attachments/assets/14f2abc3-c493-4de6-8c24-4c33068d00c7" />
After one click
<img width="1190" height="820" alt="1 click 2" src="https://github.com/user-attachments/assets/6dff886d-d3d2-43c9-8a74-7f499b15757e" />
After multiple clicks
<img width="1190" height="817" alt="multiple clicks 2" src="https://github.com/user-attachments/assets/d1c1ff32-9fb6-4963-afbf-41cd6e3cd5b6" />

### Wall Drawing 936
First Generated
<img width="1195" height="821" alt="first generated 2" src="https://github.com/user-attachments/assets/67832a1a-8e9c-49c7-a8a0-d9252ff9a90d" />
Mouse moved up/down
<img width="1192" height="820" alt="mouse moving up and down to rotate colours 2" src="https://github.com/user-attachments/assets/ee0abdff-6f26-47c5-8bbc-14d8ede38f64" />
Mouse moved across to high end of x-axis
<img width="1196" height="821" alt="mouse moved across to right fully  2" src="https://github.com/user-attachments/assets/24a379e4-d878-4f93-8d4f-72c254cc192c" />
Mouse moved to middle
<img width="1194" height="818" alt="mouse in middle 2" src="https://github.com/user-attachments/assets/525a6daa-21f2-4f8c-834a-ce5cc2c205e9" />


## Setup
### Requirements 
- First download [Processing](https://processing.org/download)
- Once in Processing, click the mode dropdown in the top right corner and install Python Mode if not already installed

### Getting Started
- Download or copy either or both of the sketch folders named **Wall_Drawing_935** and **Wall_Drawing_936**
- Open the '.pyde' file from the folder in Processing (Note: keep '.pyde' file inside folder with same name, otherwise Processing can't find the sketch)

## Usage
- Press **Run** (play button) in Processing to generate the artwork
  
**Wall Drawing 935**  
- Click with the mouse anywhere on the artwork to interact with it and watch the colours cycle through

**Wall Drawing 936**
- Move the mouse over the artwork and notice the rotation of colours (up and down) and changing of curve width (side to side)
- Press down with the mouse to increase the curve width, release to go back

## Project Status
- Project is complete


## Room for Improvement
- Incorporate more and/or different interactions


## Acknowledgements 
- This project was inspired by Sol LeWitt's famous **Wall Drawings** collection, specifically the two works [Wall Drawing 935](https://www.sfmoma.org/artwork/2000.302/) and [Wall Drawing 936](https://www.sfmoma.org/artwork/2000.303/).
- I relied on this Processing reference list <https://py.processing.org/reference/> throughout my whole project development to experiment and then further research how to use different references
- GeeksForGeeks <https://www.geeksforgeeks.org/python/python-programming-language-tutorial/> was used throughout the project development 
- This Processing tutorial <https://py.processing.org/tutorials/interactivity/> was used to guide interactivity
- Daniel Shiffman's tutorial on <https://hello.processing.org/editor/#interact> guided my learning and application 
- I used the README template to structure this <https://github.com/ritaly/README-cheatsheet/blob/master/README.md?plain=1>

## Creator
Created by Isabel Kuhn

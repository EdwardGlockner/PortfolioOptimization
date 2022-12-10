# Portfolio Optimization
# Table of Contents
- [About the Project](#about-the-project)
  * [Description](#description)
  * [Assignment 1](#assignment-1)
  * [Assignment 2](#assignment-2)
  * [Assignment 3](#assignment-3)
  * [Assignment 4](#assignment-4)
  * [Assignment 5](#assignment-5)
  * [Assignment 6](#assignment-6)
  * [Assignment 7](#assignment-7)
  * [Assignment 8](#assignment-8)


- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Run Locally](#run-locally)

- [Contact](#contact)
- [Links](#links)
  

<!-- About the Project -->
## About the Project

<!-- Description -->
### Description
This is the final project of the course Scientific Computing II at Uppsala University, Sweden. In this project we solve the wave equation in both the 1 dimensional case (a string) and the 2 dimensional case (a plane) using the numerical methods Runge Kutta of fourth order and Central Difference of second order. We analyze both Neumann and Dirichlet boundary conditions.

By obtaining discrete spatial finite difference approximations of the wave equation, the equation transforms into an initial-value problem (IVP). To get the discretisation matrixes we use the function FSBP4.m, provided by the course administrator. This IVP can be solved fairly easiliy with the use of numerical approximation methods. The files Assignment1-Assignment7 treats the wave equation in 1 dimension, and Assignment8 solves the wave equation in 2 dimensions.

The project is split into 8 sub assignments, and are divided into 8 folders. Each folder has a "main" file, called "Assignment{x}.m" with different helper functions and images. 

-----------
<!-- Assignment 1 -->
### Assignment 1 

In this file, Assignment1.m, we analyze the IVP:s eigenvalues for the case with Dirichlet boundary condition. We plot both the analytical and the numerical solutions.

-----------
<!-- Assignment 2 -->
### Assignment 2 

In this file, Assignment2.m, we find the biggest eigenvalues for Neumann and Dirichlet boundary condition. This will tell us what the biggest time-steps we can use for numerical stability are when solving using Runge Kutta 4.

-----------
<!-- Assignment 3 -->
### Assignment 3

In this file, Assignment3.m, we solve the wave equation using Runge Kutta 4 using both Neumann and Dirichlet boundary condition. 

-----------
<!-- Assignment 4 -->
### Assignment 4

In this file, Assignment4.m, we analyze the convergence rate of Runge Kutta 4, to verify that the accuracy is fourth order.

-----------
<!-- Assignment 5 -->
### Assignment 5

-----------
<!-- Assignment 6 -->
### Assignment 6

In this file, Assignment6.m, we solve the wave equation using Central Difference 2.

Below are snapshots of the wave equation at different times with Dirichlet boundary condition:

<div class="align-center"> 
  <img src="https://github.com/EdwardGlockner/Wave-Equation-Simulation/blob/main/Assignment%206/Images/Ass6_D_0.2.png" width="410" height="350"/>
  <img src="https://github.com/EdwardGlockner/Wave-Equation-Simulation/blob/main/Assignment%206/Images/Ass6_D_0.7.png" width="410" height="350"/>
</div>

-----------
<!-- Assignment 7 -->
### Assignment 7

In this file, Assignment7.m, we analyze the converegence rate of central difference 2, to verify that the accuracy is of order 2.

-----------
<!-- Assignment 8 -->
### Assignment 8

In this file, Assignment8.m, we solve the wave equation on a plane for both Neumann and Dirichlet boundary conditions using Central Difference of order 2. 

Below are snapshots of the wave equation at different times with Dirichlet boundary condition:

<div class="align-center"> 
  <img src="https://github.com/EdwardGlockner/Wave-Equation-Simulation/blob/main/Assignment%208/Images/Ass8_D_0.0.png" width="410" height="350"/>
  <img src="https://github.com/EdwardGlockner/Wave-Equation-Simulation/blob/main/Assignment%208/Images/Ass8_D_1.png" width="410" height="350"/>
</div>

<div class="align-center"> 
  <img src="https://github.com/EdwardGlockner/Wave-Equation-Simulation/blob/main/Assignment%208/Images/Ass8_D_2.png" width="410" height="350"/>
  <img src="https://github.com/EdwardGlockner/Wave-Equation-Simulation/blob/main/Assignment%208/Images/Ass8_D_10.png" width="410" height="350"/>
</div>

<!-- Getting Started -->
## Getting Started

<!-- Prerequisites -->
### Prerequisites

Since this project is a MATLAB project, an active MathWorks license is needed to compile the code. See: https://se.mathworks.com/pricing-licensing.html.  

<!-- Run Locally -->
### Run Locally

Clone the project

```bash
  git clone https://github.com/EdwardGlockner/Wave-Equation-Simulation.git
```

Go to the project directory

```bash
  cd my-project
```

and navigate to one of the assignment folders. Open the folder in MATLAB, and run Assignment{x},m file. If you don't have the ability to run MATLAB, you can see the .pdf-file.


<!-- Contact -->
## Contact

Edward Glöckner - [@linkedin](https://www.linkedin.com/in/edwardglockner/) - edward.glockner5@gmail.com

Project Link: [https://github.com/EdwardGlockner/Wave-Equation-Simulation](https://github.com/EdwardGlockner/Wave-Equation-Simulation)


<!-- Links -->
## Links

Here are some helpful links:

 - [Wave equation](https://en.wikipedia.org/wiki/Wave_equation)
 - [Finite difference](https://en.wikipedia.org/wiki/Finite_difference)
 - [Runge kutta](https://en.wikipedia.org/wiki/Runge–Kutta_methods)


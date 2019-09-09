


ScaffCC - NISQ Version
================
This is a light weight version of ScaffCC designed specifically with NISQ applications in mind. It compiles scaffold programs to flattenedQASM, hierarchicalQASM and OpenQASM and features and updated version of the Resource Counts pass that utilizes IBMQ to generate resource estimates. 

### What's Changed?
## 1. Clang and LLVM V.8.0.1
    a. OpenQASM pass working
    b. Some issues with the other passes not being able to access files
    c. Building using cmake 
    
## 2. Automated Testing Suite
     a. Compiles and runs NISQ scaffold programs on IBM's simulators and checks counts 
     b. Requires IBM token
     
## 3. Resource Estimation Pass
     a. Relies on IBM's simulator to estimate resources
     b. Flag added to pick between default (original) resource estimation versus IBM version
     c. Requires a openQASM file

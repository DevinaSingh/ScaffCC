


ScaffCC - NISQ Version!
================
This is a light weight version of ScaffCC designed specifically with NISQ applications in mind. It compiles scaffold programs to flattenedQASM, hierarchicalQASM and OpenQASM and features an updated version of the Resource Counts pass that utilizes IBMQ to generate resource estimates. 

### What's Changed?
## 1. Clang and LLVM V.8.0.1
    a. OpenQASM pass working
    b. Some issues with the other passes not being able to access files
    c. Built using cmake 
    
## 2. Automated Testing Suite
     a. 9 NISQ scaffold tests added 
     a. Testing suite compiles and runs programs on IBM's simulators to generate counts
     c. Compares these counts against what they should be  
     b. Requires IBM token 
     
## 3. Resource Estimation Pass
     a. Relies on IBM's simulator to estimate resources
     b. Flag added to pick between default (original) resource estimation versus IBM version
     c. Requires a openQASM file

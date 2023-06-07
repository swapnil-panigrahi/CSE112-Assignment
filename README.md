# CSE112-Assignment
# CO ASSembler-Simulator Assignment
This is the repository for group B1000<sub>2</sub> for the Computer Organization course during the Winter 2022 semester at IIITD.

## About the repository
- This repository includes a Simple-Assembler and Simple-Simulator called Assembler and Simulator respectively.
- The purpose of the assembler is to convert a given code, as per the ISA (refer to Assignment.pdf), into its binary equivalent. Additionally, it can provide detailed error reports, including line numbers.
- The simulator processes such binaries and dumps the program counter and the registers while the program is running, and after an `hlt` instruction, it dumps the state of the memory. It is important to note that we follow a Von-Neumann Architecture (unified memory | Instruction memory, hlt, followed by variables). It also plots the graph of memory access per cycle and is not capable of handling exceptions.
- `automated-testing` is a testing suite designed to testify the correctness of outputs from the `assembler` and `simulator`. It contains the traces, binaries and a few assembly codes.
- It is important to note that the assumption is made that a Von Neumann Architecture is being used.

## Evaluation process
To evaluate the repository, follow these steps:

- Change your current directory to the root directory where you have cloned the repository
- Go to the `automatedTesting` directory
- Execute the following command: `./run` for evaluation
- Add the option `--no-sim` for evaluation of assembler only
- Add the option `--no-asm` for evaluation of simulator only

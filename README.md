# MLIR Examples

This repository contains MLIR  examples that can be helpful for writing a 
programming language.

MLIR (Multi-Level Intermediate Representation) is an LLVM project made to 
address some of the shortcomings of LLVM IR. Many languages using LLVM as 
a backend (e.g. Swift, Rust) have resorted to defining their own IRs 
because dropping all the way down to LLVM IR loses almost all of a language’s semantics.

Note that the recommendation is to use the C++ API, or bindings for a language (C, Python, etc.). 
Writing the MLIR without using the provided APIs can be daunting. So, these examples are for educational 
purposes only.

MLIR concepts:

* Lowering
* Dialect
* Module
* Operation
* Region
* Block

### Lowering
A pipeline of passes (steps) to lower the code from high level code to low level code.
For example: C is the high level code and binary machine code is the low level code. 
Each pass in the pipeline has the opportunity to improve performance and/or semantics 
of the lowered code.

### Dialect
A collection of rules, operations, and types for a specific domain (Math, Memory, Concurrency, etc.).

Some default dialects:
* scf: structured control flow, loops and conditionals
* index: accessing elements in arrays and tensors
* func: defining and calling functions
* memref: memory allocation and management. Buffers
* arith: arithmetic, bitwise, and comparison operations for integers/floats. Including vectors, scalars, tensors
* tensor: multi-dimensional arrays (tensors)
* linalg: linear algebra

### Module
The top level set of Operations.

### Operation
A collection of Regions.

### Region
A collection of Blocks. Syntax: `{}`

### Block
A collection of Operations. Syntax: `^` and a label. Like: `^bb1`.

```
module {
  func.func @select(%a: i32, %b: i32, %flag: i1) -> i32 {
    cf.cond_br %flag, ^bb1(%a : i32), ^bb1(%b : i32)
    
    ^bb1(%x : i32) :
      return %x : i32
  }
}
```

The above MLIR can be read this way:
* definition of a Module
* the Operation `func.func` defines a function with the symbol name `select`
  * `select` function takes 3 arguments: `a`, `b` and `flag`
  * `a` and `b` have `i32` type, `flag` has `i1` type 
  * `select` function returns an `i32` type
* inside the function we have one Region
* inside the Region we have an entry Block
  * an entry Block is a Block with no label and no arguments that may occur at the beginning of a Region
* inside the entry Block we have one Operation and one basic Block
  * the Operation `cf.cond_br` is a condition that checks if `flag` is `1` or `0`
    * if `flag` is `1`. it calls the basic Block `^bb1` with the value of `a`
    * if `flag` is `0`. it calls the basic Block `^bb1` with the value of `b`
  * basic Block `^bb1` takes 1 argument of type `i32`
    * basic Block `^bb1` returns from the Function with the value received in the argument `x`

### Install

The examples use the Python bindings. Most of this document should work for Mac and Linux. 
Find Python's correct path, version and get latest pip:

```shell
readlink -f $(which python3)
python3 --version
python3 pip install --upgrade pip
```
Current python3 version: 3.13.5

Because we are using the Python bindings, we need to tell CMake to build the bindings. Double check that 
the following variables are passed to the cmake command:

```shell
MLIR_ENABLE_BINDINGS_PYTHON=ON
Python3_EXECUTABLE=$(readlink -f $(which python3))
```

In order to install the MLIR tools you need the following in your system:

```
llvm cmake ninja ccache
``` 

Now we can build the tools:

```shell
cd $HOME
git clone https://github.com/llvm/llvm-project
cd llvm-project
python3 -m pip install -r mlir/python/requirements.txt
mkdir build
cd build
cmake -G Ninja ../llvm \
  -DLLVM_ENABLE_PROJECTS=mlir \
  -DMLIR_ENABLE_BINDINGS_PYTHON=ON \
  -DPython3_EXECUTABLE=$(readlink -f $(which python3))
  -DLLVM_BUILD_EXAMPLES=ON \
  -DLLVM_TARGETS_TO_BUILD="Native;ARM;X86" \
  -DCMAKE_BUILD_TYPE=Release \
  -DLLVM_ENABLE_ASSERTIONS=ON \
  -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ \
  -DLLVM_CCACHE_BUILD=ON
cmake --build . --target check-mlir
sudo cmake --build . --target install
```
It's going to take a while!

Verify:
```shell
mlir-opt --version
ninja check-mlir-python
```

You need to add 2 environment variables
```shell
export LLVM_PROJECT="$HOME/llvm-project"
export PYTHONPATH="$LLVM_PROJECT/build/tools/mlir/python_packages/mlir_core"
```

### Disclaimer
I'm a noob with all things related to MLIR and LLVM.

### Resources
* [MLIR rationale](https://mlir.llvm.org/docs/Rationale/Rationale/) - docs - great read to understand better the design choices
* [MLIR Symbol Tables](https://mlir.llvm.org/docs/SymbolsAndSymbolTables/) - docs - module names, function names, etc., and visibility (public, private, nested)
* [MLIR source code](https://github.com/llvm/llvm-project/tree/main/mlir) - Github
* [Introduction to MLIR](https://www.stephendiehl.com/posts/mlir_introduction/) - Blog 
* [MLIR For Beginners](https://github.com/j2kun/mlir-tutorial?tab=readme-ov-file) - Github
* [Using MLIR from C and Python](https://youtu.be/E2xLXcrkOTE) - YouTube (2024)
* [MLIR Tutorial](https://youtu.be/Y4SvqTtOIDk) - YouTube (2020)

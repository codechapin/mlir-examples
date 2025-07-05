The following 2 files should produce the same assembly 
with Clang:

* `001-simple-return-0.c`
* `001-simple-return-0.mlir`

A simplified MLIR workflow:

## First pass
Lower the MLIR to LLVM Dialect:

```shell
 mlir-opt 001-simple-return-0.mlir \
  --convert-func-to-llvm \
  --convert-arith-to-llvm \
  --reconcile-unrealized-casts \
  -o 001-simple-return-1.mlir
```

The lowered code is now in `001-simple-return-1.mlir`

Verify:

```shell
mlir-runner -e main -entry-point-result=i32 001-simple-return-1.mlir
```
It will print the result from calling the `@main` Function

## Second pass
Lower the MLIR to LLVM IR

```shell
mlir-translate 001-simple-return-1.mlir -mlir-to-llvmir -o 001-simple-return-2.ll
```
The lowered is now in `001-simple-return-2.ll` as LLVM IR.

## Third pass
Lower the LLVM IR to Object file

```shell
llc -filetype=obj 001-simple-return-2.ll -o 001-simple-return.o
```
## Fourth pass
Lower Object file to executable

```shell
clang 001-simple-return.o -o 001-simple-return.exe
```
Verify
```shell
./001-simple-return.exe
echo $?
```
Should print `39` which is the main function return code

### Resources

* [builtin dialog](https://mlir.llvm.org/docs/Dialects/Builtin/#builtinmodule-moduleop) - docs for module. Note that a module can have a name, more info: [Symbol Tables](https://mlir.llvm.org/docs/SymbolsAndSymbolTables/).
* [func dialog](https://mlir.llvm.org/docs/Dialects/Func/) - docs
* [arith dialog](https://mlir.llvm.org/docs/Dialects/ArithOps/) - docs
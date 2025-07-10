This is very similar to the 001 example, so we follow the same pipeline:

## First pass

```shell
 mlir-opt --convert-func-to-llvm \
  --convert-arith-to-llvm \
  --reconcile-unrealized-casts \
  002-function-call-0.mlir \
  -o 002-function-call-1.mlir
```

The lowered code is now in `002-function-call-1.mlir`

Verify:

```shell
mlir-runner -e main -entry-point-result=i32 002-function-call-1.mlir
```
It will print the result from calling the `@main` Function

## Second pass
Lower the MLIR to LLVM IR

```shell
mlir-translate -mlir-to-llvmir 002-function-call-1.mlir -o 002-function-call-2.ll
```
The lowered code is now in `002-function-call-2.ll` as a LLVM IR.

## Third pass
Lower the LLVM IR to Object file

```shell
llc -filetype=obj 002-function-call-2.ll -o 002-function-call.o
```
## Fourth pass
Lower the Object file to executable

```shell
clang 002-function-call.o -o 002-function-call.exe
```
Verify
```shell
./002-function-call.exe
echo $?
```
Should print `33` which is the main function return code

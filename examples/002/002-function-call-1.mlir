module {
  llvm.func @add(%arg0: i32, %arg1: i32) -> i32 {
    %0 = llvm.add %arg0, %arg1 : i32
    llvm.return %0 : i32
  }
  llvm.func @main() -> i32 {
    %0 = llvm.mlir.constant(11 : i32) : i32
    %1 = llvm.mlir.constant(22 : i32) : i32
    %2 = llvm.call @add(%0, %1) : (i32, i32) -> i32
    llvm.return %2 : i32
  }
}


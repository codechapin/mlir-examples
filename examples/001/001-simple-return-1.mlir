module {
  llvm.func @main() -> i32 {
    %0 = llvm.mlir.constant(39 : i32) : i32
    llvm.return %0 : i32
  }
}


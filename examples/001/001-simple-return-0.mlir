module {
    func.func @main() -> i32 {
        %ret = arith.constant 39 : i32
        func.return %ret : i32
    }
}
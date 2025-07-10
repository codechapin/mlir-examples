module {
    func.func @add(%a: i32, %b: i32) -> i32 {
        %sum = arith.addi %a, %b : i32
        func.return %sum : i32
    }

    func.func @main() -> i32 {
        %lhs = arith.constant 11 : i32
        %rhs = arith.constant 22 : i32

        %ret = call @add(%lhs, %rhs) : (i32, i32) -> i32
        func.return %ret : i32
    }
}
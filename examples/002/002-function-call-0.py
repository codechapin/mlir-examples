from mlir.ir import Context, Location, Module, InsertionPoint, IntegerType
from mlir.dialects import func, arith

with Context(), Location.unknown():
    i32 = IntegerType.get_signless(32)
    module = Module.create()
    with InsertionPoint(module.body):
        @func.func(i32, i32, name="add", results=[i32])
        def add(a, b):
            sum = arith.AddIOp(a, b)
            func.ReturnOp([sum])

        main_func = func.FuncOp("main", ([], [i32]))
        with InsertionPoint(main_func.add_entry_block()):
            lhs = arith.ConstantOp(value=11, result=i32)
            rhs = arith.ConstantOp(value=22, result=i32)

            ret = func.CallOp([i32], "add", [lhs, rhs])

            func.ReturnOp([ret])


    print(module)

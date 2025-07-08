from mlir.ir import Context, Location, Module, InsertionPoint, Block, IntegerType, IntegerAttr
from mlir.dialects import builtin, func, arith

with Context(), Location.unknown():
    i32 = IntegerType.get_signless(32)
    module = Module.create()
    with InsertionPoint(module.body):
        main_func = func.FuncOp("main", ([], [i32]))

        with InsertionPoint(main_func.add_entry_block()):
            ret_code = IntegerAttr.get(value=39, type=i32)
            ret_const = arith.ConstantOp(value=ret_code, result=i32)
            func.ReturnOp([ret_const])


    print(module)

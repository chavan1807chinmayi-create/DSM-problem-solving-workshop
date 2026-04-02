math = 50
chem = 50
phys = 50
hindi = 40
print(id(math))
print(id(chem))
print(id(phys))
print(id(hindi))
# Since both math and chem , phys have the same value, they will point to the same memory location, which is why their ids are the same. This is an optimization technique used by Python to save memory.
# different values will have different memory locations, which is why the id of hindi is different from math, chem, and phys.
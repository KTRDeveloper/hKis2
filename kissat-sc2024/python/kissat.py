#!/usr/bin/python3

import ctypes
lib=ctypes.CDLL ("../build/libkissat.so")

print("c Loaded shared Kissat library.")

lib.kissat_init.argtypes = []
lib.kissat_init.restype = ctypes.c_void_p

lib.kissat_release.argtypes = [ctypes.c_void_p]

lib.kissat_add.argtypes = [ctypes.c_void_p, ctypes.c_int]

lib.kissat_solve.argtypes = [ctypes.c_void_p]
lib.kissat_solve.restype = ctypes.c_int

lib.kissat_value.argtypes = [ctypes.c_void_p, ctypes.c_int]
lib.kissat_value.restype = ctypes.c_int

print("c Set types of some library functions.")

class Kissat:
	def __init__(self):
		self.handle = ctypes.c_void_p(lib.kissat_init ())
	def __del__(self):
		lib.kissat_release(self.handle)
	def add(self,lit):
		lib.kissat_add(self.handle,lit)
	def solve(self):
		res = lib.kissat_solve (self.handle)
		return res

print("c Defined Python wrapper class.")

solver = Kissat()

print("c Initialized solver.")

solver.add(1)
solver.add(2)
solver.add(0)

print("c Added some clauses.")

match solver.solve ():
	case 10: print("s SATISFIABLE")
	case 20: print("s UNSATISFIABLE")
	case _: print("s UNKNOWN")

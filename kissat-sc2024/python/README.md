Calling Kissat from Python
--------------------------

After configuring and compiling Kissat with `configure --shared && make` you will get `../build/libkissat.so`.  This can directly be used from Python with the `ctypes` built-in library.  This is explored in `kissat.py` and eventually should become a python module.

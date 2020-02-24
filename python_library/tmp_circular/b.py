# sample for circular import
def b():
    from python_library.tmp_circular.a import a
    pass
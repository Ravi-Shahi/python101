#function to extend modes 
def mode_fullform(str):
    file_modes = {
        "r" : "read",
        "w" : "write",
        "a" : "append",
        "x" : "create"
    }
    return file_modes[str]
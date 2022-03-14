# in, not in
print("str" in "thisisastring")
print("str" not in "thisisastring")

# find, index
print("strinrig".find("ri"))
print("strinrig".rfind("ri"))
print("strinrig".find("ri", 0, 2))
print("strinrig".find("no"))
####################################
print("strinrig".index("ri"))
print("strinrig".rindex("ri"))
try: print("strinrig".index("ri", 0, 2))
except: print("ValueError")
try: print("strinring".index("no"))
except: print("ValueError")
# startswith, endswith
print("startswith".startswith("start"))
print("endswithend".endswith("end"))



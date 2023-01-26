import unreal

# https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/Vector.html?highlight=vector#unreal.Vector

v1 = unreal.Vector(0, 1, 0)
v2 = unreal.Vector(1, 0, 0)
v3 = v1.cross(v2)
print(v3)
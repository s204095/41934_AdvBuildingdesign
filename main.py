import ifcopenshell

from external.BIManalyst_g_48.rules import SpaceRequirement


model = ifcopenshell.open("C:/Users/feizh/Downloads/25-08-D-ARCH.ifc")
name = "Meeting room"
num = 12





SpaceResult = SpaceRequirement.check_space_requirement(model,name,num)




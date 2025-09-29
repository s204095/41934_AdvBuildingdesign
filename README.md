# Focus Area: **Build**

-Manager group 49

## Description of the script
This script is a simple menu-driven IFC tool.

When started, it asks the user for an IFC file path and loads the model.

It then shows a menu with currently available functions:

 - 1. Check space requirement → prompts for a space name and required number, then calls the rule from SpaceRequirement.
 - 2. List column types → fetches and prints all column type names using main.get_column_type_names.
 - 3. Quit → exits the program.

The menu runs in a loop, so the user can perform multiple checks until they choose to quit.

# Claims by analyst groups 

**[Group 48](https://github.com/Schabinsky/BIManalyst_g_48/).**

Whether the number of meeting rooms in the BIM model corresponds to what is stated in the report. The report states that there should be 12 meeting rooms.

 - Number of meeting rooms: Report: 25-08-D-CLIENT, page 2. 

**Description of the script Group 48.:** The script checks whether the specified number of meeting rooms stated in the report is consistent with the BIM model’s design. Step 1: Search for and list rooms named 'Meeting room' Step 2: For meeting room, look up and list NetFloorArea Step 3: Compare agarinst requirement of 2 x 50 m2 & 10 x 30 m2

**[Group 46](https://github.com/riccardopadoan28/BIManalyst_g_46)**

Whether the types of columns in the BIM model correspond to what is stated in the report. 
The report states the following types of columns: 530x200, 360x200, 380x200, 200x300, 200x240, 270x270, 640x200, 260x220, 200x200, 200x1090, 200x120, 380x280, 580x200, 400x300, HE160B, HE120B, HE180B, HE100B, HE140B, HE2200B.

 - Types of columns: Report: 25-08-D-STR, page 14.

**Description of the script Group 46:** checks whether the types of columns mentioned in the report as being used are also consistent with the BIM model’s structural design. Step 1: import the ifcopenshell library; Step 2: open the 25-08-D-STR.ifc file; Step 3: define the building using IfcBuilding; Step 4: extract all the type of columns modeled in the building; Step 5: check out if there are any lack of communication between model and report: an empty dictionary is filled with column type names

**[Group 46](https://github.com/Grumstrup1/41934_G42)**

## Group: 49

Focus Area: 
 ** Build **

Claims checking:
Group 48
1. Whether the number of meeting rooms in the BIM model corresponds to what is stated in the report.
The report states that there should be 12 meeting rooms.

Group 46
2. Whether the types of columns in the BIM model correspond to what is stated in the report.
The report states the following types of columns:
530x200, 360x200, 380x200, 200x300, 200x240, 270x270, 640x200, 260x220, 200x200, 200x1090, 200x120, 380x280, 580x200, 400x300, HE160B, HE120B, HE180B, HE100B, HE140B, HE2200B.

The report and page number or the claims are found in:
Clame no. 1 - Number of meeting rooms: Report: 25-08-D-CLIENT, page 2.
Clame no. 2 - Types of columns: Report: 25-08-D-STR, page 14.
  
Description of the script
Group 48.
The script checks whether the specified number of meeting rooms stated in the report is consistent with the BIM model’s design. 
Step 1: Search for and list rooms named 'Meeting room'
Step 2: For meeting room, look up and list NetFloorArea
Step 3: Compare agarinst requirement of 2 x 50 m2 & 10 x 30 m2

Group 46
The cript checks whether the types of columns mentioned in the report as being used are also consistent with the BIM model’s structural design. 
Step 1: import the ifcopenshell library;
Step 2: open the 25-08-D-STR.ifc file;
Step 3: define the building using IfcBuilding;
Step 4: extract all the type of columns modeled in the building;
Step 5: check out if there are any lack of communication between model and report: an empty dictionary is filled with column type names



For Managers: A summary of the scripts you are running with links to their repos.

# Introduction

## Questions:
- Describe the use case you have chosen
- Who is the use case for?
- What disciplinary (non BIM) expertise did you use to solve the use case
- What IFC concepts did you use in your script (would you use in your script)
- What disciplinary analysis does it require?
- What building elements are you interested in?
- What (use cases) need to be done before you can start your use case?
-What is the input data for your use case?
-What other use cases are waiting for your use case to complete?


## Case decription
- The goal of the tool made is to ...

## The method is ...


## The specific builings elements used in this case, are ...


## How to use the tool
- The script (main.py) is ...

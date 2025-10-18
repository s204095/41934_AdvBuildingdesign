# A2 — Cost-Checking Use Case

## A2a. About Your Group
- **Group coding level (total):** 2  
- **Focus area:** Build  
- **Role:** Manager  

---

## A2b. Identify Claim

### Building
- **ID:** #2508  

### Claim
Cost estimation for structural elements, windows, and spaces.

### Purpose of Checking This Claim
The purpose of verifying this claim is to determine the costs associated with columns/beams, windows, and spaces.  

- **Columns/Beams:** quantity, material type, and dimensions  
- **Windows:** number, dimensions, and type  
- **Spaces:** classification and evaluation  

All elements use the **Molio price database** for cost estimation.  
Cost estimation is critical for financial feasibility — poor control can make a project unviable.  

> *Jeg kan ikke finde nogle priser for spaces.*

---

## A2c. Use Case

### How Would You Check This Claim?
1. Identify three cost-related claims from the report.  
2. Analysts each develop Python scripts to verify them.  
3. Manager integrates all results into a single tool.  
4. Extract quantities using **BlenderBIM** and **ifcOpenShell**.  
5. Compare results with **Molio** price data.

### When Would This Claim Need to Be Checked?
During the **design development phase**, when the model holds sufficient detail but design flexibility remains.

### What Information Does This Claim Rely On?

#### Columns and Beams
- Quantity  
- Material type  
- Dimensions  

#### Windows
- Quantity  
- Dimensions  
- Type  

#### Spaces
- Classification  
- Area and volume  

### What Phase?
**Tender phase (Build focus area)**

At this stage, verified cost estimates ensure bids reflect accurate quantities and materials, reducing financial risk before construction begins.


### What BIM Purpose Is Required?
**Analyse** (extract and compute), then **Communicate** (report to stakeholders).

### Closest BIM Use Case
**Use Case 02 — Cost Estimation**

### BPMN Diagram
_Add SVG or link here:_  
`![BPMN – Cost Estimation](docs/bpmn/uc02_cost_estimation.svg)`

---

## A2d. Scope the Use Case
Identify where a new script or function is needed within the BPMN diagram.  
Highlight this area clearly in a marked SVG.

_Add BPMN diagram with highlighted step here:_  
`![BPMN Highlighted Step](docs/bpmn/uc02_cost_estimation_tool_highlight.svg)`

---

## A2e. Tool Idea

### Overview
Python-based **cost-checking and validation tool** using ifcOpenShell.

### Core Function
Automatically extract quantities and materials from an IFC model, combine with Molio unit prices, and calculate total costs.

### Features
- Integrates results from multiple analysts  
- Visualises data and creates reports  
- Supports **OpenBIM** principles of interoperability, collaboration, and traceability

### Business Value
- Automates quantity take-offs and price calculations  
- Improves accuracy and efficiency  
- Enables stronger budget control  

### Societal Value
- Promotes transparency and sustainability through OpenBIM standards  

### BPMN Diagram
_Add SVG or link here:_  
`![BPMN – Tool Summary](docs/bpmn/tool_summary.svg)`

---

## A2f. Information Requirements

### Information to Extract
| Category | IFC Class | Data Needed |
|-----------|------------|--------------|
| Columns | `IfcColumn` | Quantity, material, dimensions |
| Beams | `IfcBeam` | Quantity, material, dimensions |
| Windows | `IfcWindow` | Quantity, dimensions, type |
| Spaces | `IfcSpace` | Classification, area, volume |

### Is It in the Model?
_To be verified._

### Access via ifcOpenShell?
_To be verified._

### What Do You Need to Learn?
_Add notes or link to Excel in Teams._

---

## A2g. Software Licence
Select appropriate licence:
- MIT  
- Apache 2.0  
- GPL 3.0  

_To be decided._

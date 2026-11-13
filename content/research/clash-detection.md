---
title: "Clash Detection"
date: 2026-09-03
category: "AEC Software"
article_type: "Research"
summary: "Clash Detection Workflow & Method"
cover: "images/research/clash-detection/thumbnail.png"
---

## Clash Detection

{{< research-image src="images/research/clash-detection/clashdetection1.png" alt="ClashDetection1" size="large" >}}

**Clash** Detection is a process to identifies conflicts or "clashes" among engineering disciplines (Structure, Architecture, and MEP), using 3D models that created during the design process from each disciplines. BIM Clash Detection allows engineer to identified potential conflict in advance to helps prevent construction errors and costly adjustments during the construction phase.

It is required to conduct and manage an adequate Clash Detection and resolved before construction. The goal is to reduce the number of clash interferences to zero.

Approach to clash detection depends on the project, including:

- Splitting level by level for MEPF (Mechanical, Electrical, Plumbing, Fire Service) Coordination
- Splitting by zone if the floor is large.
- Typically 3d clash detection continues on a single floor by single floor

*Collaborate Working Group. CWG-002 BIM Management Plans: Review of the NATSPEC BIM Management Plan. 2014.*

{{< research-image src="images/research/clash-detection/clashdetection2-2.png" alt="ClashDetection2" size="small" >}}

### Types of Clashes

**1. Hard Clash (Intersecting Clashes)**  
Hard Clash is a direct physical conflict between objects, where two elements overlap or occupy the same space.

**2. Soft Clash (Clearance Clashes)**  
Soft clash is a clearance conflict, where objects do not necessarily collide, but the required space around them is not enough for access, operation, or maintenance.

### Clash Hierarchy

{{< research-image src="images/research/clash-detection/clashdetection3-2.png" alt="ClashDetection3" size="large" >}}

Clash Hierarchy is a method to rank building from the most difficult and expensive to move to the most mobile as outlined in the diagram below. The hierarchy also indicates the default right-of-way between systems. Lower systems generally take precedence over higher systems because they are more fixed, harder to move, or more critical to the building.

## Clash Management

Resolving Clashes requires a structured process to filter true clashes, address root causes, and implement solutions.

Not all clashes are coordination issues. A priority system is needed to determine whether a group of clashes should be addressed, downgraded, marked as acceptable, or excluded from the current coordination scope. Too many false or low-value clashes can make it difficult to identify the important clashes that require resolution. Therefore, meaningful clash detection requires a clear set of rules, filters, priorities, and selection sets. Clash filtering is the process of reducing irrelevant clash results so the coordination team can focus on critical issues. In Autodesk Forma Coordination, this can be achieved with object exclusion, clash matrix, and search set method.

*Seyler, K. (2026, April 9). Have You Tried It? Clash Management. Autodesk Digital Builder.*

### Object Exclusion

{{< research-image src="images/research/clash-detection/clashdetection4.png" alt="ClashDetection4" size="medium" >}}

Object exclusion is the first method to filter clashes. By cleaning the model from the beginning, a significant amount of clashes can be reduced.

#### Issue Type

List of object that should be included in clash:

- Architecture: Wall, Door & Window, Floor, Ceiling, Stairs, Facade (exclude column)
- Structure: Column, Wall, Floor, Framing, Foundation
- Mechanical: Ducting, Mechanical Equipment
- Plumbing: Piping, Plumbing Fixture
- Electrical: Cable Tray, lighting fixture
- Electronica: Cable Tray
- Fire Protection: Piping, Sprinkler

### Clash Matrix

**Clash Matrix** is a structural approach to categorized clash based on different building elements. This matrix is produce during the development of the BIM execution plan. The matrix defines model and elements that needs to be coordinate with each other.

Clash priority should be defined as the BIM Execution Plan is developed. Clash priority considerations including:

- model discipline
- Component type / Category
- Intersection Orientation (parallel or crossing)
- Component Size
- Construction State (proposed / existing)
- Construction Sequencing and Critical Path

Clash matrix is determined based on our **Model Breakdown Structure** and the important component inside each discipline. The component classification will be:

- Architecture: Wall, Door-Window, Floor, Ceiling, Stairs, Facades
- Structure: Column, Wall, Floor, Framing, Foundation
- MEP: Ducting, Piping, Cable Tray, Equipment (AHU, VRV, etc)

{{< research-image src="images/research/clash-detection/clashdetection5.png" alt="ClashDetection5" size="medium" >}}

*The number of this matrix define the clash-check sequence based on each element's spatial significance, coordination impact, and difficulty of relocation.*

This clash matrix was developed based on our project needs and practical experience. As a design consultant, our BIM models are generally developed up to LOD 300. At this level, model elements represent the designed quantity, size, shape, location, and orientation required for design coordination.

The main objective of BIM implementation in our company is to support interdisciplinary design coordination, rather than to produce fabrication models, installation details, or construction sequencing. Therefore, the clash-detection process primarily focuses on hard clashes, that is physical intersections between elements, that may indicate cross-disciplinary conflicts and require design decisions during the design stage.

The clash matrix adopts a risk-based approach by prioritizing elements that:

- occupy significant physical space;
- are difficult or costly to relocate;
- affect multiple disciplines; and
- may require design revisions when conflicts occur.

This approach enables the coordination process to focus on major design conflicts while avoiding excessive low-priority clash results involving small, flexible, or installation-level components.

### Search Set

{{< research-image src="images/research/clash-detection/clashdetection6.png" alt="ClashDetection6" size="medium" caption="A selection set is created by manually selecting and grouping the elements to be checked." >}}

Search set is a filtering method that groups model objects based on to predefined properties or criteria, making clash inspection more specific and detailed.

{{< research-image src="images/research/clash-detection/clashdetection7.png" alt="ClashDetection7" size="medium" >}}

Several clash tests have been created based on the clash matrix. The naming convention follows the format:

{{< research-image src="images/research/clash-detection/clashdetection8.png" alt="ClashDetection8" size="small" >}}

**[Sequence]-[Status]-[Element A] X [Element B]**

Example: **[1]-[A]-AR-Wall X PK-FireProtection**

The first index indicates the clash-check sequence. The second index indicates whether the clash combination is applicable or not applicable, while the final part identifies the two element groups being checked.

Clash combinations classified as **Not Applicable**, such as ARS-Wall × STR-Wall or ARS-Wall × STR-Column, may be assigned directly to the **Not an Issue** category when the clashes result from an agreed modelling convention.

All clashes generated from combinations classified as **Applicable** should then be reviewed and resolved individually. After the predefined clash sets have been assessed, the remaining unclassified clashes can be reviewed separately to identify any additional conflicts not covered by the clash matrix.

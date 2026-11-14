---
title: Building Energy Modelling
category: Environmental Simulation
summary: null
slug: building-energy-modelling
article_type: Research
date: '2026-11-13'
cover: /images/research/building-energy-modelling/pasted-image-20261112175032-025e6eb43a.png
---

{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261112175032-025e6eb43a.png" alt="Pasted image 20261112175032" size="large" >}}
## Building Energy Modelling

Building Energy Modelling is the process of **creating** a digital model to **predict** how much energy a building needs and consumes. An energy model also considers how the building behaves under real-world conditions, including weather, materials, and building systems. 

Building require energy for **cooling, heating, lighting, and operating equipment**. However, energy consumption is not only determined by mechanical and electrical systems. Architectural design also plays an important role, especially in aspects like **building orientation, window size, glazing, and shading**. Architectural elements affect how much cooling is needed to maintain comfortable indoor conditions. 

The **purpose** of Building Energy Modelling is to understand how design decisions affect energy consumption and identify opportunities to improve energy efficiency. 

## How Does Building Energy Modelling Work?

Building Energy Modelling combines three main types of information that is building design, building operation, and building systems. 
1. **Building Design**
	Building design aspects that are important in Building Energy Modelling include building geometry, orientation, windows, shading, and construction materials. These elements influence how the building gains, loses, and stores heat. 
2. **Building Operation**
	Building design aspects that are important in Building Energy Modelling include occupancy, lighting, electrical equipment, and operating schedules. These describe how the building is used and when energy is required.
3. **Building Systems**
	Building systems including heating, ventilation, air conditioning (HVAC), and other energy-consuming systems, determine how the building's heating and cooling needs are served and how much energy is consumed.
The simulation then combines all this information with local weather data to calculate:
**Building Heat Gains and Losses → Heating and Cooling Demand → System Operation → Energy Consumption**
The result is an estimate of how much energy the building requires under the conditions represented in the model.

## What Does the Analysis Tell Us?

Building Energy Modelling provides several important results.

| Analysis Output                      | What It Tell Us                                                                              |
| ------------------------------------ | -------------------------------------------------------------------------------------------- |
| Annual Energy Consumption (kWh/year) | How much energy the building is predicted to use annually                                    |
| Energy Use Intensity (kWh/m²/year)   | How much energy is used relative to the building's floor area                                |
| Energy End-Use Breakdown             | How energy use is distributed among cooling, heating, lighting, equipment, and other systems |
| Heating and Cooling Loads            | How much heating or cooling the building requires                                            |
| Energy Performance Comparison        | How changes in design or building systems affect predicted energy use                        |
These results help designers understand where energy is used and which design decisions can improve efficiency.

## Energy Modelling with Autodesk Insight

{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261113205013-67c9b0fd69.png" alt="Pasted image 20261113205013" size="large" >}}

### Create a Simplified Building Model


{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261113205052-5d96ec5d0d.png" alt="Pasted image 20261113205052" size="medium" >}}



The Energy Model is developed from a simplified Revit model containing only essential building elements, such as walls, floors, roofs, and openings represented by basic curtain wall families.


### Create and Configure Spaces

**Spaces are created to represent individual areas of the building and define how each area is used.**
In Building Energy Modelling, Spaces provide important information about room functions, occupancy, lighting, electrical equipment, and ventilation requirements.
This information helps the simulation estimate the heat generated inside each space and the energy needed to maintain its indoor conditions.

{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261113211530-7c19f2c77e.png" alt="Pasted image 20261113211530" size="large" >}}

After creating the Spaces, assign the following information to each one:

| Parameter                | Description                                                               |
| ------------------------ | ------------------------------------------------------------------------- |
| Space Type               | Defines the room's function, such as office, corridor, or meeting room    |
| Condition Type           | Specifies whether the space requires heating, cooling, or no conditioning |
| Occupancy                | Defines the number of people expected to use the space                    |
| Lighting Loads           | Defines the electrical power used for lighting                            |
| Equipment Loads          | Defines the electrical power used by computers and other equipment        |
| Operating Schedules      | Defines when occupants, lighting, and equipment are active                |
| Outdoor Air Requirements | Defines the amount of fresh air required for ventilation                  |
*These parameters can be assigned using predefined Space Types or adjusted individually to reflect the intended use of each space.

### Configure Energy Settings

Before running the energy simulation, we need to define the basic information about the building, its location, and how it will be used.

These inputs help the simulation understand **how the building operates, when energy is needed, and what influences its energy consumption.**

There are five main inputs:

#### 1. Location & Weather

{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261113210502-4447e68ee3.png" alt="Pasted image 20261113210502" size="large" >}}

The building's location determines the climate conditions used in the simulation.

Weather information includes outdoor temperature, sunlight, humidity, and wind conditions. These factors influence how much heat enters or leaves the building and how much heating or cooling may be required.

**Required information:**
- Project location
- Local weather data or weather station

#### 2. Building Type

{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261113210634-e16f49ffcc.png" alt="Pasted image 20261113210634" size="large" >}}

Different types of buildings use energy differently.
For example, an office typically operates during working hours, while a hotel may operate throughout the day and night.
Defining the building's function helps establish suitable assumptions for occupancy, lighting, equipment, and energy use.

**Required information:**
- Building type (Office, Residential, Hotel, Commercial, etc.)
- Main building function

#### 3. Material Thermal Properties
{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261113212048-7ad1cef08c.png" alt="Pasted image 20261113212048" size="large" >}}

Material thermal properties describe **how building materials respond to heat**.
Different materials allow different amounts of heat to pass through or be stored within the building. For example, walls, roofs, and windows can influence how much heat enters the building from the outside.
These properties are important in Building Energy Modelling because they affect indoor temperatures and the amount of heating or cooling needed.

**Key Thermal Properties**

| Property                               | Description                                                                                                |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| U-Value                            | Measures how easily heat passes through a building element. A lower value means better thermal insulation. |
| R-Value                            | Measures resistance to heat flow. A higher value means better thermal insulation.                          |
| Solar Heat Gain Coefficient (SHGC) | Indicates how much solar heat passes through glazing. A lower value reduces solar heat gain.               |
| Thermal Mass                       | Describes a material or construction's ability to store heat and release it over time.                     |

**Thermal Properties Settings in Revit**
1. **Conceptual Types**
	Uses predefined thermal properties for common building elements.
	Suitable for early design stages when specific materials have not yet been selected.
2. **Schematic Types**
	Allows users to select specific analytical constructions for walls, roofs, floors, and glazing.
	Suitable for evaluating different construction and glazing options without creating detailed material assemblies.
3. **Detailed Elements**
	Uses thermal properties from the actual material layers assigned to building elements in Revit.
	Suitable for more developed models where construction materials, thicknesses, and thermal properties have been properly defined.


### Assign Zones and HVAC Systems

After defining the Spaces, the next step is to determine **which areas of the building require air conditioning and how they will be served by HVAC systems**.
These systems control indoor temperatures and provide ventilation. They also consume energy, making them an important part of Building Energy Modelling.
In Revit, HVAC systems can be represented using analytical components without modelling the actual equipment, ducts, or pipes in detail.

#### 1. Define System-Zones

{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261114131820-66cdc4b16a.png" alt="Pasted image 20261114131820" size="large" >}}

System-Zones are used to group Spaces that will be served by the same HVAC equipment or system. For example, several office rooms on the same floor may be grouped into one System-Zone, while corridors and service areas may be assigned to different zones. This helps the simulation identify **which areas are served by each HVAC system**.
**Required information:**
- Areas served by each HVAC system
- Spaces included in each System-Zone
- Areas with different conditioning or ventilation requirements

#### 2. Define HVAC Systems

{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261114132253-ae39c4427e.png" alt="Pasted image 20261114132253" size="large" >}}

HVAC systems are defined to represent how the building provides cooling, heating, and ventilation.
Revit provides three main types of analytical HVAC components:

| Component          | Description                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| **Zone Equipment** | Equipment that directly serves one or more Spaces, such as a VRF indoor unit or fan coil unit                |
| **Air System**     | A system that supplies or distributes conditioned air or ventilation air, such as an air handling unit (AHU) |
| **Water Loop**     | A system that circulates water for heating or cooling, such as a chilled water system                        |
Not every building requires all three components.
For example, a VRF system can be represented using Zone Equipment, while a central chilled water system may require Water Loops and Air Systems.
The selected components should reflect the HVAC design being evaluated.

#### 3. Assign HVAC Equipment to System-Zones

{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261114132726-ccca70b605.png" alt="Pasted image 20261114132726" size="large" >}}

After defining the HVAC components, assign the appropriate equipment to each System-Zone.
For example, office Spaces may be assigned to a VRF fan coil system, while a separate Air System may provide fresh air.
This connection allows the simulation to understand **how each area is conditioned and which systems are responsible for its energy use**.

### Create and Review the Energy Analytical Model

After defining the building's energy settings, Spaces, and HVAC systems, the next step is to create the **Energy Analytical Model** and run the energy simulation.
The Energy Analytical Model converts the building information into a simplified model that can be used to calculate energy performance.

#### 1. Review Energy Related Information

Before creating the Energy Analytical Model, verify the MEP Space information to ensure that each space is correctly defined and contains the necessary data for energy simulation.
The information should represent the actual room functions, occupancy, internal heat loads, and ventilation requirements.


{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261114150805-da57f3e957.png" alt="Pasted image 20261114150805" size="large" >}}

###### Space Identification
Verify that every space has the correct identity and location within the building.
**Parameters:**
- `Level` — Identifies the floor where the space is located.
- `Number` — Provides a unique reference for each space.
- `Name` — Describes the room, such as Office, Toilet, or Lobby

###### Space Classification

Verify that every space is classified according to its function and environmental requirements.
**Parameters:**
- `Space Type` — Defines how the space is typically used.
- `Condition Type` — Defines whether the space is cooled, heated, ventilated, or unconditioned.
- `Occupiable` — Identifies whether the space is intended for occupants.
- `Plenum` — Identifies spaces used as air distribution plenums.

###### Occupancy and People Heat Gain

Verify the number of people expected to use each space and the heat they produce.
**Parameters:**
- `Number of People` — Expected number of occupants.
- `Area per Person` — Floor area allocated to each person.
- `Sensible Heat Gain per person` — Heat released by people that increases room temperature.
- `Latent Heat Gain per person` — Heat released by people as moisture.
The occupancy should reflect the room function. Unoccupied spaces, such as empty shafts and voids, should not have unintended occupant loads.

###### Lighting and Equipment Loads

Verify the estimated electrical loads from lighting and equipment within each space.
**Parameters:**
- `Specified Lighting Load per area` — Estimated lighting power per square meter.
- `Specified Power Load per area` — Estimated equipment power per square meter.
- `Specified Lighting Load` — Total lighting power for the space.
- `Specified Power Load` — Total equipment power for the space.
These loads affect both electricity consumption and the amount of heat generated inside the building.
Values should be based on the lighting and electrical design where available, or documented design assumptions.

###### Ventilation Requirements

Verify the amount of outdoor air required to maintain indoor air quality.
**Parameters:**
- `Outdoor Air Method` — Defines how the ventilation requirement is calculated.
- `Outdoor Air per Person` — Outdoor air required for each occupant.
- `Outdoor Air per Area` — Outdoor air required based on floor area.
- `Air Changes per Hour` — Number of times the air in a space is replaced per hour, when this method applies.
- `Outdoor Airflow` — Calculated total outdoor air requirement.
Ventilation requirements should be based on the room function and the mechanical design.
Outdoor air is different from the total supply air used for cooling.

###### HVAC Airflow Requirements

Verify the designed airflow supplied to, returned from, or exhausted from each space.
**Parameters:**
- `Specified Supply Airflow` — Designed amount of air supplied to the space.
- `Specified Return Airflow` — Designed amount of air returned to the HVAC system.
- `Specified Exhaust Airflow` — Designed amount of air removed from the space.
These values should be checked against the MEP design information where available.
Not all spaces require every type of airflow, and unavailable design quantities should not be estimated without an appropriate basis.

###### Operating Schedules

Verify when occupants, lighting, electrical equipment, and HVAC systems are expected to operate.
**Information to verify:**
- Occupancy Schedule
- Lighting Schedule
- Power Schedule
- HVAC Operating Schedule
Operating schedules help the simulation estimate energy consumption throughout the day and year, rather than assuming that all systems operate continuously.
These schedules are verified through the relevant Revit settings and may not appear directly in the Space Schedule.

##### Final Data Review

Before creating the Energy Analytical Model, confirm that:
- Spaces are correctly identified and classified.
- Occupancy and internal loads are appropriate for each room.
- Ventilation requirements are consistent with the MEP design.
- Available design airflow information has been verified.
- Operating schedules represent the intended building operation.
- Missing information and design assumptions are documented.

**Note:** Parameters such as `Actual Lighting Load`, `Actual Power Load`, `Calculated Cooling Load`, and `Calculated Supply Airflow` are not required to be manually populated during this input verification stage. They are reviewed as calculated or analytical results where applicable.

**Expected Outcome**
A verified MEP Space dataset that provides a consistent foundation for creating the Energy Analytical Model and performing building energy simulation.

#### 2. Create the Energy Analytical Model

{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261114150908-25643a1ecd.png" alt="Pasted image 20261114150908" size="large" >}}

Revit generates the Energy Analytical Model based on the building geometry and energy settings.
The model consists of two main components:
- **Analytical Spaces:** Represent the building's indoor air volumes.
- **Analytical Surfaces:** Represent walls, floors, roofs, windows, and other surfaces that affect heat transfer.
These components allow the simulation to calculate how heat enters, leaves, and moves through the building.




### Run Energy Analysis

{{< research-image src="/images/research/building-energy-modelling/pasted-image-20261114151229-48483383c6.png" alt="Pasted image 20261114151229" size="large" >}}

Once the Energy Analytical Model has been reviewed, run the simulation using Revit Systems Analysis.
Revit uses EnergyPlus, a building energy simulation engine, to calculate the building's energy performance based on the defined inputs.
For Building Energy Modelling focused on annual energy consumption, select **Annual Building Energy Simulation**.

### Review the Energy Analysis Report


After the simulation is completed, Revit generates a report containing the predicted building energy performance.
The main results include:
1. Annual Energy Consumption: total energy predicted to be used over one year
2. Energy Use Intensity (EUI): annual energy use per square meter of building area
3. Energy End-Use Breakdown: energy used for cooling, heating, lighting, equipment, and other systems
4. Monthly Energy Use: how energy consumption changes throughout the year

These results help identify which building systems consume the most energy and provide a basis for evaluating improvements to the design.
After running the energy simulation in Revit, the results can be reviewed through the generated Energy Analysis Report.

{{< research-media type="html" src="/images/research/building-energy-modelling/energy-analysis-2026-11-14-15-12-220000-2eef820c7e.htm" title="Energy Analysis 2026-11-14 15-12-22.0000" >}}

#### 1. OpenStudio Results (.htm)
This report shows the predicted energy performance of the building, including:
- **Annual Overview:** Total yearly energy use for cooling, lighting, equipment, and other systems.
- **Monthly Overview:** Monthly energy consumption and peak energy demand.
- **Detailed Report:** Building energy performance, energy use intensity (EUI), and thermal comfort results.
- **Measure Warnings:** Warnings or issues found during the analysis.
The HTML report can be opened in a web browser and printed as a PDF.

#### 2. Verify Simulation Results
Check that the calculated energy use, HVAC systems, and indoor comfort results match the intended building design.
Any unusual results or warnings should be reviewed before using the report for design evaluation.

## Key Takeaway
Energy Analysis combines the building geometry, thermal properties, space usage, weather conditions, and HVAC systems to predict how much energy the building will consume.
Reliable Building Energy Modelling depends not only on the simulation software, but also on the accuracy and consistency of its input data.
Incorrect assumptions about materials, occupancy, building operation, or HVAC systems can produce misleading energy consumption estimates, even when the simulation runs successfully.
Therefore, the Energy Analytical Model and its critical inputs must be carefully reviewed before the results are used to evaluate building energy performance.

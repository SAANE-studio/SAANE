---
title: Daylight Analysis
category: Environmental Simulation
summary: null
slug: daylight-analysis
article_type: Research
date: '2026-11-12'
cover: /images/research/daylight-analysis/pasted-image-20261112175022-0e57d79d98.png
---

{{< research-image src="/images/research/daylight-analysis/pasted-image-20261112175022-0e57d79d98.png" alt="Pasted image 20261112175022" size="large" >}}
## Understanding Daylight Analysis

Daylight analysis is used to evaluate the quality of natural light in a building. It measures the amount of daylight in a space. The data then can be used to asses how daylight affects the occupants and energy consumption. 

Practical Use:

| Usage                            | Objectives                                                                                 | Outputs                                                    |
| -------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| Daylight Distribution Assessment | Identify interior areas with high and low natural daylight availability                    | Spatial Daylight Autonomy (DA) heatmap                     |
| Annual Daylight Availability     | Evaluate how frequently interior spaces achieve the target illuminance throughout the year | Daylight Autonomy (DA) percentages across sensor locations |
| Hourly Illuminance Analysis      | Analyze variations in natural illuminance at selected sensor locations throughout the year | Hourly illuminance plot (lux) for selected sensors         |
| Spatial Daylight Performance     | Determain the proportion of interior floor area meeting the daylight availability criteria | Spatial Daylight Autonomy (sDA) percentage                 |

## Simulation Using Autodesk Forma

High-level daylight analysis, especially in the scope of a building compound, can be done in Autodesk Forma Site Design using Sun Hours and Daylight Potential study features. 

#### Sun Hours


{{< research-image src="/images/research/daylight-analysis/daylight-forma-d2640f88a2.jpg" alt="daylight-forma" size="large" >}}

Forma Sun Hours Analysis measures **the number of hours of direct sun exposure** on the ground and on building surfaces for selected date(s) and time interval(s).
The study simulates solar exposure on selected dates and evaluates _how many hours of direct sun reach building facades, roofs, and outdoor spaces.

**How Does It Affect Design Decision?**
This analysis helps you understand whether certain parts of the design get too much sun, too little sun, or the right amount depending on the use. It helps with decisions about:
- orientation,
- massing,
- façade treatment,
- shading,
- and outdoor comfort.

#### Daylight Potential


{{< research-image src="/images/research/daylight-analysis/daylight-potentialforma-1-5ff062a022.jpg" alt="daylight-potentialforma 1" size="large" >}}

Daylight Potential Analysis is expresses as a **Vertical Sky Component (VSC)** **Percentage** that measure the amount of direct skylight reaching the center of a window on a building’s exterior façade, typically from a CIE standard overcast sky. The simulation calculates :

- How much visible sky a facade can see
- How much diffuse sky light reaches each facade point in obstruction from buildings, terrain, and vegetation

**Key Benchmark**

The simulation measures VSC (illuminance received on a vertical surface) divided by Illuminance on a horizontal surface under unobstructed sky. Based on **BRE,** the benchmark is _(BRE Guide (BR209), Littlefair, 2011):_

- ≥ 27% : Daylight usually satisfactory
- 15-27% : Larger windows may be needed
- 5-15% : Difficult to achieve adequate daylight
- <5% : Adequate daylight often impossible

**How Does It Affect Design Decision?**

- If VSC <15%, consider increase spacing, reduce podium height, adjust building orientation, increase window size
- if VSC ≥ 27%, conventional window will be sufficient
- If lower floors show very low VSC, tower spacing maybe inadequate, urban canyon effect may exist



## Simulation using Honeybee
{{< research-image src="/images/research/daylight-analysis/pasted-image-20261107185454-071ad3c1cf.png" alt="Pasted image 20261107185454" size="small" >}}


Honeybee is a building analysis tool that supports detailed daylighting modelling that is relevant during mid and later stages of design. It runs the daylight simulation using Radiance. The simulation is run by the Grasshopper using Rhino Inside Revit to utilize Revit 3D data. 

Honeybee simulates how natural daylight enters interior spaces through building openings, considering room geometry, walls, and glazing properties. Environmental factors such as weather conditions, surrounding building masses, and shading elements are included to represent realistic daylight conditions. Honeybee then generates a sensor grid across the interior floor area to measure the amount of daylight received at different locations. Using the Radiance simulation engine, it calculates daylight availability throughout the year. The results are visualized through **Daylight Autonomy (DA) heatmaps**, **Hourly Illuminance plots**, and **Spatial Daylight Autonomy (sDA)** to help architects evaluate natural lighting performance within a building.

{{< research-image src="/images/research/daylight-analysis/daylightanalysis-1-9540ddb0cd.png" alt="DaylightAnalysis 1" size="large" >}}

There are three main steps in this simulations: 
1. Geometry Preparation
	   {{< research-image src="/images/research/daylight-analysis/daylightanalysis-geometry-0dc36cc7b0.png" alt="DaylightAnalysis-geometry" size="wide" >}}
	There are three types of geometry that needed to be retrieve from Revit models:
	1. Opaque Faces (Room Boundary)
	2. Apertures (Room Openings)
	3. Context (Shading Elements)
	*Rhino Inside Revit is used to retrieve Revit Building Elements to be simulated by Honeybee.*

#### Simulation Principles:  
{{< research-image src="/images/research/daylight-analysis/principles-bf8195faf3.png" alt="Principles" size="small" >}}

Opaque Faces acted as the room boundary while Apertures as the room openings. The Aperture geometry will be projected into the Opaque geometry (careful to check if the aperture geometry retrieves from Revit model contains double faces). 


#### Model Assembly and Sensor Grid Generation
{{< research-image src="/images/research/daylight-analysis/daylightanalysis-assembly-d890e0b39d.png" alt="DaylightAnalysis-assembly" size="medium" >}}

The model of Opaque Faces, Apertures, and Contexts will be assembled into a simulation model. Sensor Grid is generated by making points on the workplane inside the room as the evaluation plane. 


#### Annual Daylight Simulation
{{< research-image src="/images/research/daylight-analysis/daylightanalysis-analysis-bdb5280d90.png" alt="DaylightAnalysis-analysis" size="medium" >}}

Radiance evaluates the daylight contribution on the sensor points based on sky conditions (from the weather or epw files), building geometries and light obstacles. In this stage, simulation contexts can be adjusted, including north position, thresholds, and simulation schedules. 


#### Results Processing and Visualization
{{< research-image src="/images/research/daylight-analysis/daylightanalysis-results-e8196c4d81.png" alt="DaylightAnalysis-results" size="medium" >}}

Simulation results will then be processed to produce: 
1. DA (Daylight Autonomy): Time percentage when the sensor daylighting achieve targets (300 lux)
2. Hourly Illuminance: illumination value in lux anunally on the selected sensor
3. sDA: area percentage that received annual daylight criteria

#### Results and Interpretation
1. **Hourly Illuminance Plot**
	this represents illuminance (lux) graph for one censor in a whole year that is plotted in month horizontally and daily hour vertically. 
	{{< research-image src="/images/research/daylight-analysis/pasted-image-20261107201908-fca51033fd.png" alt="Pasted image 20261107201908" size="small" >}}
	{{< research-image src="/images/research/daylight-analysis/hourlyilluminance-2a7d026ce9.png" alt="hourlyilluminance" size="large" >}}
	This plot shows that most the time, the point receives low amount of daylight, but in certain condition, red and yellow color are present, indicating the censor receive higher amount of daylight. 
2. **Daylight Autonomy (DA) Heatmap**
	
	{{< research-image src="/images/research/daylight-analysis/da-c6195a5337.png" alt="DA" size="large" >}}
	This is daylight performance map on all sensor grid area in a room. Every pixel represents a sensor that is being analyzed. The legend shows the time percentage of a censor point receiving a sufficient daylight. 0% means that point almost never achieve target, 50% indicates that the points receive sufficient daylight half the occupancy time, and 92% means that the points always receive the targeted amount of daylight.
1. **sDA - Spatial Daylight Autonomy**
	{{< research-image src="/images/research/daylight-analysis/pasted-image-20261107202352-d0539349b9.png" alt="Pasted image 20261107202352" size="large" >}}
	This is the summary of room performance indicating room percentage area that receive targeted daylight in a yearly period. Honeybee default setting use 300 lux as the target illuminance. 47.44 result in sDA means that 47.44% of the room area have achieve sufficient daylight as targeted (300 lux).

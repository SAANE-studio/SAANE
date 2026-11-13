---
title: Natural Ventilation
category: Environmental Simulation
summary: Natural airflow, heat balance, and adaptive thermal comfort through a comparison
  of ventilation ON and OFF simulations.
slug: natural-ventilation
article_type: Research
date: 2026-11-11
cover: /images/research/natural-ventilation/pasted-image-20261112175045-1c4061a8a7.png
---

{{< research-image src="/images/research/natural-ventilation/pasted-image-20261112175045-1c4061a8a7.png" alt="Pasted image 20261112175045" size="large" >}}

## Understanding Natural Ventilation

Natural ventilation is the movement of outdoor air into and through a building **without relying on mechanical ventilation systems**. This movement is mainly driven by wind and temperature differences between indoor and outdoor environments.

Through appropriately designed openings, such as windows and vents, outdoor air can enter a building while indoor air is allowed to leave. This exchange helps replace indoor air with outdoor air and can influence indoor thermal conditions.

However, **allowing air to move through a building does not automatically mean that the building will become cooler or more comfortable**. The effectiveness of natural ventilation depends on how much air enters the space, the temperature of that air, and how it interacts with the indoor environment.

{{< research-image src="/images/research/natural-ventilation/pasted-image-20261113154640-946f9c57fb.png" alt="Pasted image 20261113154640" size="large" >}}

Air carries heat. When outdoor air enters a room, it brings its own temperature and thermal energy into the indoor environment.

If the incoming outdoor air is cooler than the indoor air, ventilation can help remove accumulated heat and lower the indoor temperature. However, if the outdoor air is warmer, increasing ventilation may introduce additional heat instead. Besides outdoor air, indoor temperature also depends on other sources of heat, including solar radiation, building materials, occupants, and electrical equipment. Natural Ventilation analysis will learn how this exchange affects the overall heat balance of the room.

## Understanding How Air Moves Through a Building

The first question in natural ventilation analysis is whether the building allows sufficient airflow.

**The position, size, and arrangement of openings** influence how outdoor air enters and leaves a room. Wind conditions and temperature differences also affect the resulting airflow.

To understand this exchange, two measurements are particularly useful: **Airflow Rate and Air Changes per Hour (ACH)**.

Airflow Rate measures the volume of air moving into or out of a space over a certain period, commonly expressed in cubic meter per second (m³/s).

ACH describes how frequently an amount of air equivalent to the room's total volume is exchanged within one hour. For example, an ACH of 3 means that the volume of air exchanged over an hour is equivalent to three times the room's volume.

Together, these measurements help us understand the **quantity of ventilation** taking place. However, they do not directly indicate whether the indoor environment is thermally comfortable, therefore **Adaptive Thermal Comfort** and **Thermal Comfort** statistic is needed to provide a useful approach to evaluate comfort. 

## Natural Ventilation Simulation Workflow

{{< research-image src="/images/research/natural-ventilation/pasted-image-20261113155334-b8d6e8f6f8.png" alt="Pasted image 20261113155334" size="large" >}}

The simulation begins by **selecting one room as the study area**. 
The room geometry, window openings (apertures), and surrounding shading elements are prepared using Honeybee. Building properties, including construction materials, room usage, internal heat sources, and weather data, are then defined to establish the simulation conditions.

To evaluate the contribution of natural ventilation, the analysis is divided into **two simulation scenarios**. In **Scenario 1 (Window Closed)**, the room is simulated without natural ventilation through the windows. In **Scenario 2 (Window Open)**, the same room is simulated with operable windows, allowing natural ventilation based on outdoor conditions and predefined ventilation controls. Both scenarios use identical geometry, materials, internal conditions, and weather data.

For each scenario, the geometry, building properties, and ventilation settings are combined into a complete **Honeybee Energy Model**, which is then processed and simulated using **EnergyPlus**.

The simulation results are visualized using **Ladybug Hourly Plots and Adaptive Comfort Charts**. The analysis examines **Operative Temperature, Thermal Comfort, and Adaptive Thermal Comfort** to evaluate indoor thermal conditions and occupant comfort in both scenarios. Additionally, **Airflow Rate and Air Changes per Hour (ACH)** are calculated for the Window Open scenario to quantify natural air exchange.

By comparing the thermal comfort results of both scenarios, the analysis helps determine **whether natural ventilation contributes to improved indoor thermal conditions and occupant comfort**.

#### Grasshopper Script

{{< research-image src="/images/research/natural-ventilation/daylightanalysis-3-4b9a1f0c88.png" alt="DaylightAnalysis 3" size="large" >}}
#### Result: Operative Temperature
{{< research-image src="/images/research/natural-ventilation/ventilationsimulation-a99f532955.png" alt="ventilationsimulation" size="large" >}}

Operative temperature represents the combined effect of indoor air temperature and heat radiated from surrounding surfaces.

Both scenarios show similar temperature patterns, with higher temperatures occurring mainly during the afternoon. The **Window Open** scenario shows some changes in temperature intensity compared with **Window Closed**, but the reduction is not consistent throughout the year.

This indicates that **natural ventilation influences indoor temperature, although overheating can still occur in both scenarios**.

#### Result: Thermal Condition
{{< research-image src="/images/research/natural-ventilation/ventilationsimulation---copy-3-b702ded734.png" alt="ventilationsimulation - Copy (3)" size="large" >}}

The thermal condition chart shows how the room is perceived over time using three simple categories: **hot**, **neutral**, and **cold**.

In both scenarios, the charts are dominated by **red**, which means the room is **hot for most hours of the year**, especially during the daytime and afternoon. Yellow areas show **neutral** conditions, meaning the space feels more acceptable during some periods. There is almost no blue, so **cold conditions are not a major issue**.

When the two cases are compared, one scenario shows **slightly more neutral hours and slightly fewer hot hours**, which suggests a small improvement in thermal comfort. However, the overall pattern still indicates that **overheating remains the main condition in both cases**.

#### Adaptive Chart Comparison

{{< research-image src="/images/research/natural-ventilation/ventilationsimulation---copy-2-1-e78c822a20.png" alt="ventilationsimulation - Copy (2) 1" size="medium" >}}

The adaptive chart helps explain whether the indoor condition is acceptable **in relation to the outdoor climate**. It compares **operative temperature** inside the room with the **prevailing outdoor temperature**.

The sloped comfort band in the middle represents the range where occupants are expected to feel comfortable under adaptive comfort criteria. Points **inside the band** indicate acceptable comfort, while points **above the band** indicate that the space feels **too warm**.

In both scenarios, most of the data points are concentrated **near or above the upper comfort limit**, which means the room is warm for a large portion of the time. Some hours fall within the comfort zone, but the charts show that **comfort is still limited overall**.

When comparing the two charts, the better-performing scenario is the one with **more points inside or closer to the comfort band**, because that means the indoor condition is more acceptable for occupants.

#### Results: ACH and Airflow Rate

{{< research-image src="/images/research/natural-ventilation/ventilationsimulation---copy-94f86db8bb.png" alt="ventilationsimulation - Copy" size="large" >}}

The charts illustrate the amount of air exchange through natural ventilation throughout the year. **ACH** represents the rate of air replacement relative to the room volume, while **Airflow Rate** measures the volume of air moving through the openings per second.

Both charts show similar patterns, with **higher ventilation rates during nighttime and early morning** and lower rates during much of the daytime. This variation is influenced by outdoor weather conditions and the predefined window ventilation controls.

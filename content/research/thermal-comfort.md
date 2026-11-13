---
title: Thermal Comfort
category: Environmental Simulation
summary: Understanding what makes an indoor environment comfortable and how building
  design can achieve it.
slug: thermal-comfort
article_type: Research
date: '2026-11-12'
cover: /images/research/thermal-comfort/pasted-image-20261112175052-c929efb3e9.png
---

{{< research-image src="/images/research/thermal-comfort/pasted-image-20261112175052-c929efb3e9.png" alt="Pasted image 20261112175052" size="large" >}}
## Thermal Comfort

Thermal comfort is a condition in which people feel satisfied with the temperature and thermal environment around them. However, thermal comfort is not simply about maintaining a specific room temperature. Two rooms with the same air temperature can feel very different depending on sunlight, surrounding surfaces, air movement, and humidity. For example, a room at 26°C may still feel uncomfortable if sunlight heats the surrounding walls and windows. According to ASHRAE, thermal comfort is fundamentally about **how people experience and respond their thermal environment**, rather than temperature alone.


## Factor that Influences Thermal Comfort
Thermal comfort is influenced by six primary factors, divided into two categories: **environmental factors** and **personal factors**. Environmental factor stems for conditions created by the building and its surrounding environment, such as air temperature, radiant temperature, air speed, and humidity, while personal factor is conditions related to the people occupying the space, including clothing and activity level factors. These six factors form the foundation of thermal comfort assessment under ASHRAE Standard 55.
{{< research-image src="/images/research/thermal-comfort/thermal-comfort-factors-infographic-3-ff995d93d2.png" alt="Thermal Comfort Factors Infographic 3" size="small" >}}


## The Way to Achieve Thermal Comfort
Achieving thermal comfort means **creating a balance** between the heat produced by the human body and the heat exchanged with the surrounding environment. Thermal comfort can be achieved by understanding how heat affects people inside a building.

Throughout the day, heat enters and leaves a building through it walls, roof, windows, and surrounding environment. At the same time people and equipment generate heat indoors. These factors continuously influence indoor temperatures and how comfortable a space feels. 

How much heat enters a building is affected by the building orientation, shading devices, window design, and construction materials. For example, external shading can reduce direct sunlight entering through windows, while appropriate wall and roof materials can help limit heat transfer. By controlling heat gain, the building can maintain more stable indoor conditions that can be measured by temperature and PMV. 

But temperature is not the sole factor that determines comfort. Air movement and humidity also influence how people experience the indoor environment. Appropriate airflow can help the body release heat, while humidity affects how easily sweat evaporates. Therefore, natural ventilation, fans, and humidity control can contribute to a more comfortable indoor environment. 

When these natural strategies are not sufficient, **mechanical** cooling systems can help maintain the desired indoor conditions. Air conditioning removes heat from the space and helps regulate indoor temperature and humidity. However, achieving a specific temperature doesn't guarantee comfort, since surrounding surface temperatures and individual factors also influence how people feel. 

While indoor temperature helps understand the thermal condition of a space, it doesn't fully explain **how people experience those conditions**. A room maintained at 26°C may still feel too warm if surrounding surfaces are hot, humidity is high, or air movement is insufficient. Therefore, thermal comfort can be evaluated using **Predicted Mean Vote (PMV)**. PMV considers six factors, which are air temperature, mean radiant temperature, air speed, humidity, clothing insulation, and metabolic activity. By combining these factors, PMV predicts how a group of people is likely to feel in a particular indoor environment. PMV uses a seven-point thermal sensation scale, ranging from -3 (Cold) to +3 (Hot), with 0 representing a neutral thermal sensation. 


## Simulation Workflow

{{< research-image src="/images/research/thermal-comfort/thermal-simulation-workflow-infographic-24b385f788.png" alt="Thermal Simulation Workflow Infographic" size="medium" >}}



The simulation begins by **selecting one room as the study area**. Using Honeybee and EnergyPlus, a building is prepared based on the room geometry, aperture (room opening), and surrounding shading elements, as shown in the green inputs groups. The windows are modeled as unopenable, allowing the analysis to focus on the building's thermal conditions without natural ventilation. 

The analysis is then divided into **two simulation scenarios** using the same room geometry and building properties. In **Scenario 1**, the room is simulated **without mechanical cooling**. Its indoor temperature is influenced by outdoor weather, solar heat gain, building materials, and internal heat sources. This scenario helps us understand how the room responds thermally to its surrounding environment without air conditioning. In **Scenario 2**, the room is simulated **with mechanical cooling**. The simulation allows us to define the **AC cooling capacity, cooling limits, operating schedule, and desired indoor temperature**. EnergyPlus then calculates how the room responds to the available cooling system and whether the desired temperature can be maintained. 

For each scenario, the room geometry, aperture, shading elements, and thermal properties are combined into a complete **Honeybee Model**, represented by the red groups. The models are then processed and simulated using EnergyPlus. 



{{< research-image src="/images/research/thermal-comfort/daylightanalysis-2-46115dd218.png" alt="DaylightAnalysis 2" size="large" >}}







The simulation evaluates two thermal indicators: **Indoor Air Temperature** and **Operative Temperature**.
Indoor Air Temperature refers to the temperature of the air inside a room. However, people also exchange heat with surrounding surfaces, such as walls, ceilings, floors, and windows. This influence is represented by **Mean Radiant Temperature (MRT)**, which describes the combined effect of thermal radiation from surrounding surfaces.

**Operative Temperature combines Air Temperature and Mean Radiant Temperature** to provide a more representative understanding of the thermal conditions experienced by occupants. Therefore, even when the indoor air is cooled, the room may still feel warmer due to heat radiating from surrounding surfaces.

{{< research-image src="/images/research/thermal-comfort/thermal_comfort_simulation-2-d1feefd7b9.png" alt="Thermal_Comfort_Simulation 2" size="large" >}}

The simulations compare an **Unconditioned Room (left)**, without mechanical cooling, and a **Conditioned Room (right)**, equipped with a mechanical cooling system with a maximum cooling capacity of 30 kW.

In the unconditioned room, both Indoor Air Temperature and Operative Temperature increase significantly during the daytime, particularly between **12 PM and 6 PM**, reaching approximately 40°C or higher during hotter periods. This indicates substantial heat accumulation within the room, influenced by solar radiation, outdoor conditions, and heat transfer through the building envelope.

In contrast, the conditioned room maintains a much lower Indoor Air Temperature, generally close to the cooling setpoint of **26°C**. The Operative Temperature also decreases significantly, although it remains somewhat higher than the air temperature during certain daytime periods due to the influence of surrounding surface temperatures.

These results demonstrate how **mechanical cooling significantly improves indoor thermal conditions** by reducing air temperature and limiting heat buildup. However, the difference between Air Temperature and Operative Temperature also highlights the importance of building envelope design in controlling radiant heat.

While these simulations demonstrate the effectiveness of mechanical cooling in reducing indoor temperatures, **temperature alone does not fully determine whether occupants feel comfortable**. Therefore, the analysis is further developed using Predicted Mean Vote (PMV) to evaluate how these thermal conditions are likely to be perceived by occupants.



Following the indoor temperature analysis, the simulation is further evaluated to understand **how the resulting thermal conditions are likely to be perceived by occupants**. Two analyses are used: Predicted Mean Vote (PMV) and the Psychrometric Chart. 
#### Predicted Mean Vote (PMV)
{{< research-image src="/images/research/thermal-comfort/thermal_comfort_simulation---copy-1-424bd455a1.png" alt="Thermal_Comfort_Simulation - Copy 1" size="large" >}}

**Predicted Mean Vote (PMV)** is a method used to estimate how warm or cold people are likely to feel in a particular indoor environment. Unlike temperature measurements alone, PMV considers air temperature, radiant temperature, humidity, air movement, clothing, and activity level. It uses a scale ranging from −3 (Cold) to +3 (Hot), with 0 representing a neutral thermal sensation.

The simulation results show a significant difference between the **Unconditioned Room (left)** and the **Conditioned Room (right)**.

In the unconditioned room, the PMV chart is dominated by red throughout the daytime, indicating that occupants are likely to experience **hot and uncomfortable conditions**, particularly between morning and evening. This corresponds to the high indoor temperatures observed in the previous simulation.

In contrast, the conditioned room shows a noticeable reduction in thermal sensation, with the chart dominated by yellow and orange, representing conditions ranging from slightly warm to warm. This indicates that **mechanical cooling significantly reduces the predicted thermal discomfort** experienced by occupants.

However, the conditioned room does not consistently achieve a neutral thermal sensation. Although the cooling system maintains a lower indoor temperature, occupants may still experience some degree of warmth due to other environmental and personal factors.

#### Psychrometric Chart
{{< research-image src="/images/research/thermal-comfort/thermal_comfort_simulation---copy---copy-9655e77868.png" alt="Thermal_Comfort_Simulation - Copy - Copy" size="large" >}}

The **Psychrometric Chart** provides additional information about the relationship between indoor air temperature and moisture content. It shows how frequently different combinations of temperature and humidity occur throughout the simulation period.

In the unconditioned room, the chart shows a wider distribution of indoor conditions, particularly toward higher temperatures. This indicates that the room experiences considerable variations in temperature and humidity throughout the year.

In comparison, the conditioned room shows a much narrower distribution, concentrated around the mid-20°C range. This demonstrates how **mechanical cooling helps maintain more stable indoor air temperatures**, reducing the variation observed in the unconditioned room.

While the Psychrometric Chart helps explain the temperature and humidity conditions within the space, it does not independently determine whether occupants feel comfortable. Its results therefore support the PMV analysis, which provides a more comprehensive assessment of predicted human thermal sensation.

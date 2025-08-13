# Opentrons-antifungal-assay-scripts 
Code to run specific steps involved in phenotypic screening assays, using an Opentrons OT2-2 Robot.

This repository contains 3 scripts to semi-automate phenotypic screening assays for antifungal drug discovery, designed for the Opentrons OT-2 automated liquid handling robot. These protocols cover the steps below:
- Preparation of drug dilutions and combinations.
- Cell lysis procedure.
- Liquid transfer to 384-well plates and substrate addition.

For clarity, the complete pipeline of the phenotypic screening assay are described here below, highlighting the steps that must be performed at the bank (not on the robot). Otherwise specific required labware and procedural steps for each protocol are detailed in each .py file.

## LABWARE
Labware used by these scripts is [validated by Opentrons](https://labware.opentrons.com). 

## KEY ASSAY INFORMATION
Although we try to provide flexible and adaptable code to users, some parameters in these scripts remain fixed, such as plate position, labware, and rack placement on the robot platform. These codes were designed to optimize and minimize both assay time (by reducing movement between plates, racks, and trash bin) and potential errors (such as possible dripping when passing repeatedly over the plates). For biological assay parameters, such as cell lysis or antifungal combination volumes, these values were determined through extensive optimization testing. The fixed volumes represent the conditions that yielded the best experimental results in our validation studies.

## PHENOTYPIC SCREENING PIPELINE/ PROTOCOL
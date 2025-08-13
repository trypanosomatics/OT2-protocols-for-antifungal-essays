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
The protocol is considered "semi-automated" because only 3 steps of the complete phenotyping assay protocol were automated. The main reason of this is that our institution has only one automated pipetting system available, which is located in areas not approved for handling pathogenic organisms. In other words, we automated only those steps involving non-viable parasites, due to biosafety considerations.
Although we try to provide flexible and adaptable code to users, some parameters in these scripts remain fixed, such as plate position, labware, and rack placement on the robot platform. These codes were designed to optimize and minimize both assay time (by reducing movement between plates, racks, and trash bin) and potential errors (such as possible dripping when passing repeatedly over the plates). For biological assay parameters, such as cell lysis or antifungal combination volumes, these values were determined through extensive optimization testing. The fixed volumes represent the conditions that brought the best experimental results so far.

## PHENOTYPIC SCREENING PIPELINE/ PROTOCOL
The standard protocol used for phenotypic screening assays was performed over 4 distinct days. Briefly, on Tuesdays we seeded Vero cells and on Wednesdays cells were infected with the TUL-2 β-gal strain and left in ON incubation. The subsequent steps (performed on Fridays and Mondays) were conducted using the scripts detailed in this repository.

### Friday: Compound preparations
Preparation of serial dilutions and compound combinations

### Monday: Cell lysis and plate reading
Addition of lysis buffer to the plates, cell lysate homogenization and transference to solid-black 384-well plates for fluorescencemeasurement, and addition of MUG substrate



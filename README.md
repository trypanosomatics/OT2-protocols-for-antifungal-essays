# Opentrons-antifungal-assay-scripts 
Code to run specific steps involved in phenotypic screening assays, using an Opentrons OT2-2 Robot.

This repository contains 3 scripts to semi-automate phenotypic screening assays for antifungal drug discovery, designed for the Opentrons OT-2 automated liquid handling robot. These protocols cover the steps below:
- Preparation of drug dilutions and combinations.
- Cell lysis procedure.
- Liquid transfer to 384-well plates and substrate addition.

For clarity, the complete pipeline of the phenotypic screening assay is described here below, highlighting the steps that must be performed at the bank (not on the robot). Otherwise specific required labware and procedural steps for each protocol are detailed in each `.py` file.

## LABWARE
Labware used by these scripts is [validated by Opentrons](https://labware.opentrons.com). 

## KEY ASSAY INFORMATION

The protocol is considered "semi-automated" because only 3 steps of the complete phenotyping assay protocol were automated. The main reason of this is that our institution has only one automated pipetting system available, which is located in areas not approved for handling pathogenic organisms. In other words, we automated only those steps involving non-viable parasites, due to biosafety considerations.

Although we try to provide flexible and adaptable code to users, some parameters in these scripts remain fixed, such as plate position, labware, and rack placement on the robot platform. These codes were designed to optimize and minimize both assay time (by reducing movement between plates, racks, and trash bin) and potential errors (such as possible dripping when passing repeatedly over the plates). For biological assay parameters, such as cell lysis or antifungal combination volumes, these values were determined through extensive optimization testing. The fixed volumes represent the conditions that brought the best experimental results so far.

The standard protocol used for this phenotypic screening assay was performed over 4 different days. Briefly, we first seeded Vero cells and on the next day these cells were infected with the TUL-2 β-gal strain and left in ON incubation. The subsequent steps (addition of compounds and cell lysis for plate reading) were conducted using the scripts detailed in this repository.

## PHENOTYPIC SCREENING PIPELINE/ PROTOCOL

### I. Preparation of serial dilutions and compound combinations

1. Dispense manually in wells A2 and B2 of a [NEST_96-well plate_100ul_PCR_full_skirt](https://labware.opentrons.com/#/?loadName=nest_96_wellplate_100ul_pcr_full_skirt) plate, at least 80 uL of compound solution (in each well). Additionally, prepare and place in the A1 position of an [opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap](https://labware.opentrons.com/#/?loadName=opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap), an Eppendorf tube with 1 mL DMSO.
2. Run the `Drugs_combination.py` script on the Opentrons OT-2.
3. Transfer this mix to cell culture plate.

### II. Addition of lysis buffer to the plates, cell lysate homogenization 

1. Prepare and dispense manually, 10 mL of lysis solution at column A1 of a [NEST_12-well_reservoir_15ml](https://labware.opentrons.com/#/?loadName=nest_12_reservoir_15ml). Additionally prepare a washing solution for tips (e.g. bleach) and dispense it at column A12 of this same reservoir. 
- Note: This step will need as culture plate a [NEST_96-well plate_200ul_flat](https://labware.opentrons.com/#/?loadName=nest_96_wellplate_200ul_flat) or similar, to dispense de lysis solution in.
2. Run the `Cell_lysis.py` script on Opentrons OT-2. 

### III. Transference to solid-black 384-well plates for fluorescencemeasurement, and addition of MUG substrate

1. Prepare and place manually an Eppendorf tube with (at least) 600 uL of substrate, in the A1 position of an [Opentrons_24-tube Rack_with Eppendorf_1.5ml_safelock_snapcap](https://labware.opentrons.com/#/?loadName=opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap).
- Note: User must have a black [corning_384_wellplate_112ul_flat](https://labware.opentrons.com/#/?loadName=corning_384_wellplate_112ul_flat) and at least one [nest_96_wellplate_200ul_flat](https://labware.opentrons.com/#/?loadName=nest_96_wellplate_200ul_flat) or similar to run this protocol.
2. Run the `Transfer_to_384_well_plate.py` script on Opentrons OT-2. 
3. Read plate.

### NOTES ON THE SCRIPTS
This README is not exhaustively detailed, for specifications see comments in scripts.

## ALTERNATIVE USES OF THIS PROTOCOL
These scripts were designed to be easily modified and adapted to user requirements. It is possible to use them for multiple plates if the line(s) commented with the style "#Write  the amount of plates...." are modified in the `.py` file. In `Transfer_to_384_well_plate.py` protocol, you can also specify the 384 well plate column from where you want to start using it (useful if the 384 well plate has already been used). This enables:
- Group processing of multiple plates in a single run
- Capacity to transfer liquids from up to 4 96-well plates into a single 384-well reading plate. 

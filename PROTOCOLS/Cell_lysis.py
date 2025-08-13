from opentrons import protocol_api
metadata = {
    "apiLevel": "2.11",
    "protocolName": "Parasite Lysis",
    "description": "Protocol for lysing parasites in a 96-well plate",
    "author": "Salas Sarduy Emir, Didier Garnham Mercedes, Aguero Franco Agustin"
}

def run(ctx: protocol_api.ProtocolContext):
    # LABWARE INPUTS
    reservoir_position = 1
    reservoir = ctx.load_labware("nest_12_reservoir_15ml", reservoir_position)

    # Plates and tipracks
    plates = 1                                           #Write de amount of plates you want to lysis
    tips_list = []
    plates_list = []
    
    plate_slots = [2, 4, 6, 8]  
    tiprack_slots = [3, 5, 7, 9] 

    for i in range(plates):
        plate_i = ctx.load_labware("nest_96_wellplate_200ul_flat", plate_slots[i])
        plates_list.append(plate_i)

        tips_i = ctx.load_labware("opentrons_96_tiprack_300ul", tiprack_slots[i])
        tips_list.append(tips_i)
    #Pipette
    left_pipette = ctx.load_instrument("p300_single_gen2", "left", tip_racks= tips_list)


    # PROTOCOL
    ctx.home()
    # PROTOCOL
    def wash_tip():
        left_pipette.mix(1, 100, reservoir["A12"]) #sino probar source= reservoir["A12"]
        left_pipette.blow_out()
    _96_wells_list = []
    abc= ["B","C","D","E","F","G"]
    for i in range(2,12):
        for j in abc:
            well_j = j + str(i)
            _96_wells_list.append(well_j)
    def lysis_solution(reservoir_columns_list, plate_wells_list, amount_plates):
        for plate in range(amount_plates): #sino probar plates_list
        #This function aliquots 100 ul of the lysis solution and mixes it with the plate medium
            left_pipette.pick_up_tip()
            for well_plate in plate_wells_list:
                left_pipette.aspirate(100, reservoir[reservoir_columns_list[plate]])
                left_pipette.dispense(105, plates_list[plate][well_plate])
                left_pipette.mix(2, 100, plates_list[plate][well_plate])
            
                wash_tip()
                left_pipette.drop_tip()
                left_pipette.pick_up_tip()
            left_pipette.return_tip()
    plate_wells = _96_wells_list
    res_columns = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8","A9","A10","A11","A12"]
    lysis_solution(res_columns, plate_wells, len(plates_list))
    ctx.home()

    for line in ctx.commands():
       print(line)
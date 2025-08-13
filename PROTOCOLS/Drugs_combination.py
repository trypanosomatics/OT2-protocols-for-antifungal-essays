from opentrons import protocol_api
metadata = {
    "apiLevel": "2.11",
    "protocolName": "Drugs combination",
    "description": """Protocol for combining different compounds on a PCR plate""",
    "author": "Salas Sarduy Emir, Didier Garnham Mercedes, Aguero Franco Agustin"
    }

def run(ctx: protocol_api.ProtocolContext):
    #LABWARE INPUTS
    ctx.home()
    plate_pcr = ctx.load_labware("nest_96_wellplate_100ul_pcr_full_skirt", 1)
    reservoir = ctx.load_labware("opentrons_24_tuberack_nest_1.5ml_snapcap", 2)
    #          (TIP RACKS) 
    p300_tips=1
    p300_tips_list=[]
    for i in range (1, p300_tips+1):
        position_tips_i=2+i
        tips_i = ctx.load_labware("opentrons_96_tiprack_300ul", position_tips_i)
        p300_tips_list.append(tips_i)
        i+=1
    p20_tips=1
    p20_tips_list=[]
    for j in range (1, p20_tips+1):
        position_tips_j= position_tips_i +j
        tips_j = ctx.load_labware("opentrons_96_tiprack_20ul", position_tips_j)
        p20_tips_list.append(tips_j)
        j+=1
    #Pipettes 
    p300_pipette = ctx.load_instrument("p300_single_gen2", "left", tip_racks= p300_tips_list)
    p20_pipette = ctx.load_instrument("p20_single_gen2", "right", tip_racks= p20_tips_list)

    # PROTOCOLS

    #Add DMSO in first row
    p300_pipette.pick_up_tip()
    for k in range (2,10):
        p300_pipette.aspirate(50, reservoir["A1"])
        p300_pipette.touch_tip(v_offset=-3)
        p300_pipette.dispense(50, plate_pcr.rows()[0][k], rate= 0.5)
        p300_pipette.blow_out(plate_pcr.rows()[0][k])
        p300_pipette.touch_tip(plate_pcr.rows()[0][k])
    #p300_pipette.drop_tip()

    #Add DMSO in first column
    #p300_pipette.pick_up_tip()
    for j in range (2,7):
        p300_pipette.aspirate(50, reservoir["A1"])
        p300_pipette.touch_tip(v_offset=-3)
        p300_pipette.dispense(50, plate_pcr.wells()[j], rate= 0.5)
        p300_pipette.blow_out(plate_pcr.wells()[j])
        p300_pipette.touch_tip(plate_pcr.wells()[j])
    #p300_pipette.drop_tip()

    #Add 10 uL DMSO in column 11
    #p300_pipette.pick_up_tip()
    for j in range (80,87):
        p300_pipette.aspirate(10, reservoir["A1"])
        p300_pipette.touch_tip(v_offset=-3)
        p300_pipette.dispense(10, plate_pcr.wells()[j], rate= 0.5)
        p300_pipette.blow_out(plate_pcr.wells()[j])
        p300_pipette.touch_tip(plate_pcr.wells()[j])
    p300_pipette.drop_tip()

    #Drug dilution on first column, B1 to F1 (G1 has no compound)
    p300_pipette.pick_up_tip()
    for i in range (1, 5):
        p300_pipette.aspirate(25, plate_pcr.columns()[0][i])
        p300_pipette.dispense(25,  plate_pcr.columns()[0][i+1], rate= 0.5)
        p300_pipette.mix(10, 60)
        p300_pipette.blow_out()
        p300_pipette.touch_tip()
    p300_pipette.aspirate(25,plate_pcr.columns()[0][5])
    p300_pipette.dispense(25,plate_pcr.columns()[0][7], rate= 0.5)
    p300_pipette.blow_out()
    p300_pipette.touch_tip()
    p300_pipette.drop_tip()

    #Drug dilution on first row, A2 to A9 (A11 has no compound)
    p300_pipette.pick_up_tip()
    for i in range (1, 9):
        p300_pipette.aspirate(25, plate_pcr.columns()[i][0])
        p300_pipette.dispense(25,  plate_pcr.columns()[i+1][0], rate= 0.5)
        p300_pipette.mix(10, 60)
        p300_pipette.blow_out()
        p300_pipette.touch_tip()
    p300_pipette.aspirate(25,plate_pcr.columns()[9][0])
    p300_pipette.dispense(25,plate_pcr.columns()[11][0], rate= 0.5)
    p300_pipette.blow_out()
    p300_pipette.touch_tip()
    p300_pipette.drop_tip()

    # COMBINATIONS
    # Put 5 uL in each column from right to left (takes from column B1 and distribute in columns B2 to B10)
    for k in range(1,7):
        p20_pipette.pick_up_tip()
        for i in range (1,10):
            p20_pipette.aspirate(5, plate_pcr.columns()[0][k])
            p20_pipette.dispense(5, plate_pcr.columns()[10-i][k], rate= 0.5)
            p20_pipette.blow_out(plate_pcr.columns()[10-i][k])
            p20_pipette.touch_tip(plate_pcr.columns()[10-i][k], v_offset=-2)
        p20_pipette.drop_tip()

    # Dilutions from down to top (takes from A2 and distribute in rows A2 to F2)
    for k in range(1,10):
        p20_pipette.pick_up_tip()
        for i in range (1,7):
            p20_pipette.aspirate(5, plate_pcr.columns()[k][0])
            p20_pipette.dispense(5, plate_pcr.columns()[k][7-i], rate= 0.5)
            p20_pipette.mix(5, 10)
            p20_pipette.dispense(20, plate_pcr.columns()[k][7-i], rate= 0.5)
            p20_pipette.blow_out(plate_pcr.columns()[k][7-i])
            p20_pipette.touch_tip(plate_pcr.columns()[k][7-i], v_offset=-2)
        p20_pipette.drop_tip()

    ctx.home()

    for line in ctx.commands():
        print(line)
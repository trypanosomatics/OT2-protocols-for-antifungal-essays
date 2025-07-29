from opentrons import protocol_api
metadata = {
    "apiLevel": "2.11",
    "protocolName": "Transfer from 96 to 384 well plate",
    "description": """Protocol for moving liquids and substratums to a 384 well plate""",
    "author": "Salas Sarduy Emir, Didier Garnham Mercedes, Aguero Franco Agustin"
    }

def run(ctx: protocol_api.ProtocolContext):
    ctx.home()
    plates=2                     #Write the amount of plates you want to transfer
    first_384_column= 1          #Write the 384 well plate column from where you want to start using
    _384_wells_list = []
    abc= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
    for i in range(first_384_column,25):
        for j in abc:
            well_j = j + str(i)
            _384_wells_list.append(well_j)

    tips_list=[]
    tips_p20_list=[]
    plates_list=[]
   
    if plates == 1:
        plate_384_lot = [8]
        plates_96_lot = [9]
        tips_300_lot = [6]
        reservoir_lot = [11]
        tips_20 = [10]
    elif plates == 2:
        plate_384_lot = [8]
        plates_96_lot = [9, 11]
        tips_300_lot = [6,10]
        reservoir_lot = [7]
        tips_20 = [5]
    elif plates == 3:
        plate_384_lot = [8]
        plates_96_lot = [5, 9, 11]
        tips_300_lot = [6, 7, 10]
        reservoir_lot = [4]
        tips_20 = [1]
    elif plates == 4:
        plate_384_lot = [8]
        plates_96_lot = [6,9,10,11]
        tips_300_lot = [3,4,5,7]
        reservoir_lot = [2]
        tips_20 = [1]
   
    plate_384 = ctx.load_labware("corning_384_wellplate_112ul_flat", plate_384_lot[0])
    plate_384.set_offset(x=0.50, y=1.50, z=3.00)

    for i in range(plates):
       
        plate_i = ctx.load_labware("nest_96_wellplate_200ul_flat", plates_96_lot[i])
        plate_i.set_offset(x=1.00, y=2.00, z=0.00)
        plates_list.append(plate_i)
       
        tips_i = ctx.load_labware("opentrons_96_tiprack_300ul", tips_300_lot[i])
        tips_i.set_offset(x=0.00, y=2.00, z=0.00)
        tips_list.append(tips_i)
       
        if i < len(reservoir_lot):
            reservoir = ctx.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", reservoir_lot[i])
            reservoir.set_offset(x=0.00, y=1.00, z=0.00)
       
        if i < len(tips_20):
            tips_p20_i = ctx.load_labware("opentrons_96_tiprack_20ul", tips_20[i])
            tips_p20_i.set_offset(x=0.00, y=1.50, z=0.00)
            tips_p20_list.append(tips_p20_i)
   
    p300_pipette = ctx.load_instrument("p300_single_gen2", "left", tip_racks= tips_list)
    p20_single_pipette = ctx.load_instrument("p20_single_gen2","right", tip_racks=tips_p20_list)

    # PROTOCOL for moving solution from 96 to 384 well plate
    _384_wells = _384_wells_list
    i = 0  
    k_start = 9  

    for plate in plates_list:
        k = k_start  
        while k < 86:
            for j in range(k, k + 6):
                p300_pipette.pick_up_tip()
                p300_pipette.mix(5, 100, plate.wells()[j])  
                p300_pipette.aspirate(90, plate.wells()[j])  
                p300_pipette.dispense(90, plate_384.wells_by_name()[_384_wells[i]])
                p300_pipette.drop_tip()
                i += 1  
            k += 8  


    # PROTOCOL for adding substratum
    def substratum_to_384 (k,j):
    for i in range(k,j):
            p20_single_pipette.aspirate(15, reservoir["A1"])
            p20_single_pipette.dispense(10,plate_384[_384_wells_list[i]])
            p20_single_pipette.dispense(5, reservoir["A1"])
            i+=1
   
    #For controls
    a=1
    m=54
    n=60
    p20_single_pipette.pick_up_tip()
    while a<= plates:
        x= substratum_to_384(m,n)
        m+=60
        n+=60
        a+=1
    p20_single_pipette.drop_tip()
    #For the other wells
    a=1
    m=0
    n=54
    p20_single_pipette.pick_up_tip()
    while a<= plates:
        x= substratum_to_384(m,n)
        m+=60
        n+=60
        a+=1
    p20_single_pipette.drop_tip()


    ctx.home()

    # for line in ctx.commands():
        #print(line)
"""
Author: Nicholas Pilgrim-Minaya
Created: 11/2022
Email: npilgrim@asu.edu

Description: This program creates 10 ml of a PVK solution (Ratio of DMF to DMSO is 1:4) for a perovskite solar cell
and places it in a test tube on the top left corner of the tube rack on the heater shaker module. This program
takes your DMSO, DMF, and solutes and mixes them using the shaker module

Instructions: 
0. Make sure all custom labware definitions (.json files) in the folder are loaded into the opentrons app
1. Place heater shaker module in slot 10 on the deck
2. Lock a tube rack on the heater shaker module
3. Place tube rack in slot 10 on the deck
4. PLace a vial of DMF solvent in space A1 of the tuberack (This is the top left corner of the tube rack)
5. PLace a vial of DMSO solvent in space B1 of the tuberack (This space is one below A1)
6. Place the tip rack in slot 8 on the deck
7. Place the measured pervoskite solutes in the test tube in top left corner of the tube rack on the shaker module
8. Calibrate robot within the protocol in opentrons app with your labware. This is called a labware position check in the opentrons app. It is seen after pressing run on the protocol in the protocol list.
9. Make sure the tip rack is full of tips
10. Run and when the robot pauses, place cap on the test tube on the shaker module before hitting resume
"""

#These lines of codes get labware definitions from opentrons
def get_values(*names):
    import json
    _all_values = json.loads("""{"well_plate":"nest_96_wellplate_200ul_flat","pipette":"p300_single_gen2","tips":"opentrons_96_tiprack_300ul","pipette_mount":"left"}""")
    return [_all_values[n] for n in names]

#These lines import functions from opentrons
from opentrons import protocol_api
from opentrons import types

#This defines version number
metadata = {'apiLevel': '2.13'}


def run(protocol):

    #These lines convert strings into an array
    [well_plate, pipette, tips, pipette_mount] = get_values(  # noqa: F821
        "well_plate", "pipette", "tips", "pipette_mount")

    #Loads Opentron's definitons into python variables
    tiprack = protocol.load_labware(tips, '8')
    hs_mod = protocol.load_module('heaterShakerModuleV1', 10)
    hs_well = hs_mod.load_labware('12_tuberack_15ml_shaker')
    tuberack = protocol.load_labware('12_tuberack_15ml', 7)

    protocol.set_rail_lights(on=True)
    
    # Definies right and left pipettes
    right = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])
    left = protocol.load_instrument('p300_single_gen2', 'left', tip_racks=[tiprack])
    
    #Robot's physical functionality starts here
    hs_mod.close_labware_latch()
    
    #Right and left pick up tips
    right.pick_up_tip(tiprack['A1'])
    left.pick_up_tip(tiprack['A2'])
    
    #Loop to transfer 250 ul of DMF to Shaker module 8 times (2ml)
    #To Demo robot enter 1 instead of 8 and 32
    right.default_speed = 200
    for DMF in range(8): 
        right.aspirate(250, tuberack['A1'])
        right.dispense(250, hs_well['A1'].top(-20))  
        right.blow_out()
    
    left.default_speed = 200
    #Loop to transfer 250 ul of DMSO to Shaker module 32 times (8ml)
    for DMSO in range(32):
        left.aspirate(250, tuberack['B1'])
        left.dispense(250, hs_well['A1'].top(-20))
        left.blow_out()
        
    #throws tips into trash bin
    right.drop_tip()
    left.drop_tip()
    
    #Pauses system to wait for user to place cap on the test tube on the shaker module
    protocol.pause('WARNING: Place cap on the test tube of the shaker before pressing resume')
    
    #Shakes the well plate for 1.5 minutes at 1000 rpm to mix solution
    hs_mod.set_and_wait_for_shake_speed(1000)
    protocol.delay(minutes=1.5)
    hs_mod.deactivate_shaker()

    
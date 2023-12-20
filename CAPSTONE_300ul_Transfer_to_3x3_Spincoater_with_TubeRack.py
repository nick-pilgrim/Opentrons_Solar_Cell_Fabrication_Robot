"""
Author: Nicholas Pilgrim-Minaya
Created: 11/2022
Email: npilgrim@asu.edu

Description: This program transfers 300ul of a PVK solution (Ratio of DMF to DMSO is 1:4) 
from the shaker module to a 2.5cm by 2.5cm subtrate sitting on the spin coater.
The robot will dispense 300 ul making 3x3 droplet grid with each drop being 33ul and 5mm separated. The center droplet is 36ml.
This protocol assumes the spincoater is spinning. The protocol pauses before every droplet so you can press resume to dispense the droplet at your desired time

Instructions: 
0. Make sure all custom labware definitions (.json files) in the folder are loaded into the opentrons app
1. Place heater shaker module in slot 10 on the deck
2. Lock a tuberack on the heater shaker module
3. Place tube rack in slot 10 on the deck (The tuberack isn't used in this protocol. You can ignore this)
4. PLace a vial of PVK solution in space A1 of the tuberack on top on the shaker module (This is the top left corner of the tube rack)
5. Place the tip rack in slot 8 on the deck
6. Place spincoater with substrate on slot 1 on the deck (It does not need to fit perfectly. You can calibrate the arm to be in the location where you place the spincoater)
7. Calibrate robot within the protocol in opentrons app with your labware. This is called a labware position check in the opentrons app. It is seen after pressing run on the protocol in the protocol list.
8. When calibrating the robot arm to the location of the subrate, make sure that the arm is 2.5mm down and to the right of the top left corner of the substrate. 
The robot drops liquid in the center first and then from top left corner to bottom right corner
9. Make sure the tip rack is full of tips
10. Make sure the cap is off the test tube on the rack and press run. The code will always pause to make sure you have done this. Just press resume when it pauses
"""
#These lines of codes get labware definitions from opentrons
def get_values(*names):
    import json
    _all_values = json.loads("""{"well_plate":"nest_96_wellplate_200ul_flat","pipette":"p300_single_gen2","tips":"opentrons_96_tiprack_300ul","pipette_mount":"left"}""")
    return [_all_values[n] for n in names]

#Opentrons imports
from opentrons import protocol_api
from opentrons import types

#Opentrons code version
metadata = {'apiLevel': '2.13'}

#Run function
def run(protocol):
    #These lines convert strings into an array
    [well_plate, pipette, tips, pipette_mount] = get_values(  # noqa: F821
        "well_plate", "pipette", "tips", "pipette_mount")

    # load labware
    tiprack = protocol.load_labware(tips, '8')
    hs_mod = protocol.load_module('heaterShakerModuleV1', 10)
    hs_well = hs_mod.load_labware('12_tuberack_15ml_shaker')
    spincoater = protocol.load_labware('capstone_demo_spincoater_25_slots', 1)

    protocol.set_rail_lights(on=True)
    
    # load instrument
    right = protocol.load_instrument('p300_single_gen2', 'right', tip_racks=[tiprack])
    
    hs_mod.close_labware_latch()
    
    protocol.pause('WARNING: Take off the cap of the test tube holding the PVK solution on the shaker before pressing resume')
    
    #Picks up tip and 300 ul of the solution and dispenses it on spin coater
    right.pick_up_tip(tiprack['A3'])
    right.aspirate(300, hs_well['A1'])
    right.default_speed = 50
    
    #A1,B1,etc are the grid spaces on the substrate where the droplets are places
    #C3 is the center droplet and the first droplet to drop. Its 36ul while the others are 33
    protocol.pause('Press Resume to drop the 1st Drop')
    right.dispense(36, spincoater['C3'])
    protocol.pause('Press Resume to drop the 2nd Drop')
    right.dispense(33, spincoater['B2'])
    protocol.pause('Press Resume drop to the 3rd Drop')
    right.dispense(33, spincoater['C2'])
    protocol.pause('Press Resume drop to the 4th Drop')
    right.dispense(33, spincoater['D2'])
    protocol.pause('Press Resume to drop to the 5th Drop')
    right.dispense(33, spincoater['B3'])
    protocol.pause('Press Resume to drop to the 6th Drop')
    right.dispense(33, spincoater['D3'])
    protocol.pause('Press Resume to drop to the 7th Drop')
    right.dispense(33, spincoater['B4'])
    protocol.pause('Press Resume to drop to the 8th Drop')
    right.dispense(33, spincoater['C4'])
    protocol.pause('Press Resume to drop to the last Drop')
    right.dispense(33, spincoater['D4'])
    right.blow_out()
    
    
    right.drop_tip()
    
        # -*- coding: utf-8 -*-
    
Instructions for the Final Protocols using the tube racks are listed here and at the top of every .py file.
These are the protocols that I intend labworkers to use to create their perovskites. 

For Python file: CAPSTONE_PVK_Solution_Creator_with_TubeRack

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
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For Python file: CAPSTONE_300ul_Transfer_to_3x3_Spincoater_with_TubeRack

Description: This program transfers 300ul of a PVK solution (Ratio of DMF to DMSO is 1:4) 
from the shaker module to a 2.5cm by 2.5cm subtrate sitting on the spin coater.
The robot will dispense 300 ul making 3x3 droplet grid with each drop being 33ul and 5mm separated. However, The center droplet is 36ml.
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
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The other python files in the folder that have Demo in their name are earlier versions of the code or protocols that use the wellplate attachment on the heatshaker instead of the tube rack.
I included these for reference to learn how the code works in order for you to make your own changes to the code if need be.



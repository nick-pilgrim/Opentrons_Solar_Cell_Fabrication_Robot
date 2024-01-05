"""
Author: Nicholas Pilgrim-Minaya
Description: With give a given pervoskite chemical formula, this code outputs
the total cost of chemicals, the amount of chemcials, and the predicted
Band Gap of the perovskite using a formula made from MACHINE LEARNING

"""
import numpy as np

import matplotlib.pyplot as plt

#Constants for Predictor of band gap
r_Cs = 1.81
r_FA = 2.79
r_MA = 2.7
r_Cl = 1.81
r_Br = 1.96
r_I = 2.03


def Band_Gap_Predictor(Cs, FA, fixed_MA, Br, fixed_Cl, I):
    R = (Cs*r_Cs + FA*r_FA + (1 - Cs - FA)*fixed_MA)/(fixed_Cl*r_Cl + Br*r_Br + (1 - fixed_Cl - Br)*r_I)
    Eg = -4.960 + 2.214*Cs - 0.315*FA + 0.814*fixed_Cl + 0.436*Br + 4.913*R
    return Eg
    


#Millimols of formula created
total_mmol = 10.0
#Lead
COST_DMSO_DMF = 7.40
Pb  = 3.0

#MOLAR MASS (g/mol)
CsI_mm = 259.81
FAI_mm = 171.97
PbBr2_mm = 367.01
PbI2_mm = 461.01
PbCl2_mm = 278.1
MACl_mm = 58.44

#Prices of chemicals
CsI_pr = 105.00
FAI_pr = 189.00
PbBr2_pr = 54.00
PbI2_pr = 129.00
PbCl2_pr = 82.70
MACl_pr = 27.00


#What you get for the price?
#Amount in milligrams per cost price
CsI_c = 10.0 * 1000
FAI_c = 5.0 * 1000
PbBr2_c = 5.0 * 1000
PbI2_c = 5.0 * 1000
PbCl2_c = 10*1000
MACl_c = 5.0*1000

run = 1

while(run == 1):
    #Porportions of chemicals
    Cs = float(input('Enter Porportion of Cs: '))
    #FA = float(input('Enter Porportion of FA: '))
    I = float(input('Enter Porportion of I: '))
    MBC = float(input('Is there an additional 4% mol of MAPbCl3? (1 for yes or 0 for no): '))
    #Br = float(input('Enter Porportion of Br: '))
    fixed_MA = 0
    fixed_Cl = 0
    FA = 1 - Cs
    Br = 1 - I
    mix = np.array([Cs, FA, I, Br])
    cost = np.zeros(4, float)
    
    mix[0] = mix[0]*total_mmol*CsI_mm
    if(MBC == 1):
        mix[0] =mix[0]*(1/1.04)
    print("\nAmount of CsI in mg:", mix[0])
    cost[0] = round(mix[0]*CsI_pr/CsI_c, 2)
    print("Cost of CsI: ",  cost[0])
    
    
    mix[1] = mix[1]*total_mmol*FAI_mm
    if(MBC == 1):
        mix[1] =mix[1]*(1/1.04)
    print("\nAmount of FAI in mg:", mix[1])
    cost[1] = round(mix[1]*FAI_pr/FAI_c, 2)
    print("Cost of FAI: ", cost[1])
    
    mix[2] = mix[2]*Pb*total_mmol*PbI2_mm
    if(MBC == 1):
        mix[2] =mix[2]*(1/1.04)
    print("\nAmount of PbI2 in mg:", mix[2])
    cost[2] = round(mix[2]*PbI2_pr/PbI2_c, 2)
    print("Cost of PbI2: ", cost[2])
    
    
    mix[3] = mix[3]*Pb*total_mmol*PbBr2_mm
    if(MBC == 1):
        mix[3] =mix[3]*(1/1.04)
    print("\nAmount of PbBr2 in mg: ", mix[3])
    cost[3] = round(mix[3]*PbBr2_pr/PbBr2_c, 2)
    print("Cost of PbBr2: ", cost[3])
    
    if(MBC == 1):
        PbCl2_a = (0.04/1.04)*total_mmol*PbCl2_mm
        print("\nAmount of PbCl2 in mg: ", PbCl2_a)
        PbCl2_cost = round(PbCl2_a*PbCl2_pr/PbCl2_c, 2)
        print("Cost of PbCl2: ", PbCl2_cost)
        
        MACl_a = (0.04/1.04)*total_mmol*MACl_mm
        print("\nAmount of MACl in mg: ", MACl_a)
        MACl_cost = round(MACl_a*MACl_pr/MACl_c, 2)
        print("Cost of MACl: ", MACl_cost)
    
    
    total_cost = cost[3]+cost[2]+cost[1]+cost[0] + COST_DMSO_DMF
    if(MBC == 1):
        total_cost = total_cost + PbCl2_cost + MACl_cost
    print("\nTotal Cost: ", round(total_cost,2))
    
    Eg_prediction = Band_Gap_Predictor(Cs, FA, fixed_MA, Br, fixed_Cl, I) 
    print("\nBand Gap Prediction in eV: ", Eg_prediction)
    
    run =int(input("Run again? (YES=1, NO=0) : "))
    
    
    #plt.bar(x_pos, energy, color='green')
    #plt.plot(source_v, meas_i, label='Measured Current')
    #plt.title('Perovskite Cost')
    #plt.xlabel('Source Voltage (V)')
    #plt.ylabel('Current (A)')
    #plt.yscale('log')
    #plt.legend()
    #plt.show()




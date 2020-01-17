import pandas as pd
import numpy as np
import xlrd
import math

noxef_cars = pd.read_excel("rtp_Copert5_NOxEFs_final_trimmed.xlsx", sheet_name = "Cars")
noxef_lgv = pd.read_excel("rtp_Copert5_NOxEFs_final_trimmed.xlsx", sheet_name = "LGVs")
noxef_hgv = pd.read_excel("rtp_Copert5_NOxEFs_final_trimmed.xlsx", sheet_name = "HGVs & Buses")
noxef_mbike = pd.read_excel("rtp_Copert5_NOxEFs_final_trimmed.xlsx", sheet_name = "Motorcycles")

#print("Column headings:")
#print(noxef.columns)

# Column guide
# D = ALPHA
# E = BETA
# F = GAMMA
# G = DELTA
# H = EPSILON
# I = ZITA
# J = ITA
# K = THITA
# L = RF
# O9 = AVG_SPEED

# Excel g/km calculation
# AVG_SPEED = IF(AVG_SPEED_ALL < MIN_SPEED THEN AVG_SPEED_ALL,IF(AVG_SPEED_ALL>MAX_SPEED THEN MAX_SPEED, OTHERWISE AVG_SPEED_ALL))

# Diesel and Petrol: Pre-Euro NOx EF (g/km) = ((ALPHA * AVG_SPEED ^ 2) + (BETA * AVG_SPEED) + GAMMA + (DELTA * LOG(AVG_SPEED)) + (EPSILON * EXP(ZITA * AVG_SPEED)) + (ITA * (AVG_SPEED ^ THITA))) * (1 - RF)
# =(($D9 * $O9 ^ 2) + ($E9 * $O9) + $F9+ ($G9 * LOG($O9)) + ($H9 * EXP($I9 * $O9)) + ($J9 * ($O9 ^ $K9))) * (1 - $L9)

# Diesel: Euro 1 - 5 NOx EF & Petrol: Euro 1-6
# =(($D10 + $F10 * $O10 + $H10 * $O10 ^2 + $I10 / $O10 ) / (1 + $E10 * $O10 + $G10 * $O10 ^ 2)) * (1 - $L10)

# Diesel: Euro 6_1,6_2,6_3 EF
# =(D15*O15^2+E15*O15+F15+G15/O15)/(H15*O15^2+I15*O15+J15)*(1-L15)
AVG_SPEED = 30

class Speed_function:
    def Speed(row):
	    if noxef_cars.loc[row,'Min speed (km/h)'] > AVG_SPEED:
	        SPEED = noxef_cars.loc[row,'Min speed (km/h)']
	    elif noxef_cars.loc[row,'Max speed (km/h)'] < AVG_SPEED:
	        SPEED = noxef_cars.loc[row,'Max speed (km/h)']
	    else: 
	        SPEED = AVG_SPEED
	    return(SPEED)

class Car_EF_functions:
    def Diesel_Pre_Euro_NOx_EF(row): 
        EF = ((noxef_cars.loc[row,'ALPHA'] * (Speed_function.Speed(row) ** 2)) + (noxef_cars.loc[row,'BETA'] * Speed_function.Speed(row)) + noxef_cars.loc[row,'GAMMA'] + (noxef_cars.loc[row,'DELTA'] * math.log(Speed_function.Speed(row))) + (noxef_cars.loc[row,'EPSILON'] * math.exp(noxef_cars.loc[row,'ZITA'] * Speed_function.Speed(row))) + (noxef_cars.loc[row,'ITA'] * (Speed_function.Speed(row) ** noxef_cars.loc[row,'THITA']))) * (1 - noxef_cars.loc[row,'RF'])
        return(str(EF))

    def Diesel_Euro_1_to_5_NOx_EF(row):
        EF = ((noxef_cars.loc[row,'ALPHA'] + noxef_cars.loc[row,'GAMMA'] * AVG_SPEED + noxef_cars.loc[row,'EPSILON'] * AVG_SPEED  ** 2 + noxef_cars.loc[row,'ZITA'] / AVG_SPEED ) / (1 + noxef_cars.loc[row,'BETA'] * AVG_SPEED + noxef_cars.loc[row,'DELTA'] * AVG_SPEED ** 2)) * (1 - noxef_cars.loc[row,'RF'])
        return(str(EF))

    def Diesel_Euro_6_NOx_EF(row):
        EF =(noxef_cars.loc[row,'ALPHA']*AVG_SPEED**2+noxef_cars.loc[row,'BETA']*AVG_SPEED+noxef_cars.loc[row,'GAMMA']+noxef_cars.loc[row,'DELTA']/AVG_SPEED)/(noxef_cars.loc[row,'EPSILON']*AVG_SPEED**2+noxef_cars.loc[row,'ZITA']*AVG_SPEED+noxef_cars.loc[row,'ITA'])*(1-noxef_cars.loc[row,'RF'])
        return(str(EF))

    def Petrol_Pre_Euro_NOx_EF(row):
        EF = ((noxef_cars.loc[row,'ALPHA'] * (AVG_SPEED ** 2)) + (noxef_cars.loc[row,'BETA'] * AVG_SPEED) + noxef_cars.loc[row,'GAMMA'] + (noxef_cars.loc[row,'DELTA'] * math.log(AVG_SPEED)) + (noxef_cars.loc[row,'EPSILON'] * math.exp(noxef_cars.loc[row,'ZITA'] * AVG_SPEED)) + (noxef_cars.loc[row,'ITA'] * (AVG_SPEED ** noxef_cars.loc[row,'THITA']))) * (1 - noxef_cars.loc[row,'RF'])
        return(str(EF))

    def Petrol_Euro_1_to_6_NOx_EF(row):
        EF = ((noxef_cars.loc[row,'ALPHA'] + noxef_cars.loc[row,'GAMMA'] * AVG_SPEED + noxef_cars.loc[row,'EPSILON'] * AVG_SPEED  ** 2 + noxef_cars.loc[row,'ZITA'] / AVG_SPEED ) / (1 + noxef_cars.loc[row,'BETA'] * AVG_SPEED + noxef_cars.loc[row,'DELTA'] * AVG_SPEED ** 2)) * (1 - noxef_cars.loc[row,'RF'])
        return(str(EF))
        
### work on conditional location of row to feed into functon:
## next step: make variables for input and get function to run based on row back from conditional

#x = input("Input fuel type: ")
#y = input("Input Euro Standard: ")


# for i in range(0,len(noxef)):
# 	if (noxef.loc[i,'Euro standard'] == y) and (x in noxef.loc[i,'Fuel / Size']): 
# 		Diesel_Pre_Euro_NOx_EF(i) 

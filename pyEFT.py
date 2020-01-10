import pandas as pd
import numpy as np
import math

noxef = pd.read_excel("Copert5_NOx_EFs_Trimmed.xls", sheet_name = "Cars")

#print("Column headings:")
#print(noxef.columns)

## Column guide
## D = ALPHA
## E = BETA
## F = GAMMA
## G = DELTA
## H = EPSILON
## I = ZITA
## J = ITA
## K = THITA
## L = RF
## O9 = AVG_SPEED

# Excel g/km calculation
# AVG_SPEED = IF(AVG_SPEED_ALL < MIN_SPEED THEN AVG_SPEED_ALL,IF(AVG_SPEED_ALL>MAX_SPEED THEN MAX_SPEED, OTHERWISE AVG_SPEED_ALL))

# Diesel and Petrol: Pre-Euro NOx EF (g/km) = ((ALPHA * AVG_SPEED ^ 2) + (BETA * AVG_SPEED) + GAMMA + (DELTA * LOG(AVG_SPEED)) + (EPSILON * EXP(ZITA * AVG_SPEED)) + (ITA * (AVG_SPEED ^ THITA))) * (1 - RF)
# =(($D9 * $O9 ^ 2) + ($E9 * $O9) + $F9+ ($G9 * LOG($O9)) + ($H9 * EXP($I9 * $O9)) + ($J9 * ($O9 ^ $K9))) * (1 - $L9)

# Diesel: Euro 1 - 5 NOx EF & Petrol: Euro 1-6
# =(($D10 + $F10 * $O10 + $H10 * $O10 ^2 + $I10 / $O10 ) / (1 + $E10 * $O10 + $G10 * $O10 ^ 2)) * (1 - $L10)

# Diesel: Euro 6_1,6_2,6_3 EF
# =(D15*O15^2+E15*O15+F15+G15/O15)/(H15*O15^2+I15*O15+J15)*(1-L15)

AVG_SPEED = 30


def Diesel_Pre_Euro_NOx_EF(row): 
	EF = ((noxef.loc[row,'ALPHA'] * (AVG_SPEED ** 2)) + (noxef.loc[row,'BETA'] * AVG_SPEED) + noxef.loc[row,'GAMMA'] + (noxef.loc[row,'DELTA'] * math.log(AVG_SPEED)) + (noxef.loc[row,'EPSILON'] * math.exp(noxef.loc[row,'ZITA'] * AVG_SPEED)) + (noxef.loc[row,'ITA'] * (AVG_SPEED ** noxef.loc[row,'THITA']))) * (1 - noxef.loc[row,'RF'])
	print(EF)

def Diesel_Euro_1_to_5_NOx_EF(row):
	EF = ((noxef.loc[row,'ALPHA'] + noxef.loc[row,'GAMMA'] * AVG_SPEED + noxef.loc[row,'EPSILON'] * AVG_SPEED  ** 2 + noxef.loc[row,'ZITA'] / AVG_SPEED ) / (1 + noxef.loc[row,'BETA'] * AVG_SPEED + noxef.loc[row,'DELTA'] * AVG_SPEED ** 2)) * (1 - noxef.loc[row,'RF'])
	print(EF)

def Diesel_Euro_6_NOx_EF(row):
	EF =(noxef.loc[row,'ALPHA']*AVG_SPEED**2+noxef.loc[row,'BETA']*AVG_SPEED+noxef.loc[row,'GAMMA']+noxef.loc[row,'DELTA']/AVG_SPEED)/(noxef.loc[row,'EPSILON']*AVG_SPEED**2+noxef.loc[row,'ZITA']*AVG_SPEED+noxef.loc[row,'ITA'])*(1-noxef.loc[row,'RF'])
	print(EF)

def Petrol_Pre_Euro_NOx_EF(row):
	EF = ((noxef.loc[row,'ALPHA'] * (AVG_SPEED ** 2)) + (noxef.loc[row,'BETA'] * AVG_SPEED) + noxef.loc[row,'GAMMA'] + (noxef.loc[row,'DELTA'] * math.log(AVG_SPEED)) + (noxef.loc[row,'EPSILON'] * math.exp(noxef.loc[row,'ZITA'] * AVG_SPEED)) + (noxef.loc[row,'ITA'] * (AVG_SPEED ** noxef.loc[row,'THITA']))) * (1 - noxef.loc[row,'RF'])
	print(EF)

def Petrol_Euro_1_to_6_NOx_EF(row):
	EF = ((noxef.loc[row,'ALPHA'] + noxef.loc[row,'GAMMA'] * AVG_SPEED + noxef.loc[row,'EPSILON'] * AVG_SPEED  ** 2 + noxef.loc[row,'ZITA'] / AVG_SPEED ) / (1 + noxef.loc[row,'BETA'] * AVG_SPEED + noxef.loc[row,'DELTA'] * AVG_SPEED ** 2)) * (1 - noxef.loc[row,'RF'])
	print(EF)

### work on conditional location of row to feed into functon:

a = noxef.loc[0,'Fuel / Size']
b = 'Diesel <1,4 l'
c = 'Pre-Euro'

for i in range(0,len(noxef)):
	if (noxef.loc[i,'Euro standard'] == c) and ('Diesel' in noxef.loc[i,'Fuel / Size']): 
		print(i) 

noxef.loc[0,'Fuel / Size']

## function test
#Diesel_Pre_Euro_NOx_EF(0)



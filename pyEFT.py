import pandas as pd
import numpy as np
import math

noxef = pd.read_excel("Copert5_NOx_EFs_Trimmed.xls", sheet_name = "Cars")

#print("Column headings:")
#print(noxef.columns)

AVG_SPEED = 30

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

# Pre-Euro NOx EF (g/km) = ((ALPHA * AVG_SPEED ^ 2) + (BETA * AVG_SPEED) + GAMMA + (DELTA * LOG(AVG_SPEED)) + (EPSILON * EXP(ZITA * AVG_SPEED)) + (ITA * (AVG_SPEED ^ THITA))) * (1 - RF)
# =(($D9 * $O9 ^ 2) + ($E9 * $O9) + $F9+ ($G9 * LOG($O9)) + ($H9 * EXP($I9 * $O9)) + ($J9 * ($O9 ^ $K9))) * (1 - $L9)

# Euro 1 NOx EF
# =(($D10 + $F10 * $O10 + $H10 * $O10 ^2 + $I10 / $O10 ) / (1 + $E10 * $O10 + $G10 * $O10 ^ 2)) * (1 - $L10)

Pre_Euro_NOx_EF = ((noxef.loc[0,'ALPHA'] * (AVG_SPEED ** 2)) + (noxef.loc[0,'BETA'] * AVG_SPEED) + noxef.loc[0,'GAMMA'] + (noxef.loc[0,'DELTA'] * math.log(AVG_SPEED)) + (noxef.loc[0,'EPSILON'] * math.exp(noxef.loc[0,'ZITA'] * AVG_SPEED)) + (noxef.loc[0,'ITA'] * (AVG_SPEED ** noxef.loc[0,'THITA']))) * (1 - noxef.loc[0,'RF'])
Euro_1_NOx_EF = 


print((a + b + c + d + e * f) * g)
print(NOx_EF)



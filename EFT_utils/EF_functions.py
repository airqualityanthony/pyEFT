from .read_input_files import read_files
from .speed import Speed_function
import math

noxef_cars = read_files.read_cars()


class Car_EF_functions:
    def Diesel_Pre_Euro_NOx_EF(avg_speed,row): 
        EF = ((noxef_cars.loc[row,'ALPHA'] * (Speed_function.Speed(avg_speed,row) ** 2)) + (noxef_cars.loc[row,'BETA'] * Speed_function.Speed(avg_speed,row)) + noxef_cars.loc[row,'GAMMA'] + (noxef_cars.loc[row,'DELTA'] * math.log(Speed_function.Speed(avg_speed,row))) + (noxef_cars.loc[row,'EPSILON'] * math.exp(noxef_cars.loc[row,'ZITA'] * Speed_function.Speed(avg_speed,row))) + (noxef_cars.loc[row,'ITA'] * (Speed_function.Speed(avg_speed,row) ** noxef_cars.loc[row,'THITA']))) * (1 - noxef_cars.loc[row,'RF'])
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
from .read_input_files import read_files
from pyEFTUI import Ui_MainWindow

noxef_cars = read_files.read_cars()

class Speed_function:
    def Speed(avg_speed,row):
	    if noxef_cars.loc[row,'Min speed (km/h)'] > avg_speed:
	        SPEED = noxef_cars.loc[row,'Min speed (km/h)']
	    elif noxef_cars.loc[row,'Max speed (km/h)'] < avg_speed:
	        SPEED = noxef_cars.loc[row,'Max speed (km/h)']
	    else: 
	        SPEED = avg_speed
	    return(SPEED)

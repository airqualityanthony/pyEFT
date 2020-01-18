import pandas as pd
import xlrd
import os


class read_files:
	def read_cars():
		noxef_cars = pd.read_excel(r"input_files/rtp_Copert5_NOxEFs_final_trimmed.xlsx", sheet_name = "Cars")
		return(noxef_cars)
	def read_lgv():
		noxef_lgv = pd.read_excel(r"input_files/rtp_Copert5_NOxEFs_final_trimmed.xlsx", sheet_name = "LGVs")
		return(noxef_lgv)
	def read_hgv():	
		noxef_hgv = pd.read_excel(r"input_files/rtp_Copert5_NOxEFs_final_trimmed.xlsx", sheet_name = "HGVs & Buses")
		return(noxef_hgv)
	def read_mbike():	
		noxef_mbike = pd.read_excel(r"input_files/rtp_Copert5_NOxEFs_final_trimmed.xlsx", sheet_name = "Motorcycles")
		return(noxef_mbike)                            
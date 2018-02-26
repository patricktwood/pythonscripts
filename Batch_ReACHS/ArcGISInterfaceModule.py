###################################################################################
# ArcGIS Interface Module
# This module includes classes to interface with ArcGIS.
# The functions provide insulation from ArcGIS changes and provides friendlier error
# messages.
#
# OG Author: Jim Graham
# Date: 4th of November, 2011 
# Modified: March 20th, 2017
# By: Patrick T Wood
###################################################################################
import arcpy

arcpy.CheckOutExtension("Spatial") # make sure the spatial analyst is checked out
arcpy.env.overwriteOutput=True # allow overwrites

###########################################################################################
# ASPECT FUNCTION
###########################################################################################
def Aspect(InputFilePath,OutputFilePath): # perform aspect on a DEM and return it
    """
    Performs an aspect calculation using ArcGIS

    Inputs:
     - InputFilePath: The full path to the file to process
     - OutputFilePath: Full path to the file to save the results to
    """
    try:
        print("""
Processing Aspect Layer...
                """)            
        
        TheRaster=arcpy.sa.Aspect(InputFilePath) # Call ArcGIS to perform the aspect transform
        TheRaster.save(OutputFilePath)
        print("Complete")            

    except Exception, err: # an error occurred (probably in arcGIS)
        raise RuntimeError("** Error: Aspect Failed ("+str(err)+")")


###########################################################################################
# CONTOUR FUNCTION
###########################################################################################
def Contour(InputFilePath,OutputFilePath): # perform contour on a DEM and return it
    """
    Performs contour calculation using ArcGIS

    Inputs:
     - InputFilePath: The full path to the file to process
     - OutputFilePath: Full path to the file to save the results to
    """
    try:
        print("""
Processing Contour Layer...
                """)            

        TheRaster=arcpy.gp.Contour_sa(InputFilePath,OutputFilePath,"75","0","1")
        print("Complete")            

    except Exception, err: # an error occurred (probably in arcGIS)
        raise RuntimeError("** Error: Contour Failed ("+str(err)+")")



###########################################################################################
# HILLSHADE FUNCTION
###########################################################################################
def Hillshade(InputFilePath,OutputFilePath): # perform hillshade on a DEM and return it
    """
    Performs a hillshade calculation using ArcGIS
    
    Inputs:
     - InputFilePath: The full path to the file to process
     - OutputFilePath: Full path to the file to save the results to
    """
    try:
        print("""
Processing Hillshade Layer...
                """)            
        
        TheRaster=arcpy.sa.Hillshade(InputFilePath, 315, 45, 1)
        TheRaster.save(OutputFilePath)
        print("Complete")
        
    except Exception, err: # an error occurred (probably in arcGIS)
        raise RuntimeError("** Error: Hillshade Failed ("+str(err)+")")    


###########################################################################################
# PROJECT RASTER FUNCTION
###########################################################################################
def Projected(InputFilePath,OutputFilePath): # perform a reproject raster onto a DEM and return
    """
    Performs a ReProject Raster into a new coordinate system using ArcGIS
    
    Inputs:
    - InputFilePath: The full path to the file to process
     - OutputFilePath: Full path to the file to save the results to
    """
    try:
        print("""
Reprojecting Raster...
                """)            
        
        arcpy.ProjectRaster_management(in_raster=InputFilePath,out_raster=OutputFilePath,out_coor_system="PROJCS['NAD_1983_StatePlane_California_III_FIPS_0403',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',2000000.0],PARAMETER['False_Northing',500000.0],PARAMETER['Central_Meridian',-120.5],PARAMETER['Standard_Parallel_1',37.06666666666667],PARAMETER['Standard_Parallel_2',38.43333333333333],PARAMETER['Latitude_Of_Origin',36.5],UNIT['Meter',1.0]]",resampling_type="NEAREST",cell_size="27.8165597364916 27.8165597364914",geographic_transform="WGS_1984_(ITRF00)_To_NAD_1983",Registration_Point="#",in_coor_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
        print("Complete")
        
    except Exception, err: # an error occurred (probably in arcGIS)
        raise RuntimeError("** Error: Project Raster Failed ("+str(err)+")")    
    
    
    
###########################################################################################
# SLOPE FUNCTION
###########################################################################################
def Slope(InputFilePath,OutputFilePath): # perform a slope raster onto a DEM and return
    """
    Performs a slope calculation using ArcGIS
    
    - InputFilePath: The full path to the file to process
     - OutputFilePath: Full path to the file to save the results to
    
    """
    try:
        print("""
Processing Slope Layer...
                """)            
        
        
        arcpy.gp.Slope_sa(InputFilePath, OutputFilePath, "DEGREE", "1")        
        print("Complete")
        
    except Exception, err: # an error occurred (probably in arcGIS)
        raise RuntimeError("** Error: Slope Failed ("+str(err)+")")    
###########################################################################################
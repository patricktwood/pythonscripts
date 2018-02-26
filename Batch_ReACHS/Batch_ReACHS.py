###################################################################################
# Batch_ReACHS (Reproject, Aspect, Contour, Hillshade, Slope) Processing Script Created in Lab on March 7th, 2017
#
# Author: Patrick T Wood
# Date: 7th of March, 2017, Modified: March 20th, 2017
#
# Please read the READ ME File!
###################################################################################
import os
import arcpy
import ArcGISInterfaceModule

# Sets the InputPath and the OutputPath. Put all files that are to be processed in the Inputs folder!
InputPath="C:/Temp/Inputs/"
OutputPath="C:/Temp/Outputs/"

# Creates a list of all the files in the input folder
TheList=os.listdir(InputPath)

# Creates variables to get count information at the end.
InputCount=0
ProcessCount=0
ProjectCount=0
AspectCount=0
HillshadeCount=0
ContourCount=0
SlopeCount=0

print("""
*********************************************************
Batch Script Commencing...
*********************************************************
                """)            

# Beginning of Main Script!
# Goes through the created list from the input folder.
for TheFile in TheList:
    # breaks up the file name into pieces based on periods
    TheFileName, TheFileExtension = os.path.splitext(TheFile) #Split Ext - Splits the file name into two variables based on file name and file ext.

    # create the full path to the file using the variables from above^^
    InputFilePath=InputPath+TheFileName+TheFileExtension
    
    #Add ones to the InputCount
    InputCount=InputCount+1

    # determine if this is a file (not a directory), has just a name and extension, and the extension is "img" or "tif"
    if (TheFileExtension==".img") or (TheFileExtension==".tif"):
        # Aster DEM files from EarthExplorer are responsible for the next line of code:
        if "_num" not in TheFileName:
            print("""*******************
Found a file to process:"""+InputFilePath)
            
            ProcessCount=ProcessCount+1            
            
            # PROJECT RASTER TOOL
            ProjectedFile=OutputPath+TheFileName+"_Project"+TheFileExtension
            OutRaster=ArcGISInterfaceModule.Projected(InputFilePath,ProjectedFile)
            ProjectCount=ProjectCount+1            
            
            # ASPECT TOOL
            OutputAspectFilePath=OutputPath+TheFileName+"_Aspect"+TheFileExtension
            OutRaster=ArcGISInterfaceModule.Aspect(ProjectedFile,OutputAspectFilePath)
            AspectCount=AspectCount+1

            # HILLSHADE TOOL        
            OutputHillshadeFilePath=OutputPath+TheFileName+"_Hillshade"+TheFileExtension
            OutRaster=ArcGISInterfaceModule.Hillshade(ProjectedFile,OutputHillshadeFilePath)
            HillshadeCount=HillshadeCount+1
            
            # CONTOUR TOOL
            OutputContourFilePath=OutputPath+TheFileName+"_Contour.shp"
            OutContour=ArcGISInterfaceModule.Contour(ProjectedFile,OutputContourFilePath)            
            ContourCount=ContourCount+1
            
            # SLOPE TOOL
            OutputSlopeFilePath=OutputPath+TheFileName+"_Slope"+TheFileExtension
            OutRaster=ArcGISInterfaceModule.Slope(ProjectedFile,OutputSlopeFilePath)
            SlopeCount=SlopeCount+1
            
            print("""
Processing Complete for the file: """+TheFileName+"""
*******************

            """)            
            
                       
print("""
*********************************************************
Batch Script Complete

Files in the Input Folder: """+format(InputCount)+"""
Files Processed: """+format(ProcessCount)+""" 

Reproject Raster Layers Created: """+format(ProjectCount)+""" 
Aspect Layers Created: """+format(AspectCount)+""" 
Hillshade Layers Created: """+format(HillshadeCount)+"""
Contour Layers Created: """+format(ContourCount)+""" 
Slope Layers Created: """+format(SlopeCount)+"""

   Have a Good Day!
*********************************************************
""")
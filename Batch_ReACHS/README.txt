Read Me file for Batch_ReACHS (Reproject, Aspect, Contour, Hillshade, Slope) Processing folder by Patrick T Wood.
9th of March, 2017

This folder contains python scripts that can be used to batch process files using ArcPy.

The python script requires .tif or .img raster data to operate. 

The Python script will Reproject each raster into NAD 1983 State Plane California FIPS 0403.

Using the reprojected layers, the script will then also create an Aspect layer, a Contour layer, a Hillshade layer, and a Slope layer for each one.

The files to be processed need to be placed in a folder named Inputs in the Temp folder on the C Drive     [  "C:/Temp/Inputs/  ] 

A folder named Outputs needs to exist in the Temp folder on the C Drive.      [  "C:/Temp/Outputs/  ]

This python script was created for GSP 318 in Spring of 2017 at Humboldt State University.

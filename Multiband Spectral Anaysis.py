#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Annoop Shahhare (ashahhar)
#
# Created:     03/23/2016
# Copyright:   (c) ashahhar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import division
import arcpy
import numpy as np


def main():
    input_img = arcpy.GetParameterAsText(0)
    arr_Pixels = arcpy.RasterToNumPyArray(input_img)
#    arcpy.AddMessage("arr_Pixels: %s"  % str(arr_Pixels))
#    arcpy.AddMessage("arr_Pixels: %s"  % str(arr_Pixels.shape))
    size = arr_Pixels.shape
    nBands = size[0]
    row_size = size[1]
    col_size = size[2]
    neighborhood_size = int(arcpy.GetParameterAsText(1))  
    padding = neighborhood_size/2
#    arcpy.AddMessage("padding %d"  % padding  )
    mat_Final =np.array([[ 0 for c in range(col_size) ] for r in range(row_size)])
    i_name =  input_img.split(".")
    f_name = i_name[1]
    w= 10
#    arcpy.AddMessage("matrix_1: %s"  % str(matrix_1.shape))

    for r in range(0,row_size):                     ##row_size
        for c in range(0, col_size):                   ##
#            arcpy.AddMessage("[a][b]  11 %d"  % r  + " %d" %c)
            num = 1 
            temp_matrix =[[ 0 for x in range(neighborhood_size) ] for y in range(neighborhood_size)]
            for q in range(0, nBands):
                temp = arr_Pixels[q]
                temp = np.array(temp).astype(np.float32)
                temp = np.reshape(temp, (-1, col_size))
                
#                Handling the tif and images for bands and layers
                if f_name == "tif":
                    in_layer = "\Band_"+ str(num)
                if f_name == "img":
                    in_layer = "\Layer_"+ str(num)
#                in_layer = "\Layer_"+ str(num)
                num +=1
                desc = arcpy.Describe(input_img + str(in_layer))
#                arcpy.AddMessage("desc.noDataValue: %s"  % str(desc.noDataValue))  
                if desc.noDataValue == None:
                    noDataValue = -999.0
                else:
                    noDataValue = float(desc.noDataValue)
#                arcpy.AddMessage("padding %d"  % padding  )                
                pixels = np.pad(temp, (padding,padding), mode='constant', constant_values=(noDataValue, noDataValue))
#                arcpy.AddMessage("pixels: %s"  % str(pixels))                
#                arcpy.AddMessage("pixels: %s"  % str(pixels.shape))
                ngbh_matrix = [ [ 0 for k in range(neighborhood_size) ] for j in range(neighborhood_size) ]
                a=r
                for j in range(0, neighborhood_size): 
                    b=c 
                    for k in range(0,neighborhood_size):       
                        ngbh_matrix[j][k] = pixels[a][b]
                        b+=1
                    a+=1
#                arcpy.AddMessage("ngbh_matrix: %s"  % str(ngbh_matrix))        
                if np.amin(ngbh_matrix) == noDataValue:
                    min = np.amin(np.array(ngbh_matrix)[ngbh_matrix != np.amin(ngbh_matrix)])
                else:
                    min = np.amin(ngbh_matrix)
                if (np.amax(ngbh_matrix)) == noDataValue:
                    max = np.amax(np.array(ngbh_matrix)[ngbh_matrix != np.amax(ngbh_matrix)])
                else:
                    max = np.amax(ngbh_matrix)
#                arcpy.AddMessage("max and min: %f"  % min + " %f" % max)
                Centroid = (max + min)/2
                for j in range(0, neighborhood_size):
                    for k in range(0,neighborhood_size): 
#                        value  = ngbh_matrix[j][k]
                        if ngbh_matrix[j][k] != noDataValue:
                            dist = math.pow((Centroid - ngbh_matrix[j][k]),2)
                            temp_matrix[j][k] = temp_matrix[j][k] + float(dist)
                        else:
                            temp_matrix[j][k] = noDataValue
            sqrt_temp = np.sqrt(temp_matrix)
#            arcpy.AddMessage("temp_matrix: %s"  % str(temp_matrix ))
#            arcpy.AddMessage("sqrt_temp: %s"  % str(sqrt_temp ))
            count = 0
            addition =0
            for j in range(0,neighborhood_size):
                for k in range(0,neighborhood_size):
                    if all([sqrt_temp[j][k] != np.sqrt(noDataValue),  math.isnan(sqrt_temp[j][k]) == False])  :
#                        arcpy.AddMessage("sqrt_temp[j][k]: %s"  % str(sqrt_temp[j][k] ))
                        addition += sqrt_temp[j][k]
                        count +=1
#            arcpy.AddMessage("Count: %d"  % count + " Addition: %f" % addition)
            
#            value = addition/count
#            Handling if the count ==0
            try:
                value = addition/count
            except ValueError as e:
                arcpy.AddMessage("sqrt_temp: %s"  % str(sqrt_temp))
                arcpy.AddMessage("addition: %f"  % addition + " count:  %d" % count)
            except ZeroDivisionError as ze:
                arcpy.AddMessage("sqrt_temp: %s"  % str(sqrt_temp))
                arcpy.AddMessage("addition: %f"  % addition + " count:  %d" % count) 
                count =1
                value = addition/count
                
                
                
#            if count ==0:
#                
#                arcpy.AddMessage("sqrt_temp: %s"  % str(sqrt_temp))
#                arcpy.AddMessage("addition: %f"  % addition + " count:  %d" % count + "row number: %d" % row_size)
#                count =1
#                value = addition/count
#            else:
#                value = addition/count
#            arcpy.AddMessage("addition: %f"  % addition + " count:  %d" % count)
#            arcpy.AddMessage("value: %f"  % value )
            
            mat_Final[r][c] = int(value)
        
        if r >w:
            arcpy.AddMessage("Number of Rows Prcocessed: %d"  % r)     
            w +=10
#    arcpy.AddMessage("mat_Final: %s"  % str(mat_Final))    
    result_array = arcpy.NumPyArrayToRaster(mat_Final)
    result_img = arcpy.GetParameterAsText(2)
    result_array.save(result_img)
    
if __name__ == '__main__':
    main()
    
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Annoop Shahhare (ashahhar)
#
# Created:     03/15/2016
# Copyright:   (c) ashahhar 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from decimal import *
import arcpy
import numpy as np
import math

alpha_keys =[]
alpha_values =[]
shannon_list =[]
shan_pi= []

def alpha_func(Alpha):
    alpha_raster = arcpy.NumPyArrayToRaster(Alpha)
    alpha_img = arcpy.GetParameterAsText(3)
    alpha_raster.save(alpha_img)
         
def shannon_func(Shannon):
    shannon_raster = arcpy.NumPyArrayToRaster(Shannon)
    shannon_img = arcpy.GetParameterAsText(3)
    shannon_raster.save(shannon_img)
   
def main():
    input_img = arcpy.GetParameterAsText(0)
  
#    printing the array size and array of pixels
    arr_Pixels = arcpy.RasterToNumPyArray(input_img)
    size_arr_Pixels = arr_Pixels.shape
    row_size = size_arr_Pixels[0]
    col_size = size_arr_Pixels[1]

#   Create a Describe object from the raster dataset to get noDataValues
    desc = arcpy.Describe(input_img)
#    arcpy.AddMessage("noDataValue 1: %s"  % str(desc.noDataValue))
    if desc.noDataValue == None:
        noDataValue = -999.0
    else:
        noDataValue = float(desc.noDataValue)
 
#   Padding the original matrix       
    neighborhood_size = int(arcpy.GetParameterAsText(1))
    padding = neighborhood_size/2
    pixels = np.pad(arr_Pixels, (padding,padding), mode='constant', constant_values=(noDataValue, noDataValue ))
#    arcpy.AddMessage("pixels: %s"  % str(pixels))
#    arcpy.AddMessage("noDataValue 2: %s"  % str(noDataValue))
    new_matrix = [[ 0 for k in range(col_size) ] for l in range(row_size)]
    alpha_matrix = [[ 0 for k in range(col_size) ] for l in range(row_size)]
    shannon_matrix = [[ 0 for k in range(col_size) ] for l in range(row_size)]
    
    cnt =0
    index =0
    for i in range(0,row_size):
        for j in range(0,col_size):
            temp = [ [ 0 for k in range(neighborhood_size) ] for l in range(neighborhood_size) ]
            a=i
            dict_temp ={}
            for k in range(0, neighborhood_size): 
                b=j   
                for l in range(0,neighborhood_size):       
                    temp[k][l] = pixels[a][b]
                    b+=1
                    if temp[k][l] in dict_temp:
                        cnt = dict_temp.get(temp[k][l])
                        cnt =cnt+1
                        dict_temp.update({temp[k][l]:cnt})
                    else:
                        if temp[k][l]== noDataValue:
                            continue
                        else:
                            count = 0
                            count =count + 1
                            dict_temp.update({temp[k][l]:count})
                a+=1
            new_matrix[i][j] = temp
            alpha_keys.append(dict_temp.keys())
            alpha_values.append(dict_temp.values())
            addition =0
            add =0
            for m in range(len(alpha_values[index])):                
                addition =addition + alpha_values[index][m]
                add +=1
            alpha_matrix[i][j] = add
            shan_add = 0
            shan_multi = 0
            for m in range(len(alpha_values[index])):
                pi = float(alpha_values[index][m])/float(addition)
                shan_multi = float(pi)* float(math.log(pi))*(-1)
                shan_add = shan_add + shan_multi
                shan_pi.append(pi)
            index +=1
            shannon_matrix[i][j] = shan_add 

    Alpha = np.reshape(alpha_matrix, (-1, col_size))
    Shannon = np.reshape(shannon_matrix, (-1, col_size))
    
    input_func = arcpy.GetParameterAsText(2)
    if(input_func == "Alpha Diversity"):
        alpha_func(Alpha)
    if(input_func == "Shannon Diversity"):
        shannon_func(Shannon)

if __name__ == '__main__':
    main()
    

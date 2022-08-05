#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Omar Medhat Aly
# DATE CREATED: 04.08.2022                                 
# REVISED DATE: 04.08.2022
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    
    filename_list = listdir(image_dir)
    
    #empty dictionary at the beginning ,we'll store the values later
    results_dic = dict()
    
    #Note : MacOs files / Win files can start with ' . ' so we must ignore those files
    for idx in range( 0 , len(filename_list) , 1) :
        if filename_list[idx][0] != '.' :
            # we can safely go through the loop now !!
            #now create a variable pet_images to be able to compare files names 
            #the strings should be separeted with _ and all lower case
            pet_images = filename_list[idx].lower().split("_")
            
            #create a temp value acts as labels later
            # as long as it's a string therfore it will be equal to ""
            pet_label =""
            
            #loop over all pet_images files and check if they're only real files
            for i in pet_images:
                if i.isalpha():#means that the filename doesn't contain any numbers
                    pet_label += i + " "
                    
            #don't forget to easre the spaces
            pet_label = pet_label.strip()
            
            # If filename doesn't already exist in dictionary add it and it's
            # pet label - otherwise print an error message because indicates 
            # duplicate files (filenames)
            
            if filename_list[idx] not in results_dic:
                    results_dic[filename_list[idx]] = [pet_label]
            else:
                print("** Warning: Key=", filename_list[idx], 
               "already exists in results_dic with value =", 
               results_dic[filename_list[idx]])
    
            print("\nFilename=", filename_list[idx], "   Labfilename_list[idx]el=", pet_label)
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic

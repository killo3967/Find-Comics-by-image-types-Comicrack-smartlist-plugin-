#
#ComicsImageFilter.py
#
#Author: Tomas Platero
#
#Date: 22/06/2023
#
#Description:   This script create a filter for image file type inside comics files (smarlist)
#
#Versions: 1.0 
#
#ComicRack Declarations
#
#@Name  Books with images in format
#@Hook CreateBookList
#@Key WebpComic
#@Enabled true
#@List comics with "all OR any" pages in "JPG/JPEG/PNG/GIF/WEBP/AVIF/BMP" extension
#@PCount 2
#

import clr
import System, sys, os
import zipfile
import zlib
import datetime

#Debugging switches
debug = True
logging = True

def ComicsImageFilter(books,a,b):
    # Testing parameters
    if a not in ["all", "any"]:
        if debug:
            print("Invalid value for parameter 'a'. Setting it to 'any'.")
        a = "any"
    # List of trusted image extensions 
    image_extensions = ['.jpg', '.jpeg', '.gif', '.webp', '.png', '.avif', '.bmp']
    if  str("." + b) not in image_extensions: 
        if debug:
            print("Invalid value for second parameter. Setting it to 'jpg'.")
        b = "jpg"
    
    # Inicio
    if debug:
        print ("")    
        print ("          >>>>> Looking for comics in CBZ format, that " + a.upper() +  " of their images have the " + b.upper() + " extension. <<<<<<" )
    if logging:
        mensaje = "Looking for comics in CBZ format, that " + a.upper() +  " of their images have the " + b.upper() + " extension."
        generate_log_file( mensaje )
    # Create an empty list called lista_comics.
    lista_comics = []
    # Define a string variable called extension and set it to "."+b  parameter 
    extension = "." + b
    
    # Iterate through each book in the books list.
    for book in books:
        # Convert the file path of the book to unicode and store it in a variable called comic.
        comic = unicode(book.FilePath)
        # print ("FilePath: " + comic) # only for debug
        # Check if the book is a zip file using the is_zipfile method from the zipfile module.
        if zipfile.is_zipfile(comic):
            # If it is a zip file, open the zip file using the ZipFile method and iterate through each file in the zip file. 
            with zipfile.ZipFile(comic, 'r') as zip_file:
                match_condition = False
                # Iterates through a list of comics in cbz format
                for file_name in zip_file.namelist():
                    if not file_name.endswith('/'): # Exclude direcotries in the list 
                        # Only include image files previusly defined
                        file_extension = os.path.splitext(file_name)[1].lower()
                        if file_extension in image_extensions: 
                            if a == 'all': # all images "must" match. If one fail the comic is not included
                                if extension==file_extension: 
                                    match_condition = True
                                else:
                                    match_condition = False
                                    break
                            else: # at least one image must match to include the comic in the list
                                if extension==file_extension: 
                                    match_condition = True
                                else:
                                    match_condition = False
                                    break
            if match_condition==True:
                lista_comics.append(book)
                if debug:
                    print("Comic found: " + comic)
                    mensaje = "Comic found: " + comic
                if logging:
                    generate_log_file( mensaje )
                    
        else:
            # If the book is not a zip file, append the book to the lista_comics list.
            lista_comics.append(book)
            if debug:
                print ("Found comic not in CBZ format: " + comic)
   
    if not lista_comics:
        # No se ha encontrado ningun comic
        if debug:
            print("No comics found.")
    
    #Return the lista_comics list.
    if debug:
        print("Found " + str(len(lista_comics)) + " comics.")
        print ("          >>>>> FINSIH THE SCAN <<<<<")
        print ("")
    
    return lista_comics            


def generate_log_file(string):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ComicsImageFilter.log", "a") as log_file:
        log_file.write("{}: {}\n".format(timestamp, string))
        


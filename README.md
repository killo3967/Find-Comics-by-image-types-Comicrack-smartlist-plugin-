# Find Comics by image types in Comicrack smartlist plugin 
Plugin for Comicrack permit to create a smartlist to filter comics by image file types.

The script first imports necessary libraries and sets debugging and logging options. 
It then defines a function called ComicsImageFilter that takes three parameters: a list of books, and two string parameters 'a' and 'b'. 
The 'a' parameter can be either "all" or "any", and the 'b' parameter is the desired image file extension. 
 
The function iterates through each book in the list and checks if the book is a zip file. If it is, it opens the zip file and iterates through each file inside. 
It checks if the file is an image file with the specified extension. The smartlist has two paarameters 'a' and 'b'
The first ('a' parameter) could have two values "all" ot "any"
If the 'a' parameter is set to "all", all images in the comic must have the specified extension for the comic to be included in the list. 
If the 'a' parameter is set to "any", at least one image must have the specified extension for the comic to be included in the list. 

The second parameters is the extension of the image type and could be "jpg", "png", "bmp", "webp", "gif" and "avif".

With this and it's negation, you can create combinations for all the posibilities. 
 
In summary, this script helps users filter comic book files based on the image file types they contain.

Be carefull selecting a lot of comics, because this script unzip all of them and view the files inside. This could be a a hard process for your machine.

If you like to view what is doing, then start comicrack with "-ssc" option to open the console.

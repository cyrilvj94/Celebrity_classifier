##Step 1 : Scrapping
- All the files for scrapping is in Scrapping_files direcctory
- Scrapper.py contains
    * build_query: builds the query for the website
    * get_link(name , start_page, end_page): gets the image 
      links of name from start_page to end_page
    *get_image(links, name): saves the image in the directory

- scrapper_main.py : is the executable file which calls Scrapper.py.
.The names of the celebrity whose image is needed is given as list in `names`

- After executing scrapper.py the images are obtained in cwd.
in repective folders

 
 
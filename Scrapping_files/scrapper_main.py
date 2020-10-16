from Scrapper import *
import os

os.chdir('..') # Since the cwd is 'Scrapping_files'
names = ['sterling' ,'timo werner'] # enter the celb names needed in the list
directory = 'Dataset/Train_set/' # use 'Dataset/Train_set/' for train data  andd 'Dataset/Test_set/' for test data
for name in names:
    links = get_link(name,1 ,1)
    get_image(links, name, directory)
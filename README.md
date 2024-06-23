# Factly_DataCleaningTask
This Repository consists of the Task given to scrape the data from website sahitya akademi awards
and to perform the cleaning task
TO PERFORM SCRAPING


1.Install scrapy in your device
```sh
    pip install scrapy
```
2.we start the project by creating an scrapy project by using command
```sh 
    scrapy  startproject sahitya_akademi
```
3.In spiders folder you will find a python  file named `sahitya_akademi_spider` you can add
  code thier which consists of different parts like naming the spider parsing and output it
  into a file
4.Run the spider using command prompt from this command
```sh
   scrapy crawl sahitya_akademi
```
5. output will be saved in a file scapping.csv
6. after that craete an python file named as cleaning.py and i wrote the code which is essential
   to perform the task given and save it
7.run the file using command
```sh
   python cleaning.py
```
8. u will find that output will be saved into a file name cleaned_sahitya_akademi.csv there
9. That is our final output






a)The code for scraping task is in the folder Spiders named Sahitya_akademei_spider

b)the code for cleaning task is cleaning.py

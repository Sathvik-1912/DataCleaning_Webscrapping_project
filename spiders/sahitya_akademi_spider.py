import scrapy
import csv

class SahityaAkademiSpider(scrapy.Spider):
    name = "sahitya_akademi"
    start_urls = ['https://sahitya-akademi.gov.in/awards/akademi%20samman_suchi.jsp']

    def parse(self, response):
        # Find all the tables on the page
        tables = response.css('table')

        # Create a CSV writer
        with open('Scrapped_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write the header row
            writer.writerow(['year', 'book', 'author', 'language'])

            # Iterate over each table
            for table in tables:
                # Find the table name (e.g. "ASSAMESE")
                language = table.xpath('./preceding-sibling::center[1]//a[@class="midheader"]/text()').get()

                # Find all the rows in the table
                rows = table.css('tr')

                # Iterate over each row
                for row in rows:
                    # Find all the cells in the row
                    cells = row.css('td.matter')

                    # Check if the row contains data
                    if cells:
                        # Extract the data from each cell
                        year = cells[0].css('div p::text, div::text').get()
                        book = cells[1].css('div p::text, div::text').getall()
                        book = ' '.join(book)
                        author = cells[2].css('div p::text, div::text').getall()
                        author = ' '.join(author)

                        # Write the row to the CSV file with the table name
                        writer.writerow([ year, book, author, language])

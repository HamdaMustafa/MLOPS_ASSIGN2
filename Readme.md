Extraction and Preprocessing:

Data Extraction:
I utilized the requests library to make HTTP requests to the URLs of the two news websites. Then, leveraging the BeautifulSoup library, I parsed the HTML content of the web pages and extracted relevant information. Specifically, I targeted the titles and descriptions of articles by identifying the appropriate HTML tags (<h2> for titles and <p> for descriptions) using BeautifulSoup's find_all method.
Data Preprocessing:
Following the extraction of article titles and descriptions, I engaged in text preprocessing to ensure the cleanliness and standardization of the text data. This involved several key steps:
•	Converting all text to lowercase to ensure consistency.
•	Employing regular expressions to remove special characters, punctuation, and digits, thus cleaning the text.
•	Eliminating extra whitespace to normalize the text and enhance readability.
Challenges Encountered with DVC:
During the integration of DVC for versioning the extracted data, I faced challenges when attempting to utilize the DVC API (import dvc.api). Despite multiple troubleshooting attempts, including ensuring proper installation and configuration of the DVC module, I encountered difficulties in successfully utilizing the DVC API for versioning the data.
Resolution:
The issue was resolved by executing the commands in the PowerShell terminal with administrator privileges. This allowed for the successful integration and utilization of the DVC API for versioning the extracted data.

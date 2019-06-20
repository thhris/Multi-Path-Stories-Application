# Multi Path Stories Application Report 

### Requirements:

 * Python 2
 * Flask >= 1.0.2
 
### How to start:

 * Navigate to the /web-app folder using Terminal
 * Open the web-server.py with Python 2 : $ python2 web-server.py
 * Open a web browser and go to http://127.0.0.1:4000/index
 * Use Ctrl+C to close server when finished

### Pre-Production, design and implementation

Before starting to create the application, it is crucial to plan out the strategy for approaching the task. After weighing several options, I decided that the web app should be developed in Python using the Flask web framework.
My decision was based on the simplicity and flexability of Flask as it was able to achieve the expected requirements in a quick and smooth manner, and as well as having room to further extend the functionality of the application if needed based on further customer requirements.

###### The application consists of two files: 
 * A Python file that starts the web server at port 4000 and handles all information on the client's browser.
 * HTML file that displays the web page buttons, table and hiperlinks for each story.

###### The HTML file (webpage.html)

The HTML file contains the usual header, name and displays two main components in the body: a link that returns the user back to the index page and a 3x3 grid where each cell that should contain relevant information has a page id, position, a text area and a submit button. Once the cell has a page id associated with it, the cell only contains a hiperlink based on its page id. The only cell that is excluded from this rule is the middle cell which only displays the sentence for the particular page's id.

###### Server application (web-server.py)

 The server application uses the Flask web driver to handle most backend taks. The module contains well commented methods for creating a unique dictionary of sentences for each page, creating unique 6 string alphanumerical IDs for each new pages and a way to link pages to one another, which is achieved by a dictionary of pages. The application creates an initial dictionary with index page sentence and all sentences around it set to null. The application then relies on Flask to render and display the correct sentence in the correct cell of the table.

### Implications of shortcuts taken 

The applcation is lacking proper styling and formatting. Using CSS inside the HTML tags I have set the cell width, but words are not centered and I am not wrapping the text and as such, long sentences stretch the table instead of fitting the cell. 

The lack of a favicon on the web application caused it to throw exceptions in its stack trace. This made debugging more difficult. To combat this issue I passed an empty link as an icon in the HTML file which is not a favorable solution, but stopped the errors in the stack so I could proceed.

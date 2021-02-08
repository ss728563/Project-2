## Project-2

The aim of this project was to create a makeup dashboard that incorporates both back-end data access and front-end visualization. In order to create this, the following was done:

# Back-End
  - In Jupyter Notebook, web scrapper was created with beautifulsoup and splinter to scrape bestselling producct urls from Ulta.com within 4 categories: foundation, eyeshadow,         lipstick, and blush
    - These urls were then scrapped for the following product information: brand name, product name, price, rating, and image URL
    - Scrapped information was appended to a list then transformed into a dictionary
  - Using the dictionary, a Mongo database was created
  - A Flask app was created with routes that returned jsonified data
    - Home route returned all data within the database
    - Four other routes were created that filtered the data by category
  
 # Front-End
  - HTML page was created with CSS style to hold our visualization
    - Buttons with Javascript on-click function coded in the navbar that allows for filtering data by category
    - Empty graph and product panel div coded to be filled
  - Jinja2 was utilized in the HTML to link the variable created from our Flask app
  - A Javascript app was created that connected the Flask app routes to our html
    - Using D3 library, function created to create scatterplot based on data accessed
    - Using jQuery, function created to pull JSON data from different routes depending on button pressed
  - Within D3 function, circlegroup function created to fill panel product HTML depending on which product circle is clicked.
   

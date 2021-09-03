# Jobscraper
My second major project, a webscraper!

The idea behind the project is to practice the automated process of job-searching through the construction of a webscraper in Python.
The webscraper is iterating through 49 pages of a swedish jobsite. In each iteration, a text-file is created containing:
- The title of the job advertisement 
- The name of the company and the location
- The employment type (part-time or full-time)
- The URL-link to the ad

All text files are concatenated into a single file during the process, with a clear structure and spacing between the different ads.
Filtration is done based on lacking skill and experience that the applicant may have, which is advertised in the title of the ads.
The whole codeblock is placed within a function, which is then called within a timer so that the webscraper runs every 100 seconds.


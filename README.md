# FSecureAssignment
This repository contains python assignment for FSecure Test Automation Role

Problem Statement:

Implement a program, preferably using Python or Kotlin, that monitors web sites and reports their availability. This tool is intended as a monitoring tool for web site administrators for detecting problems on their sites.

##Main functions:
1. Reads a list of web pages (HTTP URLs) and corresponding page content requirements from a configuration file.
2. Periodically makes an HTTP request to each page.
3. Verifies that the page content received from the server matches the content requirements.
4. Measures the time it took for the web server to complete the whole request.
5. Writes a log file that shows the progress of the periodic checks.
6. (Optional) Implement a single-page HTTP server interface in the same process that shows (HTML) each monitored web site and their current (last check) status.


## Prerequisite

1. Clone this project to your workspace or download a zip file and extract it
2. Install requirements.txt file containing all python libraries
    pip install -r requirements.txt
3. Run monitor.py file on command prompt or run button from any editor.
    python3 monitor.py

### Project Structure

* data - contain site_lists.py file which include URLs and content requirements for respective web site
* libs - 
    * filters.py - applies the filter to requests and response
    * log_writer.py - appends the log statements with information like
                  1. Request/Response of the URL
                  2. If any anamolies found in the response
                  3. timestamp of start and end of requests
    * requests.py - module for sending requests in loop
    * response.py - Class type of ResponseInformation with http response data
    * logs - contains monitor_log file
* config.py - contains checking_period, flag for content_req
* monitor.py - the main application for running the httprequests continuosly
* requirements.txt - contains pip libraries being used

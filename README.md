# mlab_demo

Demonstration of accessing an mlab.com MongoDB database from Python code
(separate from a web app).

This demonstration uses JSON data from the [CORGIS project](https://think.cs.vt.edu/corgis/).

Specifically, we use the [food_access.json](https://think.cs.vt.edu/corgis/json/food_access/food_access.html) dataset.

There are three Python files:


* `food_access.py` contains methods for reading the JSON data in
    `food_access.json`, and demonstrates a few computations that can
    be done over the data.   These are not necessarily the most interesting computations&mdash;they are simply examples.
    
* `upload_json_data_to_mongodb.py` demonstrates how to store the JSON data
   in an mlab document.
   
* `get_json_data_from_mongodb.py` demonstrates how to retrieve the data
   from an mlab document, and then do computations on it (importing the
   functions from `food_access.py`

Note that the database access methods require database credentials to
be defined in environment variables.   The file env.sh.EXAMPLE shows how
to define these.   You should copy this to a file called env.sh (which is `.gitignore`d) before editing it.  Use `. env.sh` to run the file and define the variables it contains in your shell.






# csvImporter

Welcome to a Django CSV importer demonstrated with simple models. CSVs are read using python and rows are transformed into model objects using Django's built in get_or_create.

### Demo

*Demo is taken from another project with substancially more data. The importer for the other project uses the same structure.*

![Demo from shell](https://github.com/bradster45/csvImporter/blob/master/csv_importer/public/static/images/shell.JPG)

Run time was ~7 minutes when hitting the get case of the get_or_create. When hitting the create (fresh database) run time was ~45 minutes. It made ~14k database requests.

### The code

CSVs for import are located [here](https://github.com/bradster45/csvImporter/tree/master/csv_importer/public/csvs) with dummy data.

Python import code is located [here](https://github.com/bradster45/csvImporter/blob/master/csv_importer/public/importer.py), in the run() function. One by one it opens the CSVs, constructs the Django objects and creates them. This must happen in the right order to create any relationships. I.e. Page has an FK to Article, so an Article must be created before it can be referenced in the relationship to Page.
 

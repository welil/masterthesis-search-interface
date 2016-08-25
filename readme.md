The masterthesis-search-interface is an Elasticsearch Searchinterface for Campaign Metadata.
It includes a faceted search for the metadata as well as an autocomplete- and a term-highlight-functionality
to simplify search for the user.

## Installation

### Python

Install all dependencies as defined in requirements.txt e.g.

    pip install -r requirements.txt

or create a virtual environment.


### Elasticsearch

Create the index and load some data

    python es/helper/create_index.py ~/Desktop/elasticsearch-2.1.1/linksJSON.json

Example of a linksJSON file with one entry:

    {"create":{ "_index": "links", "_type": "link"}}
    {"CreatedLinkID":"1542746","UniqueLinkId":"abc","CreatedOn":"01.04.2014 15:41:51","Target URL":"github.com/","Brand":"github","Campaign Name":"Github new search","Topic":"Search","Subtopic":"ES","Media Spendings":"yes","Placement Type":"Search Engine","Placement Name":"Google","Ad Format":"Text Ad","Ad Group":"Search","Payment Type":"Performance","Date from":"01.01.2014","Date to":"31.12.2014"}

## Search Interface

Start the application with

    python server.py

The server.py file includes the application routes that render the templates.

### Package ES

The ES package includes definitions, the index mapping, utils, helpers and performance tests.
The definitions define the facets for the faceted search and the fields that should be searched in the fulltext search.
The index mapping specifies the mapping for the index fields.
The utils contains functions used in server.py:  get_results, filter_on_date, filter_on_clicked_checkboxes,
sort_results, get_suggestions and get_completions.
The helper-package includes functions for creating the index and producing more random links by duplicating an existing
link-file.
The performance test file performs a query 100 times and returns the individually measured response times as well as the
mean value, the maximum and the minimum.

### Package Frontend

The Frontend package includes all css files, the templates for displaying the interface and the javascript files.
The functions.js includes the Ajax-Calls for loading new data, the search_state.js includes the search-history-functions.
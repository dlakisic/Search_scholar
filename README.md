# README for Google Scholar Search Tool

## Overview

This repository contains a Python script for searching academic papers and publications via Google Scholar using the `scholarly` Python library. The script provides an efficient way to query Google Scholar and retrieve relevant academic information, including titles, authors, abstracts, and citation counts. It features caching to improve performance and reduce redundant queries.

## Features

- **Google Scholar Integration**: Leverages the `scholarly` library to search Google Scholar.
- **Proxy Support**: Includes a proxy setup to bypass any potential access restrictions on Google Scholar. You might want to adapt the proxy used : https://scholarly.readthedocs.io/en/stable/ProxyGenerator.html
- **Query Normalization**: Processes and normalizes queries for more effective searching.
- **Caching Mechanism**: Implements caching to store and retrieve previous search results, reducing redundant server requests and speeding up retrieval.
- **Customizable Search Results**: Allows specifying the maximum number of results to return.

## Requirements

- Python 3.x
- `scholarly` Python library
- Internet access for fetching results from Google Scholar

## Installation

To set up this tool, clone the repository and install the required dependencies.

```bash
git clone https://github.com/dlakisic/Search_scholar.git
cd ./Search_scholar
pip install -r requirements.txt
```
## Usage
To use the script, import the search_scholar function and call it with your search query.

```python
from Search_scholar import search_scholar

query = "your search query"
results = search_scholar(query, max_results=5)
# Process the results as needed
```

## Function Documentation

search_scholar(query, max_results=10): Searches Google Scholar with the given query and returns a list of dictionaries, each representing a publication.

## Contributing

Contributions to improve the script or extend its functionality are welcome. Please follow the standard pull request process for contributions.

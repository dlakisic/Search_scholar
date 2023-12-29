from scholarly import scholarly, ProxyGenerator
import os
import re
import json
import hashlib

def search_scholar(query, max_results=10):
    """
    Searches Google Scholar for the given query using the scholarly library, then returns the search results.
    Args:
        query (str): The search query.
        max_results (int, optional): The maximum number of search results to return. Defaults to 10.
    Returns:
        search_results (list): A list of dictionaries. Each dictionary contains fields such as 'title', 'authors', 'abstract', 'eprint', and 'num_citations'
    """
    
    # Set up a ProxyGenerator object and use it to set up a proxy for scholarly
    pg = ProxyGenerator()
    success = pg.FreeProxies()
    if not success:
        raise ConnectionError("Could not configure a proxy for scholarly.")
    scholarly.use_proxy(pg)
    
    # Normalize the query, removing operator keywords
    query = re.sub(r"[^\s\w]", " ", query.lower())
    query = re.sub(r"\s(and|or|not)\s", " ", " " + query + " ")
    query = re.sub(r"\s+", " ", query).strip()
    
    # Generate a unique file name for caching based on the query and max results
    key = hashlib.md5(("search_scholar(" + str(max_results) + ")" + query).encode("utf-8")).hexdigest()
    cache_dir = ".cache"
    if not os.path.isdir(cache_dir):
        os.mkdir(cache_dir)
    fname = os.path.join(cache_dir, key + ".cache")

    # Check if we have a cache hit, if so, return the cached results
    if os.path.isfile(fname):
        with open(fname, "r", encoding="utf-8") as fh:
            return json.load(fh)

    # Fetch results from Google Scholar
    search_query = scholarly.search_pubs(query)
    search_results = []
    for i, pub in enumerate(search_query):
        if i >= max_results:
            break
        search_results.append({
            'title': pub['bib']['title'],
            'authors': pub['bib']['author'],
            'abstract': pub['bib'].get('abstract', ''),
            'eprint': pub.get('eprint_url', ''),
            'num_citations': pub.get('num_citations', 0)
        })

    # Cache the results
    with open(fname, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(search_results))

    return search_results

# Example usage
query = "artificial intelligence in advertising"
results = search_scholar(query, max_results=5)

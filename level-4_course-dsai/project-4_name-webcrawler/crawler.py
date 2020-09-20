# Created 7/2/2020 by Benjamin Velie (veliebm@gmail.com).
"""
Visits all links on a website to map its structure.

Summary
-------
This is a website crawler. It completely maps the input website then stores
 the structure in a file named "structure.txt".

"""

import argparse
import requests
import re

# This is where we will store the nodes and edges we find.
graph_fetus_filename = "graph_fetus.txt"


def main():
    # Clear the files where we'll store the urls we find.
    open(graph_fetus_filename, "w").close()

    # Get target website using argument variables.
    parser = argparse.ArgumentParser(description="Visits all links on a website to map its structure.")
    parser.add_argument("website", type=str, help="The website to crawl. Must start with 'https://' or 'http://'.")
    parser.add_argument("--exclude", type=str, nargs='*', help="All the URLs you want to blacklist.")
    arguments = parser.parse_args()
    target_website = arguments.website
    excluded_url_list = arguments.exclude
    print(f"Crawling {target_website}.")

    # Call recursive crawler function on the target website.
    url_children = get_url_children(target_website, excluded_url_list)
    print("Got URL children.")
    output_nodes_and_edges(target_website, url_children)


def crawl(target_url, excluded_url_list):
    url_children = get_url_children(target_url, excluded_url_list)
    
    
    pass


def output_nodes_and_edges(parent_url: str, child_url_list: list):
    """Write a parent URL and its children to a file to use in our graph."""

    with open(graph_fetus_filename, "a") as graph_fetus:
        graph_fetus.write(f"{parent_url} ")
        for url in child_url_list:
            graph_fetus.write(f"{url} ")
        graph_fetus.write("\n")


def exclude_urls(url_list: list, excluded_url_list: list) -> list:
    """Returns the given URL list with the excluded URLs removed."""

    trimmed_url_list = []
    for url in url_list:
        if excluded_url_list:
            if url not in excluded_url_list:
                trimmed_url_list.append(url)
        else:
            trimmed_url_list.append(url)

    return trimmed_url_list


def get_url_children(target_url: str, excluded_url_list: list) -> list:
    """Outputs a list of URLs on the target page."""

    # Store the HTML data of the target URL.
    url_contents = requests.get(target_url).text

    # Use a regular expression to get a list of all URLs in the HTML data.
    regex = r"""(?<=href=[\"'])         # URL must be preceded by href= and a string beginning
                .+?                     # Any characters
                (?=[\"'])"""            # URL ends once we find a string end
    url_list = re.findall(regex, url_contents, re.VERBOSE)

    return url_list


if __name__ == "__main__":
    main()

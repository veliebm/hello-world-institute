"""
Visits all links on a website to map its structure.

Summary
-------
This is a website crawler. It completely maps the input website then stores
the structure in a file named "graph_fetus.txt".


Created 7/2/2020 by Ben Velie.
veliebm@gmail.com

"""

import argparse
import re
import requests


# This is where we will write the nodes and edges we find.
GRAPH_FILENAME = "graph_fetus.txt"

class Crawler():

    def __init__(self, website, excluded_urls):
        """
        Crawls the selected website and recursively stores the structure of all child URLS.

        """

        self.root = website
        self.excluded_urls = excluded_urls


    def __repr__(self):
        """
        Sets how the object represents itself as a string internally.

        """

        return f"Crawler({self.root}, excluded_urls={self.excluded_urls})"


    def crawl(website):
        """
        Recursively crawls the input website.

        """

        pass


    def get_children(self, website):
        """
        Finds all URLs on the target website.

        Doesn't return URLs excluded at the object attribute level.


        Parameters
        ----------
        website : str
            Target website to search.
        

        Returns
        -------
        set
            Websites found in the search.

        """

        # Store the HTML data of the target URL.
        url_contents = requests.get(website).text

        # Use a regular expression to get a list of all URLs in the HTML data.
        regex = r"""(?<=href=[\"'])         # URL must be preceded by href= and a string beginning
                    https?://.+?            # http and any other characters
                    (?=[\"'])"""            # URL ends once we find a string end
        url_list = re.findall(regex, url_contents, re.VERBOSE)

        return {url for url in url_list if url not in self.excluded_urls}


if __name__ == "__main__":
    """
    Empower the user to use the program from the command line.

    """

    parser = argparse.ArgumentParser(description="Visits all links on a website to map its structure.")

    parser.add_argument(
        "website",
        type=str,
        help="The website to crawl. It must start with 'https://' or 'http://'."
    )

    parser.add_argument(
        "--exclude",
        "-e",
        type=str,
        nargs='+',
        metavar="WEBSITE",
        help="All the URLs you want to blacklist."
    )

    args = parser.parse_args()
    
    Crawler(args.website, args.exclude)
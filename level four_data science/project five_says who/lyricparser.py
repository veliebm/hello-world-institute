"""
This class parses lyrics.txt and provides tools to clean it up.

Created 8/20/2020 by Benjamin Velie.
veliebm@gmail.com
"""

import pathlib
import nltk.stem

class LyricParser():
    """
    This class parses lyrics.txt and provides useful tools to analyze it.

    Parameters
    ----------
    input_path : str, Path
        Path to the lyrics file.

    ...

    Attributes
    ----------
    path : Path
        Path to the lyrics file.
    taylor : list of strings
        List of all PREPROCESSED lyrics in the file for Taylor Swift.
    beatles : list of strings
        List of all PREPROCESSED lyrics in the file for the Beatles.
    """

    def __init__(self, input_path):

        self.path = pathlib.Path(input_path)

        self.taylor = self.lyrics("taylor_swift")
        self.beatles = self.lyrics("the_beatles")

    
    def lyrics(self, artist):
        """
        Returns a list of all lyrics from the text file for an artist.
        """

        # Get raw, unedited lyrics for the artist.
        lines = self.path.read_text().splitlines()
        raw_lyrics = [line.split("\t")[1] for line in lines if artist in line]

        # Remove caps and punctuation
        depunctuated_lowercased_lyrics = [self._depunctuate(lyric).lower() for lyric in raw_lyrics]    

        # Destem the words.
        stemmer = nltk.stem.PorterStemmer()
        stemmed_lyrics = [stemmer.stem(lyric) for lyric in depunctuated_lowercased_lyrics]

        return stemmed_lyrics


    def _depunctuate(self, lyric: str) -> str:
        """
        Removes unwanted punctuation from a lyric.
        """

        unwanted_punctuation = r"\"\\!@#$%^&*()_=+][{},./?':"

        for character in unwanted_punctuation:
            lyric = lyric.replace(character, "")

        return lyric
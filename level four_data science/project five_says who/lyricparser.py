"""
This class parses lyrics.txt and provides tools to clean it up.

Created 8/20/2020 by Benjamin Velie.
veliebm@gmail.com
"""

import pathlib
import nltk.stem
import sklearn


class LyricParser():
    """
    This class parses lyrics.txt and provides useful tools to analyze it.

    For preprocessing, the class depunctuates, lowercases, and stemifies the lyrics.


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
    taylor_train, beatles_train : list of strings
        Training data for an AI, each encompassing 80% of the initial datasets.
    taylor_dev, beatles_dev : list of strings
        Dev data for an AI, each encompassing 10% of the initial datasets.
    taylor_test, beatles_test : list of strings
        Test data for an AI, each encompassing 10% of the initial datasets.
    """

    def __init__(self, input_path):

        self.path = pathlib.Path(input_path)

        self.taylor = self.lyrics("taylor_swift")
        self.beatles = self.lyrics("the_beatles")

        self.taylor_train, self.taylor_dev, self.taylor_test = self.split(self.taylor)
        self.beatles_train, self.beatles_dev, self.beatles_test = self.split(self.beatles)
        
    
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


    def split(self, sequence):
        """
        Returns a training set, a dev set, and a test set for the input sequence of data.

        Allowed inputs are lists, numpy arrays, scipy-sparse matrices or pandas dataframes.
        Training set encompasses 80% of the data, and the dev and test set each encompass 10% of the data.
        """

        training, dev_test = sklearn.model_selection.train_test_split(sequence, train_size=.8)

        dev, test = sklearn.model_selection.train_test_split(dev_test, test_size=.5)

        return training, dev, test


    def _depunctuate(self, lyric: str) -> str:
        """
        Removes unwanted punctuation from a lyric.
        """

        unwanted_punctuation = r"\"\\!@#$%^&*()_=+][{},./?':"

        for character in unwanted_punctuation:
            lyric = lyric.replace(character, "")

        return lyric
#!C:\Users\Ben\miniconda3\envs\helloworld\python.exe

"""
This class parses lyrics.txt and provides tools to clean it up.

Created 8/20/2020 by Benjamin Velie.
veliebm@gmail.com
"""

import pathlib
import nltk.stem
import sklearn
import pandas


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
    taylor : DataFrame of strings
        DataFrame of all PREPROCESSED lyrics in the file for Taylor Swift.
    beatles : DataFrame of strings
        DataFrame of all PREPROCESSED lyrics in the file for the Beatles.
    """

    def __init__(self, input_path):

        self.path = pathlib.Path(input_path)

        self.taylor = self.lyrics("taylor_swift")
        self.beatles = self.lyrics("the_beatles")

        self.taylor_train_dev, self.taylor_test = self.split(self.taylor)
        self.beatles_train_dev, self.beatles_test = self.split(self.beatles)

    
    def lyrics(self, artist):
        """
        Returns a dataframe of all lyrics from the text file for an artist.
        """

        # Get raw, unedited lyrics for the artist.
        lines = self.path.read_text().splitlines()
        raw_lyrics = [line.split("\t")[1] for line in lines if artist in line]

        # Remove caps and punctuation
        depunctuated_lowercased_lyrics = [self._depunctuate(lyric).lower() for lyric in raw_lyrics]    

        # Destem the words.
        stemmer = nltk.stem.PorterStemmer()
        stemmed_lyrics = [stemmer.stem(lyric) for lyric in depunctuated_lowercased_lyrics]

        return pandas.DataFrame(stemmed_lyrics)


    def split(self, sequence) -> tuple:
        """
        Returns a mixed training/dev set, and a test set for the input sequence of data.

        Allowed inputs are lists, numpy arrays, scipy-sparse matrices or pandas dataframes.
        Training/dev set encompasses 90% of the data, and test set encompasses 10% of the data.
        """

        training_dev, test = sklearn.model_selection.train_test_split(sequence, random_state=1, train_size=.9)

        return training_dev, test


    def cross_validate(self, dataframe):
        """
        Returns a dataframe of 10 cross-validated training/dev datasets for the given DataFrame dataset.
        """

        # Get the INDICES of the data split into split_datasets, a DataFrame.
        cross_validator = sklearn.model_selection.KFold(n_splits=10, random_state=1, shuffle=True)
        split_datasets = pandas.DataFrame(cross_validator.split(dataframe), columns=("training", "dev"))

        for column_name in split_datasets:
            column = split_datasets[column_name]
            for row in column:
                indices = row
                row = self._replace_indices(indices, list(dataframe))
        
        return split_datasets


    def _depunctuate(self, lyric: str) -> str:
        """
        Removes unwanted punctuation from a lyric.
        """

        unwanted_punctuation = r"\"\\!@#$%^&*()_=+][{},./?':"

        for character in unwanted_punctuation:
            lyric = lyric.replace(character, "")

        return lyric


    def _replace_indices(self, indices, input_list):
        """
        Given a list of indices, return list of all objects at those indices in the input list.
        """

        return [input_list[i] for i in indices]


parser = LyricParser(r"level four_data science\project five_says who\lyrics.txt")
parser.cross_validate(parser.taylor_train_dev)
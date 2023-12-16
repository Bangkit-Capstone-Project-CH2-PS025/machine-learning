# Packages
from tensorflow.keras.preprocessing.text import Tokenizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

class TextPreprocessing():
  def __init__(self, data, city):
    """
    Initialize TextPreprocessing class.

    Parameters:
    - data (dict): Dictionary containing dataset for different cities.
    - city (str): The city to be processed within the data.
    """
    self.data = data
    self.city = city
    self.column = 'metadata'

  def stemming(self):
    """
    Preprocess the corpus with stemming.

    Returns:
    - list: A list of stemmed documents.
    """
    stemmed_documents = []
    # Define the corpus
    corpus = self.data[self.city][self.column]
    # Preprocessing with stopword before stemming
    stopword_factory = StopWordRemoverFactory()
    remover = stopword_factory.create_stop_word_remover()
    # Stemming the stopword
    stemming_factory = StemmerFactory()
    stemmer = stemming_factory.create_stemmer()
    # append the cleaned text with stopword and stemming
    for doc in corpus:
      stemmed_doc = [stemmer.stem(word) for word in doc.split()]
      cleaned_text = remover.remove(' '.join(stemmed_doc))
      stemmed_documents.append(cleaned_text)
    return stemmed_documents

  def tokenizer(self, stemmed_documents):
    """
    Preprocess the stemmed corpus with a tokenizer.

    Parameters:
    - stemmed_documents (list): A list of preprocessed documents after stemming.

    Returns:
    - dict: Updated datasets containing tokenized strings.
    - list: A list of tokenized strings.
    """
    num_words = None
    oov_tok = "<OOV>"
    lower=True
    char_level = False
    filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    # Define the tokenizer
    tokenizer = Tokenizer(num_words=num_words,
                          filters=filters,
                          oov_token=oov_tok,
                          lower=lower,
                          char_level=char_level)
    # Fit tokenizer on stemmed documents
    tokenizer.fit_on_texts(stemmed_documents)
    # Tokenized texts to sequences
    tokenized_texts = tokenizer.texts_to_sequences(stemmed_documents)
    # Tokenized sequences to texts
    self.tokenized_strings = tokenizer.sequences_to_texts(tokenized_texts)
    # Create column 'metadata_tokenized' on the dataset
    self.data[self.city]['metadata_tokenized'] = self.tokenized_strings
    return self.data, self.tokenized_strings
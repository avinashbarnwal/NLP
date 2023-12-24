## NLP

### Learning NLP Systematically

#### Link
- https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/discussion/91432#latest-636275

### Word2Vec

#### Link
- https://towardsdatascience.com/an-implementation-guide-to-word2vec-using-numpy-and-google-sheets-13445eebd281

#### Classification using BERT
- https://www.kaggle.com/anushakarthik1991/nlp-with-disaster-tweets-eda-cleaning-and-bert

#### Multilabel
- https://towardsdatascience.com/journey-to-the-center-of-multi-label-classification-384c40229bff

#### BERT

- Question Answering (SQuAD v1.1),
- Natural Language Inference (MNLI)
- NER Modeling

#### How to use BERT (Fine-tuning)
Using BERT for a specific task is relatively straightforward:
- BERT can be used for a wide variety of language tasks, while only adding a small layer to the core model:
Classification tasks such as sentiment analysis are done similarly to Next Sentence classification, by adding a classification layer on top of the Transformer output for the [CLS] token.
- In Question Answering tasks (e.g. SQuAD v1.1), the software receives a question regarding a text sequence and is required to mark the answer in the sequence. Using BERT, a Q&A model can be trained by learning two extra vectors that mark the beginning and the end of the answer.
- In Named Entity Recognition (NER), the software receives a text sequence and is required to mark the various types of entities (Person, Organization, Date, etc) that appear in the text. Using BERT, a NER model can be trained by feeding the output vector of each token into a classification layer that predicts the NER label.

#### ROC-Star

- https://github.com/iridiumblue/roc-star/blob/master/README.md

#### LLM
- https://www.manning.com/books/build-a-large-language-model-from-scratch

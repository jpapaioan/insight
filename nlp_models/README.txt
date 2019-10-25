contains all of the jupyter notebooks where I analyzed and tested NLP techniques on data sets I webscraped

comedy_works_EDA.ipynb contains exploratory data analysis of the comedy works comedian bios

feature_experimentation.ipynb contains initial exploration of using reading level measures to distinguish smart/witty comedy from silly/absurd/irreverant comedy, and LDA topic modeling using bag-of-words and TF-IDF, importantly this is also where I tested profanity checker and binned comedians into PG, PG-13, and R categories based on their profanity ratio

word_sentence_embedding_test.ipynb is an exploration of word2vec embeddings and similarity measures and testing the initial idea of a similarity autocorrelation

joke_form_analysis.ipynb contains all of the functions needed for assessing whether a comedian is short or long form, cleaning, preprocessing, word2vec embeddings, similarity autocorrelation, and ensemble averaged random shuffled similarities to get a baseline similarity for each comedian

feature_merge.ipynb takes the content rating and joke form series from previous data frames and combines them and cleans up the culminating dataframe for use in the webapp

data_visuals.ipynb uses seaborn to plot some visuals of the joke form distributions

validation_metrics.ipynb tested a google query validation method to assess joke form independent of my modeling

import pandas as pd
from collections import Counter

class NaiveBayes:
    '''A naive implementation of Naive bayes,using python Only(mostly)'''
    
    def __init__(self,dataframe,label_attribute):
        '''stroing recurring data'''
        self.dataframe = dataframe
        self.attribute_list = dataframe.columns

        self.label_attribute = label_attribute
        self.dataframe_length = len(dataframe)
        self.labels = set(dataframe[label_attribute])

    def frequency_table(self,label):
        '''Create a Table of frequencies for each label'''
        labeled_dataframe = self.dataframe[self.dataframe[self.label_attribute] == label]

        counts = dict()
        for attribute in labeled_dataframe.columns:
            counts[attribute] = Counter(labeled_dataframe[attribute])
        return counts
    
    def calculate_prob_table(self,label):
        freq_table = self.frequency_table(label)
        prob_table = dict()

        for attribute in freq_table:
            prob_table[attribute] = dict()

            for value in freq_table[attribute]:
                prob_table[attribute][value] = freq_table[attribute][value]/sum(freq_table[attribute].values())

        self.prob_table = prob_table
        

    
    def vector_prob(self,X,label):
        prod = 1
        self.calculate_prob_table(label)
        
        for i,j in zip(self.attribute_list,X):
            prod *= self.prob_table[i][j]
        return prod

    def prob_label(self,label):
        return len(self.dataframe[self.dataframe[self.label_attribute] == label])/self.dataframe_length

    def bayes_output(self,X,label):
        return self.prob_label(label)*self.vector_prob(X,label)
    
    def predict(self,X):
        '''generalize me later'''
        if self.bayes_output(X,'yes') > self.bayes_output(X,'no'):
            return 'yes'
        else:
            return 'no'




tennis_data = pd.read_csv('tennis.csv')
classifier = NaiveBayes(tennis_data,'play')

#print(classifier.bayes_output(('sunny','hot','high',False),'no'))
#print(classifier.bayes_output(('sunny','hot','high',False),'yes'))

print(classifier.predict(('sunny','mild','normal',False)))
    
    





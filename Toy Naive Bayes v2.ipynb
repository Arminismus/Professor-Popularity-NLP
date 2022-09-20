{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c09a875b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import data\n",
    "import pandas as pd\n",
    "\n",
    "tennis_data = pd.read_csv('tennis.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3ee86401",
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import Counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "11ff23f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['sunny', 'hot', 'high', False, 'no'],\n",
       "       ['sunny', 'hot', 'high', True, 'no'],\n",
       "       ['overcast', 'hot', 'high', False, 'yes'],\n",
       "       ['rainy', 'mild', 'high', False, 'yes'],\n",
       "       ['rainy', 'cool', 'normal', False, 'yes'],\n",
       "       ['rainy', 'cool', 'normal', True, 'no'],\n",
       "       ['overcast', 'cool', 'normal', True, 'yes'],\n",
       "       ['sunny', 'mild', 'high', False, 'no'],\n",
       "       ['sunny', 'cool', 'normal', False, 'yes'],\n",
       "       ['rainy', 'mild', 'normal', False, 'yes'],\n",
       "       ['sunny', 'mild', 'normal', True, 'yes'],\n",
       "       ['overcast', 'mild', 'high', True, 'yes'],\n",
       "       ['overcast', 'hot', 'normal', False, 'yes'],\n",
       "       ['rainy', 'mild', 'high', True, 'no']], dtype=object)"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tennis_data.values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "d177f7a8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['outlook', 'temp', 'humidity', 'windy', 'play'], dtype='object')"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tennis_data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "113707e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create the Frequency List\n",
    "counts = dict()\n",
    "for attribute in tennis_data.columns:\n",
    "    counts[attribute] = Counter(tennis_data[attribute])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b18671bd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'outlook': Counter({'sunny': 5, 'overcast': 4, 'rainy': 5}),\n",
       " 'temp': Counter({'hot': 4, 'mild': 6, 'cool': 4}),\n",
       " 'humidity': Counter({'high': 7, 'normal': 7}),\n",
       " 'windy': Counter({False: 8, True: 6}),\n",
       " 'play': Counter({'no': 5, 'yes': 9})}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counts #Amazing! let's write a frequency table maker fucntion!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7c19258e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def FrequencyTable(dataframe):\n",
    "    counts = dict()\n",
    "    for attribute in dataframe.columns:\n",
    "        counts[attribute] = Counter(dataframe[attribute])\n",
    "    return counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "adaa0c59",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'outlook': Counter({'sunny': 5, 'overcast': 4, 'rainy': 5}),\n",
       " 'temp': Counter({'hot': 4, 'mild': 6, 'cool': 4}),\n",
       " 'humidity': Counter({'high': 7, 'normal': 7}),\n",
       " 'windy': Counter({False: 8, True: 6}),\n",
       " 'play': Counter({'no': 5, 'yes': 9})}"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "FrequencyTable(tennis_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d979b85a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "s\n",
      "t\n"
     ]
    }
   ],
   "source": [
    "s = {'s':1,'t':2}\n",
    "for i in s:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0ddeeeaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#We must be able to produce the yes/no frequency table:\n",
    "def FrequencyTable(dataframe,label_attribute,label):\n",
    "    dataframe = dataframe[dataframe[label_attribute] == label]\n",
    "    \n",
    "    counts = dict()\n",
    "    for attribute in dataframe.columns:\n",
    "        counts[attribute] = Counter(dataframe[attribute])\n",
    "    return counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2d2aa256",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      no\n",
       "1      no\n",
       "2     yes\n",
       "3     yes\n",
       "4     yes\n",
       "5      no\n",
       "6     yes\n",
       "7      no\n",
       "8     yes\n",
       "9     yes\n",
       "10    yes\n",
       "11    yes\n",
       "12    yes\n",
       "13     no\n",
       "Name: play, dtype: object"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tennis_data['play']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e5ad63b4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'outlook': Counter({'sunny': 3, 'rainy': 2}),\n",
       " 'temp': Counter({'hot': 2, 'cool': 1, 'mild': 2}),\n",
       " 'humidity': Counter({'high': 4, 'normal': 1}),\n",
       " 'windy': Counter({False: 2, True: 3}),\n",
       " 'play': Counter({'no': 5})}"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "FrequencyTable(tennis_data,'play','no') #hooray!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "aa57bf3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Now let's calculate probabilities:\n",
    "#What probabilities are we going to calculate? \n",
    "\n",
    "#1. Label Probabilites\n",
    "#2. Value Probability conditioned on labels, based on each attribute\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "freq_table = FrequencyTable(tennis_data,'play','yes')\n",
    "prob_table = dict()\n",
    "for attribute in freq_table:\n",
    "    prob_table[attribute] = dict()\n",
    "    for value in freq_table[attribute]:\n",
    "        #We need to calculate the probability, and this means calculating frequences and diving by \n",
    "        #totals:\n",
    "        \n",
    "        prob_table[attribute][value] = freq_table[attribute][value]/sum(freq_table[attribute].values())\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "e3359d2f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'outlook': {'overcast': 0.4444444444444444,\n",
       "  'rainy': 0.3333333333333333,\n",
       "  'sunny': 0.2222222222222222},\n",
       " 'temp': {'hot': 0.2222222222222222,\n",
       "  'mild': 0.4444444444444444,\n",
       "  'cool': 0.3333333333333333},\n",
       " 'humidity': {'high': 0.3333333333333333, 'normal': 0.6666666666666666},\n",
       " 'windy': {False: 0.6666666666666666, True: 0.3333333333333333},\n",
       " 'play': {'yes': 1.0}}"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prob_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "33de6c06",
   "metadata": {},
   "outputs": [],
   "source": [
    "def prob_table_if_label(dataframe,label_attribute,label):\n",
    "    freq_table = FrequencyTable(dataframe,label_attribute,label)\n",
    "    prob_table = dict()\n",
    "    \n",
    "    for attribute in freq_table:\n",
    "        prob_table[attribute] = dict()\n",
    "        \n",
    "        for value in freq_table[attribute]:\n",
    "                prob_table[attribute][value] = freq_table[attribute][value]/sum(freq_table[attribute].\n",
    "                                                                               values())\n",
    "    return prob_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "83bc0169",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'outlook': {'sunny': 0.6, 'rainy': 0.4},\n",
       " 'temp': {'hot': 0.4, 'cool': 0.2, 'mild': 0.4},\n",
       " 'humidity': {'high': 0.8, 'normal': 0.2},\n",
       " 'windy': {False: 0.4, True: 0.6},\n",
       " 'play': {'no': 1.0}}"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prob_table_if_label(tennis_data,'play','no') #hooray!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "fe7a53e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'outlook': Counter({'overcast': 4, 'rainy': 3, 'sunny': 2}),\n",
       " 'temp': Counter({'hot': 2, 'mild': 4, 'cool': 3}),\n",
       " 'humidity': Counter({'high': 3, 'normal': 6}),\n",
       " 'windy': Counter({False: 6, True: 3}),\n",
       " 'play': Counter({'yes': 9})}"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "freq_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "94f29f40",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'outlook': {'overcast': 0.4444444444444444,\n",
       "  'rainy': 0.3333333333333333,\n",
       "  'sunny': 0.2222222222222222},\n",
       " 'temp': {'hot': 0.2222222222222222,\n",
       "  'mild': 0.4444444444444444,\n",
       "  'cool': 0.3333333333333333},\n",
       " 'humidity': {'high': 0.3333333333333333, 'normal': 0.6666666666666666},\n",
       " 'windy': {False: 0.6666666666666666, True: 0.3333333333333333},\n",
       " 'play': {'yes': 1.0}}"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prob_table #Perfection. Now that we have the probabilities(conditioned on yes)\n",
    "# %= means \"useful to consider equality\"\n",
    "#we can find:P(Yes|sunny ^ hot ^ High ^ False ) %= P(sunny|yes)*P(Hot|Yes)*P(High|Yes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "23dc5c2a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.04938271604938271"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#let's calculate P(sunny|yes)*P(Hot|yes)\n",
    "prob_table['outlook']['sunny'] * prob_table['temp']['hot']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0dc0bd04",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.3333333333333333"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prob_table['windy'][True]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ccafb934",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.005486968449931412"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#let X be a feature vector\n",
    "names = 'outlook','temp','humidity','windy'\n",
    "X = 'sunny','hot','high',True\n",
    "\n",
    "#What is P(X|Yes)?\n",
    "\n",
    "#calculate P(i|yes), and take the product on i\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "23e82bb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def prob_x_if_label(X,attributes,prob_table,label,label_attribute):\n",
    "    prod = 1\n",
    "    for i,j in zip(names,X):\n",
    "        prod *= prob_table[i][j]\n",
    "    return prod\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17d9db12",
   "metadata": {},
   "outputs": [],
   "source": [
    "prob_x_if"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "dd2574de",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Counter({'yes': 9})"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#We calculate P(yes)\n",
    "freq_table['play']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "b8092b3b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6428571428571429"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(tennis_data[tennis_data['play'] == 'yes'])/len(tennis_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "144b077c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def prob_label(dataframe,label_attribute,label):\n",
    "    return len(dataframe[dataframe[label_attribute] == label])/len(dataframe)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "51f13a5a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.35714285714285715"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prob_label(tennis_data,'play','no') #Correct!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "6bcfe1a2",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "prob_x_if_label() takes 3 positional arguments but 4 were given",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m----------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m          Traceback (most recent call last)",
      "Cell \u001b[1;32mIn [66], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;66;03m#Now we calculate bayes:\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m prob_label(tennis_data,\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mplay\u001b[39m\u001b[38;5;124m'\u001b[39m,\u001b[38;5;124m'\u001b[39m\u001b[38;5;124myes\u001b[39m\u001b[38;5;124m'\u001b[39m)\u001b[38;5;241m*\u001b[39m\u001b[43mprob_x_if_label\u001b[49m\u001b[43m(\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43msunny\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mhot\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mhigh\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\u001b[43mprob_table_if_label\u001b[49m\u001b[43m(\u001b[49m\u001b[43mtennis_data\u001b[49m\u001b[43m,\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mplay\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43myes\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m      3\u001b[0m \u001b[43m                                                     \u001b[49m\u001b[43m,\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mplay\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43myes\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "\u001b[1;31mTypeError\u001b[0m: prob_x_if_label() takes 3 positional arguments but 4 were given"
     ]
    }
   ],
   "source": [
    "#Now we calculate bayes:\n",
    "prob_label(tennis_data,'play','yes')*prob_x_if_label(('sunny','hot','high',False),prob_table_if_label(tennis_data,'play','yes')\n",
    "                                                     ,'play','yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d127ac7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

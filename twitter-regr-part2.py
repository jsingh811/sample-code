
import urllib
import httplib
import json
import ast
import datetime

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.sandbox.regression.predstd import wls_prediction_std

data = open('plot_superbowl.txt', 'r')
window = 2
tweet_num = []
retweet_num = []
sum_followers = []
max_followers = []
hour = []
hashtag = []
impressions = []
urls = []
mentions = []
feature1 = []
feature2 = []
feature3 = []
feature4 = []
feature5 = []
feature6 = []
feature7 = []
feature8 = []
feature9 = []
predictant = []
for line in data:
    cols = line.rstrip()
    cols = cols.split()
    tweet_num = tweet_num + [float(cols[3])]
    retweet_num = retweet_num + [float(cols[4])]
    sum_followers = sum_followers + [float(cols[5])]
    max_followers = max_followers + [float(cols[6])]
    hour = hour + [float(cols[1])]
    mentions = mentions + [float(cols[7])]
    urls = urls + [float(cols[8])]
    hashtag = hashtag + [float(cols[9])]
    impressions = impressions + [float(cols[10])]
data.close()
#print tweet_num, retweet_num, sum_followers, max_followers,hour
t = len(tweet_num)-1
corridor = window - 1
overlap = 2
#print t
for x in xrange(0,t-1-(window/overlap),(int(window/overlap))):
    #print x
    if (x+window)> t-1:
        continue
    feature1 = feature1 + [sum(tweet_num[i] for i in range(x,x+corridor))]
    feature2 = feature2 + [sum(retweet_num[i] for i in range(x,x+corridor))]
    feature3 = feature3 + [sum(sum_followers[i] for i in range(x,x+corridor))]
    feature4 = feature4 + [sum(max_followers[i] for i in range(x,x+corridor))]
    feature5 = feature5 + [sum(hour[i] for i in range(x,x+corridor))]
    feature6 = feature6 + [sum(mentions[i] for i in range(x,x+corridor))]
    feature7 = feature7 + [sum(urls[i] for i in range(x,x+corridor))]
    feature8 = feature8 + [sum(hashtag[i] for i in range(x,x+corridor))]
    feature9 = feature9 + [sum(impressions[i] for i in range(x,x+corridor))]
    predictant = predictant + [tweet_num[x+window]]
#print feature1, feature2, feature3, feature4, feature5, predictant
test = []
index = []
X = np.column_stack((feature1,feature2,feature3,feature4,feature5,feature6,feature7,feature8,feature9))
#print X
model = sm.OLS(predictant, X)
results = model.fit()
print(results.summary())
print('Mean Squared Errors: ', results.mse_resid)
print('Accuracy :', results.rsquared)
print('t values', results.tvalues)
for i in results.tvalues:
    test = test + [abs(i)]
print test
for i in xrange(0,4):
    temp = test.index(max(test))
    index = index + [temp]
    test[temp] = 0
print index
plt.scatter(X[:,index[0]], predictant, color='blue')
plt.xlabel("Top Feature 1")
plt.ylabel("No. of tweets in next hour")
plt.title("Predictant vs First top feature")
plt.plot()
plt.show()

plt.scatter(X[:,index[1]], predictant, color='blue')
plt.xlabel("Top Feature 2")
plt.ylabel("No. of tweets in next hour")
plt.title("Predictant vs Second top feature")
plt.plot()
plt.show()

plt.scatter(X[:,index[2]], predictant, color='blue')
plt.xlabel("Top Feature 3")
plt.ylabel("No. of tweets in next hour")
plt.title("Predictant vs Third top feature")
plt.plot()
plt.show()

plt.scatter(X[:,index[3]], predictant, color='blue')
plt.xlabel("Top Feature 4")
plt.ylabel("No. of tweets in next hour")
plt.title("Predictant vs Fourth top feature")
plt.plot()
plt.show()

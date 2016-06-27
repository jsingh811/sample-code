**AUDIENCE BUILDING**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **PLATFORMS**  | **CONSUMER ATTRIBUTES**| **AUDIENCE BUILDING APPROACH**
  ---------------| -------------------------------------------------------------| ------------------------------
  Facebook       | -   Interaction with creator’s content (likes and comments)  | Based on number of likes and comments by the consumer on content belonging to particular categories.
  Twitter       |  -  Tweets & retweets  -   Interaction with creator  -   Location  -   Followers -   Following | Tweets – TFIDF – Naïve Bayes classifier- classify tweets to categories                                 Assign interest topic to consumer based on results from above.
  YouTube       |   - Public Subscriptions  -   Comments on creator’s content   | Based on content categories of subscriptions of consumers.
  Google Plus   |  -   Gender  -   Location -   Comments and +1s on creator’s posts |Based on number of +1s and comments by consumers on creator’s content. (similar to Facebook)
  Vimeo         |  -   Followers    -   Following      -   Videos, Channels, Groups | Based on content categories of videos from consumer’s Vimeo profile (under following, videos posted, channels, groups). (similar to YouTube)
 
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**DETAILS:**
-----------------------------------------------------------------------------
**FACEBOOK AUDIENCE BUILDING:**

*Known*: Categories of content posted by consumer.

*Aim:* Find audiences that are likely to be interested in particular
category on content.

Some audience has higher comment activity while other have higher liking
activity.

Filter out audiences based on requirements (commenters/ likers)

*Features:*

Let the category of interest be A

1\. \#contents of A liked by consumer/ \#content of A presented to
consumer

2\. \#contents of A commented on by consumer/ \#content of A presented to
consumer

3\. \#contents of A liked by consumer/ \#contents liked by consumer

4\. average \#comments on contents of A

5\. \#likes on content A by consumer/ \#likes by consumer

6\. \#comments on content A by consumer/ \#comments by consumer

Depending on type of audience is desired, assign weights to features.

**TWITTER AUDIENCE BUILDING:**

*Method*: Supervised learning

*Training data*: 1400 samples of tweets for each of the content
categories were crawled from twitter.

*Feature*: TF-IDF was implemented on the words in the tweets.

*Classifier*: Bernoulli’s Naïve Bayes

*Results*:

A person’s tweets can be used to classify them into categories and
marking categories to user interests depending on frequency of the
category tweets.

-   10-fold Cross validation accuracy for tweet topic classification
    using the training set: **84.69%**

-   Accuracy for each category testing by splitting data 75%training 25%
    testing

  **Category**               |**Accuracy of Classification %**
  ---------------------------| ----------------------------------
  Animals and pets          | 90.53
  Animation                 | 91.52
  Beauty, fashion and Style | 87.16
  Vehicles                  | 91.57
  Comedy                    | 91.96
  Education                 | 82.61
  Entertainment             | 74.72
  Health and lifestyle      | 67.66
  Music                     | 81.27
  Politics                  | 76.06
  Non-profit                | 93.39
  Science                   | 64.38
  Technology                | 85.09
  Sports                    | 75.58
  Gaming                    | 90.36

-   This algorithm was also tested on 18 people. I got their results and
    asked them to order their interests among these categories. For 15
    out of the 18 people, the results were about right. For 3, the
    ordering was not accurate. Some external reasons could be that a
    person’s tweets may not represent a person’s actual interests in
    their entirety.

**YOUTUBE AUDIENCE BUILDING:**

This is explained in the flowchart below

![](media/image1.png){width="6.361111111111111in"
height="4.805555555555555in"}

*Feature:* Categories of content that consumers like as obtained from
their other subscriptions

Based on the categories subscribed to, assign interest category to
consumers.

**GOOGLE+ AUDIENCE BUILDING (TODO):**

Get commenters and +1s of creator’s content, and based on number of
comments and likes, assign interest topics to consumers (approach
similar to Facebook audience building).

**VIMEO AUDIENCE BUILDING (TODO):**

Get categories of:

-   Videos posted in Channels and by users that consumer is following

-   Videos in groups that the consumer is a part of

-   Videos posted by the consumer



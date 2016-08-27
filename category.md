**Problem statement**

Our goal is to map provider videos to ICX categories.

YouTube, Facebook and Vimeo have their own separate defined categories
for videos.

The list of categories differs on each provider and ICX.

The table below shows a list of assignable categories on each provider
and ICX.

  -------------------------------------------------------------------------------------
  YouTube                 Facebook          Vimeo                      ICX
  ----------------------- ----------------- -------------------------- ----------------
  Film & Animation        Science           Animation                  Animation

  Music                   Technology        Art                        Animals

  Pets & Animals          Beauty\_fashion   Camera Techniques          Vehicles

  Sports                  Business          Comedy                     Home & DIY

  Travel & Events         Cars\_trucks      Documentary                Camera Effects

  Autos & Vehicles        comedy            Experimental               Comedy

  Gaming                  Cute\_animals     Fashion                    Documentary

  People & Blogs          Entertainment     Food                       Other

  Comedy                  Family            Instructionals             Fashion & Style

  Entertainment           Food\_health      Music                      Beauty

  News & Politics         Home              Narrative                  Food

  Howto & Style           Lifestyle         Personal                   Howto

  Education               Music             Reporting And Journalism   Science

  Science & Technology    News              Sports                     Technology

  Nonprofits & Activism   Politics          Talks                      Business

                          Sports            Travel                     Health

                          Videogames                                   Music

                          Other                                        Entertainment

                                                                       Film

                                                                       Family

                                                                       Animals

                                                                       Pets

                                                                       News

                                                                       Politics

                                                                       People & Blogs

                                                                       Non Profit

                                                                       Sports

                                                                       Videogames

                                                                       Education

                                                                       Travel
  -------------------------------------------------------------------------------------

When a creator comes into ICX, we crawl all of his videos he has posted
on the providers he authenticates with us. We then want his videos from
the providers to classify to ICX categories.

Following the above we also want to generate category recommendation for
when the creator posts a video on ICX to distribute to providers and
enters a title, description and tags for his uploaded video.

**Issues**

- Large % of videos on facebook are inaccurately categorized into
facebook categories.

- Large % of videos on vimeo are inaccurately categorized into vimeo
categories and may not have any category associate with them.

**Approach**

Supervised learning with bag of words on title, description, and tags of
videos using logistic regression.

**Training data**: title, description, and tags for **1500** videos for
each ICX category collected manually from YouTube. Total of \~**39000**
samples.

**Tested on**: Manually collected **14083** videos from YouTube and
**2522** videos from Facebook.

**Summary of results**

10-fold Cross Validation Accuracy \~95%

On **YouTube** test data:

\~ 80 % accuracy

\~ 75 % recall

On **Facebook** test data: (not well labelled)

\~ 65 % accuracy

\~ 65 % recall

Issues:

-   Very few words in title + description + tags in a lot of
    Facebook videos.

-   Videos can be associated with more than 1 category (for example,
    **education** video about **science**)

    (this was seen many false classification samples)

    &lt;=2 class classification improves the accuracy for YouTube test
    data by 5-6%

The table summarizes accuracy and precision per category on data split
(75% training, 25% testing) videos with one class classification.

  **Category**        **% Accuracy on test videos from YouTube**   **% Precision on test videos from YouTube**
  ------------------- -------------------------------------------- ---------------------------------------------
  Animals             97.56                                        97.56
  Animation           96.94                                        98.28
  Beauty              96.76                                        96.05
  Business            98.14                                        96.35
  Camera Effects   91.75                                        96.61
  Comedy              97.97                                        98.72
  Education           97.29                                        98.36
  Entertainment       96.79                                        97.51
  Family              99.00                                        99.75
  Fashion             95.01                                        97.44
  Film                96.51                                        94.96
  Food                94.55                                        94.66
  Gaming              99.49                                        97.03
  Health              97.14                                        96.45
  Home                96.73                                        99.25
  Music               98.84                                        91.91
  News                96.92                                        94.59
  Nonprofit           91.44                                        99.74
  Pets                98.96                                        97.95
  Politics            98.32                                        98.66
  Science             95.27                                        94.78
  Sports              97.38                                        97.13
  Technology          96.81                                        96.11
  Travel              98.52                                        98.77
  Vehicles            98.04                                        96.69

The table summarizes accuracy per category on YouTube test videos with
one class classification.

  **Category**        **% Accuracy on test videos from YouTube**
  ------------------- --------------------------------------------
  Animals             82.7
  Animation           87.6
  Beauty              94.8
  Business            78.1
  Camera Effects   98.3
  Comedy              79.3
  Education           64.1
  Entertainment       35.8
  Family              94.3
  Fashion             82.8
  Film                84.8
  Food                83.2
  Gaming              77.7
  Health              84.5
  Home                72.4
  Music               95.8
  News                66.9
  Nonprofit           35.5
  Pets                82.1
  Politics            78.1
  Science             85.7
  Sports              81.3
  Technology          90.7
  Travel              80.0
  Vehicles            95.7

The table summarizes accuracy per category on Facebook test videos with
one class classification.

  **Category**        **% Accuracy on test videos from Facebook**
  ------------------- ---------------------------------------------
  Animals             53.5
  Animation           62.4
  Beauty               
  Business            64.2
  Camera Effects   73.5
  Comedy              32.4
  Education           50.1
  Entertainment       43.8
  Family               
  Fashion             76.4
  Film                93
  Food                76.8
  Gaming              60.9
  Health              58
  Home                91.1
  Music               54.1
  News                47.3
  Nonprofit           37.3
  Pets                100
  Politics            78.6
  Science             75.7
  Sports              80.5
  Technology          57.4
  Travel              52.3
  Vehicles            65.7

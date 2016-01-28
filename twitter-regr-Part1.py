import time
import json
import re

def function(filename,dates,plot,plot2,followers,retweets,newdata1,newdata2,newdata3,newdata4): #defining function to collect required data from the given tweet files
 #opening files where extracted data is to be stored
 f_rtw=open(retweets,'a')
 f_fol=open(followers,'a')
 f_dates=open(dates,'a')
 f1=open(newdata1,'a')
 f2=open(newdata2,'a')
 f3=open(newdata3,'a')
 f4=open(newdata4,'a')
 len_dates=0
 sum_retweets=0
 sum_folcount=0
 # extracting data from given tweet files
 with open(filename) as file:
   for line in file:
    if(re.search('^{"firstpost_date":', line)):
     data=json.loads(line)
     f1.write(str(len((data["tweet"]["entities"]["user_mentions"])))+'\n')
     f2.write(str(len(data["tweet"]["entities"]["urls"]))+'\n')
     f3.write(str(len(data["tweet"]["entities"]["hashtags"]))+'\n')
     f4.write(str(data["metrics"]["impressions"])+'\n')
     f_rtw.write(str(data["metrics"]["citations"]["total"])+'\n')
     len_dates+=1
     sum_retweets=sum_retweets+data["metrics"]["citations"]["total"]
     f_dates.write(str(data["firstpost_date"])+'\n')
     f_fol.write(str(data["tweet"]["user"]["followers_count"])+'\n')
     sum_folcount=sum_folcount+data["tweet"]["user"]["followers_count"]
 #calculation of average number of retweets and followers count
 avg_retw=float(sum_retweets)/len_dates
 avg_foll=float(sum_folcount)/len_dates
 f_fol.close()
 f_rtw.close()
 f_dates.close()
 f1.close()
 f2.close()
 f3.close()
 f4.close()
 
 #opening files required to get statistics on an hourly basis
 f=open(dates,"r")
 c=0
 y=0
 folw=open(followers,'r')
 ftemp=folw.readlines()
 n1=open(newdata1,'r')
 n1temp=n1.readlines()
 n2=open(newdata2,'r')
 n2temp=n2.readlines()
 n3=open(newdata3,'r')
 n3temp=n3.readlines()
 n4=open(newdata4,'r')
 n4temp=n4.readlines()
 rt=open(retweets,'r')
 rtemp=rt.readlines()
 l=f.readlines() 
 p1=open(plot,"a")
 p2=open(plot2,'a')
 x=int(l[0])
 temp=0
 denom=0
 num=0
 t=0
 
 #calculating statistics on an hourly basis and storing them in text files
 while(c<=(len_dates-1)):
  z=x+3600
  count=0
  f_count=0
  r_count=0
  n1_count=0
  n2_count=0
  n3_count=0
  n4_count=0

  maxq=int(ftemp[c])
  while(temp==0):
   if (c<=(len_dates-1) and int(l[c])<=z):
    count=count+1
    if(int(ftemp[c])>maxq):
	 maxq=int(ftemp[c])
    y=int(l[c])
    f_count+=int(ftemp[c])
    r_count+=int(rtemp[c])
    n1_count+=int(n1temp[c])
    n2_count+=int(n2temp[c])
    n3_count+=int(n3temp[c])
    n4_count+=int(n4temp[c])
    c=c+1 
   
   elif(c>=len_dates or int(l[c])>z):
    denom+=1
    temp=temp+1
    t+=1
    x1=x
    if(c<len_dates):
     x=z+1
  hour=time.ctime(x1)
  hour=hour[11:13]
  end_hour=time.ctime(z)
  end_hour=end_hour[11:13]
  if(x1<1422806400):
   zone=1
  elif (x1<=1422849600):
   zone=2
  elif(x1>1422849600):
   zone=3
  if(count!=0):
   p1.write(str(zone)+'\t'+(str(hour).zfill(2))+'\t'+ (str(end_hour).zfill(2))+'\t'+ str(count).zfill(10)+'\t'+ str(r_count).zfill(10)+ '\t'+(str(f_count).zfill(10))+ '\t'+str(maxq).zfill(10)+'\t'+str(n1_count).zfill(4)+'\t'+str(n2_count).zfill(4)+'\t'+str(n3_count).zfill(4)+'\t'+str(n4_count).zfill(8)+'\n')
  if(count==0):
   maxq=0
  p2.write(str(zone)+'\t'+str(hour).zfill(2)+'\t'+ str(end_hour).zfill(2)+'\t'+ str(count).zfill(10)+'\t'+ str(r_count).zfill(10)+ '\t'+str(f_count).zfill(10)+ '\t'+str(maxq).zfill(10)+'\t'+str(n1_count).zfill(4)+'\t'+str(n2_count).zfill(4)+'\t'+str(n3_count).zfill(4)+'\t'+str(n4_count).zfill(8)+'\n')
  num=num+count
  temp=0
 avg_tweets_per_hour=float(num)/denom
 
 #storing answer to part 1 in file resultsques1.txt
 x=open('resultsques1.txt','a')
 x.write(filename+'\n')
 x.write("avg. number of followers: "+str(avg_foll)+'\n')
 x.write("avg. number of retweets: "+str(avg_retw)+'\n')
 x.write("avg. number of tweets per hour: "+str(avg_tweets_per_hour)+'\n')
 x.close()
 f.close()
 p1.close()
 folw.close()
 n1.close()
 n2.close()
 n3.close()
 n4.close()
 p2.close()
 rt.close()
 
 #calling function defined above for each tweet file
function('tweets_#gopatriots.txt','dates_gopatriots.txt','plot_gopatriots.txt','plotwith0_gopat.txt','followers_gopat.txt','retweets_gopat.txt','newdata1_gopat.txt','newdata2_gopat.txt','newdata3_gopat.txt','newdata4_gopat.txt')
function('tweets_#gohawks.txt','dates_gohawks.txt','plot_gohawks.txt','plotwith0_gohawk.txt','followers_gohawk.txt','retweets_gohawk.txt','newdata1_gohawk.txt','newdata2_gohawk.txt','newdata3_gohawk.txt','newdata4_gohawk.txt')
function('tweets_#nfl.txt','dates_nfl.txt','plot_nfl.txt','plotwith0_nfl.txt','followers_nfl.txt','retweets_nfl.txt','newdata1_nfl.txt','newdata2_nfl.txt','newdata3_nfl.txt','newdata4_nfl.txt')
function('tweets_#patriots.txt','dates_patriots.txt','plot_patriots.txt','plotwith0_pat.txt','followers_pat.txt','retweets_pat.txt','newdata1_pat.txt','newdata2_pat.txt','newdata3_pat.txt','newdata4_pat.txt')
function('tweets_#sb49.txt','dates_sb49.txt','plot_sb49.txt','plotwith0_sb49.txt','followers_sb49.txt','retweets_sb49.txt','newdata1_sb49.txt','newdata2_sb49.txt','newdata3_sb49.txt','newdata4_sb49.txt')
function('tweets_#superbowl.txt','dates_superbowl.txt','plot_superbowl.txt','plotwith0_superbowl.txt','followers_suberbowl.txt','retweets_superbowl.txt','newdata1_superbowl.txt','newdata2_superbowl.txt','newdata3_superbowl.txt','newdata4_superbowl.txt')


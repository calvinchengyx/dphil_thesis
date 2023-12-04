# Memo 
This is a working memo for tracking Calvin's DPhil project. And here is the daily summary.

* [20231204](## 20231204)
* [20231002](## 20231002)

## 20231002 
[original tweet dataset](https://github.com/echen102/COVID-19-TweetIDs)
What i would like to do is download self OR ask Liang to access CUHK VM again
1. download data to my local laptop
2. save them to local file (friends list downloaded already)

[Nitter](https://nitter.net/), a mirrored Twitter website which can web crawl tweets based on usernames. 
* Maneul shared his web crawler in the Slack channel, and also several paper classifying political stands
    * [Claim Extraction and Dynamic Stance Detection in COVID-19 Tweets](https://dl.acm.org/doi/abs/10.1145/3543873.3587643)
    * [The COVMis-Stance dataset: Stance Detection on Twitter for COVID-19 Misinformation](https://arxiv.org/abs/2204.02000)
    * [Stance Detection in COVID-19 Tweets](https://aclanthology.org/2021.acl-long.127/)

Haixin is uploading the data to google drive where i have a SQL data (500G) including one year of the dataset. How to deal with that dataset is a problem. Probably i won't use it, just use small data to do different truncks. 

__Daily Summary__
* i am using one hour data `coronavirus-tweet-id-2022-11-01-00.jsonl` for code testing. 

## 20231204
__Daily Summary__
* All tweet data is saved on OneDrive, HKU acount. 
* All code is running on Scott's VM, using python. 
* Decided project goals. 
* Schedule the execution plan. 

__Daily Questions__
* Q1. Conceptualization - shall i stick to conspiracy theory or switch to misinformation? (Scott Discussion on Nov 17, 2023)
    * Answer - stick to conspiracy theory, when preparing for PNAS, because (1) still misinformation, remaining the space to change when putting into the thesis (2) easier to argue the significance of the duration research (3) echo the findings in this paper [the spreading of misinformation online](https://www.pnas.org/doi/10.1073/pnas.1517441113#supplementary-materials). (4) save time and resources to re-collect data, more accuratly, to re-filter the data
    >  For conspiracy-related content the lifetime increases with cascade size (Vicario et al., 2016).
* Q2. Project Goals
    * practice research data managaement skills, use small data truncks for code testing, and use big data for final analysis
    * practice python coding skills, and use python to do data analysis instead of R, plz write reproducible with structural organization of codes, comments and datasets
    * practice more computational writing skills, and write a paper for PNAS
* Q3. Execution Plan in Dec 2023
    * literature review revision - redo the research questions, _Dec 4-5_
    * data collection - how to best filtering target tweets, _Dec 6-12_
    * clustering - how to best clustering tweet strains or conspiracy claims - make sure the study unit (Dec 19-25)
    * survival analysis - this is your statistical lession for this project. (Dec 26-31)
    * data visualization - how to best visualize the results with Python (Jan 1-7)
    * content revision - tailoring writing to PNAS  (Jan 8-14)

# Memo 
This is a working memo for tracking Calvin's DPhil project. And here is the daily summary.

* [20231002](##20231002)
* [20231204](##20231204)
* [20231205](##20231205)
* [20240110](##20240110)


## 20240110 
### Method - Data Collection 
1. I have a (1) keywords list that used to filter conspiracy theory relevant tweets, and (2) 1 year tweets 
2. 



## 20231205

[GPT 4.0 Turbo budget](https://platform.openai.com/docs/models/continuous-model-upgrades) calculation
1. for pilot study - $25 per month user interface
2. for API service - 
    1. `gpt-4-1106-preview` model (also known as `GPT-4 Turbo`)
        1. input token price - $0.01 / 1k tokens
        2. output token price - $0.03 / 1k tokens
    2. `gpt-3.5-turbo 16k` model as comparison
        1. input token price - $0.001 / 1k tokens
        2. output token price - $0.002 / 1k tokens
3. [token and language](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)
    1. for English, 100 tokens = 75 words
    1. for Chinese, 100 tokens = 50 words (may need more tokens for Chinese, depending on the tokenization method, GPT-4 has about 2000 Chinese tokens)

For a typical tweet study -
1. input 
    1. tweet 
        1. maximum tweet length - 280 characters, which is about 40-70 words
        2. average tweet length - assuming 50 words (280 characters), which is about 67 tokens, let's just say `70 tokens` (should always budget more tokens)
    2. prompt - depending on the prompt length, in the sentiment tasks, i used 300 words prompt, which is about 400 tokens, let's just say `500 tokens`. 
    3. exmaples (optional)
        1. normally 3 examples, tweets + output, for few shot learning, which is about 150 words, which is about `250 tokens`
2. output - depending on the task requirment, let's just say moral foundation values
    1. moral foundation values - 5 values, which is about 2-5 tokens
    2. rationale (optional & controllable) - 50 tokens 
    3. overall, let's just say `50 tokens` for the output
3. assuming we have 1 million tweet, the total cost is 
    1. input - 1,000,000 * (70 + 500 + 250) / 1000 * 0.01 = $8,400 
    2. output - 1,000,000 * 50 / 1000 * 0.03 = $1,500
    3. total - 8,400+1,500 = $ 9,900, 

So, probably `$10,000` for a typical tweet study is a reasonable budget. If we include Chinese tweets, for 1 million Chinese tweets, the total cost is 1.5 to 2 times more, which is about $15,000 to `$20,000`.

For customized/fine-tuninng GPT-4 training model, price can be considerably higher. For example, `GPT-3.5-Turbo fine-tuning` model is 8 times expensive than `GPT-3.5-Turbo` model in the training dataset. And double the price for the input/output tokens in the fined-tuned model. But unlike `GPT-3.5-Turbo`, `GPT-4-turbo` fine-tuning service is not open to all developers, additional application is needed.


## 20231204
__Daily Summary__
* All tweet data is saved on OneDrive, HKU acount. 
* All code is running on Scott's VM, using python. 
* Decided project goals. 
* Schedule the execution plan. 
* overleaf re-writing project is `dphil_paper1_comm_version`

__Daily Questions__
* Q1. Conceptualization - shall i stick to conspiracy theory or switch to misinformation? (Scott Discussion on Nov 17, 2023)
    * Answer - stick to conspiracy theory, when preparing for PNAS, because (1) still misinformation, remaining the space to change when putting into the thesis (2) easier to argue the significance of the duration research (3) echo the findings in this paper [the spreading of misinformation online](https://www.pnas.org/doi/10.1073/pnas.1517441113#supplementary-materials). (4) save time and resources to re-collect data, more accuratly, to re-filter the data
    >  For conspiracy-related content the lifetime increases with cascade size (Vicario et al., 2016).
* Q2. Project Goals
    * practice research data managaement skills, use small data truncks for code testing, and use big data for final analysis
    * practice python coding skills, and use python to do data analysis instead of R, plz write reproducible with structural organization of codes, comments and datasets
    * practice more computational writing skills, and write a paper for PNAS
* Q3. Execution Plan in Dec 2023
    * literature review revision - rewrite intro, lr and research questions, _Dec 4-5_
    * data collection - how to best filtering target tweets, _Dec 6-12_
    * clustering - how to best clustering tweet strains or conspiracy claims - make sure the study unit (Dec 19-25)
    * survival analysis - this is your statistical lession for this project. (Dec 26-31)
    * data visualization - how to best visualize the results with Python (Jan 1-7)
    * content revision - tailoring writing to PNAS  (Jan 8-14)


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

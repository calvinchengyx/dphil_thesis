# Memo 
This is a working memo for tracking Calvin's DPhil project. And here is the daily summary.

## General ToDo list (20240115 updated)
> Legends for tracking the progress of tasks [^1]
> * Work scheduled: &#10066;
> * Work in progress:  &#9998;
> * Completed: &check;

### Method Task Breakdown
1. &check; ~~Original Twitter dataset [^2] saved at local OneDrive~~
2. &#9998; Select COVID-19 conspiracy theory relevant tweets from fact-checking articles [^3] 
    1. &#9998; fact-checking articles check - for each conspiracy claim, there must be linked with an institutional fact-checking article. 
        - &#9998; CT definition filter - go through all factchecking articles collected at 20200601, making sure they fit the `3 fold` conceptualization
        - &#9998; CT claim summary - summarize CTs for each factchecking article, each CT claim (from fact-checks) is the highest level of topic
        - &#9998; Additional CT claims - add CT claims to the EXCEL and link them to one fact-check article 
    2. &#10066; keyword check - for each conspiracy claim, they must be collected from the original dataset by a set of keywords, [keywrod working doc](/Users/calvincheng/Library/CloudStorage/OneDrive-Nexus365/thesis/paper1/keywords_0407.R)
    3. &#10066; keyword fectching check - for each conspiracy claim, its corresonding keyword must be able to fetch relevant tweets from the original dataset
        - &#10066; prepare the testing dataset: ONE-month original dataset (20206-202105), one hour from each day, 30 hours in total
        - &#10066; keyword fetching test - for each conspiracy claim, collect 100 tweet and count how many are CT claim relevant
        - &#10066; iteration 
            - &#10066; remove fact-checking keywords
            - &#10066; adjust keyword lists
    - &#10066; CT tweets fetching from the original dataset

### Time Commitment Reflection
| Task   | Time Budget | Time Spent  | Start | Finished | 
|--------|-------------|-------------|-------|----------|
| Intro rewriting | 8 hours | 12 hours | Late Dec 2023 | 4 Jan 2024 | 
| LR rewriting | 1 week | 1 week | 4 Jan | 9 Jan |
| Project Task Planning | 8 hours | 12 hours | 12 Jan | 15 Jan |
| MPhil Data Configuration | 8 hours | 8 hours | Nov 2023 | 14 Jan |
| Keywords Redo | 1 week |  | 15 Jan | in progress |
| Data Collection | 1 week |  |  |  |
| Method Clustering | 1 week |  |  |  |
| Variable Construction | 1 week |  |  |  |
| Model Running | 1 week |  |  |  |
| Sensitivity Test | 1 week |  |  |  |
| Conclusion and pic | 1 week |  |  |  |
| Proofreading and wrap-up | 1 week |  |  |  |


[^1]: VS Code Markdown support HTML unicode for symbols and emojis. Please find the [HTML unicode cheatsheet](https://www.toptal.com/designers/htmlarrows/symbols/)
[^2]: Full tweets dataset is saved at youer CUHK OneDrive folder _/Users/calvincheng/Library/CloudStorage/OneDrive-TheUniversityofHongKong-Connect_
[^3]: The working document for this step is _keywords_0116.md_, saved at folder: Oxford OneDrive - thesis - paper 1 

----------
# 20241015 an idea
for the survival paper, since i have threads, why dont i just cluster threads with dorian's methods and study the life CT threads?

# 20241008 very struggle
- struggling with this research design
    - lost interest in the unpublished mphil thesis
    - don't know how to define the study unit
        - previously just clustering - hierachical clustering, but no gurantee that study unit is relevant, and the "strain" definition does not make sense
        - keyword topic - yes, works, fewer study units (80ish), this is more like a topic level study unit, many will never die, difficult to make sense of the survival analysis
        - claim-matching? good approach, but can be totally different from what i have already done.

# 20241007 review previous works 
- decision made
    - stop doing more data collection validation, use what you have at the moment to re-write the paper
    - finish survival analysis code
    - move all code to a new folder to manage on Scott's server
    - will think about the conspiracy claim matching part later 

# 20240812 
- finished
    - moral + emo variables
    - re-do the ct claim matching based on retweet chain
- todo
    - homogeniety (Mon)
    - fact-checking timing (Tue)
    - survival analysis in python (Tue)
    - study-unit claim matching with LLMs (Wed)

# 20240810 re-do the ct claim matching based on retweet chain
- finished
    - decision regarding the thread, i will use the thread instead of content similarity for the spread
- todo
    - homogeniety

# 20240714
- todo 
    - measure moral emotions with dictionary methods
    - fix the ct1_1 to ct1 bug, that you can not replace them in a long string (`.str.replace` vs `.replace` function error, where the former is for substrings, the later only works on the entire value). 

# 20240713
- todo
    - LR for moral emotions measurements 
    - prepare for the whole dataset for paper 1

# 20240711 Llama 3 with Huggingface 
- errors
    - GPU memory, when initializing the model with `transformers.pipeline()` function, it often shows CUDA out of memory **Fixed**
        - ANSWER 
        0. you can just say `device_map="auto"`
        1. `nvidia-smi` to check GPU use 
        2. specify the GPU that is available `device="cuda:3"` (using GPU 3 for example, by default `device="cuda"` will use the first GPU )
        3. some info, the pipeline function will use 90% memory of L40S GPU, or 50% memory of A100 GPU
        4. open another terminal window to continously monitor the GPU usage `watch -n 1 nvidia-smi`, presse `Command + C`to exit the continuous watching mode
- finished
    - the model runs perfectly with line-by-line python code in python3 mode
    - transferring data between local machine and `brians`, the current approach is to use `curl` command to download from Github with the link, for example `curl -o 1_initiation.py https://raw.githubusercontent.com/calvinchengyx/dphil_misinfo/main/1_initiation.py`

- todo 
    - wrap up the code into python scripts 
        - Script 1. initialize the model, define prompts, define output format 
        - Script 2. all about prompt
        - Script 3. all about the dataset, that ready to be classified 
        - Script 4. run the classification and save the output into csv or other files 

- REVIEW YOUR THESIS GOAL AND PLAN
    1. current plan, use Llama 3-8b for content analysis, no fine-tuning, only prompt engineering tuning with few shots 


# 20240710 Llama 3 on OII GPU server
- errors
    - port error, submitted to oii-help, but the easiest solution is to start a new port `--master_port=25678`
- finished
    - run the LLaMa 3 official test file on OII GPU server, and it works fine. 
    - created a new environment `ct-hg-env` to run llama 3 via huggingface architecture, because 99% of tutorials are using huggingface, and it is easier to find help online.
    - `pip install` packages `transformers` and `torch` to the `ct-hg-env` environment


# 20240709 Llama 3 on OII GPU server
- Check Setup settings (Requirment, for 8B model, it needs a GPU with a minimum of 16GB VRAM)
    1. `nvidia-smi` command line to check OII's GPU info [tutorial](https://llama.meta.com/docs/llama-everywhere/running-meta-llama-on-linux/) **double check with Scott for the configuration meaning**
    2. clone the LLaMa 3 repo from GitHub and download to my OII brain folder **DONE**
    3. install the requirements for LLaMa 3, including `pytorch` **not yet**
    4. spent some time to understand the brains' python environment, Python 3 interpreter in the sever is using the system’s default Python, not part of a virtual environment or a Conda environment. Should i create a virtue environment for my project? **double check with Scott**
- errors
    1. could not initiate the llama3 for a permission error `PermissionError: [Errno 13] Permission denied: '/tmp/data-gym-cache/3f0264bb26172277b9aab5a43e0268e84eda1575.ae7c066e-f7c4-4c69-b32a-7d257a66a988.tmp`, **Done**
    2. try to use `sudo` but the passport is not correct, not the scro4316 password? **Done, you can not SUDO**
    3. ANSWER - [You will get this error in a multi-user system. When some other users have already created the cache dir /tmp/data-gym-cache, they own the directory, and you don't have the permission. It's a bad idea to hard-code the temporary directory.](https://github.com/openai/tiktoken/issues/75). The best solution is to set up a new cache directory in the home folder.
- finished
    1. created a `ct-env` virtual environment under `\scro4316\llama3-8b\llama3` folder path `python3 -m venv ct-env` (it is generally a good practice to create a virtual environment for each project, and keep them within the repository folder you’ve cloned from GitHub.)
    2. `source ct-env/bin/activate` to activate the virtual environment; `deactivate` to deactivate it
    3. `pip install -r requirements.txt` to install the requirements for LLaMa 3 (the `requirements.txt` file comes with the `llama3` repo)
    4. still have the file permission error and my password does not work - waiting to see if IT can help me with this.


# 20240708
- finished
    - use GPT-4 finished validation big CT claims (14 claims + no claim) on spreadsheet
    - summary 
        - the GPT-4 performance on classifying CT relevant tweets varies significantly across different CT claims.
        - for big well-established CTs, like qanon and plademic, GPT-4 performs well, with an accuracy rate of 100% or above.
        - for well-established CTs, like bio-weapon, coverup, planned covid, deep state, accuracy rate range from 58-85%
        - for less well-established CTs, like flu kill, hoax, twisted death toll, the accuracy rate is below 50% (some very poor, manmade is only like 10%)
    - reasons
        - further fine-tune the prompt, on the "claim" section
        - add more example tweets ?
        - try another LLMs like LLama 3?
        - anything else? (talk to Anna)

# 20240624
- Todo
    - set up my OII GPU server account and waiting for IT team to send me an-email about my own folder. 
    - the problem is i can not access it via VS code, weird, but only vis Mac terminal. very annoying. 
    
- finished
    - use GPT-4 finished validation big CT claims (14 claims + no claim) 
- todo
    - summarize the findings from the validation and proceed to next step - applying LLaMa 3 on OII GPU server



# 20240623 
- Claim Validation 
    1. how to do the claim validation? 
        1. randomly sample 10 tweets from one category
        2. prompt the LLMs with the CT claim and the tweet content
        3. ask the LLMs to code the relevance of the tweet to the CT claim
        4. human code the 10 tweets 
        5. compare the results
        6. then do the rest with LLMs

- LLMs Validation Prompt, revised from [Chew et al., (2023)](http://arxiv.org/abs/2306.14924)

```
prompt1

You are a qualitative coder who is annotating tweets related to the COVID-19 pandemic conspiracy theories. Your task is to decide whether the given content is discussing the conspiracy claim: "COVID is a hoax" 

To code this text, do the following:
- First, read the conspiracy claim "covid is a hoax, covid is not real" and the tweet. 
- Next, decide whether the tweet is relevant to the conspiracy claim, if so, print 0; if not, print 1; if not enough information to decide, print 2. 
- Finally, print your rationale (fewer than 10 words) for the coding decision

Use the following format for output:
- text_id: 
- code: 0 or 1 or 2.
- reason: 

Examples 

Input:
    - 39161, deaths from the us civil war averaged about 16 000 per month in just over 4 years in only about 5 1 2 months covid 19 has killed over 135 000 american people which is about 24 500 per month yes it is very serious and no it s not the flu or a hoax whyiwearamask
    - 97971, i suggest trump cultists get the vaccine last because after all covid is a hoax right
    - 76811, conspiracy theory trump s covid was an elaborate hoax used to give trump a chance for a nip tuck facelift he ll come back looking refreshed
Output: 
    - text_id: 39161
    - code: 0
    - reason: the tweet is discussing the seriousness of COVID-19 and refuting the claim that it is a hoax
    - text_id: 97971
    - code: 0
    - reason: the tweet satirically suggests that Trump supporters should get the vaccine last because they believe COVID-19 is a hoax
    - text_id: 76811
    - code: 0
    - reason: the tweet is discussing a conspiracy theory that Trump's COVID-19 diagnosis was a hoax to give him a facelift

```

- finished GPT validation - in the sampled `ct70` dataset
    - 1 out of 100 does not match human coder's result, saying GPT-4.0 is 99% alike a human annotator
    - as a result, in this category, 2 out of 100 is not relevant to the CT claim, so 98% accuracy for the regex match data collection. saying the claim cluster is 98% accurate. 

prompt 2

```
You are a qualitative coder who is annotating tweets related to the COVID-19 pandemic conspiracy theories. Your task is to decide whether the given content is discussing the conspiracy claim: "XXX" 

To code this text, do the following:
- First, read the conspiracy claim and the tweet. 
- Next, decide whether the tweet is relevant to the conspiracy claim, if so, print 0; if not, print 1; if not enough information to decide, print 2. 
- Finally, print your rationale (fewer than 10 words) for the coding decision

Use the following format for output, separating results with a comma:
- text_id, code, reason

Examples 

Input:
    - 39161, deaths from the us civil war averaged about 16 000 per month in just over 4 years in only about 5 1 2 months covid 19 has killed over 135 000 american people which is about 24 500 per month yes it is very serious and no it s not the flu or a hoax whyiwearamask
    - 97971, i suggest trump cultists get the vaccine last because after all covid is a hoax right
    - 76811, conspiracy theory trump s covid was an elaborate hoax used to give trump a chance for a nip tuck facelift he ll come back looking refreshed
Output: 
    - 39161, 0, the tweet is discussing the seriousness of COVID-19 and refuting the claim that it is a hoax
    - 97971, 0, the tweet satirically suggests that Trump supporters should get the vaccine last because they believe COVID-19 is a hoax
    - 76811, 0, the tweet is discussing a conspiracy theory that Trump's COVID-19 diagnosis was a hoax to give him a facelift
```

- todo
    - do CT claims validation with LLMs for other CT claims (unique content >= 10K) using prompt 2, let's do the claim one by one using conversation GPT-4.0, not API service yet

# 20240621 project recap and plan
- Working Plan
    1. claim validation (must do) - what is the most efficienty way to do it? 100 tweets from each category - LLMs is the most efficient way to do it.
        1. tasks: code how many tweets in each category are CT claim relevant. 
        2. provided: CT claim, prompt, and 100 tweets from each category
        3. outputs: coding results of the CT claims relevance. 
    2. I can do the validation via ChatGPT chat interface - have to do it before leaving for China.
    3. contact Jon for the Department GPU for LLaMa 3 usage. `Done`

- todo
1. LLMs validation for CT tweet relevant (the conclusion might be there is a need to do further data collection validation)
    1. randomly sample 10 tweets from one category
    2. prompt the LLMs with the CT claim and the tweet content
    3. ask the LLMs to code the relevance of the tweet to the CT claim
    4. human code the 10 tweets 
    5. compare the results
2. learn how to use LLaMa 3


# 20240619 unmatched claim check
- round 5th, unique no-match-claims: _N = 26,226_
    1. redo the things in `20240615`
- round 6th, unique no-match-claims: _N = 22,186_
    1. keywords missing `flu`, `kill` - added to ct80
    2. check `patent`, `vaccine` keywords list - added ct81
    3. check `cdc`, `kill` keywords list - added to ct76
    4. with only one keyword - `patent` 
    5. check `ivanka` keyword list, `patent`
    6. check `trump`, `bleach` - revised ct19
    7. check `patent`, `hoax` - added o ct80
    8. add `ivanka`, `patent`, `voting machine`, `China`
    9 add `|\b2019ncov\b` to all covid relevant keywords
- round 7th, and two general category: N = 15,853
    10. add `\bhoax\b` to ct82, N = 2,515
    11. add `\bconspira\b` to ct83, N = 1,132
    12. consider there are 275778 unique content (0.5 million uniuqe tweetid), there are 15,853 unmatched unique content, which is 41,049 unique tweetid, accounting for 7.15% of the total dataset. that's acceptable. Let's proceed to the next step. 
- `decision: i will let them go and go to the next validation step`

`twt_en_20240619_claim_coocurrence.csv` is the claim result dataset (with text_id and claim groups). 


# 20240615
- finished
    1. re-do the whole dataset preparation - add all retweets' original tweet into the whole dataset as original tweets
    2. re-do the whole dataset preparation - add reply_to_tweetid and quoted_tweetid and user_id into the whole dataset and keep the links between tweet_ids/reuser_ids
    3. re-do the claim-matching process for the unique content,keywords claim matching is part of the data wrangling only working with the text content. 
    4. for the unmatched content - talking about it in the meeting (review the meeting notes)
- todo
    1. deal with the unmatched content (1) use the links dataset to match again (2) refer back to the meeting notes and preceed next. 


# 20240614
- finished
    - 2nd round ct_keywords match (sampled 10 times 10 rows), unique no-match-claims: _N = 33,735_
        1. DONE - [(r'\bgene\w*\b', r'\bengineer\w*\b|\bmodif\w*\b')], added to ct_4
        2. DONE - add `vax, shot, dose` to all vaccine word 
        3. DONE -  `hoax/hoaxhicks/hoaxerg8`, with `covid/virus/pandemic/corona/vaccine/vax/cdc/flu/liberal/democrat/russian/cv19/mask`, i probably should add `hoax` as a category. 
        4. DONE - `patent`, `(corona)virus/vax/cdc/covid`
        5. DONE - combine ct31 and ct32 as one depopulation one
        6. DONE - add `virus/covid` to ct4, added `\b\w*covid\w*\b|\b\w*virus\w*\b|\bpandem\w*\b|\bcorona\w*\b|\bcv19\b`
        7. DONE - add `kill` to ct71 about the flu
        8. DONE - add `corona` to all virus relevant keywords
        9. DONE - remove the `covid` in microchip one - ct48
        10. DONE - add `republican/democrat`, and `die`, 
        11. DONE - add `covid/virus/` to the `invent` conspiracy claim, ct4
        12. `DONE run it in a seperate round of keyword` - `plandemic/plannedemic/fake pandemic` consider adding this category (add this keyword in the end of the list) 
        13. DONE - add `bleach` to `hydroxychloroquine` claim, ct19, add to `trump` keyword
        14. DONE - `kary mullis` add another claim
        15. DONE - remove `gates` in ct37
        16. DNOE - add a new combination `virus+weapon` to ct1
        17. DONE - add `pandemic` to `flu`ct, ct75
        18. DONE - add `artificial (artificially depressed)` to `cases`, that's ct53
        19. DONE - add `communist` to all china relevant keywords
    - 3rd round ct_keywords match, unique no-match-claims: _N = 33,735_
        20. remove `patent` in ct4; ct32 is about profiting from virus rather than man-made ct
        21. remove `murder` and `kill` in ct75, differentiating from ct54
    - 4th round, ct_keywords match, unique no-match-claims: _N = 19,833_
        22. add more general category, ct78, ct79, ct80. Should be noted that, for the claim analysis, you should use the ct1-77 first, as they are more specific. ct78-80 are more general, think about how to use them. 

# 20240613
- todo: re-run the 80 ct claims and see if the results - how many no-match left, currently there are _N = 66713_


# 20240610 (server down for several days)
- finished
    1. 62 conspiracy theory claims, from 121 fact-checking claims, based on the CT definition and 4 content features. expert coded, with the assistance of GPT 4.0 (June 10, 2024)
    

# 20240606
- finished
    1. finished the fact-checking article collection, and summarized the CT claims, in total 121 fact-checking claims which are CT relevant.
    2. what is a conspiracy theory claim? the relationship between a CT claim and a fact-checking claims - the hypothesis is one CT claim may include multiple fact-checking claims


# 20240601 
- finisihed 
    1. decided to use the `claim` as the study unit. What shall we do next? go to the fact-checking list, and find the corresponding fact-checked claims, and then match them with the tweets - replace the clustering with claim-matching methods. 
    2. how to do claim matching? - i literally have no idea. will look into that, probably will be LLMs assisted task. 

# 20240605
- notes
    1. while preparing for the `claim matching`, I am recollecting the fact-checking articles and summarize their conspiracy theory claims. let's see how many claims can I collect. 
        1. for Snopes, i found a page summarizing COVID relevant CT claims [snope covid](https://www.snopes.com/collections/coronavirus-conspiracy-theories/), it has 22 claims in total.
        2. the work flow is (1) use snopes to search each topic for CT claims as Snope has the best fact-checking topic collection; (2) combine all caims with current claims in the list 


# 20240531
- data demographics 
    1. 542,923 tweets in total where 522,244 unique ids
    2. 332,468 retweets where 62,100 are unique (based on tweetid)
    3. 101,410 replies tweet, where only 1,809 has original tweet contents (the API does not return reply_to tweet content, only reply_to tweetid)
    4. 36,375 quoted tweets, where 1,433 has original tweet contents (same, the API does not return quoted tweet content, only quoted tweetid) _note_ both quoted and retweet may have their own content, while quoted tweet will prioritize user's own content. 

- operation
    1. for original tweets, use the content, N = 71,870
    2. for retweet, use both the original tweet and retweet as content, N = 332,468
    3. for replies, only use the replies as content, N = 108,854
    4. for quoted tweets, only use the quoted tweet as content, N = 29,731

- todo
    1. review the definition of `claim`, let's conceptualize the study unit first 
    2. each CT must have at least one corresponding claim, and the claim fit in your conceptaluization
    3. after this, you should have an idea of the total claim numbers in your dataset 
    4. for `no-match-claim tweets`, sample 100 and know more about the dataset 
    5. for big CT topics like `Qanon`, `plandemic`, you can run Bertopic to find possible claims 
    6. timeline: June 25, finish paper 1, and put on archive, 3 weeks to go! 



# 20240530 study unit
- learning - hierarchical clustering
    - ward, measuring the total within cluster variance. total within cluster variance measures the spread of the data points within the cluster, not similarities. a high variance means that the data points are more spread out from the centroid. 
    - In the context of the 'ward' method in hierarchical clustering, the total within-cluster variance is used as a criterion to decide which clusters to merge at each step. The algorithm chooses the pair of clusters to merge that results in the smallest increase in the total within-cluster variance.
- todo 
    - re-do the 3_Data_Preparation.ipynb for (1) update `vacci` regex, as i read many cleaned tweets are just vacci (2) update claim keywords (3) add a new content column for retweets (including its retweet as contextual information) 

- the goal - is to track the lifespan of a CT claim relevant discussions (tweets). 
    1. Challenge one, many CTs do not have a specific claim, such as plandemic, hoax, deep state, and qanon. topics themselves are CTs
    2. challenge two, many tweets can be classified into multiple claims
- plans for tomorrow
    1. Add context info - differentiate original tweets and retweets; then add retweeted content as context info for retweets, set a new column
    2. re-run theme and claim filters
    3. skip clustering-needed claim/topic, and directly go to the survival analysis for the rest of the claims???


# 20240529
- todo
    - hierarchical clustering with only claims
    - or use Dorian's clustering but figure out the threshold

# 20240528
- finished
    - read Dorian's paper and understand how to evaluate the clustering results
    - ask dorian to share the clustering evaluation code
    - evaluate the clustering results - descriptive
        - problems of dorian's cluster methods: the majority tweets were clustered into one cluster, and the rest scarsly distributed in other clusters. that's not very helpful for the survival analysis.
    - decision on clustering methods
        - cluster by themes
        - hierarchical clustering

# 20240527
- finished
    - clustering rationale
        - the analysis unit should be `ct claims`
        - so, i will cluster the content data based on the `theme`, and use `claim` which is measured by at least 2 keywords as a benchmark for the classification methods. 
        - replicated Dorian's clustering methods, and get the first result
- todo
    - read Dorian's paper and understand how to evaluate the clustering results
    - ask dorian to share the clustering evaluation code
    - evaluate the clustering results (by theme, by claims and by human validation)
    - decide how to optimize the clustering results (cluster by themes?)

 
# 20240522
- finished
    - claim column construction, updated the content into `twt_en_20240522_textid.csv` and `twt_en_20240522_content.csv`
- todo
    - clustering the content data based on topic


# 20240516
- finished
    - theme column construction is fixed
    - `twt_en_20240516_textid.csv` is the latest dataset with text_id and raw meta CT data
    - `twt_en_20240516_content.csv` is the latest dataset with unique text content and themes, ready for clustering
    - `theme` column in `twt_en_20240516_content.csv` contains multiple themes in one cell, seperated by `,`
    - first round of sample validation `twt_en_20240516_samplevali.csv`
        - across 10 themes (without `filmyourhospital`), the CT relevant rate is 0.92 from 100 random samples where 
        - 6 out of 8 CT irrelevant samples are from `china` theme.
        - there is no data for `filmyourhospital` theme (thus, I dropped this theme from the analysis)
            - maybe because of the data processing in the previous steps, but it is not worth it spending more time to figure this out. will just drop this now. 
    - check the `China` theme, did the second time human validation, very good results, all relevant 
    - do the 3rd round of validation, accuracy is 0.96, 4 out of 100 is irrelevant
    - text clean the &amp, &gt characters solved in `3_data_preparation.ipynb`

- todo 
    - clustering the content data
    - data structure for the date and time 
    

# 20240515
- finished
    - `twt_en_20240515.csv` is the latest dataset with all raw CT tweet meta info
- todo 
    - theme column construction is not right

# 20240506 
-  finished
    - all keywords filtering `1_data_collection.ipynb`, done in local machine
    - all language filtering `2_data_cleaning.ipynb`, done in local machine
    - save the result (around 522,231 tweets in total) in `twt_en_20240502.csv`, and uploaded to the server
- todo
    - uploaded the `twt_en_20240502.csv` file to the server
    - write the code `3_data_preparation` to prepare the data for (1) match the keywords again for subthemes, (2) unique content for clustering
    - prepare for the ct classifier

# 20240430 
- `1_data_collection` local running track
- finished (approximately 1 hour per day)
    - 2022-11, 10, 09, 08, 07, 06, 05, 04, 03, 02, 01
    - 2021-12, 11, 10, 09, 08, 
    - 2020-01, 02, 
- downloaded 
    - 2022-

# 20240430
- finished
    - fixed the data structure bug in `1_data_collection`
    - tested both `1_data_collection` and `2_data_cleaning`
    - decided to run the code on my local machine, and upload the data to the cloud 
    - finished `2022-11` data collection and cleaning
    - fixed the code running on local machine, stick to `ipynb` format 
- todo
    - run `1_data_collection` and `2_data_cleaning` on my local machine.

# 20240429
- finished
    - write the function for keyword extraction
    - save the output to a new json file
    - ask Scott regarding the data storage 
        - update: not available at the moment, will run on my local machine month by month; then upload to the cloud
    - test the code `1_data_collection` on one month data 
        - it takes 128s to process 1 day data, processing all data needs 127*30*12*3/3600 = `38` hours approximately. 
        - i ran the code for 2 day data, and it works fine.
        - `Question`: any way to speed up the process? run parallel?
    - add more ct keywords to the list from MPhil thesis (dropped the idea)
- todo
    - write the code `2_data_cleaning` to clean the data and prepare, save the data by month in zip
    - something wrong with the `1_data_collection` output 

# 20240426
- finished
    - language only keep English and chinese data
    - regular expression, finish all regex for keywords list
    - tested the reliability of regex for keywords list
- todo
    - create a `pattern` for the regular expression
    - write the keywords filter into a function
    - save the output to a new json file 


# 20240424 
- todo 
    - keyword extraction 1, keep as much as raw data as possible
    - keyword extraction 2, regular expression to filter out the irrelevant tweets
- finished
    - understand the tweet api data structure
    - understand the [lang code from twitter api](https://devcommunity.x.com/t/unkown-language-code-qht-returned-by-api/172819/)
        - after 2022-06-14, Twitter introduceed some new lang code, indicating tweets only with hashtags, emojis, mentions, media links, and cashtags. 
        - i removed all those tweets based on their API `lang` code, but keep the `art` code, which is emoji only tweets.

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

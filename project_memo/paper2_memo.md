# DSO Paper 2 Memo 2024

## Timeline and Tasks (Updated Jan 29)

### Major Deadline and Task Goals
1. Feb 20 , finish ME and LE on testing dataset 
2. Feb 23, 2-page extended abstract for IC2S2, [IC2S2 submission deadline](https://ic2s2-2024.org/submit_abstract)
3. March 1, a upd   ated memo for DSO milestone - "_Analysis of features that affect misinformation surviving across languages, cultures, countries, and ​​platforms based on the identified taxonomy_"

### Timeline
| Task   | Time Budget| Time Spent  | Start | Finished | 
|--------|:----------:|:-----------:|:-----:|:--------:|
| Topic Extraction (ME) | 5d |  | Jan 29 |  | 
| ME - BERTopic | 3d |  | Jan 29 |  | 
| Linguistic Extraction (LE) |  | |  | |
| LE - NER |  | |  | |
| LE - number |  | |  | |
| LE - emotions |  | |  | |
| LE - vulnerable groups |  | |  |  |
| Narrative Extraction (NE) |  |  |  |  |
| Model Running |  | |  | |
| Figures |  | |  | |
| Writing |  | |  | |
| Pre-print |  |  | | |

### Relevant Documents
1. [Overleaf Writing Document](https://www.overleaf.com/project/6533fee1a120e748186859cb) for DSO paper 2 writing
2. [Original Research Milestone Proposal](https://docs.google.com/document/d/1CuCw9ve-OUZ4xbUoNeiFUcmc6g05w6eSd0Vw82vZkgs/edit) for tracking general project progress.

## Useful Information
### Data Structure (Jan 29)
| Column Name| Example Conetent | Description |
|-------------|-------------|-------------------|
|team_id | 1741 | unique id for the fact-checking org |
|team_slug|check-message-demo |unique string for the fact-checking org (demo account in this case)|
|media_id |117489| unique id for the specific media (text, image, video, audio). Exact duplicates will have the same id (can be used to infer which media is the most prevalent) |
|media_text |Test August 16th - 1| text if the media is text |
|filename | empty | ignore |
|media_url| empty | URL if the media is image, video, or audio|
|pm_id |129076 | unique id for the media in the specific team |
|wa_id |d09bf7030afb0f7edaef3c61 |id for the author|
|claim_type|Claim|type of media (Claim = text, Link, UploadedAudio, UploadedVideo, UploadedImage)|
|link_url | Anonymous| link if claim_type is link |
|current_status_user|caio-almeida | `user who last updated the status of the fact-check`|
|current_status|verified | rating|
|report_status|published| whether a fact-check has been published|
|pm_url | https://checkmedia.org/check-message-demo/media/353158|url to the item, you won't be able to access this
|pm_created_at| February 14, 2022, 12:03 AM | time the item was created
|deleted| 0 | whether the item has been deleted
|smooch_message| {"_id": "620a655dfa77bf00ed369a9e", "name": "Caio Almeida", "role": "appUser", "text": "1\n⁣1\n⁣https://www.nytimes.com/2021/12/13/health... | JSON representing the raw message. The "text" has a longer conversation|
|smooch_created_at | February 14, 2022, 2:21 PM | time the message was created |
|claim_id | 3,720 | unique id for the claim |
|claim_description | New Covid-19 Pills Carry Risks | Claim that is being fact-checked as written by the fact-checking org |
|fact_check_title | New Covid-19 Pills Carry Risks: What Patients Should Know | title of the fact-check|
|fact_check_summary| The first Covid-19 antiviral pills... |summary of the fact-check
|fact_check_url| empty| URL to the fact-check if published (optional)|

## Daily Updates
Summarize the work done on each day
### Jan 29
- Tasks Finished
    1. proof-read the overleaf writing document 
    2. scheduled the paper 2 working plan (all updated in this memo)
    3. check the data structure from the sample data _Check demo test workspace_ 
        1. read json file into pandas dataframe
        2. check the language distribution of the sample data `json`  file

| language | count |
|----------|-------|
|en    |   1509|
|pt_BR |   50|
|pt    |26|
|es    | 21|
|hi    | 7|
|te    | 2|
|ar    | 2|
|fr    | 2|

- Challenges Faced
    - maybe the data is a bit small for the topic extraction
- Next Steps
    - ask Scott for more data?? 
    - check sample data - csv file and see if there is any difference

### Jan 30 
- Task Finished
    1. check sample data - csv and json file - they are the same, N = 1,620
    2. revise the memo and reply to Scott on Slack.
- next steps
    1. ask Scott for more sample data
    2. add the definition of "narrative changes" in the writing doc for RQ2.2

### Feb 2
- Task Planned
    1. add the definition of "narrative changes" in the writing doc for RQ2.2
    2. add more sample data from the coding tweet dataset
    3. check potential datasets: fetch folder, misinfo_tweet.csv, and paper1 manual dataset 
- Task Finished
    1. asked dorian for the data and clustering result 
    2. 
- Task Next
    1. Sample dataset questions
        1. claim_type: do I need to collect the linked textual message?
        2. current_status: remove `report-true`? and what is the difference between `verified` and `true`?
        3. do i need to cluster the same misinformation claim ? feel like the current category in the dataset `claim_description`, many rows do not have this information?
        4. possible data (1) dorian's clustering result + match back included linked text (2) fetch data from Meedan? 

### Feb 5
- Task planned
    1. add the definition of "narrative changes" in the writing doc for RQ2.2
    2. use `crosslan_mutation0331.csv` to do the topic extraction
    3. understand the `demo data` better and write code to clean the demo, making it ready as `crosslan_mutation0331.csv` to be used for other tasks
- Task Finished
    1. BERTopic on the demo data in `bertopic_pipeline.ipynb` 
        1. big picture & basics - go through the the [best practice of using BERTopic](https://maartengr.github.io/BERTopic/getting_started/best_practices/best_practices.html) 
        2. step 1-7 in the best practice
- Task Next
    1. add the definition of "narrative changes" in the writing doc for RQ2.2 [Feb 6 am] 
    2. Step 8-9 in the best practice [Feb 6 pm]
    3. apply a python script to the demo data - finalize your goal and method approach (current challenge). 

### Feb 6
- Task Finished
    1. add the definition of "narrative changes" in the writing doc for RQ2.2 [Feb 6 am] 

### Feb 7
- Task Finished
    1. Step 8-9 in the best practice [Feb 6 pm]
    2. apply a python script to the demo data - finalize your goal and method approach (current challenge).
    3. finish meeting preparation

### Feb 9 Scott Meeting - BERTopic
- Methods. Bertopic
    - Step 1.1 illustrate the idea data format - run t-test to see whether there will be group difference on each extracted topic
    - Step 1.2 data proprocessing - clean the data and remove the stop words
        - go through the data cleaning part
        - remove urls? - solved by using text_claims
        - stop words? - not for embeddings 
        - emojis - keep for now
        - non-informative submissions (e.g., _"check this out - url"_ or _"is this true"_)? so many of them - MAYBE they will be grouped into one topic, and should remove later
    - Step 1.3 embedding and clustering - not too many questions
    - Step 1.4 model evaluation
        - outliers?
        - metrics?
        - human evaluation - will be subjective 
    - Step 1.5 comparison
        - whether there is statistic difference on extracted topics between mono-lingual and cross-lingual groups
- Methods (10 days)
    - NER - try 
    - Numbers - dictionary? ask
    - Emotions - dictionary
    - Vulnerable groups - GPT-4?
    - Rhetoric Features - GPT-4?
- timeline - Feb 20 preliminary results on the testing dataset-

### Feb 12 
- Task finished
    1. match-back dorian data as the demo data
    2. get results for BERTopic modelling
    3. start writing the BERtopic python script for the real data
- Task to be done
    1. asked Dorian about the 0.0 cluster in each threshold and the number of clusters in each threshold. 

### Feb 19
- Task finished
    1. asked Dorian about the clustering python script
    2. get the results for BERTopic modelling

### Feb 20
- Task finished
    1. finish representation model with GPT-3.5 labelling
    2. 3 times iteration trail bertopic model
    3. get the results 
    4. run the t-test on the results 
- Task to be done
    1. bertopic visualization
    2. bertopic evaluation metrics

### Feb 21
- Task finished
    1. bertopic visualization
    2. bertopic preliminary interpretation
- Task to be done
    1. numbers (Thu + Fri)
    2. LLMs (Sat) 

### Feb 23 
- Task finished
    1. GPT-4 for NER, numbers, emotions, and vulnerable groups
- Notes
    1. GPT-4 for coding - 10 tweets works best for each request
    2. emotion is not accurate - mainly hallucination issues, it will forget the coding category
        - use function calling 
    3. vulnerable groups - not accurate, but can be used as a reference (use subjects probably is more better, subject of the action instead of using the normaltive words)
    4. numbers - very accurate, but can be used as a reference
    5. NER - pretty okay
    6. unpredicted results - the model will not return the result of all input (token limit?)
    
### Feb 27 GPT token limit for LLMs - MFT project, paper 2.5
- token N = 5511 in total for 50 records
- prompt Token N = 3,105 (500 for system prompt)
- completion tokken N = 2,406 (50 records, this is very predictable, 48 tokens per record output)
- GPT-4 completion token limit is 4096 tokens, which is about 135-50+1 = 85 records per request
- in theory, GPT-3.5 turbo completion token limit should also be 4096, however, it happened to me onnce that the token limit is only 2,448, which is 185-135+1 = 51 records, per request _weird, why 3.5 limit is lower than 4?_

Actually, here is a detailed token limite  
| Model | input token Limit | Output token limit | appro Records |
|-------|-------------------|---------------------|---------------|
| GPT-4 | 128K | 4096 | 85 MFT |
| GPT-3.5| 16K | 4096 | 85 MFT |
| GPT-3.5| 16K | 2448 | 51 MFT |

### Feb 28 
- Task finished
    1. prevalence - how likely the linguistic entities will change within the same misinformation claim across tweets
        1. prevalence1 - how many misinformation include numbers?
        2. prevalence2 - among the claims with numbers, how many are multilingual?
        3. difference3 - among multilingual claims with numbers, what's the change different between monolingual and multilingual pairs 
    2. same to NER, volunerable groups, and emotions
    3. note regarding the `dorian_scott_paper1_data0219.csv` and `dorian_scott_paper1_data.csv`
        - there are only 500 identical records in the demo data, however, more tweets when i drop duplicates grouped by tweetid. It means many tweets are duplicated across groups. meaning, multiple fact-checking articles are cross-checking the same piece of misinformation tweet. technically speaking, they should be the same misinformation claim thus clustered in the same cluster, but somehow they are not. well, not too many, only 20ish, can be seen as outliers.
    4. save the chi2 test result to a table 

    | Variables  |Numbers | NER | Vulnerable Groups | Emotions |
    |------------|--------|-----|--------------------|----------|
    | prevalence 1 | 37.70%  | 89.26% | 18.55% | 1 |
    | prevalence 2 - mono | 60.32%  | 96.83% | 25.40%| 99.20% |
    | prevalence 2 - multi| 68.85%  | 98.36% | 40.98%| 1 |
    | Chi-Square (df) |3.45 (1) | 6.54 (1) | 0 (1) | 14.32 (1)|
    | p-value | 0.06 |0.01 | 1 | 0.00 |

    5. output the difference to a `ic2s2_pairwise_comparison0228.csv` file 
- Task todo 
    1. start writing the IC2S2 abstract
    2. make another figure to illustrate the mutation pattern across languages with 2 examples 


### March 2
- Task finished
    1. write the IC2S2 abstract
    2. make tables and figures

### March 3 
- Task finished
    1. proofread the IC2S2 abstract
    2. Meeting with Dorian and sort out the clustering task and paper plan
    3. exchange demo dataset and relevant codes

### March 7
- Task finished
    1. finish wrapping up Bertopic code to be used for the real data (Friday???)
    2. discuss the abstract and paper plan for meeting tomorrow (Thursday???)

### March 8. Paper 2 Project Kick-off

1. What we have done so far
    1. BERTopic on the demo data
    2. GPT-4 for NER, numbers, emotions, and vulnerable groups classification
    3. IC2S2 abstract, also the paper framework 
2. what we need to do next 
    | Section    | Tasks  | People | Time Estimation | Results   | Progress |
    |------------|--------|--------|-----------------|-----------|----------|
    | Methods 1  | claim clustering | Dorian | March 7 | .py apply to real data | done |
    | Methods 2  | Bertopic | Calvin | March 15 | .py | ongoing |
    | Methods 3  | Classification tasks | Calvin | `discuss` | .py | ongoing |
    | Methods 4  | Qualitative Analysis? | Calvin | March 30 | `discuss` | ongoing |
    | Methods 5  | Data analysis | Calvin | 1 week |  `discuss` | yet to start |
    | Methods 6  | Visualization | Calvin | 1 week | - | yet to start |
    | Writing Up | full paper | Calvin |  | 1 week | yet to start |
    | Code Review| full paper | - | 1 week |  - | yet to start |
    | Proof-read | full | all | 1 week | `discuss` | yet to start |
3. Milestones and Timeline
    1. March 30, finish all methods part
    2. April 30, finish Y2M3 and Y2M5 project goals 
        - Y2M3, Feb 2024, Analysis of features that affect misinformation surviving across languages, cultures, countries, and ​​platforms based on the identified taxonomy
        - Y2M5, April 2024, Test the effectiveness of factors to predict misinformation mutation and diffusion across languages and platforms in different situations. Analysis will examine three multilingual situations: (i) within platform, cross-lingual spread, (ii) cross-platform, single-language spread, and (iii) cross-country spread.

### March 19
- Task finished
    1. taiwan fact-check data cleaning - not yet, the loop does not work 

### March 20
- Task finished
    1. taiwan fact-check data alignment
    2. clustering code tested with new data
    3. dataset column description and alignment
- Task to be done
    1. bertopic code
    2. sharing prompts for GPT-4

### March 21
- task finished
    1. bertopic - embeddings at scale
    2. bertopic - workplan
- task to be don
    1. bertopic - trails 
    2. bertopic - content, id, and prob, export

### March 25 Bertopic writing
- task finished
    1. bertopic - content, id, and prob, export, how to save to pickles
- task to be don
    1. bertopic - try parameters
    2. [evaluation metrics, score](https://github.com/MaartenGr/BERTopic/issues/428)

Decision - I used bertopic default setting to find topics, for outliers, I just kept them in the -1 cluster. 

First tried no dimension reduction on sampled data, the results is very bad. across 4k datapoints, there are only 3 clusters where half of datapoints are outliers. therefore, it sugggests we should employ dimension reduction methods. 

Second, what dimensino reduction methods should be used? I selected three popular methods: PCA, SVD, and UMAP for testing for their effectiveness, scalability, and interpretability. PCA is faster to train and perform inference due to its linear nature, it is easy to implement and computationally efficient. truncated SVD is well-suited for sparsed dataset and is robust in handling noises. UMAP excels in preserving both the local and global structure of the high-dimension data which is crucial to capture nuanced relationships between misinformation. it also provides a good balance between computational efficiency and flexibility. 

In the test, UMAP more capable of capturing nuanced topics than PCA and SVD under the default setting (98 topics, 5 topics, and 2 topics). While all methods showed similar robustness in handling noises (amost 1/2 of data points are outliers). Also, results from UMAP are more interpretable than PCA and SVD. Though UMAP is much slower than PCA and SVD, it is potentially more scalable as we can use `cuML` to speed up the computation through GPT cacceleration. Therefore, I will keep dimension reduction and use UMAP the task for the bertopic model.

Third, for the cluster methods, we decided to use HDBSCAN rather than other clustering methods such as K-Means  as (1) it is quite capable of capturing structures with different densities (2) it is an explorative methods without pre-specifying the number of clusters, (3) scalable to large datasets with `cuML` via GPU accceleration.

Then we gonna try different parameters for UMAP and HDBSCAN to find the best combination for the bertopic model.

validations - we will use the same validation methods as the original bertopic paper, silhouette score, coherence score, and topic distribution.    

### March 27
- task finished 
    1. bertopic - try parameters: neighbors,components, min_cluster, min_sample, nr_topics (reduction)
    2. evaluation scores: silhouette_score, topic_diversity_score, coherence_score


evaluation 1. see [Bertopic VS CTM VS Top2Vec](https://wandb.ai/vsharifian/FYP%20OCTIS/reports/BERTopic-vs-CTM-vs-Top2Vec--VmlldzoyNDg4NDk1). Interesting to see the comparison between Bertopic and CTM as both of them support multilingual. Bertopic is better. 

evaluation 2. now we use bertopic, we chose three evaluation metrics to do the hyperparameter tuning - [topic coherence](https://github.com/MaartenGr/BERTopic/issues/90) with [GENSIM package](https://radimrehurek.com/gensim/models/coherencemodel.html), [silhouette score](https://github.com/MaartenGr/BERTopic/issues/428), and [topic diversity](https://github.com/MaartenGr/BERTopic/issues/627).

for hypterparameters tuning, we will use the following parameters:
1. `min_topic_size`, with 1 million doc, it should be set as 100-500 
2. `nr_topics`, tricky one, it specifies, after training the topic model, the number of topics that will be reduced. can set this to `auto` for efficiency
3. `n_neighbors`, increasing this value often results in larger clusters being created. by default is 15. try 15-25
4. `n_components`, by default is 5, increasing it will keep more dimensional data. try 5-15
5. `min_cluster_size`, by default is 10, minimum size of a cluster and thereby the number of clusters that will be generated. Increasing this value results in fewer clusters but of larger size. try 10-20
6. `min_samples`, by default is 1, the number of samples in a neighborhood for a point to be considered as a core point. Increasing this value will result in fewer clusters but of larger size. try 1-5

### March 28
- task finished 
    1. prompts for paper 2, shared on [google colab](https://colab.research.google.com/drive/1yflSE3cSrtnZSBLJ03qm7sabUTcPWkPg?usp=sharing)
    2. Paper 1, proofread

### April 4
- task finished
    1. bertopic - topic coherence, 
        1. replaced with labse tokenizers. it does not improve the score much. labse tokenizer is not very good at Chinese characters in the sample data. and it is also a challenge to remove stop words and punctuations in multiple languages.
        2. used `c_v` sliding window instead of `c_npmi` normalized pointwise mutual information for the coherence score. this indirect confirmation measure returned a better score than npmi.
    2. `1_data_prep.ipynb`, `2_embedding_clustering.ipynb` and `3_bertopic.ipynb` are ready to be used for the real data.

### April 5 LLMs selection
#### Candidates
- GPT-4 (not open)
- Claude 3 (not open)
- Replicate - Cloud API service for running open source LLMs, includnig LLama 2.0 and 
    - [Mistral AI ](https://mistral.ai/news/mixtral-of-experts/)
        - cons: It handles English, French, Italian, German and Spanish.
    - LLMa 2.0 (open sourced)

#### Pricing
| Model | input token (1M) | Output token (1M) | notes|
|-------|-------------------|-------------------|------|
| GPT-4 | $10 | $30 | - |
| Claude 3 | $0.25/3/15 | $1.25/5/75 | light-medium-powerful |
| Replicate - Llama2 | $0.65| $2.75 | 70b |
| Replicate - Mistral AI | $0.30| $1.00 | 8*7b v1.0|
| Replicate - cloud service | $20.88/hr |  | 8GPU*48G, 680G RAM|
| command - from co-hear (word of mouth recommendation)|||worth testing|

Simple Budget Calculation with the demo data
- 1 piece of misinfo include: 555 prompt tokens, 27 misinfo tokens , 145 output tokens
- For best performance of __GPT-4__, we can input at most 50 piece of misinfo with 1 prompt. beyond that, the hallucinatino issue will be more severe and the model will forget the coding category and won't return results in required format. 
- So for GPT-4
    - Budget (555+27*50)*(10/1000000)+(145*50)*(30/1000000) = `$0.0008` per 50 misinfo records (per request)
    - Time - pretty fast, but it has 5,000 request per min
- other LLMs are generally cheaper. Open sourced LLMs are more than 10 times cheaper than GPT-4 on _Replicate_. Claude 3, depending on the model, can be 3 times cheaper or 2 times more expensive.  

- 20240415NOTEs: 2 A100s GPU with 80G momory each, OII department server resources

### April 7 Confirmation Timeline

Goals 
    1. Intro rewriting
    2. literature review chapter 
    3. paper 1 - full paper
    4. paper 2 - full paper 
    5. paper 2.5 - full paper

timeline
- April 19-30 paper 1 full paper 
    - methods redo
- May 1-30 paper 2 
    - waiting for real data result 
    - and LLMs 
- June 1-30 paper 2.5 

### April 11 Paper 1
the internet is very unreliable at the hotel, can not access OpenAI service and the other LLMs (super super low). So i shift my focus to my paper 1 

- Data collection 
    - ct claims tweet sample - found 6, and there are 61-6=55 left, can find it later
    - revised the keyword list 
    - 
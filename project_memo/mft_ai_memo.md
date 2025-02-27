# Project Memo
## Project General Info

## Project Memo
markers: ✅ done; ✔️ ongoing, ❌ not yet; ❓ to-be further discussed


### 2024-11-25
- done
    - ICWSM manuscript revision, finished until `Local language dictionaries`
    - slides `thesis overview` for dphil seminar this week
- todo
    - ICWSM manuscript revision, the rest
    - slides the rest 

### 2024-10-15
- done
    - updated llama3.1-8b performance table
    - re-running llama3.1-70b model and llama3.2-1b and -3b model
    - format the all table   
- todo
    - discussion section writing
    
 
### 2024-10-14
- have to double check all llama3.1 results in oii-brains, there must be some regular expression errors. because for the `ft-none-en` model, the model coverage is better than fine-tuned models. 
- todo
    - update the llama3.1 performance table
    - write discussion section

### 2024-10-10/11
- revise the document
    - changed where Scott left remarks
    - add more details in the data section for each benchmarking dataset.
- finish writing
    - data section
    - approach evaluation section
    - result: machine translation, local dictionary, xlm-t
- todo
    - result section: llama3.1
    - discussion section
    - abstract
    - figures - any way to make some goog figures???
    - tables double check 

### 2024-10-08/09
- finetune llama3.1-8b
  - Done
    - finished batch finetuning
    - with more local language training data (50 record each batch, there are 20 batches), the llama3.1 performance is actually not better, but worse (wonder why)
      - try trained with 200 record, same results.
  - todo
    - write up the result and experiment details 

### 2024-10-04/05
- finetune llama3.1-8b
  - Done
    - successfully ran the unsloth whole process on the test data
    - llama3.1 train with english data + english prompt
    - llama3.1 train with english data + chinese prompt
  - todo
    - translate english training data to chinese with machine translation
    - llama3.1 train with english data + translated chinese data + chinese prompt?
    - llama3.1 train with english data + translated chinese data + local labelled batch data + chinese prompt?
  

### 2024-09-24
- redo the random guess baseline model for 3 benchmarking datasets
- finish adding table results for machine translation, local dictionary, multilingual models and batch training graph, to the overleaf
- add llms table to the google drive 

### 2024-09-23
nothing

### 2024-09-22
- finished training all xml base models and batch training models
- add xml result to the scott's server. 

### 2024-09-20
- damn, model inference does seem right, 0 accuracy on 5 out of 5 models, something must be wrong.
- fuck, after 8 hours, it turns to be the training data column names - it is `label`, not `labels` in `xml_base.py` line 98, cao .
- started re-train the model, start from `sanctity` base one, as it has the least working load. 
      - did following 2 changes to be more conservative approach: (1) undersampled the majority class; (2) left 10% as in-sample test data to test first.
  


### 2024-09-19
- finished all binary model training and inference, and batch training, yaay!!!!

### 2024-09-18
- finished training `authority` and `fairness` base model
- started training `loyalty` and `sanctity` base model
- `care` base model is still on-going training. 

### 2024-09-17
- multilingual sentence embedding model training with english annotated data and local-lan labelled data
    - get the english annotated dataset ready in oii-brain
    - did the frameAxis with multilingual contextual embeddings - does not perform very well
    - have to re-do the word-embeding experiment, because `xml-multilingual` is a contextual embedding model which actually does not perform well for word embeddings. 
        - load multilingual word embedding model from [fastText](https://github.com/facebookresearch/fastText/blob/master/docs/crawl-vectors.md)
        - finished simple similarity embedding methods as Josh did with `fasttext`, did it in oii-brain
        - finished frameaxis embedding with `fasttext`, did it in oii-brain. The difference between them is how document similarity is decided: Josh, average all word embeddings in the doc and compared to the axis; FrameAxis, compare every word to the axis and average the doc.
        - decide to keep the `xml-multilingual` embedding result, but prob won't go into the main doc, it does not perform very well. technically speaking, it should, as it provide more contextual information in the document tokenization. 
    - started training `xml-multilingual` model on 3 gpus on oii-server, `care`, `authority` and `fairness`. each task may take 20 hours-ish to train on a L40S GPU. damn - keep training, 
    - the fine base models may take more than 1 day to train on. why it is so slow? last time for the multi-label model, with 1/3 less training data, it took about 2 hours to finish training. 
    - then the batch training should be faster as i have batches. 

### 2024-09-16
- frameaxis with cmfd2
    -  updated cmfd2 with sentiment, as FrameAxis needs sentiment to compute the microframes, so sentiment can not be random, i used a bert model to assign sentiment to CMFD2
    -  however, still only result in 14 out of 5k documents, trying to fix the bug
    -  bug fixed, with all comments saved in the `e_tool_lexicon.ipynb` file
    -  finished `cmfd2 frameaxis` experiment and result report - performance is super poor.
- Todo
    - re-train the new multilingual models with binary settings (instead of using a multi-factor classifier)

### 2024-09-15
- frameaxis with cmfd2
    -  updated the multilingual word embedding model, made the script run
    -  however it only return limited data
    -   

### 2024-09-12
- scott server
    - start a new folder `paper_linked_final` to synchronize all coding files with the overleaf writing project
    - checked all datasets and synchronized with the writing `section 3 Data`
    - check experiment `machine training`
        - added results from MoralStrength, with (1) lexicon result and (2) svm ML model + MoralStrength features result
        - added results from MoralBert

### 2024-09-10 
- overleaf writing - section dataset
- code review - all benchmark and training datasets.
- todo
      - overleaf experiment section writing - machine translation

### 2024-09-09
- notes
    1. goal: want to fine-tune the llama3.1 with local language data with `simplifine` package
        1. can not do it on oii-brains due to package conflicts `ImportError: cannot import name 'SentenceTransformerTrainingArguments' from 'sentence_transformers' (/home/scro4316/.local/lib/python3.10/site-packages/sentence_transformers/__init__.py)` highly likely is the python version
        2. can not do it on scott's server due to python version `3.9.12`, the package requires `3.10.0` or higher
        3. github codespace support it, though there will be limitations on storage and other stuff, and the documentation of the package is not clear, so i sent an email to Ali asking for help. 
        4. meanwhile, i can explore fine-tune llama3.1-70b on oii-brain with other packages. started with [llama2 example](https://colab.research.google.com/drive/1ggaa2oRFphdBmqIjSEbnb_HGkcIRC2ZB?usp=sharing#scrollTo=ZgaKTaF7bmHg)
            1. error - `from transformers import pipeline` - downgraded to `pip install transformers==4.34.1`, now it works on the oii-brain
- done 
    1. overleaf intro writing and related work section intro writing
- todo
    1. overleaf related work section 2 writing
    2. overleaf experiment section writing

### 2024-09-08
- Done
    - update the regular expression data cleaning code for llama3.1 results in `/data/scro4316/thesis/paper3/e3_model_report.ipynb`. 
    - ✔️ update the results for chinese prompts for llama3.1 in scott's server. 

### 2024-09-06
- Done
    - ✅report current results to Scott [updated 0831 report](https://github.com/calvinchengyx/llms_mft_multilingual/blob/main/report0831.ipynb)
    - ✔️E4.1.2 Llama 3.1 - fine-tune with Chinese prompt (on-going)
- Todo
    1. Check the model performance drop, why, do the subsets descriptive statistics check
    2. Finalize the baseline model
    3. ⭐ Put current results into words, write the overleaf document
    4. Add two more literature into the related work (1) moral strength (2) moralbert - think if i should add them to the current paper
 

###  Research Quesitons
RQ: what is the best approach to measure moral foundation values from non-English texts?

Conditions:
1. mass annoated English social media data 
2. wait-to-be-inferred non-English social media data

Use Chinese as a non-English language example in the experiment 

### Datasets 
1. Benchmark datasets:
    1. [Chinese CoreValue dataset](https://docs.google.com/spreadsheets/d/1Zg0mKH5rK9RpVSf61P6nI6vSdxLsp5HW/edit?gid=2050980407#gid=2050980407)
        1. labelled by crowdworkers *(N = 7K)*
        2. not strictly labelled by MF framework but traditional Chinese values
        3. no non-moral records
        4. 20% for testing
    2. [Chinese moral situations](https://docs.google.com/spreadsheets/d/1Ao7TmRC66xLz6KfYi58wWfae5CpmWbXHEEB15Flua_c/edit?gid=1934023418#gid=1934023418)
        1. reverse-labelled data - given lable asking crowd-worker to come up with moral relevant sentenses/senarios
        2. 200 for each moral foundation values (*N = 2K*)
        3. no non-moral records
    3. [moral foundation vignette](https://docs.google.com/spreadsheets/d/1fUeIth_CiIjB2ZqeL3Pra5Rp9PEF2XesLNxwChvTZ4M/edit?gid=779424641#gid=779424641)
        1. lab-designed moral scenrios by psychologists,(*N=90*), english labelled data
        2. no non-moral records
2. Training datas
    1. English labelled data
        1. [reddit]() - english labelled data
        2. [twitter]() - english labelled data
    2. Chinese labelled data: 80% of "Chinese CoreValue dataset"

### Experiments
1. E1. Dictionary 
    1. ✅ English Dictionary: MFD, MFD2.0, e-MFD
    2. ✅ Chinese Dictionary: C-MFD2.0
2. ✅ E2. Dictionary with word embeddings: FrameAxis with MFD, MFD2.0, e-MFD
3. ✅ E3. Mformer with translated data
4. ✅ E4. small language models XML-T with labelled data
    1. ✅ E4.1. XML-T trained with English data (138min on A100 GPU) - base model 1 
    2. ✅ E4.2. XML-T with machine-translated Chinese data (from English labelled data) - base model 2
    3. ✅ E4.3. XML-T base model 1 + local-language annotated data, cumulative training
    4. ✅ E4.4. XML-T base model 2 + local-language annotated data, cumulative training
    5. ✅ E4.5. XML-T base model 1 + local-language annotated data, independent training
    6. ✅ E4.6. XML-T base model 2 + local-language annotated data, independent training
5. E5. LLMs - Llama3.1
    1. ✅ E4.1 Llama 3.1 - instruct tunning only
        1. E4.1.1 Llama 3.1 - fine-tune with English prompt
        2. E4.1.2 Llama 3.1 - fine-tune with Chinese prompt (on-going)
    2. ❌ E4.2 llama 3.1 - fine-tune with local language data
    3. ❓E4.3. XML-T with English data + LLMs laballed data
    4. ❓E4.4. XML-T with English data + LLMs generated data ❓
    5. ❓E4.3 Chinese LLMs (e.g., Qwen2) `low priority`
    6. ❓E4.4 fine-tune a LLMs with local language data, small amount + big amount - `Calvin` with Simply fine-tune API


## Time Table
| Tasks | Time Budget | Track | Comments |
|----------|----------|----------|--|
| Preparation | 1 w(July 16-31) | Done - Aug 5 | 1 week late |
| Research Design | 1 w | Done 12 | on time |
| Experiment | 2 w | Aug 12 | Aug 30, revise e4|
| Data & Methods | 2 w | Aug 13 | Aug 30|
| Tables | 1 w | Aug 30 | |
| Writings | 1 w | not yet | Sep 6-7 |
| Review | 1 w | not yet | |

* Time Budget: 8 weeks (July 16 - Sep 10) to a preprint
* Track: ✅Done, ✔️ ongoing, ❌ not yet
* Brainsotrming Space: Offline notebook, blue cover
* Writing Space: [Overleaf: mft_llm project](https://www.overleaf.com/project/65ba2d37f330dedd654f3d80)
* Coding Space: [Github: mft_llm project](https://github.com/calvinchengyx/llms_mft_multilingual/tree/main)
* Figures Space: [Google Drive, Calvin2 account](https://docs.google.com/presentation/d/1WcGAvQSATJPhp3w03Urd8tsVYDelvLItUtyzvcdh6Kw/edit?usp=sharing)


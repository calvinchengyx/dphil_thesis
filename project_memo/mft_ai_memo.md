# Project Memo
## Project General Info

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

## Project Memo
markers: ✅ done; ✔️ ongoing, ❌ not yet; ❓ to-be further discussed

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

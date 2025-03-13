# Confirmation document

- overleaf address: [link](https://www.overleaf.com/project/66dad84696ec592b2669479e)
- submission deadline: before Jan 31, finish all coding and analysis
- document start from: 2025 Jan 01
- general plan
  - Jan 01-10 data preparation
  - Jan 11-20 data analysis 
  - Jan 20-31 results and figures 
  - Feb 01-28 writing (finish writing before HT)
 

# writing logs

## 20250313 - stick to the plan
after talking to dorian a couple of times, I was planning to do the mutation on the semantic level, not the thread level, because, the thread level mutation, is simple just replies and quotes. not the narrative, but that's okay! stop adding extra work to the thesis. Use the narrative flow/mutation in the next paper, not this one, just stick to the thread level longitudinal analysis. stick to the research plan, be determined, anchor yourself here. Next tasks is to finalize the research plan plot, draw it out. 

## 20250311 - mutation unit
Dorian made a brilliant point regarding claim-change measurement. the current approach is i used claim ids to estimate the thread lifespan. but, the potential risk is, so retweet per se does not change the content, content only change when it is a reply or quote, and when someone reply/quote the tweet, it almost guarantees the content change; also, it adds a timestamp to the thread, guranteed the extended lifespan of the tweet. that is, the two factors "claim change" and "thread lifespan" are determinsitc to some extent? is that correct? 

my current approach regarding the method is to use a cox time-varying model, `shift` the metadata of the tweet, that is the end time of each interval is the tweet original timestamp, the start time is last post's time. the death of a thread is defined as the no retweet/reply/quote for 30 days. 


## 20250205 - RQ2
- done
  - decide to buy LIWC22 for lexcion level mutation
  - understand how spacy work for svo extraction with a tutorial
- todo
  - for s-v-o extraction tasks, try three options with your `texts` sample (N=30) data
    - option A. spacy with open-sourced llms - this is a limitation with SpaCy integration llms, for opensourced ones on huggingface, it only support limited models until June 2024, tried `dolly-v2-3b`, worked even worse than the basic spacy model
    - option B. run latested LLMs without SpaCy, let's try llama3.1, with prompt engineering, GPT-4 returns pretty good results
    - option C. spaCy without llms - run its trained English model - do this as a baseline (basically i am comparing two models) 

## 20250128 - RQ1
- done
  - RQ1.1 with all KM test
  - RQ1.2.1 cox model with mutataion as a non-time-variant variable, less informative but okay
  - RQ1.2.2 `CoxTimeVaryingFitter()` data format
  - RQ1.2.2 `CoxTimeVaryingFitter()` the convergence issue, error message: hessian or gradient contains nan or inf value(s). - fixed
  - so, RQ1 all done so far.

> RQ1 mutation conclusion: within the same language, content mutation will contribute to longer CT claim lifespan. This effect is more sailent in smaller threads than bigger ones. 

## 20250107 - strategy thinking
done
- finished testing [fenestra](https://github.com/Roychowdhury-group/FENESTRA-Fake-News-Structure-and-Threat-Assessment) code from Tanghilini's team.
  - decision: give up, can not be directly replicated/applied
  - reason: outdated, many packages are not available anymore
  - plan: switch to spacy + LLMs strategy
- finished reading key literature
  - Tanghilini's work for CT narrative [Bridgegate, Pizzagate and storytelling on the web](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0233879) and [COVID-19 conspiracy theories pipeline](https://link.springer.com/article/10.1007/s42001-020-00086-5).
  -

Todo 
- finish reading some NLP's work in ct narrative detection [Mapping the narrative of covid conspiracy](https://dl.acm.org/doi/10.1145/3400806.3400828)
- streamline your project workflows: three levels of analysis: psycho-linguistics  

## 20250101 - data prep
done 
- finished importing covid-19 twitter data Chinese
- finished uploaded Mohsen's conspiracy data

Todo - may take 1 week todo 
- structuralize Mohsen's conspiracy data, from JSON to csv files, do it platform by platform


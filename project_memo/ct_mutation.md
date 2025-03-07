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


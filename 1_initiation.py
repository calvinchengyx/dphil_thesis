import transformers
import torch

def setup_pipeline(model_id):
    """Set up the text classification pipeline with specified model and precision."""
    return transformers.pipeline(
        "text-classification",
        model=model_id,
        model_kwargs={"torch_dtype": torch.bfloat16},
        device_map="auto"
    )

def prepare_prompt(pipeline, messages):
    """Prepare the prompt for the model using the given messages."""
    return pipeline.tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

# define the temperature to be more decisive
def generate_text(pipeline, prompt, max_tokens=512, temperature=0.2, top_p=0.9):
    """Generate text based on the given prompt."""
    terminators = [
        pipeline.tokenizer.eos_token_id,
        pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]
    return pipeline(
        prompt,
        max_new_tokens=max_tokens,
        eos_token_id=terminators,
        do_sample=True,
        temperature=temperature,
        top_p=top_p,
    )

if __name__ == "__main__":
    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
    message = [
        {"role": "system", "content": "You are a qualitative coder who is annotating tweets related to the COVID-19 pandemic conspiracy theories. Your task is to decide whether the given content is discussing the conspiracy claim: 'mask is a hoax'. To code this text, do the following: First, read the conspiracy claim and the tweet. Next, decide whether the tweet is discussing relevant the conspiracy claim, if so, print 0; if not, print 1; if not enough information to decide, print 2.  Finally, print your rationale (fewer than 10 words) if it is not 0. Use the following format for output, separating results with a comma: text_id, code, reason"},
        {"role": "user", "content": "255305	wonder how many republican deaths it will take before they admit covid is not a hoax and start taking it seriously please mask up; 202370	me and my wife we also wear masks everywhere in a county in missouri which could give a shit about covid half still thinks it s a hoax they love to chant let s go brandon here smh; 83399	while trump golfed played games claimed the virus was a hoax held pep rallies denigrated anyone who wore a mask shut down the cdc reporting because he didn t believe it how many people have gotten sick and or died because of his 2 month hiatus from seeing what happending"},
    ]

    pipeline = setup_pipeline(model_id)
    prompt = prepare_prompt(pipeline, message)
    outputs = generate_text(pipeline, prompt)

    print(outputs[0]["generated_text"][len(prompt):])
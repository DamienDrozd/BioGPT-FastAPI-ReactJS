from transformers import pipeline, set_seed
import torch

from transformers import BioGptTokenizer, BioGptForCausalLM
model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")
tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")

# from transformers import GPT2Tokenizer, TFGPT2Model
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = TFGPT2Model.from_pretrained('gpt2')


generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
set_seed(42)


def transform_text(src_text):
    encoded_input = tokenizer(src_text, return_tensors='pt')
    output = model(**encoded_input)

    with torch.no_grad():
        beam_output = model.generate(**encoded_input,
                                     min_length=100,
                                     max_length=1024,
                                     num_beams=5,
                                     early_stopping=True
                                     )

    return tokenizer.decode(beam_output[0], skip_special_tokens=True)

from transformers import pipeline 
def generate_explaination(text):
    generator=pipeline("text-generation",model="gpt2")
    explaination=generator(text,max_length=1000,num_return_sequences=5)
    return explaination[0]['generated_text']





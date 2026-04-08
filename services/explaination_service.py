from models.nlp_model import generate_explaination
def get_explaination(text):
    cleaned_text=text.strip()
    explaination=generate_explaination(cleaned_text)
    return {
        "input": cleaned_text,
        "result": explaination
    }
    

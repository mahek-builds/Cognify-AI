import os
from models.generation_model import generate_image
output_dir="data/outputs"
def create_visual(prompt):
    cleaned_prompt=prompt.strip()
    image=generate_image(cleaned_prompt)
    file_path=os.path.join(output_dir,f"{cleaned_prompt[:10]}.png")  # file name based on prompt
    image.save(file_path)
    return {
        "input": cleaned_prompt,
        "result": file_path
    }
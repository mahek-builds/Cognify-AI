from diffusers import StableDiffusionPipeline
import torch 
pipe=StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
device="cuda"if torch.cuda.is_available() else "cpu"
pipe=pipe.to(device)

def generate_image(prompt):
    image = pipe(prompt).images[0]
    return image


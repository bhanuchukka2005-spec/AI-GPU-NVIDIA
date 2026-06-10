from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import torch

# Select device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load Stable Diffusion Image-to-Image Model
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)

pipe = pipe.to(device)

# Load Input Cat Image
init_image = Image.open("/content/images (5).jpg").convert("RGB")
init_image = init_image.resize((512, 512))

# Prompt
prompt = """
A cute fluffy white cat sitting in a magical garden,
highly detailed, realistic, cinematic lighting,
4k quality
"""

# Generate New Image
result = pipe(
    prompt=prompt,
    image=init_image,
    strength=0.6, # 0-1 (higher = more changes)
    guidance_scale=7.5
)

generated_image = result.images[0]

# Save Output
generated_image.save("generated_cat.png")

print("Image generated successfully!")
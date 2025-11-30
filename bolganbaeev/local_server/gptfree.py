from g4f.client import Client

prompt = input("Enter your prompt: ")
client = Client()
response = client.images.generate(
    model = "flux",
    prompt = prompt,
    response_format = "url"
)

image_url = response.data[0].url
print("Image URL:", image_url)
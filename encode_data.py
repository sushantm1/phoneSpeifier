from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the GPT-2 tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Input text to generate a review
input_text = "The iPhone 16 Pro Max compared to the Samsung S23 Ultra is"
inputs = tokenizer.encode(input_text, return_tensors="pt")

# Generate text
outputs = model.generate(inputs, max_length=50, num_return_sequences=1, do_sample=True)

# Decode and print the generated text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Generated Review:")
print(generated_text)

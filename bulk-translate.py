import openai, tiktoken

# Setup initialisation parameters
input_language = "english"
output_language = "french"
input_paths = ["data/input.txt","data/input.txt"]
format = "markdown" # any special formatting considerations (e.g. .arb file, markdown, json, plain text, or multiple)
split_string = "\n\n" # the split string used to segment the chunks within the text.

# Import the files to be translated
texts = []
for path in input_paths:
    with open(path, "r") as f:
        texts.append(f.read())

# Simple test to get an idea of the length of the text and token cost
for text in texts:
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    encoded_text = encoding.encode(texts[0])
    input_token_count = len(encoded_text)
    print(f"length: {len(text) * 1.3}")
    print(f"estimated tokens: {input_token_count * 1.3}")


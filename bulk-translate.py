import openai, tiktoken, time

# Setup initialisation parameters
input_language = "english"
output_language = [
    "french",
    "german",
    "italian",
    "spanish",
    "japanese",
    "korean",
    "chinese_simplified",
    "russian",
    "portuguese",
]
input_paths = ["data/input.txt", "data/input.txt"]
output_paths = ["data/input.txt", "data/input.txt"]
format = "markdown (possibly including front-matter)"  # any special formatting considerations (e.g. .arb file, markdown, json, plain text, or multiple)
split_string = "\n\n"  # the split string used to segment the chunks within the text.
# TODO: whether to persist the chunks to a file or not
persist_chunks = False


# Import the files to be translated
file_contents = []
for path in input_paths:
    with open(path, "r") as f:
        file_contents.append(f.read())

# Simple test to get an idea of the length of the text and token cost
for text in file_contents:
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    encoded_text = encoding.encode(file_contents[0])
    input_token_count = len(encoded_text)
    print(f"length: {len(text) * 1.3}")
    print(f"estimated tokens: {input_token_count * 1.3}")

# Split the texts into chunks
chunks = []
for text in file_contents:
    chunks.append(text.split(split_string))

# Translate the chunks
for lang in output_language:
    system_prompt = f"You are a translation tool. You receive a text snippet from a file in the following format:\n{format}\n\n. The file is also written in the language:\n{input_language}\n\n. As a translation tool, you will solely return the same string in {lang} without losing or amending the original formatting. Your translations are accurate, aiming not to deviate from the original structure, content, writing style and tone."
    for split_text in file_contents:
        results = []
        counter = 0
        tokens_consumed = 0
        for text in split_text:
            messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": text}]
            model_paramters = { "model": "gpt-4-0613", "messages": messages, "temperature":1.0}

            max_attempts = 10  # Maximum number of retry attempts
            retry_gap = 3.0  # Initial gap between retries in seconds
            completion = None
            for attempt in range(max_attempts):
                try:
                    completion = openai.ChatCompletion.create(**model_paramters)
                    results.append(completion["choices"][0]["message"]["content"])
                    tokens_consumed += completion["usage"]["total_tokens"]
                    counter += 1
                    print(f"Completed: {counter}/{chunks}")
                    break # Break inner loop on success
                except Exception as e:
                    print(f"Request failed on attempt {attempt + 1}. Error: {str(e)}")
                    if attempt < max_attempts - 1:
                        retry_gap *= 1.5  # Increase the retry gap exponentially
                        time.sleep(retry_gap)

        # Export to output path
        with open(f"data/{lang}-output-{counter}.txt", "w") as f:
            f.write(split_string.join(results))


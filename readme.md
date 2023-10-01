# OpenAI Translator / Localisation Tool

This project provides a tool for translating Markdown documents from one language to another using OpenAI's API. It tokenizes the input document, splits it into chunks, translates each chunk, and stitches the output back together to retain the original formatting.

![image](https://github.com/richawo/llm-translator/assets/35015261/fd801bc1-b802-4b5e-a772-586bd2c57699)


## Features

- Accepts Plain Text/Markdown file as input
- Tokenizes input text using tiktoken
- Splits input into chunks at multiple newlines 
- Sends each chunk to OpenAI for translation
- Reconstructs translated output with original formatting

## Usage

To use this translation workflow:

1. Clone this repository
2. Install requirements
   ```
   pip install -r requirements.txt
   ```
3. Set OpenAI API key
4. Run the Jupyter notebook
   - Pass file path to `input_path` variable
   - Set `input_language` and `output_language`
   - Execute notebook cells
5. Translated file will be printed in the final cell 

## Configuration

The main configuration options are:

- `input_path` - Path to input file 
- `input_language` - Source language code 
- `output_language` - Target language code
- `split_string` - String used to split input into chunks

## Examples

This can be used to translate Plain Text/Markdown docs like:

- READMEs
- Wikis/documentation
- Articles/blog posts
- Books 

## Limitations

- Only tested with Markdown and plain text formatting
- Accuracy depends on OpenAI's translation model
- Currently only caters to OpenAI's GPT models

## Credits

- [tiktoken](https://github.com/openai/tiktoken) for fast encoding/tokenization
- [OpenAI API](https://openai.com/api/) for translation 

## License

MIT

# LLM-Powered Localisation Tool

This Jupyter notebook provides an automated tool for translating long-form text documents from one language to another while retaining the original document formatting and structure.

The notebook implements a complete pipeline for taking an input text file, splitting it into segments for translation, translating each segment using OpenAI's API, and reconstructing the full output document with the original formatting intact.

Key features:

- **Flexible input support** - Accepts text files in various formats including Markdown, JSON, XML, HTML, plaintext, etc.

- **Preserved document structure** - Headings, paragraphs, lists, tables, code blocks are reconstructed in the translated output.

- **Robust translation** - Leverages OpenAI's powerful neural machine translation models via the OpenAI API for high-quality translations.

- **Configurable** - Source and target languages are configurable parameters in the notebook.

- **Automated workflow** - The notebook provides an end-to-end automated pipeline for document translation requiring minimal user input.

This notebook aims to provide a simple yet powerful tool for translators, localizers, and anyone looking to make text documents accessible to readers of different languages. The automation retains document structure and formatting to minimize manual post-editing of translations.

## How it works

- Accepts text input file path as parameter
- Reads in input file in various formats like Markdown, JSON, etc.
- Splits input text into chunks for translation
- Translates each chunk using OpenAI's language models via the OpenAI API
- Stitches translated chunks back together into full output document
- Preserves original formatting like headings, lists, code blocks, etc.

## Usage

1. Clone this repository
2. Install Jupyter Notebook
   ```
   pip install jupyterlab
   ```
3. Install OpenAI API package
   ```
   pip install openai
   ```
4. Set OpenAI API key in the notebook
5. Run the notebook
   - Pass file path to input text as first parameter
   - Configure source and target languages
   - Execute cells to translate
6. Translated text with original formatting will be output

## Examples

- Translate Markdown documents like READMEs to other languages
- Localize API documentation or software user guides
- Convert large texts like ebooks or articles to new languages

## Credits

- Translation is powered by OpenAI's neural network models via the OpenAI API.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Let me know if this updated README covers the necessary details on usage and installation! I can make any other changes needed to improve it.

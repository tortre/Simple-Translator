# Text Translator

This Python script allows users to translate text into a specified language using the Google Translate API.

## Requirements

Ensure you have Python installed, then install the required package:

```sh
pip install googletrans==4.0.0-rc1
```

## Usage

Run the script and enter the target language code (e.g., `es` for Spanish) and the text you want to translate.

```python
from googletrans import Translator
language = input("What language do you want to translate to? (e.g., 'es' for Spanish): ")
text = input("Enter the text you want to translate: ")
translator = Translator() 
translated = translator.translate(text, dest=language)
print(translated.text)
```

## Language Codes

Use [Google Translate Language Codes](https://cloud.google.com/translate/docs/languages) to find the correct codes for your target language.

## Example

```sh
What language do you want to translate to? (e.g., 'es' for Spanish): fr
Enter the text you want to translate: Hello, how are you?
Translated Text: Bonjour, comment ça va ?
```

## License

This project is open-source and available under the MIT License.

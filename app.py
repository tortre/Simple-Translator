from googletrans import Translator
language = input("What language do you want to translate to? (e.g., 'es' for Spanish): ")
text = input("Enter the text you want to translate: ")
translator = Translator() 
translated = translator.translate(text, dest=language)
print(translated.text)

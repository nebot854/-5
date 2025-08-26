from translate import Translator
# Создаем переводчика с русского на английский

translator = Translator(from_lang="ru", to_lang="en")

# Переводим текст
translation = translator.translate("Люблю собак?")
print(translation)  # Hello, how are you?
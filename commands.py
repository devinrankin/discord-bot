import googletrans

def handle_command(message) -> str:
    p_message = message.lower()

    if p_message.startswith('$translate'):
        translated_message = translate_command(message, 'en')
        return translated_message.text
    if p_message.startswith('$lookup'):
        return 'Lookup command detected.'
    if p_message == '$help':
        return 'This is the help command.'
    elif p_message.startswith('$'):
        return 'Unrecognized command.'

def translate_command(message, target_language) -> str:
    translator = googletrans.Translator()

    translated_message = translator.translate(message, target_language)
    
    return translated_message
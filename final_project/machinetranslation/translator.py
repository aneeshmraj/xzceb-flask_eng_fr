"""
Converts English to French and French to English
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['API_KEY']
url = os.environ['API_URL']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """translates the english text to french text."""
    translation = language_translator.translate(
    english_text,
    model_id='en-fr').get_result()
    translation = dict(translation)
    french_text = translation["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    """translates the french text to english text."""
    translation = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    translation = dict(translation)
    english_text = translation["translations"][0]["translation"]
    return english_text

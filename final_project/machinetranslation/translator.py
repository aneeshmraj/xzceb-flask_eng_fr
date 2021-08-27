import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['API_KEY']
url = os.environ['API_URL']

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    #write the code here
    translation = language_translator.translate(
    englishText,
    model_id='en-fr').get_result()
    result = dict(json.dumps(translation, indent=2, ensure_ascii=False))
    #result = json.dumps(translation, indent=2, ensure_ascii=False)
    print(result)
    return translation["translations"]["translation"]


def frenchToEnglish(frenchText):
    #write the code here
    translation = language_translator.translate(
    frenchText,
    model_id='fr-en').get_result()
    result = dict(json.dumps(translation, indent=2, ensure_ascii=False))
    print(result)
    return translation["translations"]["translation"]
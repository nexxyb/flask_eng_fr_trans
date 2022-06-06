from ensurepip import version
import json
import os
from xml.etree.ElementTree import VERSION
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey= os.environ['apikey']
url= os.environ['url']
version='2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version, authenticator=authenticator)
language_translator.set_service_url(url)
def english_to_french(english_text):
    model_id= 'en-fr'
    translation= language_translator.translate(english_text, model_id=model_id).get_result()
    french_text= json.dumps(translation, ensure_ascii=False)
    french_text= json.loads(french_text)["translations"][0]["translation"]
    return french_text
def french_to_english(french_text):
    model_id= 'fr-en'
    translation= language_translator.translate(french_text, model_id=model_id).get_result()
    english_text= json.dumps(translation, ensure_ascii=False)
    english_text= json.loads(english_text)["translations"][0]["translation"]
    return english_text

#print(english_to_french('my love'))
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class BuscarProfessor(Action):

    def name(self) -> Text:
        return "action_buscar_professor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nome_professor = tracker.get_slot("professor_name")

        dispatcher.utter_message(text="fulano@riogrande.ifrs.edu.br")

        return[SlotSet("professor_name", None)]


class BuscarFaq(Action):

    def name(self) -> Text:
        return "action_faq_comprovate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link_matricula = "https://sia.ifrs.edu.br/aplicacoes/frame/index.php"
        link_tutorial = "https://sia.ifrs.edu.br/aplicacoes/frame/index.php"

        dispatcher.utter_message(
            text=f"Para baixar o comprovante de matrícula você precisa acessar o link {link_matricula}")
        dispatcher.utter_message(
            text=f"Caso precise de alguma ajuda, assista no link {link_tutorial}")

        return []


class ValidaNomeForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    async def validate_name(self,
                            slot_value: Any,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: DomainDict,
                            ) -> Dict[Text, Any]:
        name = slot_value
        sai = tracker.get_slot("sender_id")
        if(sai == None):
            volta = "!"
            sai = tracker.sender_id
        else:
            volta = ", fico feliz com tua volta!"

        texto = "Olá " + name+volta+" O que vai hoje?"
        dispatcher.utter_message(text=texto)
        print(name)

        return {"name": name, "sender_id": sai}

<<<<<<< HEAD
<<<<<<< HEAD
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
        
        nome_professor = dispatcher.get_slot("professor_name")

        dispatcher.utter_message(text="fulano@riogrande.ifrs.edu.br")


class BuscarFaq(Action):
    
    def name(self) -> Text:
        return "action_faq_comprovate"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Para baixar o comprovante de matrícula você precisa acessar o link tal")
        dispatcher.utter_message(text="Caso precise de alguma ajuda, assista no link tal")


        # classes = tracker.get_slot('classes')
        # calendar = tracker.get_slot('calendar')
        # courses = tracker.get._slot('courses')
        # documents = tracker.get_slot('documents')


class BuscarClasses(Action):
    
    def name(self) -> Text:
        return "action_buscar_classes"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link_classes = "XXXX"

        dispatcher.utter_message(text=f"Os horários de suas aulas e disciplinas você pode conferir neste link {link_classes}!")

        return []

class BuscarCalendar(Action):
    
    def name(self) -> Text:
        return "action_buscar_calendar"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        link_calender = "https://ifrs.edu.br/riogrande/ensino/calendario-academico/"

        dispatcher.utter_message(text=f"Confira aqui seu calendário acadêmico {link_calender}")

         return []

class BuscarCursos(Action)
     def name(self) -> Text:
        return "action_buscar_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        link_cursos = "https://ifrs.edu.br/riogrande/cursos/"

        dispatcher.utter_message(text=f"Confira aqui os cursos disponíveis no IFRS {link_cursos}")

        return []

class Buscardocumentos(Action)
     def name(self) -> Text:
        return "action_buscar_documents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         dispatcher.utter_message(text=f"Estes são os documentos que você precisa manter atualizados no IFRS: CPF, Comprovante de residência e dados cadastrais")

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
=======
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

=======
>>>>>>> dd7e48da705fc874497f49d7b9840cd4d15ebbb1
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


class BuscarClasses(Action):

    def name(self) -> Text:
        return "action_buscar_classes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link_classes = "XXXX"

        dispatcher.utter_message(
            text=f"Os horários de suas aulas e disciplinas você pode conferir neste link {link_classes}!")

        return []


class BuscarCalendar(Action):

    def name(self) -> Text:
        return "action_buscar_calendar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link_calender = "https://ifrs.edu.br/riogrande/ensino/calendario-academico/"

        dispatcher.utter_message(
            text=f"Confira aqui seu calendário acadêmico {link_calender}")

        return []


class BuscarCursos(Action):
     def name(self) -> Text:
        return "action_buscar_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        link_cursos = "https://ifrs.edu.br/riogrande/cursos/"

        dispatcher.utter_message(text=f"Confira aqui os cursos disponíveis no IFRS {link_cursos}")

        return []

class Buscardocumentos(Action):
     def name(self) -> Text:
        return "action_buscar_documents"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text=f"Estes são os documentos que você precisa manter atualizados no IFRS: CPF, Comprovante de residência e dados cadastrais")

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
>>>>>>> 33722055ef37abe992e343d59e14496d8a77180b

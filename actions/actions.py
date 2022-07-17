from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet, AllSlotsReset


class GetProfessorContact(Action):

    def name(self) -> Text:
        return "action_get_professor_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nome_professor = tracker.get_slot("professor_name")

        dispatcher.utter_message(
            text=f"{nome_professor}@riogrande.ifrs.edu.br")

        return[SlotSet("professor_name", None)]


class GetDocRegister(Action):

    def name(self) -> Text:
        return "action_get_doc_register"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link_matricula = "https://sia.ifrs.edu.br/aplicacoes/frame/index.php"
        link_tutorial = "https://sia.ifrs.edu.br/aplicacoes/frame/index.php"

        dispatcher.utter_message(
            text=f"Para baixar o comprovante de matrícula você precisa acessar o link {link_matricula}")
        dispatcher.utter_message(
            text=f"Caso precise de alguma ajuda, assista o tutorial no link {link_tutorial}")

        return []


class GetClasses(Action):

    def name(self) -> Text:
        return "action_get_classes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link_classes = "https://ifrs.edu.br/riogrande/ensino/retorno-do-calendario/horarios/"

        dispatcher.utter_message(
            text=f"Os horários de suas aulas e disciplinas você pode conferir aqui {link_classes}!")

        return []


class ClearSlots(Action):

    def name(self) -> Text:
        return "action_goodbye_and_clear_slots"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_goodbye")
        return[AllSlotsReset()]


class GetCalendar(Action):

    def name(self) -> Text:
        return "action_get_calendar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link_calendar = "https://ifrs.edu.br/riogrande/wp-content/uploads/sites/16/2022/05/Calendario-Academico-Campus-Rio-Grande-2022-alterado-em-abril-2022.pdf"

        dispatcher.utter_message(
            text=f"Confira aqui o calendário acadêmico 👇")
        dispatcher.utter_message(
            attachement=link_calendar)

        return []


class GetCourses(Action):
    def name(self) -> Text:
        return "action_get_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link_cursos = "https://ifrs.edu.br/riogrande/cursos/"

        dispatcher.utter_message(
            text=f"Confira aqui os cursos disponíveis no IFRS {link_cursos}")

        return []


class ImformToDoRegister(Action):
    def name(self) -> Text:
        return "action_inform_do_register"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link = "https://ingresso.ifrs.edu.br/"

        dispatcher.utter_message(
            text=f"Através do link abaixo tu pode te matricular em um dos nossos cursos:")
        dispatcher.utter_message(
            url=link)

        return []


class InformToRedoRegister(Action):
    def name(self) -> Text:
        return "action_inform_redo_register"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        link_tutorial = "https://www.youtube.com/watch?v=STZYUidrVAg"
        link = "https://sia.ifrs.edu.br/aplicacoes/frame/index.php"

        dispatcher.utter_message(
            text=f"As rematrículas dos cursos das modalidades **Superior** e **Subsequente** ocorrerão dos dias **25/07** à **27/07** através do link abaixo: ")
        dispatcher.utter_message(text=link)
        dispatcher.utter_message(
            text="Caso esteja com dificuldades consulte o link abaixo 👇")
        dispatcher.utter_message(text=link_tutorial)

        return []


class GetInternshipInfo(Action):
    def name(self) -> Text:
        return "action_get_internship_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link_estagio = "https://ifrs.edu.br/riogrande/extensao/estagios/"

        dispatcher.utter_message(
            text=f"Confira aqui maiores informações sobre estágios no IFRS! {link_estagio}")

        return []


class WhatBotDo(Action):
    def name(self) -> Text:
        return "action_what_bot_do"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text=f"Tu pode me solicitar:👇\n➡️ Contato dos professores\n➡️ Calendário acadêmico\n➡️ Cursos disponíveis\n➡️ Informações sobre estágio\n➡️ Comprovante de matrícula\n➡️ Informações sobre as aulas\n➡️ Documentos para matricula\n➡️ Como fazer a rematrícula")

        return []


def clean_name(name):
    return "".join([c for c in name if c.isalpha()])


class ValidaNomeForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        name = clean_name(slot_value).title()
        if len(name) == 0:
            dispatcher.utter_message(
                text="Não entendi, pode ter sido um erro de digitação")
            return {"name": None}
        return {"name": name}


class ValidaNomeForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_professor_name_form"

    def validate_professor_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        name = clean_name(slot_value).title()
        if len(name) == 0:
            dispatcher.utter_message(
                text="Não entendi, pode ter sido um erro de digitação")
            return {"professor_name": None}
        return {"professor_name": name}

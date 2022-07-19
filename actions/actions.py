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

        dispatcher.utter_message(response="utter_goodbye")
        return[AllSlotsReset()]


class GetCalendar(Action):

    def name(self) -> Text:
        return "action_get_calendar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        link_calendar = "https://ifrs.edu.br/riogrande/wp-content/uploads/sites/16/2022/05/Calendario-Academico-Campus-Rio-Grande-2022-alterado-em-abril-2022.pdf"

        dispatcher.utter_message(
            text=f"Confira aqui o calendário acadêmico 👇", attachment=link_calendar)

        return []


class GetCourses(Action):
    def name(self) -> Text:
        return "action_get_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        uri_base = "https://ifrs.edu.br/riogrande/cursos/"
        modality = tracker.get_slot("courses_modality").lower()
        print(modality)

        buttons_integrado = [
            {"payload": '/courses{"courses_name":"automação"}',
                "title": "Automação Industrial"},
            {"payload": '/courses{"courses_name":"fabricação"}',
                "title": "Fabricação Mecânica"},
            {"payload": '/courses{"courses_name":"informática"}',
                "title": "Informática para Internet"},
            {"payload": '/courses{"courses_name":"geoprocessamento"}',
                "title": "Geoprocessamento"},
            {"payload": '/courses{"courses_name":"eletrotécnica"}',
                "title": "Eletrotécnica"},
            {"payload": '/courses{"courses_name":"refrigeração"}',
                "title": "Refrigeração"}
        ]
        buttons_subsequente = [
            {"payload": '/courses{"courses_name":"automação"}',
                "title": "Automação Industrial"},
            {"payload": '/courses{"courses_name":"fabricação"}',
                "title": "Fabricação Mecânica"},
            {"payload": '/courses{"courses_name":"geoprocessamento"}',
                "title": "Geoprocessamento"},
            {"payload": '/courses{"courses_name":"eletrotécnica"}',
                "title": "Eletrotécnica"},
            {"payload": '/courses{"courses_name":"refrigeração"}',
                "title": "Refrigeração"},
            {"payload": '/courses{"courses_name":"enfermagem"}', "title": "Enfermagem"}
        ]
        buttons_superior = [
            {"payload": '/courses{"courses_name":"engenharia mecânica"}',
                "title": "Engenharia Mecânica"},
            {"payload": '/courses{"courses_name":"tads"}',
                "title": "Análise e Desenvolvimendo de Software"},
            {"payload": '/courses{"courses_name":"tce"}',
                "title": "Construção de Edifícios"},
            {"payload": '/courses{"courses_name":"formação pedagógica"}',
                "title": "Curso de Formação Pedagógica"},
            {"payload": '/courses{"courses_name":"formação pedagógica não licenciados"}',
                "title": "Curso de Formação Pedagógica para não Licenciados"},
        ]

        uri_modality = ''
        if 'integrado' in modality:
            uri_modality = 'cursos-tecnicos-integrados/'
            dispatcher.utter_message(
                title="Qual curso?", buttons=buttons_integrado)

        elif 'subsequente' in modality:
            uri_modality = 'cursos-tecnicos-subsequentes/'
            dispatcher.utter_message(
                title="Qual curso?", buttons=buttons_subsequente)

        elif 'superior' in modality:
            uri_modality = 'cursos-superiores/'
            dispatcher.utter_message(
                title="Qual curso?", buttons=buttons_superior)

        complete_uri = uri_base+uri_modality

        return [SlotSet("courses_link", complete_uri)]


class GetInfoCours(Action):

    def name(self) -> Text:
        return "action_get_info_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        courses = {
            "automação": "automacao-industrial/",
            "fabricação": "fabricacao-mecanica/",
            "informática": "informatica-para-internet/",
            "eletrotécnica": "eletrotecnica/",
            "geoprocessamento": "geoprocessamento/",
            "refrigeração": "refrigeracao-e-climatizacao/",
            "enfermagem": "enfermagem/",
            "engenharia mecânica": "engenharia-mecanica/",
            "tads": "tads/",
            "tce": "curso-superior-de-tecnologia-em-construcao-de-edificios/",
            "formação pedagógica": "curso-de-formacao-pedagogica/",
            "formação pedagógica não licenciados": "curso-de-formacao-pedagogica-para-graduados-nao-licenciados/"
        }

        course = tracker.get_slot("courses_name")
        modality = tracker.get_slot("courses_modality")
        link = tracker.get_slot("courses_link")

        link += courses[course]
        print(f"O curso de {course} é da modalidade do {modality}")
        print(f"o link de acesso para o curso é {link}")

        return [SlotSet("courses_modality", None), SlotSet("courses_name", None), SlotSet("courses_link", None)]


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


class NameFormValidate(FormValidationAction):
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


class ProfessorNameFormValidate(FormValidationAction):
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

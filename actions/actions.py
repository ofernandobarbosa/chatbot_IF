from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet, AllSlotsReset
import json
from actions.utils import *


class GetProfessorContact(Action):
    # categoria informações de servidores
    def name(self) -> Text:
        return "action_get_professor_contact"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nome_professor = tracker.get_slot("professor_name")
        sobrenome_professor = tracker.get_slot("professor_last_name")
        # with open("calendarios.json", encoding="utf8") as file:
        #     data = json.loads(file.read())

        data = req_json("contato_dos_professores/")

        for order in data:
            try:
                print(nome_professor, sobrenome_professor)
                if(order["nome_do_professor"] == nome_professor):
                    if(order["sobrenome_do_professor"] == sobrenome_professor):
                        link = order["email"]
                        msg=f"Segue o email do professor {nome_professor} {sobrenome_professor} {link}"
                        dispatcher.utter_message(text=msg)
                        break
                    if(order["sobrenome_do_professor"] != sobrenome_professor):
                        link = order["email"]
                        msg=f"Segue o email {link}"
                        dispatcher.utter_message(text=msg)
                        
            except:
                pass


        return[SlotSet("professor_name", None), SlotSet("professor_last_name", None)]


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

        # request json
        data = req_json("comprovante_de_matricula/")

        try:
            # retorno da ultima atualização
            req = last_info('nome_do_sistema', system, data)

            # variaves db
            system_db = req["nome_do_sistema"].upper()
            description = req["descricao"]
            link_1 = req["link_1"]
            link_2 = req["link_2"]
            archive_1 = req["arquivo_1"]
            archive_2 = req["arquivo_2"]

            # dispachando informações
            dispatcher.utter_message(text=description)
            dispatcher.utter_message(
                text=f'Segue o [link]({link_1}) para acessar o {system}!')

        except:
            dispatcher.utter_message(
                text=f"Estamos com dificuldades de encontrar teu tutorial para o {system}")

        return [SlotSet("system", None)]


class GetClasses(Action):

    def name(self) -> Text:
        return "action_get_classes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # buttons declaration
        buttons_integrado = [
            {"title": "Automação Industrial",
                "payload": '/courses{"courses_name": "automação"}'},
            {"title": "Fabricação Mecânica",
                "payload": '/courses{"courses_name": "fabricação"}'},
            {"title": "Informática para Internet",
                "payload": '/courses{"courses_name": "informática"}'},
            {"title": "Geoprocessamento",
                "payload": '/courses{"courses_name": "geoprocessamento"}'},
            {"title": "Eletrotécnica",
                "payload": '/courses{"courses_name": "eletrotécnica"}'},
            {"title": "Refrigeração",
                "payload": '/courses{"courses_name": "refrigeração"}'}
        ]
        buttons_subsequente = [
            {"title": "Automação Industrial",
                "payload": '/courses{"courses_name": "automação"}'},
            {"title": "Fabricação Mecânica",
                "payload": '/courses{"courses_name": "fabricação"}'},
            {"title": "Geoprocessamento",
                "payload": '/courses{"courses_name": "geoprocessamento"}'},
            {"title": "Eletrotécnica",
                "payload": '/courses{"courses_name": "eletrotécnica"}'},
            {"title": "Refrigeração",
                "payload": '/courses{"courses_name": "refrigeração"}'},
            {"title": "Enfermagem", "payload": '/courses{"courses_name": "enfermagem"}'}
        ]
        buttons_superior = [
            {"title": "Engenharia Mecânica",
                "payload": '/courses{"courses_name": "engenharia mecânica"}'},
            {"title": "Análise e Desenvolvimendo de Software",
                "payload": '/courses{"courses_name": "tads"}'},
            {"title": "Construção de Edifícios",
                "payload": '/courses{"courses_name": "tce"}'},
            {"title": "F. Pedagógica",
                "payload": '/courses{"courses_name": "formação pedagógica"}'},
            {"title": "F. Pedagógica não Licenciados",
                "payload": '/courses{"courses_name": "pedagógica não licenciados"}'}
        ]

        # variables declaration
        modality = tracker.get_slot("courses_modality").lower()

        modalities = {
            "integrado": {
                "link":"cursos-tecnicos-integrados/",
                "button": buttons_integrado,
                },
            "subsequente":{ 
                "link": "cursos-tecnicos-subsequentes/",
                "button": buttons_subsequente,
            },
            "superior": {
                "link":"cursos-superiores/",
                "button": buttons_superior,
            },
        }
        # Dispatcher the button selector according with the chosen modality
        course = dispatcher.utter_message(
            text="Para qual curso gostaria de obter os horarios?", 
            buttons=modalities[modality]["button"], 
            button_type="vertical")


        return [SlotSet("courses_name", course)]

class GetInfoClasses(Action):

    def name(self) -> Text:
        return "action_get_info_classe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        A action valida o curso selecionado pelo usuário e busca o link de acordo com o botão clicado pelo usuário.
        Além de validar o curso, a action recebe o valor do slot (courses_modality_link) para interpolar com o endpoint de acordo com o curso selecionado.
        Por fim, despacha para o usuário a informação com o link correto.
        """
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
            "pedagógica não licenciados": "curso-de-formacao-pedagogica-para-graduados-nao-licenciados/"
        }

        course_name = tracker.get_slot("courses_name").title()
        course_modality = tracker.get_slot("courses_modality").title()

        endpoint = 'grade_de_horarios'
        data = req_json(endpoint)

        for order in data:
            try:
                print(order["modalidade_do_curso"], order["nome_do_curso"])
                if(order["modalidade_do_curso"] == course_modality and order["nome_do_curso"] == course_name):
                    link = order["link_1"]
                    msg=f"Segue o link de acesso dos horários do curso {course_name} {link}"
                    dispatcher.utter_message(text=msg)
                    break
            except:
                pass

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

        ano_corrente = 2022
        dispatcher.utter_message(
            text=f"Confira aqui o calendário acadêmico 👇")
        dispatcher.utter_message(attachment=link_calendar)

        return []


class GetCourses(Action):
    def name(self) -> Text:
        return "action_get_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        A action é chamada para validar a opção da modalidade do curso escolhida pelo usário, assim que validada ela dispacha paara o usuário botões de selecão do curso de acordo com a modalidade escolhida.
        Ao final da action, vai ser retornado também o preenchimento do slot (courses_modality_link) para ser utilizada na action seguinte (action_get_info_course) das Stories.
        """

        # buttons declaration
        buttons_integrado = [
            {"title": "Automação Industrial",
                "payload": '/courses{"courses_name": "automação"}'},
            {"title": "Fabricação Mecânica",
                "payload": '/courses{"courses_name": "fabricação"}'},
            {"title": "Informática para Internet",
                "payload": '/courses{"courses_name": "informática"}'},
            {"title": "Geoprocessamento",
                "payload": '/courses{"courses_name": "geoprocessamento"}'},
            {"title": "Eletrotécnica",
                "payload": '/courses{"courses_name": "eletrotécnica"}'},
            {"title": "Refrigeração",
                "payload": '/courses{"courses_name": "refrigeração"}'}
        ]
        buttons_subsequente = [
            {"title": "Automação Industrial",
                "payload": '/courses{"courses_name": "automação"}'},
            {"title": "Fabricação Mecânica",
                "payload": '/courses{"courses_name": "fabricação"}'},
            {"title": "Geoprocessamento",
                "payload": '/courses{"courses_name": "geoprocessamento"}'},
            {"title": "Eletrotécnica",
                "payload": '/courses{"courses_name": "eletrotécnica"}'},
            {"title": "Refrigeração",
                "payload": '/courses{"courses_name": "refrigeração"}'},
            {"title": "Enfermagem", "payload": '/courses{"courses_name": "enfermagem"}'}
        ]
        buttons_superior = [
            {"title": "Engenharia Mecânica",
                "payload": '/courses{"courses_name": "engenharia mecânica"}'},
            {"title": "Análise e Desenvolvimendo de Software",
                "payload": '/courses{"courses_name": "tads"}'},
            {"title": "Construção de Edifícios",
                "payload": '/courses{"courses_name": "tce"}'},
            {"title": "F. Pedagógica",
                "payload": '/courses{"courses_name": "formação pedagógica"}'},
            {"title": "F. Pedagógica não Licenciados",
                "payload": '/courses{"courses_name": "pedagógica não licenciados"}'}
        ]

        # variables declaration
        uri_base = "https://ifrs.edu.br/riogrande/cursos/"
        modality = tracker.get_slot("courses_modality").lower()

        modalities = {
            "integrado": {
                "link": "cursos-tecnicos-integrados/",
                "button": buttons_integrado,
            },
            "subsequente": {
                "link": "cursos-tecnicos-subsequentes/",
                "button": buttons_subsequente,
            },
            "superior": {
                "link": "cursos-superiores/",
                "button": buttons_superior,
            },
        }
        uri_modality = modalities[modality]["link"]

        # Dispatcher the button selector according with the chosen modality
        button = dispatcher.utter_message(
            text="Para qual curso gostaria de mais informações?", 
            buttons=modalities[modality]["button"], 
            button_type="vertical")
        
        complete_uri = uri_base+uri_modality

        return [SlotSet("courses_modality_link", complete_uri)]


class GetInfoCours(Action):

    def name(self) -> Text:
        return "action_get_info_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        A action valida o curso selecionado pelo usuário e busca o link de acordo com o botão clicado pelo usuário.
        Além de validar o curso, a action recebe o valor do slot (courses_modality_link) para interpolar com o endpoint de acordo com o curso selecionado.
        Por fim, despacha para o usuário a informação com o link correto.
        """

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
            "pedagógica não licenciados": "curso-de-formacao-pedagogica-para-graduados-nao-licenciados/"
        }

        course_name = tracker.get_slot("courses_name")
        print(course_name)
        course_modality = tracker.get_slot("courses_modality")
        link = tracker.get_slot("courses_modality_link")

        link += courses[course_name]

        msg = f"Segue o link de acesso para o curso {link}"

        dispatcher.utter_message(text=msg)

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


class WhatBotDo(Action):
    def name(self) -> Text:
        return "action_what_bot_do"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text=f"Tu pode me solicitar:👇\n➡️ Calendário acadêmico\n➡️ Comprovante de matrícula\n➡️ Contato dos professores\n➡️ Cursos disponíveis\n➡️ Grade de horários\n➡️ Informações relevantes dos cursos\n➡️ Informações sobre inscrição/matrícula\n➡️ Informações sobre rematrícula\n➡️ Requerimentos/formulários\n➡️ Tutoriais de acessos a sistemas acadêmicos")

        return []


class Requirements(Action):
    def name(self) -> Text:
        return "action_get_requirements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # recebe slot pelo input do usuário
        requirement = tracker.get_slot("requirements").title()
        # difine arquivo padrão para busca do dado ordenado por ultima atualização
        data = req_json("requerimentos_ou_formularios/")
        try:
            # busca por todas as recorrencias do requerimento no json e recebe a ultima atualização do requerimento
            req = last_info('nome_do_requerimento', requirement, data)
            text = req["descricao"]
            link = req["link_1"]
            data_inicio = req["data_de_inicio"]
            data_fim = req["data_de_fim"]

            dispatcher.utter_message(text=text)
            dispatcher.utter_message(
                text=f"Lembrando que o prazo para preenchimento vai de {data_inicio} até {data_fim}")
        except:
            dispatcher.utter_message(
                text=f'O requerimento \n`"{requirement}"` \nestá indisponível no momento')

        return [SlotSet("requirements", None)]


class SystemsTutorial(Action):
    def name(self) -> Text:
        return "action_get_system_tutorials"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # variaveis definidas a partir de slots
        system = tracker.get_slot("system")

        # request json
        data = req_json("tutoriais_de_acessos_a_sistemas_academicos/")

        try:
            # retorno da ultima atualização
            req = last_info('nome_do_sistema', system, data)

            # variaves db
            system_db = req["nome_do_sistema"].upper()
            description = req["descricao"]
            link_1 = req["link_1"]
            link_2 = req["link_2"]
            archive_1 = req["arquivo_1"]
            archive_2 = req["arquivo_2"]

            # dispachando informações
            dispatcher.utter_message(text=description)
            dispatcher.utter_message(
                text=f'Segue o [link]({link_1}) para acessar o {system}!')

        except:
            dispatcher.utter_message(
                text=f"Estamos com dificuldades de encontrar teu tutorial para o {system}")

        return [SlotSet("system", None)]


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

    def validate_professor_last_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        name = (slot_value).title()
        if len(name) == 0:
            dispatcher.utter_message(
                text="Não entendi, pode ter sido um erro de digitação")
            return {"professor_last_name": None}
        return {"professor_last_name": name}

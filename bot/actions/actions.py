from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker  # type: ignore
from rasa_sdk.executor import CollectingDispatcher  # type: ignore
from rasa_sdk.types import DomainDict  # type: ignore
from rasa_sdk.forms import FormValidationAction  # type: ignore
from rasa_sdk.events import SlotSet, AllSlotsReset # type: ignore
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

        data = req_json("contato_dos_professores")
        dictionary = {
            "nome_do_professor": nome_professor,
            "sobrenome_do_professor": sobrenome_professor
        }

        user_id = tracker.sender_id
        name = tracker.get_slot("user_name")
        dispatcher.utter_message(text=f"Olá {name}")

        try:
            req = last_info(dictionary=dictionary, data=data)
            dispatcher.utter_message(text=req["email"])
        except:
            try:

                req = all_info(dictionary=dictionary, data=data)
                dispatcher.utter_message(
                    text="Infelizmente não localizei o contato do professor que tu me informou, seguem abaixo alguns contatos parecidos que encontrei")
                for item in req:
                    nome = item["nome_do_professor"]
                    sobrenome = item["sobrenome_do_professor"]
                    dispatcher.utter_message(
                        text=f'*{nome} {sobrenome}* 👇\n{item["email"]}')
            except:
                dispatcher.utter_message(
                    text=f"Não foi possivel encontrar o contato com os nomes informados, tente novamente 😊")

        return[SlotSet("professor_name", None), SlotSet("professor_last_name", None)]


class GetDocRegister(Action):

    def name(self) -> Text:
        return "action_get_doc_register"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # variavel recebida pelo slot com informaçoes do usuário
        system = tracker.get_slot("system")

        # request json
        data = req_json("comprovante_de_matricula")

        try:
            # retorno da ultima atualização
            dictionary = {
                'nome_do_sistema': system
            }
            req = last_info(data=data, dictionary=dictionary)

            # variaves db
            description = req["descricao"]
            system_link = req["link_1"]
            description = req["descricao"]

            # dispachando informações
            dispatcher.utter_message(text=description)
            dispatcher.utter_message(
                text=f'Segue o [link]({system_link}) para acessar o {system}!')

        except:
            dispatcher.utter_message(
                text=f"Estamos com dificuldades de encontrar informações para o {system} 😓")

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
        course_name = tracker.get_slot("courses_name").title()
        course_modality = tracker.get_slot("courses_modality").title()

        endpoint = 'grade_de_horarios'
        data = req_json(endpoint)
        try:
            dictionary = {
                "modalidade_do_curso": course_modality,
                "nome_do_curso": course_name
            }
            req = last_info(data=data, dictionary=dictionary)
            link = req["link_1"]
            msg = f"Segue o link de acesso dos horários do curso {course_name} {link}"
            dispatcher.utter_message(text=msg)
        except:
            dispatcher.utter_message(
                text=f"Estamos com dificuldades de encontrar informações para o curso {course_name}. 😓")

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
        """
        Action com finalidade de limpar o slot para a solicitação ser atendida. Dessa forma é possível reiniciar a conversa e fazer novas solicitações
        """

        dispatcher.utter_message(response="utter_goodbye")
        return[AllSlotsReset()]


class GetCalendar(Action):

    def name(self) -> Text:
        return "action_get_calendar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        A action GetCalendar retorna ao usuário do Bot o calendário acadêmico, via link, do ano em vigência.
        Link único, uma vez que é um calendário para todos os cursos disponíveis no IFRS. A action recebe o valor do slot calendar
        """
        # variável link para inserir o calendário
        # definindo variáveis setadas pelo slot do usaário
        import datetime
        now = datetime.datetime.now()
        ano = now.year
        print(ano)

        # buscando informações na api
        data = req_json("calendario_academico")
        try:
            # buscar no json o atributo e o valor setado pelo usuário=
            dictionary = {
                "ano": ano
            }
            req = last_info(data=data, dictionary=dictionary)

            # varáveis de banco de dados
            # arquivo_1 = req["arquivo_1"]
            link = req["link_1"]
            # dispatcher.utter_message(document=arquivo_1)
            dispatcher.utter_message(
                text=f"Para acessar o calendário acadêmico [clique aqui 🔗]({link})")
        except:
            dispatcher.utter_message(
                text="Desculpe, estamos com dificuldades para encontrar tua solicitação, tente novamente mais tarde! 😓")
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
        modality = tracker.get_slot("courses_modality").lower()

        modalities_buttons = {
            "integrado": buttons_integrado,
            "subsequente": buttons_subsequente,
            "superior": buttons_superior,
        }

        # Dispatcher the button selector according with the chosen modality
        dispatcher.utter_message(
            text="Para qual curso gostaria de mais informações?",
            buttons=modalities_buttons[modality],
            button_type="vertical")

        return []


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
        # definindo variaveis definidas por slots do usuário
        course_modality = tracker.get_slot("courses_modality").title()
        course_name = tracker.get_slot("courses_name").title()
        try:
            # recuperando dados da API
            data = req_json("informacoes_relevantes_dos_cursos")
            # buscando a ultima atualização conforme slots de busca do usuário
            dictionary = {
                "modalidade_do_curso": course_modality,
                "nome_do_curso": course_name
            }
            req = last_info(data=data, dictionary=dictionary)
            # definindo variaveis do json
            description = req["descricao"]
            ingress_modality = req["forma_de_ingresso"]
            requirements = req["requisitos"]
            shift = req["turno"]
            vacancies = req["numero_de_vagas"]
            coordinator_name = req["coordenador_do_curso"]
            coordinator_email = req["email_do_coordenador"]
            course_email = req["email_do_curso"]

            # dispachando mensagens para o usuário
            dispatcher.utter_message(text=f'➡️ {description}')
            dispatcher.utter_message(
                text=f'➡️ *Modalidade de ingresso*: {ingress_modality}')
            dispatcher.utter_message(text=f'➡️ *Requisitos*: {requirements}')
            dispatcher.utter_message(text=f'➡️ *Turno*: {shift}')
            dispatcher.utter_message(text=f'➡️ *Vagas*: {vacancies}')
            dispatcher.utter_message(
                text=f'➡️ *Coordenador do curso*: {coordinator_name}')
            dispatcher.utter_message(
                text=f'➡️ *Email do coordenador*: {coordinator_email}')
            dispatcher.utter_message(
                text=f'➡️ *Email do curso*: {course_email}')
        except:
            dispatcher.utter_message(
                text="Desculpe, estamos com dificuldades para encontrar tua solicitação. 😓")

        return [SlotSet("courses_modality", None), SlotSet("courses_name", None)]


class ImformToDoRegister(Action):
    def name(self) -> Text:
        return "action_inform_do_register"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Action para direcionar a forma de ingresso no IFRS. Recebe o valor do slot ingress_modality. Retorna ao usuário o link correto
        """
        # definindo variáveis setadas pelo slot do usaário
        ingress_modality = tracker.get_slot("ingress_modality")

        # buscando informações na api
        data = req_json("informacoes_sobre_inscricao_ou_matricula")
        # buscar no json o atributo e o valor setado pelo usuário
        try:
            dictionary = {
                "modalidade_de_ingresso": ingress_modality
            }
            req = last_info(data=data, dictionary=dictionary)

            # varáveis de banco de dados
            descricao = req["descricao"]
            link = req["link_1"]

            dispatcher.utter_message(text=descricao)
            dispatcher.utter_message(
                text=f"Para acessar as formas de ingresso no IFRS acesse o [🔗]({link})")
        except:
            dispatcher.utter_message(
                text="Desculpe, tivemos alguns problemas para encontrar as tuas informações! 😓")

        return [SlotSet("ingress_modality", None)]


class InformCoursesRedoRegister(Action):
    def name(self) -> Text:
        return "action_courses_redo_register"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Action que mostra informações sobre a rematrícula nos cursos ofertados pelo IFRS
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
        modality = tracker.get_slot("courses_modality").lower()

        modalities_buttons = {
            "integrado": buttons_integrado,
            "subsequente": buttons_subsequente,
            "superior": buttons_superior,
        }

        # Dispatcher the button selector according with the chosen modality
        dispatcher.utter_message(
            text="Para qual curso gostaria de obter informações sobre a rematricula?",
            buttons=modalities_buttons[modality],
            button_type="vertical")

        return []


class InformReDoRegister(Action):
    def name(self) -> Text:
        return "action_inform_redo_register"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Action que direciona para o link do sistema de rematricula de acordo com o nome do curso/modalidade
        """
        # definindo variáveis setadas pelo slot do usuário
        course_modality = tracker.get_slot("courses_modality").title()
        course_name = tracker.get_slot("courses_name").title()

        # buscando informações na api
        data = req_json("informacoes_sobre_rematricula")

        # buscando a ultima atualização conforme slots de busca do usuário
        dictionary = {
            "modalidade_do_curso": course_modality,
            "nome_do_curso": course_name
        }
        try:
            req = last_info(data=data, dictionary=dictionary)

            # varáveis de banco de dados
            data_de_inicio = req["data_de_inicio"]
            data_de_fim = req["data_de_fim"]
            link = req["link_1"]
            # descricao = req["descricao"]

            dispatcher.utter_message(
                text=f'Para realizar a rematrícula no {course_name} acesse o [link]({link})!')
            dispatcher.utter_message(
                text=f'Fique atento ao período de rematrícula que vai do dia {data_de_inicio} até {data_de_fim}!')
        except:
            dispatcher.utter_message(
                text=f'Desculpa tivemos alguns problemas para encontrar sua requisição! 😓')

        return [SlotSet("courses_modality", None), SlotSet("courses_name", None)]


class WhatBotDo(Action):
    def name(self) -> Text:
        return "action_what_bot_do"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text=f"Aqui estão alguns assuntos em que posso ajudar:👇\
            \n➡️ Calendário acadêmico\
            \n➡️ Comprovante de matrícula\
            \n➡️ Contato dos professores\
            \n➡️ Cursos disponíveis\
            \n➡️ Grade de horários\
            \n➡️ Informações sobre inscrição/matrícula\
            \n➡️ Informações sobre rematrícula\
            \n➡️ Requerimentos ou formulários\
            \n➡️ Como acessar os sistemas acadêmicos")

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
        data = req_json("requerimentos_ou_formularios")
        try:
            # busca por todas as recorrencias do requerimento no json e recebe a ultima atualização do requerimento
            dictionary = {
                'nome_do_requerimento': requirement
            }
            req = last_info(data=data, dictionary=dictionary)
            description = req["descricao"]
            link = req["link_1"]
            data_inicio = req["data_de_inicio"]
            data_fim = req["data_de_fim"]

            dispatcher.utter_message(text=f'*{requirement}* 👇')
            dispatcher.utter_message(text=f"[click aqui]({link})")
            dispatcher.utter_message(text=description)
            dispatcher.utter_message(
                text=f"Lembrando que o prazo para preenchimento vai de *{data_inicio}* até *{data_fim}*")
        except:
            dispatcher.utter_message(
                text=f'O requerimento \n"_{requirement}_" \nestá indisponível no momento 😓')

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
        data = req_json("tutoriais_de_acessos_a_sistemas_academicos")

        try:
            # retorno da ultima atualização
            dictionary = {
                'nome_do_sistema': system
            }
            req = last_info(data=data, dictionary=dictionary)

            # variaves db
            description = req["descricao"]
            link_1 = req["link_1"]
            link_2 = req["link_2"]

            # dispachando informações
            dispatcher.utter_message(text=description)
            dispatcher.utter_message(
                text=f'Segue o [link]({link_1}) para acessar o {system}!')

        except:
            dispatcher.utter_message(
                text=f"Estamos com dificuldades de encontrar teu tutorial para o {system} 😓")

        return [SlotSet("system", None)]


class UserNameFormValidate(FormValidationAction):
    def name(self) -> Text:
        return "validate_user_name_form"

    def validate_user_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:

        user_id = tracker.sender_id
        name = get_username(user_id)

        return {"user_name": name}


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

        name = slot_value.title()
        if len(name) == 0 or " " in name:
            dispatcher.utter_message(
                text="Não entendi, pode ter sido um erro de digitação")
            dispatcher.utter_message(
                text="Digite apenas o primeiro nome do professor!")
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
        if len(name) == 0 or " " in name:
            dispatcher.utter_message(
                text="Não entendi, pode ter sido um erro de digitação")
            dispatcher.utter_message(
                text="Digite apenas um sobrenome do professor!")
            return {"professor_last_name": None}
        return {"professor_last_name": name}

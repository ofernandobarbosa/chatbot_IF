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
        dispatcher.utter_message(
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
            text=f"Tu pode me solicitar:👇\n➡️ Contato dos professores\n➡️ Calendário acadêmico\n➡️ Cursos disponíveis\n➡️ Comprovante de matrícula\n➡️ Informações sobre as aulas\n➡️ Inscrições\n➡️ Como fazer a rematrícula\n➡️ Requerimentos/Formulários")

        return []


class Requirements(Action):
    def name(self) -> Text:
        return "action_get_requirements"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        requirements = {
            "aproveitamento de estudos": {
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSfwES_YoPLvp7Tda6HDVvCyEJMepUFmjrRZb0taztCI9pO3XQ/closedform",
                "description": "Os estudantes da modalidade subsequente e superior que já concluíram componentes curriculares poderão solicitar aproveitamento de estudos. Para participar, devem solicitar o aproveitamento nos prazos definidos em calendário acadêmico, esse prazo geralmente ocorre no início de cada semestre letivo.\nMaiores informações: Artigos 207 a 212 da Organização Didática.",
                "data_inicio": "",
                "data_fim": ""
            },
            "atividades complementares": {
                "link": "https://docs.google.com/forms/d/e/1FAIpQLScPbUohpBv_9St6Xl0KVHb9YhlCqOXS3SoETL9EefYzDs8dxQ/viewform",
                "description": "Os cursos superiores de tecnologia estarão organizados em uma base de conhecimentos científicos e tecnológicos, dessa maneira poderão ser previstas horas de atividades complementares realizadas por meio de desenvolvimento de projetos integradores/técnicos, de extensão e/ou de pesquisa e outras formas de atividades acadêmico-científico-culturais. \nMaiores informações: Artigos 243 e 244 da Organização Didática.",
                "data_inicio": "",
                "data_fim": ""
            },
            "cancelamento de matrícula": {
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSdXJ6XzztG7ynCO5e1lGlgQ1Zu_MjdUqfu7jH4y84CgFlZfFw/viewform?pli=1",
                "description": "Entende-se por cancelamento da matrícula, o ato pelo qual o estudante solicita sua desvinculação permanente com a Instituição. A solicitação poderá ser realizada a qualquer tempo. \nMaiores informações: Artigos 144 e 145 da Organização Didática.",
                "data_inicio": "",
                "data_fim": ""
            },
            "certificação de conhecimentos": {
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSc6FfovGNvTSnsPBw9O4NYxu4FHW52RPrpT3GSb7-Qltsg57g/closedform",
                "description": "Os alunos da modalidade subsequente e superior poderão requerer certificação de conhecimentos, adquiridos através de experiências previamente vivenciadas, inclusive fora do ambiente escolar, com o fim de alcançar a dispensa de um ou mais componentes curriculares da matriz do curso. Para participar, devem solicitar a certificação nos prazos definidos em calendário acadêmico, esse prazo geralmente ocorre no início de cada semestre letivo. A certificação de conhecimentos dar-se-á mediante a aplicação de instrumento de avaliação realizada por um professor da área, ao qual caberá emitir parecer conclusivo sobre o pleito. \nMaiores informações: Artigos 221 a 223 da Organização Didática.",
                "data_inicio": "",
                "data_fim": ""
            },
            "justificativa de falta": {
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSep-LsbRj0TOCiF3tMVInG67TI0O_mPLWcwayvgjqBkZZxT1w/viewform?pli=1",
                "description": "Entende-se por justificativa de faltas, o ato de o aluno apresentar o motivo que impediu de comparecer à atividade pedagógica. No caso de as faltas serem abonadas ocorre a reversão do registro de falta no Diário de Classe. Ao estudante que faltar a qualquer uma das verificações de aprendizagem ou deixar de executar trabalho escolar/acadêmico será facultado o direito à nova oportunidade, se requerida no prazo de 2 (dois) dias úteis após o término de vigência do atestado. \nMaiores informações: Artigos 153 a 156 da Organização Didática.",
                "data_inicio": "",
                "data_fim": ""
            },
            "quebra de pré-requisito": {
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSfO5C7i1QjDnHzw_i5ETmi3KWZzY0Y-onhDTIzoSgTPyNLZAA/closedform?pli=1",
                "description": "Entende-se por quebra de pré-requisito, o ato formal do aluno solicitar que seja matriculado em alguma disciplina de sua matriz curricular, mesmo que não cumpra o pré-requisito estipulado no Projeto Pedagógico de seu curso. A solicitação de quebra de pré-requisito deve ser solicitada em prazo determinado em calendário acadêmico, esse prazo geralmente ocorre no início de cada semestre letivo.",
                "data_inicio": "",
                "data_fim": ""
            },
            "reingresso": {
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSeWC1TQ7-utnkFvDqnR74uXzD06EtRwV89ziIST61HtV2ZjiA/closedform",
                "description": "Entende-se por reingresso, o ato formal pelo qual o estudante solicita o retorno para o mesmo curso e campus do IFRS, quando afastado por trancamento da matrícula a pedido ou de forma automática. Deve ser solicitado nos prazos definidos em calendário acadêmico, esse prazo geralmente ocorre no início de cada semestre letivo. \nMaiores informações: Artigos 146 a 149 da Organização Didática.",
                "data_inicio": "",
                "data_fim": ""
            },
            "trancamento de disciplina": {
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSd5d77N0Ze8Izbojb_8q1Opf5yIQ1P8uDoa4f0eDW3_UcMP6w/closedform",
                "description": "Entende-se por trancamento de componente curricular, o ato formal pelo qual o estudante da modalidade subsequente ou superior solicita a desistência de um ou mais componentes curriculares do curso. Será permitido o trancamento de componentes curriculares, em período previsto no calendário acadêmico, exceto quando o estudante for ingressante. \nMaiores informações: Artigos 8º e 138 da Organização Didática.",
                "data_inicio": "",
                "data_fim": ""
            },
            "trancamento de matrícula": {
                "link": "https://docs.google.com/forms/d/e/1FAIpQLSfoNbrKFESuHX6j4VZjUJddoeowxSdJV2VhrX-a38e8lH9sZg/viewform?pli=1",
                "description": "Entende-se por trancamento da matrícula, o ato formal pelo qual se dá a interrupção temporária dos estudos durante o semestre letivo, sem a perda do vínculo do estudante com a Instituição, devendo o aluno renovar a cada semestre enquanto desejado. Será permitido o trancamento de matrícula, a qualquer tempo para alunos da modalidade subsequente e superior, exceto quando o estudante for ingressante. O estudante em situação de trancamento total de matrícula perde o direito aos auxílios da Assistência Estudantil.\n\n*Maiores informações*: Artigos 138 e 143 da [Organização Didática](https://ifrs.edu.br/wp-content/uploads/2017/07/OD-Alterada-Publica%C3%A7%C3%A3o-Portal-1.pdf).",
                "data_inicio": "",
                "data_fim": ""
            },
        }

        requirement = tracker.get_slot("requirements").lower()
        text = requirements[requirement]["description"]
        link = requirements[requirement]["link"]

        dispatcher.utter_message(text=text)
        dispatcher.utter_message(text=f'`Segue` o [link]({link}) para o formulário! [](tg://user?id=<user_id>)')

        return [SlotSet("requirements", None)]


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

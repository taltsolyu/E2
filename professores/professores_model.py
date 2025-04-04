from flask import Blueprint, request, jsonify

professores_blueprint = Blueprint("professores", __name__)

dados = {
    "professores": [
        {
        'id': 1023,
        'nome': 'Lucas Silva',
        'idade': 41,
        'materia': 'Programação Orientada a Objetos',
        'observacoes': 'O professor explica os conteúdos de forma clara e organizada, facilitando o entendimento dos temas abordados.'
        },
        
        {
        'id': 1024,
        'nome': 'Ana Oliveira',
        'idade': 42,
        'materia': 'Banco de Dados',
        'observacoes': 'Durante as aulas, ela incentiva a participação dos alunos, fazendo perguntas e promovendo discussões para garantir que todos acompanhem o ritmo.'
        },
        
        {
        'id': 1025,
        'nome': 'Pedro Santos',
        'idade': 30,
        'materia': 'Estrutura de Dados',
        'observacoes': 'Ele costuma apresentar exemplos do dia a dia ou casos reais para ajudar na aplicação dos conceitos.'
        },
        
        {
        'id': 1026,
        'nome': 'Mariana Costa',
        'idade': 63,
        'materia': 'Redes de Computadores',
        'observacoes': ' A aula é bem estruturada e dinâmica, o que mantém a atenção dos alunos e evita que o conteúdo fique monótono.'
        },
        
        {
        'id': 1027,
        'nome': 'Carlos Lima',
        'idade': 34,
        'materia': 'Desenvolvimento Web',
        'observacoes': 'O professor dá retorno sobre as dúvidas e os exercícios feitos em aula, reforçando os pontos fortes e ajudando a corrigir os erros de forma construtiva.'
        }
        ]
    }

def getTodosProfessores():
  return jsonify(dados["professores"])

def criarProfessor():
    dados = request.get_json()
    for key, value in dados.items():
        if(not value):
          return jsonify({"mensagem": f"O campo '{key}' é obrigatório e deve estar preenchido."}), 400
    return jsonify(dados)

def getPorIdProfessor(idProfessor):
    for professor in dados['professores']:
        if professor['id'] == idProfessor:
            return jsonify(professor)
    return jsonify(None), 204

def attProfessor(idProfessor):
    professor = request.get_json()
    for i in range (0,len(dados['professores'])):
        if dados['professores'][i]['id'] == idProfessor:
            professor_desatualizado = dados['professores'][i] 
            professor_att = merge_dicts(professor_desatualizado,professor)
            dados['professores'][i] = professor_att
            return jsonify(professor_att)
    return jsonify(None), 400

def merge_dicts(dict1, dict2):
    merged = dict1.copy()  
    for key, value in dict2.items():
        if key in merged:
            if merged[key] != value:
                merged[key] = value
        else:
            merged[key] = value  
    return merged

def deletarProfessor(idProfessor):
    for professor in dados['professores']:
        if professor['id'] == idProfessor:
            id_para_remover = idProfessor
            dados['professores'] = [prof for prof in dados['professores'] if prof['id'] != id_para_remover]
            return jsonify(professor)
    return jsonify(None), 400

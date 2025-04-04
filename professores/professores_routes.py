from flask import Blueprint, request, jsonify
from .professores_model import getTodosProfessores, criarProfessor, getPorIdProfessor, attProfessor, merge_dicts, deletarProfessor, dados

professores_bp = Blueprint('professores', __name__)

@professores_bp.route("/professores", methods=["GET"])
def getTodosProfessores():
  return jsonify(dados["professores"])

@professores_bp.route("/professores",methods=["POST"])
def criarProfessor():
    dados = request.get_json()
    for key, value in dados.items():
        if(not value):
          return jsonify({"mensagem": f"O campo '{key}' é obrigatório e deve estar preenchido."}), 400
    return jsonify(dados)

@professores_bp.route("/professores/<int:idProfessor>", methods=['GET'])
def getPorIdProfessor(idProfessor):
    for professor in dados['professores']:
        if professor['id'] == idProfessor:
            return jsonify(professor)
    return jsonify(None), 204

@professores_bp.route("/professores/<int:idProfessor>", methods=['PUT'])
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

@professores_bp.route("/professores/<int:idProfessor>", methods=['DELETE'])
def deletarProfessor(idProfessor):
    for professor in dados['professores']:
        if professor['id'] == idProfessor:
            id_para_remover = idProfessor
            dados['professores'] = [prof for prof in dados['professores'] if prof['id'] != id_para_remover]
            return jsonify(professor)
    return jsonify(None), 400

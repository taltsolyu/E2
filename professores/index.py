from flask import Blueprint

professor = Blueprint('professore',__name__)

@professor.route('/professor', methods=["GET"])
def main():
  return 'Rotas para professor'
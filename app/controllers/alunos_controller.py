from http import HTTPStatus
from app.models.aluno_model import AlunoModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from app.configs.database import db
from app.exception.id_not_existent_exc import IDNotExistent
from app.exception.key_not_found import KeyNotFound
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from app.models.aluno_model import AlunoModel

@jwt_required()
def create_aluno():

        try:    
            data = request.get_json()
            token_id = get_jwt_identity()
            # print(token_id)

            imc_response = (data['peso']/(data['altura'] * data['altura']))
            imc_formatted = ("%.2f" % round(imc_response, 2))

            data['personal_id'] = token_id['id']
            data['imc'] = imc_formatted
            #print(type(data['imc']))

            print(f'{data=}')

            aluno = AlunoModel(**data)
           

            
            print(aluno)            

            response = {
                    "nome": aluno.nome,
                    "telefone": aluno.telefone,
                    "email":aluno.email,
                    "peso": aluno.peso,
                    "altura":aluno.altura,
                    "imc": imc_formatted, 
                    # "personal":{
                    #     "id": aluno.personal.id, 
                    #     "nome": aluno.personal.nome,
                    #     "cpf": aluno.personal.cpf,
                    # }                  
                }

            AlunoModel.add_session(aluno) 
            print(aluno)   
            
            return jsonify(aluno), HTTPStatus.CREATED
        except IntegrityError:
            return {'msg': 'Email ou telefone já existe'} 

@jwt_required()
def update_by_id(aluno_id):
    data = request.get_json()
    oficial_keys = ["nome", "telefone", "email", "peso", "altura"]
    try:
        for dkey in data.keys():
            if dkey not in oficial_keys:
                raise KeyNotFound
        return jsonify(AlunoModel.update_aluno(aluno_id, data)), HTTPStatus.OK
    except KeyNotFound:
        return {'msg': 'Chave não encontrada'}, HTTPStatus.NOT_FOUND
        
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND

@jwt_required()
def retrieve():
      session: Session = db.session()
      alunos = session.query(AlunoModel).all()
      return {'count': len(alunos),'alunos': alunos}, HTTPStatus.OK

@jwt_required()
def retrieve_by_id(aluno_id): 
      try: 
          return jsonify(AlunoModel.select_by_id(aluno_id)), HTTPStatus.OK
      except IDNotExistent: 
          return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
@jwt_required()
def delete_by_id(aluno_id):
    try:
        AlunoModel.delete_aluno(aluno_id)
        return '',HTTPStatus.NO_CONTENT
    except IDNotExistent: 
        return {'msg': 'Id não encontrado'}, HTTPStatus.NOT_FOUND
    
    
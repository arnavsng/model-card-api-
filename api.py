from flask import jsonify, request
from app import app, db
from flask_sqlalchemy import SQLAlchemy
from app.models import ModelCard
from marshmallow import fields, ValidationError
from sqlalchemy.exc import SQLAlchemyError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field


#deleted the first two api becuase they were doing the same task as the api in routes.py
# Schema for serializing/deserializing ModelCard instances; model_card_schema for single instance, model_cards_schema for multiple instances
class ModelCardSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ModelCard
        load_instance = True
        


model_card_schema = ModelCardSchema()
model_cards_schema = ModelCardSchema(many=True)


#To create new model card info 
@app.route('/add-model_card', methods=['POST'])
def create_model_card():
    data = request.get_json()
    model_card = ModelCard(**data)
    db.session.add(model_card)
    db.session.commit()
    return jsonify(model_card.to_dict()), 200



#To update existing modelcard info by inputting modelcard id
@app.route('/update-model_cards/<int:id>', methods=['PUT'])
def update_model_card(id):
    data = request.get_json()
    
    
    try:
        schema = ModelCardSchema()
        updated_data = schema.load(data, partial=True)  # Partial=True allows partial updates
    except ValidationError as e:
        return jsonify({'error': e.messages}), 400
    
    try:
        model_card = ModelCard.query.get_or_404(id)
        for key, value in updated_data.items():
            setattr(model_card, key, value)
        db.session.commit()
        return model_card_schema.jsonify(model_card), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 400


#To delete a modelcard from the database 
@app.route('/delete-model_cards/<int:id>', methods=['DELETE'])
def delete_model(id):
    try:
        model_card = ModelCard.query.get_or_404(id)
        db.session.delete(model_card)
        db.session.commit()
        return jsonify({'message': f'ModelCard with id {id} has been deleted.'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 400

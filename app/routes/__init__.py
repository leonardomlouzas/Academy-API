from flask import Flask

from .personal_route import bp as bp_personal
from .equipment_route import bp as bp_equipment
from .exercise_route import bp as bp_exercise
from .training_route import bp as bp_training
from .students_route import bp as bp_students

def init_app(app: Flask):
    app.register_blueprint(bp_personal)
    app.register_blueprint(bp_equipment)
    app.register_blueprint(bp_exercise)
    app.register_blueprint(bp_training)
    app.register_blueprint(bp_students)

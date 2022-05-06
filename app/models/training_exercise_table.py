from app.configs.database import db

treino_exercicio = db.Table(
    "treino_exercicio",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("treino_id", db.Integer, db.ForeignKey("treino.id")),
    db.Column("exercicio_id", db.Integer, db.ForeignKey("exercicio.id")),
)

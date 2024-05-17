from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///asistencias.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    asistencias = db.relationship('Asistencia', backref='estudiante', lazy=True)

class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    asistencias = db.relationship('Asistencia', backref='curso', lazy=True)

class Asistencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    asistio = db.Column(db.Boolean, default=False)

@app.route('/estudiantes', methods=['GET', 'POST'])
def manejar_estudiantes():
    if request.method == 'GET':
        estudiantes = Estudiante.query.all()
        return jsonify([{'id': estudiante.id, 'nombre': estudiante.nombre, 'apellido': estudiante.apellido} for estudiante in estudiantes])
    elif request.method == 'POST':
        data = request.get_json()
        nuevo_estudiante = Estudiante(nombre=data['nombre'], apellido=data['apellido'])
        db.session.add(nuevo_estudiante)
        db.session.commit()
        return jsonify({'id': nuevo_estudiante.id, 'nombre': nuevo_estudiante.nombre, 'apellido': nuevo_estudiante.apellido}), 201

@app.route('/estudiantes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manejar_estudiante(id):
    estudiante = Estudiante.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'id': estudiante.id, 'nombre': estudiante.nombre, 'apellido': estudiante.apellido})
    elif request.method == 'PUT':
        data = request.get_json()
        estudiante.nombre = data.get('nombre', estudiante.nombre)
        estudiante.apellido = data.get('apellido', estudiante.apellido)
        db.session.commit()
        return jsonify({'id': estudiante.id, 'nombre': estudiante.nombre, 'apellido': estudiante.apellido})
    elif request.method == 'DELETE':
        db.session.delete(estudiante)
        db.session.commit()
        return jsonify({'message': 'Estudiante eliminado correctamente'}), 204

@app.route('/cursos', methods=['GET', 'POST'])
def manejar_cursos():
    if request.method == 'GET':
        cursos = Curso.query.all()
        return jsonify([{'id': curso.id, 'nombre': curso.nombre} for curso in cursos])
    elif request.method == 'POST':
        data = request.get_json()
        nuevo_curso = Curso(nombre=data['nombre'])
        db.session.add(nuevo_curso)
        db.session.commit()
        return jsonify({'id': nuevo_curso.id, 'nombre': nuevo_curso.nombre}), 201

@app.route('/cursos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manejar_curso(id):
    curso = Curso.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'id': curso.id, 'nombre': curso.nombre})
    elif request.method == 'PUT':
        data = request.get_json()
        curso.nombre = data.get('nombre', curso.nombre)
        db.session.commit()
        return jsonify({'id': curso.id, 'nombre': curso.nombre})
    elif request.method == 'DELETE':
        db.session.delete(curso)
        db.session.commit()
        return jsonify({'message': 'Curso eliminado correctamente'}), 204

@app.route('/asistencias', methods=['GET', 'POST'])
def manejar_asistencias():
    if request.method == 'GET':
        asistencias = Asistencia.query.all()
        return jsonify([{'id': asistencia.id, 'fecha': asistencia.fecha.strftime('%Y-%m-%d %H:%M:%S'), 'estudiante_id': asistencia.estudiante_id, 'curso_id': asistencia.curso_id, 'asistio': asistencia.asistio} for asistencia in asistencias])
    elif request.method == 'POST':
        data = request.get_json()
        nueva_asistencia = Asistencia(estudiante_id=data['estudiante_id'], curso_id=data['curso_id'], asistio=data['asistio'])
        db.session.add(nueva_asistencia)
        db.session.commit()
        return jsonify({'id': nueva_asistencia.id, 'fecha': nueva_asistencia.fecha.strftime('%Y-%m-%d %H:%M:%S'), 'estudiante_id': nueva_asistencia.estudiante_id, 'curso_id': nueva_asistencia.curso_id, 'asistio': nueva_asistencia.asistio}), 201

@app.route('/asistencias/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manejar_asistencia(id):
    asistencia = Asistencia.query.get_or_404(id)
    if request.method == 'GET':
        return jsonify({'id': asistencia.id, 'fecha': asistencia.fecha.strftime('%Y-%m-%d %H:%M:%S'), 'estudiante_id': asistencia.estudiante_id, 'curso_id': asistencia.curso_id, 'asistio': asistencia.asistio})
    elif request.method == 'PUT':
        data = request.get_json()
        asistencia.estudiante_id = data.get('estudiante_id', asistencia.estudiante_id)
        asistencia.curso_id = data.get('curso_id', asistencia.curso_id)
        asistencia.asistio = data.get('asistio', asistencia.asistio)
        db.session.commit()
        return jsonify({'id': asistencia.id, 'fecha': asistencia.fecha.strftime('%Y-%m-%d %H:%M:%S'), 'estudiante_id': asistencia.estudiante_id, 'curso_id': asistencia.curso_id, 'asistio': asistencia.asistio})
    elif request.method == 'DELETE':
        db.session.delete(asistencia)
        db.session.commit()
        return jsonify({'message': 'Asistencia eliminada correctamente'}), 204

if __name__ == '__main__':
    app.run(debug=True)

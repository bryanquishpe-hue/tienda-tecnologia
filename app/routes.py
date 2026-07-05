from flask import Blueprint, render_template, request, redirect, url_for
from .models import Producto
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    busqueda = request.args.get('busqueda', '')
    
    if busqueda:
        productos = Producto.query.filter(Producto.nombre.ilike(f'%{busqueda}%')).all()
    else:
        productos = Producto.query.all()
    
    return render_template('index.html', productos=productos, busqueda=busqueda)


@main.route('/agregar', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']

        nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock)
        db.session.add(nuevo_producto)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('agregar.html')


@main.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.precio = request.form['precio']
        producto.stock = request.form['stock']

        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('editar.html', producto=producto)


@main.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('main.index'))
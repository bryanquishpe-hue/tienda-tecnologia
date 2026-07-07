from flask import Blueprint, render_template, request, redirect, url_for
from .models import Producto
from . import db


main = Blueprint('main', __name__)


# ==========================
# PÁGINA PRINCIPAL
# ==========================
@main.route('/')
def index():

    busqueda = request.args.get('busqueda', '')

    try:
        if busqueda:
            productos = Producto.query.filter(
                Producto.nombre.ilike(f"%{busqueda}%")
            ).all()
        else:
            productos = Producto.query.all()

    except Exception as e:
        print("Error cargando productos:", e)
        productos = []

    return render_template(
        "index.html",
        productos=productos,
        busqueda=busqueda
    )


# ==========================
# AGREGAR PRODUCTO
# ==========================
@main.route('/agregar', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        stock = request.form.get('stock')

        producto = Producto(
            nombre=nombre,
            precio=float(precio),
            stock=int(stock)
        )

        db.session.add(producto)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template("agregar.html")


# ==========================
# EDITAR PRODUCTO
# ==========================
@main.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':
        producto.nombre = request.form.get('nombre')
        producto.precio = float(request.form.get('precio'))
        producto.stock = int(request.form.get('stock'))

        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template("editar.html", producto=producto)


# ==========================
# ELIMINAR PRODUCTO
# ==========================
@main.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)

    db.session.delete(producto)
    db.session.commit()

    return redirect(url_for('main.index'))
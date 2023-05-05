from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from models import db, User, Car, car_schema, cars_schema
from flask_login import current_user, login_required


site = Blueprint('site', __name__,template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/cars')
@login_required
def cars():
    cars = Car.query.all()
    return render_template('cars.html', cars=cars)

# @site.route('/update')
# @login_required
# def update():
#     return render_template('update.html')

@site.route('/create_car', methods=['POST'])
@login_required
def create_car():
    vin = request.form['vin']
    year = request.form['year']
    make = request.form['make']
    model = request.form['model']
    color = request.form['color']
    user_id = current_user.id
    
    car = Car(vin = vin, year=year, make=make, model=model, color=color, user_id = user_id )
    db.session.add(car)
    db.session.commit()
    
    return redirect(url_for('site.cars'))


@site.route('/update_car/<id>', methods=['POST', 'PUT'])
@login_required
def update_car(id):
    # car = Car.query.get(id)
    vin = Car.query.filter_by(id=id).first()
    # form=update_car
    if request.method == 'POST':
        print("I printed!")
        if vin:
        
            vin = request.form['vin']
            year = request.form['year']
            make = request.form['make']
            model = request.form['model']
            color = request.form['color']
            
            car = Car(vin ='',  year ='', make='', model='', color='')
            
            db.session.update(car)
            db.session.commit()
            return  redirect(url_for('/site.cars'))
        return f"Car does not exist."
        
    
    return render_template('update.html', car=car)
    

@site.route('/delete_car/<id>', methods=['POST, GET'])
@login_required
def delete_car(id):
    car = Car.query.get(id)
    if car:
        db.session.delete(car)
        db.session.commit()
        return redirect(url_for('site.cars'))
    
    
    return redirect(url_for('site.cars'))


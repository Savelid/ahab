from flask import Flask , render_template , request , redirect , url_for, flash

# Import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import classes for database tables
from database_setup import Base, Overview

app = Flask(__name__)

# Create session and connect to DB
engine = create_engine('sqlite:///ahab.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
def restaurantID():
	restaurants = session.query(Overview).all()
	output = ''
	output += '<ul>'
	for i in restaurants:
		output += '<li>'
		output += '%s' % i.author
		output += '</li>'
	output += '</ul>'
	return output

@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
	items = session.query(MenuItem).filter_by(resturant_id = restaurant.id)
	
	return render_template('menu.html', restaurant=restaurant, items=items)

# Task 1: Create route for newMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):

    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form[
                           'description'], price=request.form['price'], course=request.form['course'], resturant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("new menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

# Task 2: Create route for editMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
	editedItem = session.query(MenuItem).filter_by(id = menu_id).one()
	if request.method == 'POST':
		if request.form['name']:
			editedItem.name = request.form['name']
		session.add(editedItem)
		session.commit()
		flash("Item edited!")
		return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))
	else:
		#USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
		return render_template('editmenuitem.html', restaurant_id = restaurant_id, menu_id = menu_id, item = editedItem)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/', methods = ['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
	item = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		session.delete(item)
		session.commit()
		flash("Item deleted!")
		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))

	else:
		return render_template('deletemenuitem.html', item=item)

##### Server stuff #####
if __name__ == '__main__' :
	# 
	app.secret_key = 'super_secret_key'
	# Debug mode let me change code without restarting the server
	# And provides a debuger in the browser
	app.debug = True
	# Run server. if 0.0.0.0 it listens in all public IP addresses
	app.run(host = '0.0.0.0', port = 5000)
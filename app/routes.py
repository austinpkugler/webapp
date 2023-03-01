from flask import render_template, url_for, redirect, flash

from app import app, db, forms, models


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/page1')
def page1():
    return render_template('page1.html', title='Page 1')


@app.route('/page2')
def page2():
    return render_template('page2.html', title='Page 2')


@app.route('/locations', methods=['GET', 'POST'])
def locations():
    form = forms.LocationForm()
    if form.validate_on_submit():
        location = models.Location(form.name.data, form.city.data, form.address.data, form.zip_code.data)
        db.session.add(location)
        db.session.commit()
        flash(f'A new location was added!', 'success')
        return redirect(url_for('home'))
    return render_template('locations.html', title='Locations', form=form, locations=models.Location.query.all())

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
CORS(app)  # Allow frontend access

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define model for storing results
class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    specimen_size = db.Column(db.Float)
    magnification = db.Column(db.Float)
    actual_size = db.Column(db.Float)

# Create the database and table (run once)
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    username = request.form.get('username')
    specimen_size = float(request.form.get('specimenSize'))
    magnification = float(request.form.get('magnification'))

    try:
        actual_size = specimen_size / magnification

        # Save result to the database
        new_result = Result(
            username=username,
            specimen_size=specimen_size,
            magnification=magnification,
            actual_size=actual_size
        )
        db.session.add(new_result)
        db.session.commit()

        return f"User: {username}, Actual Size: {actual_size:.2f} units"
    except Exception as e:
        return f"Error in calculation: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)

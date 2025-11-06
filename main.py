from app import create_app, db
from flask import render_template

app = create_app()

# Optional: provide current_year to templates
@app.context_processor
def inject_global_vars():
    from datetime import datetime
    return {'current_year': datetime.utcnow().year}

if __name__ == '__main__':
    # Create DB tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)

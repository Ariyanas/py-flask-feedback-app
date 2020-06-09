from app import app
from app.controllers.page_controller import index

app.route('/')(index)
from backend.app.data_model import load_model
from backend.app.main import app

data_model_created = False

if (data_model_created == False):
    data_model = load_model()
    data_model_created = True
if __name__ == '__main__':
    app.run(debug=True)


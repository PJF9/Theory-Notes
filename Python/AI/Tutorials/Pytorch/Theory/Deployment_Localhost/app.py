import torch
from PIL import Image
import os
from flask import Flask, request, render_template, url_for
from App.models import create_resNet18
from werkzeug.utils import secure_filename


# Initialize the App object
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')

# Creating the Pre-Trained Model
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
resNet, model_transforms = create_resNet18(num_classes=10)

# Loading the Trained Parameters
resNet.load_state_dict(torch.load(r"E:\Programming\Python\Python Modules\AI\Pytorch\Theory\Deployment Test\App\resNet.pth",
                                  map_location=torch.device("cpu")))
resNet.eval()
 

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Saving the image the user passes
    file = request.files['image']
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Performing Predictions
    with torch.inference_mode():
        model_logit = resNet(model_transforms(Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))).unsqueeze(dim=0))
        pred = classes[torch.softmax(model_logit, dim=1).argmax(dim=1)]
        prob = float(torch.softmax(model_logit, dim=1).max().item() * 100)
        
    return render_template('predict.html',
                           image=url_for('static', filename='uploads/{}'.format(filename)),
                           predict=pred,
                           prob=f"{prob:.2f}")


if __name__ == '__main__':
    app.run(debug=True)
    
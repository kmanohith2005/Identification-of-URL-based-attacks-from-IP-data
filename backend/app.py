import sys
import os
import numpy as np
import matplotlib.pyplot as plt

from flask import Flask, render_template, request

# allow backend to access model folder
sys.path.append(os.path.abspath("../model"))

from feature_extraction import extract_features

# load deep learning model
from tensorflow.keras.models import load_model


app = Flask(
    __name__,
    template_folder="../frontend",
    static_folder="../frontend/static"
)


# load .h5 model (correct file)
model = load_model("../model/url_attack_model.h5")


def attack_info(result):

    if result == "Malicious":

        return "This URL contains suspicious patterns commonly seen in phishing or malware attacks. Avoid entering personal data."

    else:

        return "This URL appears safe according to the trained deep learning model."


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    url = request.form["url"]

    # extract features
    features, ip, feature_dict = extract_features(url)

    # convert features to numpy
    features_array = np.array([features])


    # deep learning prediction
    probability = model.predict(features_array)[0][0]


    risk_score = round(probability * 100, 2)


    if probability > 0.5:

        result = "Malicious"
        attack_type = "Phishing / Malware"

    else:

        result = "Normal"
        attack_type = "Safe"


    # create graph
    labels = list(feature_dict.keys())
    values = list(feature_dict.values())

    os.makedirs("../frontend/static", exist_ok=True)

    graph_path = "../frontend/static/graph.png"


    plt.figure()

    plt.bar(labels, values)

    plt.xticks(rotation=30)

    plt.title("URL Feature Analysis")

    plt.savefig(graph_path, bbox_inches="tight")

    plt.close()


    info = attack_info(result)


    return render_template(

        "result.html",

        url=url,

        result=result,

        attack_type=attack_type,

        risk_score=risk_score,

        ip=ip,

        url_length=feature_dict["url_length"],

        info=info,

        graph="static/graph.png"

    )


if __name__ == "__main__":

    app.run(debug=True)
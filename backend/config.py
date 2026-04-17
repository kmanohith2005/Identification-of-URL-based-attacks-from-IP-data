class Config:
    # Flask settings
    DEBUG = True
    HOST = "127.0.0.1"
    PORT = 5000

    # Model paths
    MODEL_PATH = "model/url_attack_model.h5"
    LABEL_ENCODER_PATH = "model/label_encoder.pkl"

    # API settings
    JSON_SORT_KEYS = False

    # Security (for future use)
    SECRET_KEY = "url_attack_detection_secret"

# backend/routes.py
from flask import Blueprint, jsonify
from controller.connector import fetch_commits

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def index():
    return "Bem-vindo ao backend da aplicação!"

@routes.route('/commits', methods=['GET'])
def get_commits():
    commits = fetch_commits()
    commit_list = [
        {
            'id': commit.id,
            'commit_time': commit.commit_time,
            'commit_id': commit.commit_id,
            'ticket_id': commit.ticket_id,
            'commit_text': commit.commit_text,
            'prediction': commit.prediction,
            'label_status': commit.label_status,
            'history_datetime': commit.history_datetime,
        }
        for commit in commits
    ]
    return jsonify(commit_list)

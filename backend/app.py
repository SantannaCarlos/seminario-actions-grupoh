from flask import Flask, jsonify
import yaml
from pathlib import Path
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/api/workflow-summary")
def summary():
    caminho = Path("/data/deploy.yml")
    if not caminho.exists():
        return jsonify({"erro": "Arquivo deploy.yml não encontrado"}), 404

    dados = yaml.safe_load(caminho.read_text())
    jobs = dados.get("jobs", {})
    resultado = {
        "total_jobs": len(jobs),
        "detalhes": {nome: len(job.get("steps", [])) for nome, job in jobs.items()}
    }
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

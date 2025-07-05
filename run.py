import threading
from app import create_app
from app.config import Config
from app.workers.produto_worker import start_worker

app = create_app()

if __name__ == "__main__":
    # ✅ Inicia o worker em background
    t = threading.Thread(target=start_worker, daemon=True)
    t.start()

    # 🟢 Inicia o servidor Flask
    app.run(debug=Config.DEBUG, host="0.0.0.0", port=5000)


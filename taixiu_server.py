import random
import time
import os
import webbrowser
import threading
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Cho phép gọi API chéo cổng (CORS) nếu cần

# Quản lý số tiền và trạng thái người chơi trong bộ nhớ (RAM)
player_state = {
    "money": 0,
    "initialized": False
}

@app.route('/')
def home():
    # Phục vụ file taixiu.html ở thư mục gốc
    return send_from_directory('.', 'taixiu.html')

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        "money": player_state["money"],
        "initialized": player_state["initialized"]
    })

@app.route('/api/init', methods=['POST'])
def init_money():
    data = request.json or {}
    try:
        amount = int(data.get("amount", 0))
        if amount <= 0:
            return jsonify({"error": "Số tiền nạp phải lớn hơn 0"}), 400
        player_state["money"] = amount
        player_state["initialized"] = True
        return jsonify({"money": player_state["money"], "message": "Nạp tiền thành công!"})
    except (ValueError, TypeError):
        return jsonify({"error": "Số tiền không hợp lệ"}), 400

@app.route('/api/bet', methods=['POST'])
def place_bet():
    if not player_state["initialized"]:
        return jsonify({"error": "Vui lòng nạp tiền trước khi chơi"}), 400

    data = request.json or {}
    try:
        bet_amount = int(data.get("bet", 0))
        choice = data.get("choice", "").strip().upper()  # TÀI hoặc XỈU
    except (ValueError, TypeError):
        return jsonify({"error": "Dữ liệu đặt cược không hợp lệ"}), 400

    if bet_amount <= 0:
        return jsonify({"error": "Tiền cược phải lớn hơn 0"}), 400
    if bet_amount > player_state["money"]:
        return jsonify({"error": "Số dư không đủ để đặt cược"}), 400
    if choice not in ["TÀI", "XỈU"]:
        return jsonify({"error": "Lựa chọn chỉ có thể là TÀI hoặc XỈU"}), 400

    # Lắc 3 xúc xắc ngẫu nhiên
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice_sum = dice1 + dice2 + dice3

    # Xác định kết quả xúc xắc theo luật thực tế
    if dice1 == dice2 == dice3:
        result = "NỔ HŨ"  # Bộ ba đồng nhất (Tài/Xỉu đều thua, nhà cái ăn hết)
    elif 4 <= dice_sum <= 10:
        result = "XỈU"
    elif 11 <= dice_sum <= 17:
        result = "TÀI"
    else:
        result = "NỔ HŨ"  # Dự phòng cho trường hợp đặc biệt 3 hoặc 18 điểm

    # Phân định thắng thua
    win = (choice == result)
    if win:
        player_state["money"] += bet_amount
        win_amount = bet_amount
    else:
        player_state["money"] -= bet_amount
        win_amount = -bet_amount

    return jsonify({
        "dice": [dice1, dice2, dice3],
        "total": dice_sum,
        "result": result,
        "win": win,
        "win_amount": win_amount,
        "money": player_state["money"]
    })

@app.route('/api/deposit', methods=['POST'])
def deposit():
    data = request.json or {}
    try:
        amount = int(data.get("amount", 0))
        if amount <= 0:
            return jsonify({"error": "Số tiền nạp thêm phải lớn hơn 0"}), 400
        player_state["money"] += amount
        return jsonify({"money": player_state["money"], "message": f"Nạp thêm {amount} VND thành công!"})
    except (ValueError, TypeError):
        return jsonify({"error": "Số tiền nạp không hợp lệ"}), 400

def open_browser():
    time.sleep(1.5)  # Chờ server khởi động xong
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == '__main__':
    print("==================================================")
    print("SERVER TAI XIU PYTHON FLASK DANG KHOI DONG...")
    print("Hay mo trinh duyet va truy cap: http://127.0.0.1:5000")
    print("==================================================")
    
    # Chỉ mở trình duyệt một lần ở tiến trình chính (tránh mở nhiều tab khi reload)
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        threading.Thread(target=open_browser, daemon=True).start()
        
    app.run(debug=True, port=5000)

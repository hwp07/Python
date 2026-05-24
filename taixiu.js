const API_URL = window.location.origin.startsWith("file") 
    ? "http://127.0.0.1:5000/api" 
    : "/api";

// Game State
let userMoney = 0;
let selectedChoice = ""; // "TÀI" or "XỈU"
let isRolling = false;
let isInitialized = false;

// Kéo nặn bát úp
let isDragging = false;
let startX = 0, startY = 0;
let currentX = 0, currentY = 0;
let lidHasBeenOpened = true; // Bát mặc định mở khi load trang
let pendingResult = null;
let betAmountTemp = 0;

// DOM elements
const balanceDisplay = document.getElementById("balance-display");
const btnOpenDeposit = document.getElementById("btn-open-deposit");
const depositModal = document.getElementById("deposit-modal");
const btnCloseDepositModal = document.getElementById("btn-close-deposit-modal");
const btnSubmitDeposit = document.getElementById("btn-submit-deposit");
const inputDepositAmount = document.getElementById("input-deposit-amount");

const btnSelectXiu = document.getElementById("btn-select-xiu");
const btnSelectTai = document.getElementById("btn-select-tai");
const inputBetAmount = document.getElementById("input-bet-amount");
const btnShakePlay = document.getElementById("btn-shake-play");
const diceBowl = document.getElementById("dice-bowl");
const resultBubble = document.getElementById("result-bubble");
const toastBox = document.getElementById("toast-box");

// Bát úp & Hướng dẫn
const diceLid = document.getElementById("dice-lid");
const dragHint = document.getElementById("drag-hint");

const beadContainer = document.getElementById("history-bead-container");
const beadCountEl = document.getElementById("bead-count");
const logListContainer = document.getElementById("log-list-container");
const noHistoryText = document.getElementById("no-history-text");

// Set up Quick Bet buttons
document.querySelectorAll(".quick-bet-row .quick-bet-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        if (isRolling) return;
        
        // Remove active class from all quick bet buttons
        document.querySelectorAll(".quick-bet-row .quick-bet-btn").forEach(b => b.classList.remove("active"));
        
        // Add active class to clicked button
        btn.classList.add("active");
        
        if (btn.id === "btn-bet-all") {
            inputBetAmount.value = userMoney;
        } else {
            const value = parseInt(btn.getAttribute("data-val"));
            inputBetAmount.value = value;
        }
        updatePlayButtonState();
    });
});

// Initialize connection with python server
window.addEventListener("load", async () => {
    try {
        const response = await fetch(`${API_URL}/status`);
        if (response.ok) {
            const data = await response.json();
            userMoney = data.money;
            isInitialized = data.initialized;
            updateUI();
            
            if (!isInitialized) {
                // Show deposit modal immediately
                openModal();
            } else {
                showToast("Đã kết nối với máy chủ Python!", "success");
            }
        }
    } catch (err) {
        showToast("Không thể kết nối tới server Python. Vui lòng chạy file python trước!", "error");
    }
});

// Deposit actions
btnOpenDeposit.addEventListener("click", openModal);
btnCloseDepositModal.addEventListener("click", closeModal);
btnSubmitDeposit.addEventListener("click", handleDeposit);

function openModal() {
    depositModal.classList.add("show");
}

function closeModal() {
    if (!isInitialized && userMoney === 0) {
        showToast("Bạn cần nạp tiền để có thể chơi game!", "error");
        return;
    }
    depositModal.classList.remove("show");
}

async function handleDeposit() {
    const amount = parseInt(inputDepositAmount.value);
    if (isNaN(amount) || amount <= 0) {
        showToast("Vui lòng nhập số tiền hợp lệ lớn hơn 0", "error");
        return;
    }

    const endpoint = isInitialized ? "deposit" : "init";
    try {
        const response = await fetch(`${API_URL}/${endpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ amount: amount })
        });

        if (response.ok) {
            const data = await response.json();
            userMoney = data.money;
            isInitialized = true;
            updateUI();
            depositModal.classList.remove("show");
            showToast(`Nạp tiền thành công! Nhận +${formatNumber(amount)} VND`, "success");
        } else {
            const errData = await response.json();
            showToast(errData.error || "Giao dịch thất bại", "error");
        }
    } catch (err) {
        showToast("Không gửi được yêu cầu đến Server", "error");
    }
}

// Betting Choices selection
btnSelectXiu.addEventListener("click", () => {
    if (isRolling) return;
    selectedChoice = "XỈU";
    btnSelectXiu.classList.add("active");
    btnSelectTai.classList.remove("active");
    updatePlayButtonState();
});

btnSelectTai.addEventListener("click", () => {
    if (isRolling) return;
    selectedChoice = "TÀI";
    btnSelectTai.classList.add("active");
    btnSelectXiu.classList.remove("active");
    updatePlayButtonState();
});

inputBetAmount.addEventListener("input", () => {
    // Remove active class from all quick bet buttons since user is typing custom value
    document.querySelectorAll(".quick-bet-row .quick-bet-btn").forEach(b => b.classList.remove("active"));
    updatePlayButtonState();
});

function updatePlayButtonState() {
    const betVal = parseInt(inputBetAmount.value);
    const isValidBet = !isNaN(betVal) && betVal > 0 && betVal <= userMoney;
    const hasChoice = selectedChoice !== "";
    btnShakePlay.disabled = !isValidBet || !hasChoice || isRolling;
}

// Format currency helper
function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

function updateUI() {
    balanceDisplay.innerText = formatNumber(userMoney) + " VND";
    updatePlayButtonState();
}

// Show Toast Notifications
function showToast(message, type = "info") {
    let icon = "📢";
    if (type === "success") icon = "🎉";
    if (type === "error") icon = "❌";

    const toast = document.createElement("div");
    toast.className = `toast ${type}`;
    toast.innerHTML = `<span style="font-size: 2rem;">${icon}</span><div style="margin-top: 5px; line-height: 1.4;">${message}</div>`;
    toastBox.appendChild(toast);
    
    setTimeout(() => { toast.classList.add("show"); }, 50);

    setTimeout(() => {
        toast.classList.remove("show");
        setTimeout(() => { toast.remove(); }, 300);
    }, 3000);
}

// Draw Premium CSS Dice Faces
function getDiceHTML(value) {
    const dotPositions = {
        1: [5],
        2: [1, 9],
        3: [1, 5, 9],
        4: [1, 3, 7, 9],
        5: [1, 3, 5, 7, 9],
        6: [1, 3, 4, 6, 7, 9]
    };
    
    let dotsHTML = '';
    const activeDots = dotPositions[value] || [];
    
    for (let i = 1; i <= 9; i++) {
        if (activeDots.includes(i)) {
            // Dices 1 and 4 have red dots
            const isRed = (value === 1 && i === 5) || (value === 4);
            dotsHTML += `<div class="dot ${isRed ? 'red' : ''}"></div>`;
        } else {
            dotsHTML += `<div></div>`;
        }
    }
    
    // Random rotate rotation for realism
    const randomRotation = Math.floor(Math.random() * 20) - 10;
    return `<div class="dice dice-val-${value}" style="transform: rotate(${randomRotation}deg)">${dotsHTML}</div>`;
}

// Submit Play Bet
btnShakePlay.addEventListener("click", async () => {
    const betAmount = parseInt(inputBetAmount.value);
    if (isRolling || !selectedChoice || isNaN(betAmount)) return;

    isRolling = true;
    btnShakePlay.disabled = true;
    btnSelectTai.style.pointerEvents = "none";
    btnSelectXiu.style.pointerEvents = "none";
    
    // Clear active class from quick bet buttons when bet is placed
    document.querySelectorAll(".quick-bet-row .quick-bet-btn").forEach(b => b.classList.remove("active"));
    
    // Khởi tạo các phần tử wrapper
    const wrapperTop = document.querySelector(".dice-wrapper.top-center");
    const wrapperLeft = document.querySelector(".dice-wrapper.bottom-left");
    const wrapperRight = document.querySelector(".dice-wrapper.bottom-right");

    // Khởi tạo bát úp ở trạng thái ẩn và nằm ngoài đĩa
    diceLid.style.transition = "none";
    diceLid.style.transform = "translate(250px, -250px)";
    diceLid.style.opacity = "0";
    diceLid.style.pointerEvents = "none";
    lidHasBeenOpened = false;
    currentX = 250;
    currentY = -250;

    // Ẩn bóng thông báo kết quả và hướng dẫn
    resultBubble.classList.remove("show");
    dragHint.style.opacity = "0";

    // Bắt đầu hiệu ứng bay lên quay tròn bằng cách thêm class rolling-active
    if (wrapperTop) wrapperTop.classList.add("rolling-active");
    if (wrapperLeft) wrapperLeft.classList.add("rolling-active");
    if (wrapperRight) wrapperRight.classList.add("rolling-active");
    
    // Tạo hiệu ứng lắc số xúc xắc ngẫu nhiên trong lúc bay
    let tempRollInterval = setInterval(() => {
        if (wrapperTop) wrapperTop.innerHTML = getDiceHTML(Math.floor(Math.random() * 6) + 1);
        if (wrapperLeft) wrapperLeft.innerHTML = getDiceHTML(Math.floor(Math.random() * 6) + 1);
        if (wrapperRight) wrapperRight.innerHTML = getDiceHTML(Math.floor(Math.random() * 6) + 1);
    }, 100);

    try {
        const response = await fetch(`${API_URL}/bet`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                bet: betAmount,
                choice: selectedChoice
            })
        });

        if (response.ok) {
            const result = await response.json();
            
            // Đợi đúng 1.2s cho hiệu ứng xúc xắc bay lên và rơi xuống kết thúc
            setTimeout(() => {
                clearInterval(tempRollInterval);

                // Loại bỏ class hiệu ứng
                if (wrapperTop) wrapperTop.classList.remove("rolling-active");
                if (wrapperLeft) wrapperLeft.classList.remove("rolling-active");
                if (wrapperRight) wrapperRight.classList.remove("rolling-active");

                // Render kết quả xúc xắc thật (được che dưới bát)
                if (wrapperTop) wrapperTop.innerHTML = getDiceHTML(result.dice[0]);
                if (wrapperLeft) wrapperLeft.innerHTML = getDiceHTML(result.dice[1]);
                if (wrapperRight) wrapperRight.innerHTML = getDiceHTML(result.dice[2]);

                // Cho cái bát úp bay từ trên xuống đĩa để che xúc xắc
                diceLid.style.transition = "transform 0.6s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.6s ease";
                diceLid.style.transform = "translate(0px, 0px)";
                diceLid.style.opacity = "1";
                currentX = 0;
                currentY = 0;

                // Chờ cái bát trượt vào vị trí xong (0.6s) thì mới cho phép người chơi nặn
                setTimeout(() => {
                    diceLid.style.pointerEvents = "auto";
                    
                    // Lưu kết quả chờ người dùng kéo bát
                    pendingResult = result;
                    betAmountTemp = betAmount;

                    // Hiện hướng dẫn nặn bát
                    dragHint.style.opacity = "1";
                }, 600);

            }, 1200);

        } else {
            clearInterval(tempRollInterval);
            if (wrapperTop) wrapperTop.classList.remove("rolling-active");
            if (wrapperLeft) wrapperLeft.classList.remove("rolling-active");
            if (wrapperRight) wrapperRight.classList.remove("rolling-active");
            
            diceLid.style.transition = "none";
            diceLid.style.transform = "translate(250px, -250px)";
            diceLid.style.opacity = "0";
            diceLid.style.pointerEvents = "none";
            
            isRolling = false;
            btnShakePlay.disabled = false;
            btnSelectTai.style.pointerEvents = "auto";
            btnSelectXiu.style.pointerEvents = "auto";
            updatePlayButtonState();
            
            const errData = await response.json();
            showToast(errData.error || "Giao dịch đặt cược lỗi", "error");
        }
    } catch (err) {
        clearInterval(tempRollInterval);
        if (wrapperTop) wrapperTop.classList.remove("rolling-active");
        if (wrapperLeft) wrapperLeft.classList.remove("rolling-active");
        if (wrapperRight) wrapperRight.classList.remove("rolling-active");
        
        diceLid.style.transition = "none";
        diceLid.style.transform = "translate(250px, -250px)";
        diceLid.style.opacity = "0";
        diceLid.style.pointerEvents = "none";
        
        isRolling = false;
        btnShakePlay.disabled = false;
        btnSelectTai.style.pointerEvents = "auto";
        btnSelectXiu.style.pointerEvents = "auto";
        updatePlayButtonState();
        showToast("Lỗi kết nối tới Server!", "error");
    }
});

// Add history beads (the red/blue bubbles)
const historyBeads = [];
function addHistoryBead(result, total) {
    let className = "xiu";
    let shortText = "X";
    
    if (result === "TÀI") {
        className = "tai";
        shortText = "T";
    } else if (result === "NỔ HŨ") {
        className = "hu";
        shortText = "H";
    }

    const bead = document.createElement("div");
    bead.className = `bead ${className}`;
    bead.innerText = shortText;
    bead.title = `${result} (${total} điểm)`;

    // Prepend so latest is first, or append. Typically we append
    beadContainer.appendChild(bead);
    
    historyBeads.push({ result, total });
    beadCountEl.innerText = `${historyBeads.length} ván gần đây`;

    // Limit beads to 30 to prevent overflow
    if (beadContainer.children.length > 30) {
        beadContainer.removeChild(beadContainer.firstChild);
    }
}

// Add detailed textual history log
function addHistoryLog(win, choice, bet, result, total) {
    noHistoryText.style.display = "none";

    const logItem = document.createElement("div");
    logItem.className = `log-item ${win ? 'win' : 'lose'}`;
    
    const timestamp = new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    
    let betText = `${choice} ${formatNumber(bet)}đ`;
    let resultText = `Kết quả: ${result} (${total}đ)`;
    let winLoseText = win ? `+${formatNumber(bet)}` : `-${formatNumber(bet)}`;
    let valueClass = win ? "log-val-green" : "log-val-red";

    logItem.innerHTML = `
        <div>
            <span style="color: var(--text-muted); font-size: 0.75rem;">[${timestamp}]</span> 
            <strong>Cược ${betText}</strong>
            <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 2px;">${resultText}</div>
        </div>
        <div class="${valueClass}">${winLoseText}</div>
    `;

    logListContainer.insertBefore(logItem, logListContainer.firstChild);
}

// --- XỬ LÝ SỰ KIỆN KÉO BÁT NẶN XÚC XẮC ---
diceLid.addEventListener("pointerdown", onPointerDown);
window.addEventListener("pointermove", onPointerMove);
window.addEventListener("pointerup", onPointerUp);

function onPointerDown(e) {
    if (!isRolling || lidHasBeenOpened || pendingResult === null) return;
    isDragging = true;
    diceLid.style.cursor = "grabbing";
    
    // Ghi nhận vị trí bắt đầu
    startX = e.clientX - currentX;
    startY = e.clientY - currentY;
    
    diceLid.style.transition = "none";
}

function onPointerMove(e) {
    if (!isDragging) return;
    
    currentX = e.clientX - startX;
    currentY = e.clientY - startY;

    const distance = Math.sqrt(currentX * currentX + currentY * currentY);
    
    // Cập nhật vị trí cái bát
    diceLid.style.transform = `translate(${currentX}px, ${currentY}px)`;

    // Ẩn hướng dẫn kéo
    if (distance > 10) {
        dragHint.style.opacity = "0";
    }

    // Nếu kéo đủ xa (khoảng cách > 120px từ tâm) thì mở bát hoàn toàn
    if (distance > 120) {
        revealResult();
    }
}

function onPointerUp(e) {
    if (!isDragging) return;
    isDragging = false;
    diceLid.style.cursor = "grab";
    
    const distance = Math.sqrt(currentX * currentX + currentY * currentY);
    
    // Nếu nhấp chuột (click) hoặc tap nhẹ (distance rất nhỏ), mở bát luôn
    if (distance < 5) {
        revealResult();
        return;
    }
    
    // Nếu chưa kéo đủ xa, tự động trượt bát úp lại vào tâm
    if (!lidHasBeenOpened) {
        diceLid.style.transition = "transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275)";
        currentX = 0;
        currentY = 0;
        diceLid.style.transform = "translate(0px, 0px)";
        dragHint.style.opacity = "1";
    }
}

function revealResult() {
    if (lidHasBeenOpened) return;
    lidHasBeenOpened = true;
    isDragging = false;
    
    // Đẩy bát trượt hẳn ra ngoài
    diceLid.style.transition = "all 0.5s cubic-bezier(0.25, 1, 0.5, 1)";
    const angle = Math.atan2(currentY, currentX);
    
    // Nếu click hoặc nhấc chuột quá gần tâm, tự động đẩy lên phía trên
    const forceX = Math.abs(currentX) < 5 && Math.abs(currentY) < 5 ? 0 : Math.cos(angle) * 350;
    const forceY = Math.abs(currentX) < 5 && Math.abs(currentY) < 5 ? -350 : Math.sin(angle) * 350;
    
    diceLid.style.transform = `translate(${forceX}px, ${forceY}px)`;
    diceLid.style.opacity = "0";
    diceLid.style.pointerEvents = "none";
    dragHint.style.opacity = "0";

    // Hiển thị kết quả & xử lý tiền cược
    if (pendingResult) {
        const result = pendingResult;
        pendingResult = null;

        // Hiển thị kết quả đè lên đĩa
        resultBubble.innerText = `${result.result} (${result.total}đ)`;
        resultBubble.className = "result-bubble show";

        // Cập nhật ví tiền
        userMoney = result.money;
        updateUI();

        // Ghi vào cầu thống kê và lịch sử cược
        addHistoryBead(result.result, result.total);
        addHistoryLog(result.win, selectedChoice, betAmountTemp, result.result, result.total);

        // Hiển thị thông báo Thắng/Thua
        if (result.win) {
            showToast(`Chúc mừng! Bạn đã đoán đúng, nhận +${formatNumber(betAmountTemp)} VND`, "success");
        } else {
            if (result.result === "NỔ HŨ") {
                showToast(`Bộ ba đồng nhất! Bạn mất cược -${formatNumber(betAmountTemp)} VND`, "error");
            } else {
                showToast(`Sai rồi! Kết quả ra ${result.result}. Mất -${formatNumber(betAmountTemp)} VND`, "error");
            }
        }

        // Đặt lại trạng thái trò chơi cho ván tiếp theo
        isRolling = false;
        btnSelectTai.style.pointerEvents = "auto";
        btnSelectXiu.style.pointerEvents = "auto";
        updatePlayButtonState();
    }
}

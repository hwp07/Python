import logging

logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
    encoding="utf-8"
)
logger = logging.getLogger(__name__)

def get_discount_rate(tier: str, quantity: int) -> float:
    """Trả về tỷ lệ chiết khấu dựa trên hạng thành viên và số lượng"""
    logger.debug(f"Đang tính toán chiết khấu cho hạng {tier} với số lượng {quantity}")
    if quantity <= 0:
        logger.error("Số lượng sản phẩm phải lớn hơn 0")
        raise ValueError("Số lượng sản phẩm phải lớn hơn 0")

    # Xác định tỷ lệ chiết khấu cơ bản
    if tier == "silver":
        rate = 0.05
    elif tier == "gold":
        rate = 0.10
    elif tier == "diamond":
        rate = 0.15
    else:
        logger.error("Hạng thành viên không hợp lệ: %s", tier)
        raise ValueError(f"Hạng thành viên không hợp lệ: {tier}")

    # Thưởng thêm nếu mua số lượng lớn (từ 50 sản phẩm trở lên)
    if quantity >= 50:
        rate += 0.05
        logger.debug("Áp dụng chiết khấu biên cho số lượng lớn: tổng rate=%s", rate)
    return rate

def calculate_agency_total(price: float, quantity: int, tier: str) -> float:
    """Tính tổng tiền sau chiết khấu cho đại lý"""
    if price < 0:
        raise ValueError("Đơn giá không được âm")

    rate = get_discount_rate(tier, quantity)

    final_price = price * (1 - rate) * quantity

    logger.info(f"Kết quả: Tổng tiền = {final_price}")
    return final_price

# Khúc code chạy thử của Intern (Sinh viên dùng IDE Debugger để quét qua các dòng này)
if __name__ == "__main__":
    calculate_agency_total(100, 50, "gold")  # Case kiểm tra lỗi logic biên
    calculate_agency_total(100, -5, "silver") # Case kiểm tra lỗi dữ liệu đầu vào

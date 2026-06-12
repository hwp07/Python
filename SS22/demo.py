import logging

logging.basicConfig(
    filename="main.log",
    level= logging.DEBUG,
    format= "%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)

logger.info("Chuong trinh da chay thanh cong")

def handle_calc_sum (number_01: int, number_02: int) -> float:
    logger.debug(f"Ham tinh tong se chay voi doi so dau tien la {number_01} va doi so thu hai la {number_02}")
    
    try:
        result = number_01 / number_02
    except ZeroDivisionError:
        logger.error("Khong the chia cho 0")

    logger.info("Ham chia chay thanh cong")
    return result

handle_calc_sum(1, 0)
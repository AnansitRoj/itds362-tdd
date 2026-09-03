# test_kitchen.py

# รายการทดสอบ (test list)
# [x] 200 g × 3 = 600 g
# [x] การคูณต้องไม่เปลี่ยนค่าของอ็อบเจ็กต์เดิม
# [ ] ปริมาณสองค่าที่มีทั้งตัวเลขและหน่วยเท่ากันถือว่าเท่ากัน
# [ ] 1 oz ไม่เท่ากับ 1 g
# [ ] 200 g + 300 g = 500 g
# [ ] 200 g + 1 oz แปลงผลลัพธ์เป็นกรัมโดยใช้อัตราแปลงหน่วย
# [ ] (200 g + 1 oz) × 2

from kitchen import Quantity

def test_multiplication():
    flour = Quantity(200, "g")
    assert flour.times(3) == Quantity(600, "g")


def test_multiplication_by_two():
    flour = Quantity(200, "g")
    assert flour.times(2) == Quantity(400, "g")


def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200, "g")
    assert flour.times(3) == Quantity(600, "g")
    assert flour.times(2) == Quantity(400, "g")


def test_equality():
    assert Quantity(200, "g") == Quantity(200, "g")
    assert Quantity(200, "g") != Quantity(300, "g")


def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")
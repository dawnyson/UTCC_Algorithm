# Algorithm
Algorithm UTCC Class

![image](https://github.com/dawnyson/Algorithm/assets/127817052/36e4068c-c189-4495-bf21-d9c99f698ece)


Algorithm ตรวจจับ [, {, ( เมื่อมีเครื่องหมายเปิด จะนำเข้าใน Stack ถ้าตรวจจับ ], }, ) จะเช็คก่อนว่ามีข้อมูลใน Stack ก่อนหรือไม่<br>
ถ้าไม่ให้ทำการเขียน error location นี้ ถ้ามีให้ทำการตรวจเช็ค ว่าตรงกับคู่ของมันหรือไม่ ถ้าไม่อีกให้ทำการเขียน error เช่นเดิม<br>

ในการทดสอบแรก<br>
    def test_no_error(self):<br>
        test_string = '[{(Hello)}]'<br>
        isError, location = bracket_check(test_string)<br>
        self.assertEqual(isError, False)<br>
ค่านี้ไม่มี error ถูกต้องแล้ว เพราะการจับคู่ถูกต้อง<br>

การทดสอบที่สอง
    def test_error_1(self):
        test_string = '[{(Hello})]'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
ค่านี้มี error จากการสลับตำแหน่งของ {( }) ซึ่งเราสามารถตรวจวัดการการไม่เข้าคู่ของ ( และ } และ

การทดสอบที่สาม 
    def test_error_2(self):
        test_string = '[{(Hello'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
ค่านี้มี error เนื่องจากไม่มีวงเล็บปิด เรามี function เช็คครั้งสุดท้าย if not stack.isEmpty(): ตรวจว่ายังมีข้อมูลใน stack อีกไหม ปรากฏว่ายังมีอยู่เลยได้รับ error ไป

การทดสอบที่ 4 
    def test_error_3(self):
        test_string = 'Hello)('
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
ค่านี้มี error จากการตรวจเจอเครื่องหมายปิดเลย แต่เรามีการเขียนเช็ค if not stack.isEmpty(): ว่า มีข้อมูลใน stack อยู่ก่อนหรือป่าว

การทดสอบที่ 5 
    def test_error_4(self):
        test_string = '{}{'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)
        self.assertEqual([2], location)

ค่านี้ error เป็นถูกจากการเปิดวงเล็บไว้อย่างเดียวและ location คือตำแหน่งที่ 2 ( นับ 0 1 2 ) โดยจากตรวจเช็คขั้นสุดท้าย
ยังคงมีข้อมูลใน stack เหลืออยู่แต่ไม่มีการปิดเครื่องหมายเพื่อ pop ออก ทำให้เกิด error
ทำการแก้ไขโดยการจัดเก็บ index ไปยัง stack ด้วย ถ้าไม่เจอตัวปิดอีกจะฟ้องตำแหน่งที่ทำการเก็บ stack แทน และป้องกันเมื่อมี text เพิ่มเติมหลังจากวงเล็บเปิดที่ไม่มีวงเล็บปิด
ทำให้ algorithm ถูกต้องมากยิ่งขึ้น

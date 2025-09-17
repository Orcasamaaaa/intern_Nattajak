## Technical test for internship program 2024


<p align="left">
  <img src="cat_result.gif" width="640"/>
</p>


### ขั้นตอนการติดตั้ง
1. ดาวน์โหลดที่เก็บนี้มาบนเครื่อง
   ```bash
   git clone <repository-url>
   cd internship-2024-main
   ```
2. สร้าง virtual environment (แนะนำให้ใช้เพื่อแยกสภาพแวดล้อม)
   ```bash
   python -m venv venv
   ```
3. เปิดใช้งาน virtual environment
   - Windows PowerShell:
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. อัปเกรด pip ให้เป็นเวอร์ชันล่าสุด
   ```bash
   python -m pip install --upgrade pip
   ```
5. ติดตั้งไลบรารีที่จำเป็นสำหรับโปรเจกต์
   ```bash
   pip install -r requirements.txt
   ```

### วิธีรันเดโม
```bash
python yolo_detector.py
```
คำสั่งนี้จะเปิดหน้าต่าง OpenCV ที่แสดงวิดีโอพร้อมกรอบตรวจจับและเส้นทางการเคลื่อนที่ของแมว



# Setup your machine 

> การใช้งานโปรแกรมทางด้านการพัฒนาโปรแกรมส่วนใหญ่จะมีการเข้าถึงสิทธิ์ในการแก้ไขไฟล์บนเครื่องระดับ Admin หรือ Root ดังนั้นควรใช้เครื่องที่เป็นของตัวเอง หรือได้รับอนุญาตจากผู้ดูแลระบบให้ใช้งานได้ตามปกติ   


ให้ทำตามครบทุกขั้นตอนเพื่อให้แน่ใจว่า ระบบและซอฟต์แวร์สามารถทำงานได้อย่างไม่มีปัญหา **และควรทำล่วงหน้าก่อนวันอบรมสักอย่างน้อย 4-5 วัน เพราะถ้าพบว่าเครื่องของตัวเองถูก block หรือจำกัดสิทธิ์ จะได้ทำเรื่องกับฝ่าย Security หรือ Admin เพื่อดำเนินการให้สามารถติดตั้งและใช้งานได้ตามปกติ**

## ⚠️ ข้อควรระวัง เรื่องการใช้เครื่องคอมขององค์กร มาใช้ในการอบรม

- **แนะนำว่าสำหรับองค์กรที่มีการ block การทำงานผ่านอินเตอร์เน็ต เช่นการ block port หรือ certificate ให้เตรียม Account สำหรับเชื่อมต่ออินเตอร์เน็ตวงนอกให้ผู้เข้าอบรมได้เลย**
- การอบรมจะมีการรันคำสั่งผ่าน โปรแกรม Command Prompt หรือ Terminal และมีโปรเซสที่ทำการสร้างและแก้ไขไฟล์ที่อยู่บนระบบปฏิบัติการ (เช่น NodeJS process) ให้แน่ใจว่าระบบปฏิบัติการไม่ได้มีการบล๊อคการทำงาน และสามารถทำงานได้อย่างไม่มีปัญหา
- ระหว่างการอบรม จะมีการเชื่อมต่ออินเตอร์เน็ต และมีการดาวน์โหลดโค้ด รวมถึงติดตั้ง, setup, และ install โปรแกรมเพิ่มเติม **ควรให้แน่ใจว่าคอมพิวเตอร์ทีี่ใช้ไม่มีการปิดกั้นการทำงานดังกล่าว**
- หากผู้เข้าอบรมเลือกใช้วิธีการดาวน์โหลด NodeJS มาเป็นไฟล์ zip และติดตั้งด้วยตัวเอง ให้แน่ใจว่า:
     - ได้ทำการตั้งค่า PATH ให้กับ NodeJS ใน System Environment หรือ zsh ได้เรียบร้อย
     - สามารถสร้างโปรเจคโดยใช้คำสั่ง `npx create-react-app my-app` ใน Command prompt, Visual Studio Code หรือ Terminal ได้ออย่างไม่มีปัญหา

> ⚠️⚠️⚠️ หากทางผู้ดูแลระบบไม่ได้มีการอำนวยความสะดวกในการผ่อนปรนตามสถานการณ์ด้านบน ทางผู้เข้าอบรมอาจจะไม่สามารถใช้คอมพิวเตอร์นั้นเรียนรู้ หรือทำ workshop บางส่วนได้ จึงขอเรียนมาเพื่อทราบครับ

## 1. สำหรับ Computer

ทำการดาวน์โหลดตัวติดตั้ง และดำเนินการติดตั้งให้เรียบร้อย 

1. Git Client ([Download](http://git-scm.com/download/) | [คลิปแนะนำการติดตั้ง](https://www.youtube.com/watch?v=fPOoIZbDKmE))
   
2. Python 3 ([Download](https://www.python.org/downloads/) 
   - **ระหว่างการใช้งานต้องมีการติดตั้ง package เพิ่มเติม ซึ่งเป็นกลไกปกติสำหรับการพัฒนาโปรแกรม ควรทดสอบติดตั้ง Python package ในโปรเจค**
   - ทดสอบการเรียกใช้งาน ด้วยการรันคำสั่ง `python --version` ใน Terminal หรือ Command Prompt
   - ควรได้เลขเวอร์ชั่นของ Conda กลับมาประมาณตัวอย่างนี้ (เลขเวอร์ชั่นไม่จำเป็นต้องตรงเป้ะ): `Python 3.11.7`
  
3. Conda [Install instruction](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
   - ทดสอบการเรียกใช้งาน ด้วยการรันคำสั่ง `conda --version` หรือ `conda info` ใน Terminal หรือ Command Prompt
   - ควรได้เลขเวอร์ชั่นของ Conda กลับมาประมาณตัวอย่างนี้ (เลขเวอร์ชั่นไม่จำเป็นต้องตรงเป้ะ): `conda 24.4.0`
  
4. Docker [Install instruction](https://docs.docker.com/engine/install/)
   - หลังจากติดตั้งควรทดสอบด้วยการรันคำสั่งต่อไปนี้ใน Terminal หรือ Command Prompt **เพื่อให้แน่ใจว่าไม่มีการติด error **
     1. `docker --version`
     2. `docker-compose --version`
     3. `docker run hello-world`    
   
5. Visual Studio Code ([Download](https://code.visualstudio.com/))
   - เสร็จแล้วติดตั้งส่วนเสริม [Nextflow Python Extension Pack](https://marketplace.visualstudio.com/manage/publishers/teerasej/extensions/nextflow-python-pack/hub) 
   - **ให้แน่ใจว่าสามารถรันคำสั่งใน Terminal ของโปรแกรม visual studio code ได้อย่างไม่มีปัญหา**  เช่น ใช้คำสั่งในข้อ 2, 3, 4 ด้านบนมาทดสอบ ก็ได้ผลลัพธ์เช่นเดียวกัน กับการรันคำสั่งใน Terminal หรือ Command Prompt ปกติ

6. Web Browser ที่ควรมี
   1. Google Chrome ([Download](https://www.google.com/chrome/))
   2. Microsoft Edge ([Download](https://www.microsoft.com/en-us/edge/download))
   
7. แล้วก็ติดตั้ง Extension บน Web Browser ตามรายการต่อไปนี้ 
   1. [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools)
   2. [Redux Dev Tools](https://chrome.google.com/webstore/detail/redux-devtools)
  
## 2. สมัคร Account ที่ควรมี

- [Github](https://github.com/signup)
- [Sentry](https://sentry.io/signup/)



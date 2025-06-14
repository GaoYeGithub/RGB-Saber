---
title: "RGB Saber"
author: "Ye Gao"
description: "I wanna build thoose collapsing sword 3d print with like a string of neo pixels and some kind of pcb in the hilt to power it"
created_at: "2024-04-04"
---

# June 4th: Develop the basic software

Today I focused on making the software for the RGB Saber lighting. I wrote a simulation in wokwi using mircopython that where 16 NeoPixels change color based on motion like the acceleration and rotation data and translates those movements into  color and brightness. Now I just need to create the CAD model

<video width="320" height="240" controls>
  <source src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/d15d8fdf623ed5de376db096c4af2843837e347e_04.06.2025_20.14.30_rec.mp4" type="video/mp4">
</video>
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/d15d8fdf623ed5de376db096c4af2843837e347e_04.06.2025_20.14.30_rec.mp4)
https://hc-cdn.hel1.your-objectstorage.com/s/v3/d15d8fdf623ed5de376db096c4af2843837e347e_04.06.2025_20.14.30_rec.mp4

*Journal Update for highway call*

**Total time spent: 2.5h**

# June 5th: Cadded the sword

Okay so today I opened onshape and began modeling the collapsible blade sections. The walls currently are only 1 mm thick and 1.25 mm apart which hopfully is thin enough for the light to go thur but doesn't break, I need some testing to be sure tho.


![image](https://github.com/user-attachments/assets/0710ef8c-9ed3-4501-a421-e8ea59efd3dc)
![image](https://github.com/user-attachments/assets/16506541-2ae5-4e78-8afc-d9653da75c11)

**Total time spent: 1.5h**

# June 5th: Created the pcb 

Now finally the important part the electronics, I made the schematic and PCB so that it fits inside the hilt handle. The components being the thing with Adafruit powerboost 500C to provide stable 5 v to the Xiao seeed rp 2040 which is compact and enough pins for my desgin, and mpu6050 that will provide the gyroscope data for the motion.

Additionally I had to do some research on the wiring and learn some things I didn't know before like the need for decoupling capitours to prevent voltage droop, and the need for ground pour to reduce EMI

![image](https://github.com/user-attachments/assets/df379e36-34fb-46e1-84bb-c185920195a8)
![image](https://github.com/user-attachments/assets/a234ba00-4213-4664-8802-bef6b64c76b6)

**Total time spent: 4h**


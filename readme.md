# FPS Shooter Aim Assist

This project aims to provide an YOLO-backed aim assist system for FPS (First-Person Shooter) games, designed solely for educational purposes. The objective is to explore the application of computer vision and machine learning techniques in real-time game environments.

## Motivation

The motivation behind this project is to gain a deeper understanding of how computer vision can be implemented in FPS games. This project is intended to help players who struggle with aiming by demonstrating how technology can enhance their gameplay experience. It is important to note that this project is for educational purposes only and should not be used to gain unfair advantages in competitive games. We will focus on CS2.

## Features

- Real-time Object Detection using YOLOv8
- Automatic Targeting: Automatically moves the mouse to aim at detected opponents.
- Customizable Detection: Supports custom-trained models for specific games or scenarios.
- Efficient Performance: Optimized to run at high for faster response

## Project Pitfalls

### Raw Input Limitation in CS2

One significant obstacle encountered during this project is the limitation imposed by Valve in Counter-Strike 2 (CS2), where raw input for mouse movements has been disabled.

Disabling raw input in CS2 means that functions like `pyautogui.moveTo()` and similar libraries that simulate mouse movements will not work as intended. This is because these functions rely on raw input to position the mouse cursor accurately. As a result, this tool cannot move the cursor to aim the target.

### Workarounds

1. <strong>External Hardware Solutions</strong><br>
   Using external hardware devices such as programmable gaming mice or custom-built hardware interfaces that can simulate raw input might bypass the software limitations. However, this approach is complex and may still violate game terms of service.

2. <strong>Other Games and Applications</strong><br>
   While CS2 poses a challenge, the aim assist tool may still be functional and beneficial in other games or applications that do not have such raw input limitations. Testing and validating the tool in a variety of environments can provide more insights into its versatility and effectiveness.

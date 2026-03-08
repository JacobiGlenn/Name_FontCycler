# Font Cycle Animation Maker for GitHub READMEs

Create eye-catching animated headers for your GitHub profile that cycle through dozens of fonts with a cool scramble effect in between!

<h1 align="center" >
  <img src="NameFontCycle.gif" alt="Jacobi Glenn" width="550">
</h1>


## Features

- **30+ Fonts** – Cycles through a diverse mix of fonts (classic, techno, script, funny ones, and more!)
- **Scramble Transition** – 0.3 second glitch-style animation between each font
- **Perfect for GitHub** – Outputs a clean, transparent GIF that works anywhere
- **Fully Customizable** – Easy to modify fonts, colors, timing, and text

---

## How to make your own

### Prerequisites

- Python installed on your computer
- Pillow library (`pip install pillow`)

### Instructions

**1. Clone this repository**

```bash
git clone https://github.com/yourusername/font-cycle-animation.git
cd font-cycle-animation
```

**2. Customize the text**

Open `font_cycle.py` and find line 7:

```python
text = "Jacobi Glenn"          # put your name here        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```
^I tried making it very obvious

**3. (Optional) Add your own fonts**

Add more fonts to the `font_paths` list. You can use:
- Downloaded `.ttf` files in the `fonts` folder
- Windows system fonts (e.g., `C:/Windows/Fonts/arial.ttf`)
- Mac system fonts (e.g., `/System/Library/Fonts/Helvetica.ttc`)

**4. Open PowerShell/Terminal**

Press `Win + X` and select "Windows Terminal" or "PowerShell", then navigate to your project folder:

```powershell
cd onedrive
cd documents
cd git
cd name_fontcycler
```

**5. Run the script**

```powershell
python font_cycle.py
```

**6. Find your GIF!**

The script will generate `NameFontCycle.gif` in the main folder (Yes that EXACT name, it doesn't replace it with your name). Add it to your GitHub profile repo and embed it in your README!

**7? Embed in your README**

I embedded it into my readme for my git profile by making an assets folder and then calling the path. Heres what I put
```
<h1 align="center">
  <img src="Assets/NameFontCycle.gif" alt="Jacob Glenn" width="550">
</h1>
```

---

## Customization Options

In the script, you can easily tweak:

```python
text = "your name here"        # Your text
font_size = 70                 # Size of text
frame_duration = 1500          # Milliseconds per font (1.5 sec)
scramble_duration = 0.3        # Seconds of scramble between fonts
text_color = (255, 255, 255)   # White text
bg_color = (0, 0, 0, 0)        # Transparent background
```

---

## Font List

The script includes 33 fonts across 6 categories, feel free to delete or add to your liking:

| Category | Fonts |
|---|---|
| **Classic/Professional** | Arial, Calibri, Verdana, Tahoma, Trebuchet MS, Times New Roman, Georgia, Carlito, Outfit, Basic |
| **Classy** | STIXTwoText, CrimsonText, Georgia, Times New Roman |
| **Typewriter** | Courier New, Consolas, ShareTechMono |
| **Techno/Futuristic** | Audiowide, Quantico, Rajdhani |
| **Fun** | Comic Sans, Bangers, PressStart2P, Unifont, Cooper Black, Algerian, Broadway |
| **Script/Display** | Lobster, Pacifico, BebasNeue, Righteous, KronaOne, Limelight |

---

## Embed in Your README (In case you missed from above)

Once your GIF is in your profile repository, add this to your `README.md`
MAKE SURE YOU PUT THE GIF **INSIDE** THE README (I forgot to do this at first lol)

```html
<h1 align="center">
  <img src="your-gif-name.gif" alt="Your Name" width="800">
</h1>
```

---

## 🙏 Credits


**Fonts**
- [Google Fonts](https://fonts.google.com) – For their incredible open-source font library
- [Microsoft](https://learn.microsoft.com/en-us/typography/fonts/windows_11_font_list) – For Windows system fonts
- [STIX Project](https://www.stixfonts.org/) – For STIX Two Text font
- [Various open-source font creators and foundries](https://fonts.google.com/attribution)

**Animation**
- Scramble effect – Custom Python implementation using [Pillow](https://python-pillow.org)
- Inspiration – [typing-svg generator](https://readme-typing-svg.demolab.com)

---

## This project is open source. Feel free to fork, modify, and use it for your own profile!

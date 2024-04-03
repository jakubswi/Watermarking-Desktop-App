from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk


def browse_files():
    global image, width, height
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=[("Image File", '.jpg .png .jpeg')])
    label_file_explorer.configure(text="File Opened: " + filename)
    image = Image.open(filename)
    image = image.copy()
    width, height = image.size


def browse_for_watermark():
    global watermark_width, watermark_height, watermark_image
    filename_watermark = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                    filetypes=[("Image File", '.jpg .png .jpeg')])
    label_file_explorer_watermark.configure(text="File Opened: " + filename_watermark)
    watermark_image = Image.open(filename_watermark)
    watermark_width, watermark_height = watermark_image.size


def location():
    global position_final
    watermark_width_1 = watermark_width * (float(slider_size.get()) / 100)
    watermark_height_1 = watermark_height * (float(slider_size.get()) / 100)
    watermark_position = position.get()
    if watermark_position == "left up":
        position_final = (0, 0)
    elif watermark_position == "middle up":
        position_final = (width / 2 - watermark_width_1 / 2, height - 0)
    elif watermark_position == "right up":
        position_final = (width - watermark_width_1, 0)
    elif watermark_position == "left middle":
        position_final = (0, height / 2)
    elif watermark_position == "middle middle":
        position_final = (width / 2 - watermark_width_1 / 2, height / 2)
    elif watermark_position == "right middle":
        position_final = (width - watermark_width_1, height / 2)
    elif watermark_position == "left down":
        position_final = (0, height - watermark_height_1)
    elif watermark_position == "middle down":
        position_final = (width / 2 - watermark_width_1 / 2, height - watermark_height_1)
    elif watermark_position == "right down":
        position_final = (width - watermark_width_1, height - watermark_height_1)
    return (int(position_final[0]), int(position_final[1]))


def add_image_watermark():
    position_final = location()
    print(position_final)
    size = (
        int(watermark_width * (float(slider_size.get()) / 100)),
        int(watermark_height * (float(slider_size.get()) / 100)))
    watermark_image.thumbnail(size)
    watermark_image.putalpha(int(255 * (float(slider_alpha.get()) / 100.0)))
    image.paste(watermark_image, position_final)
    image.save("watermarked_image.png")


window = Tk()
python_image1 = Image.open("stop.png")
python_image = python_image1.resize((20, 20))
location_image = ImageTk.PhotoImage(python_image)
position = StringVar()
type_of_watermark = StringVar()
window.title("Watermarking App")
window.geometry("600x400")
window.config(padx=50, pady=50, bg="white")
label_file_explorer = Label(window, text="File Explorer", fg="black")
button_explore = Button(window, text="Browse Files for image", command=browse_files)
label_file_explorer.grid(row=0, column=0, columnspan=3)
button_explore.grid(row=0, column=3)
label_file_explorer_watermark = Label(window, text="Watermark file", fg="black")
button_explore_watermark = Button(window, text="Browse Files for watermark", command=browse_for_watermark)
label_file_explorer_watermark.grid(row=1, column=0, columnspan=3)
button_explore_watermark.grid(row=1, column=3)
position_radio1_1 = Radiobutton(window, image=location_image, variable=position, value="left up")
position_radio1_1.grid(row=3, column=0)
position_radio2_1 = Radiobutton(window, image=location_image, variable=position, value="middle up")
position_radio2_1.grid(row=3, column=1)
position_radio3_1 = Radiobutton(window, image=location_image, variable=position, value="right up")
position_radio3_1.grid(row=3, column=2)
position_radio1_2 = Radiobutton(window, image=location_image, variable=position, value="left middle")
position_radio1_2.grid(row=4, column=0)
position_radio2_2 = Radiobutton(window, image=location_image, variable=position, value="middle middle")
position_radio2_2.grid(row=4, column=1)
position_radio3_2 = Radiobutton(window, image=location_image, variable=position, value="right middle")
position_radio3_2.grid(row=4, column=2)
position_radio1_3 = Radiobutton(window, image=location_image, variable=position, value="left down")
position_radio1_3.grid(row=5, column=0)
position_radio2_3 = Radiobutton(window, image=location_image, variable=position, value="middle down")
position_radio2_3.grid(row=5, column=1)
position_radio3_3 = Radiobutton(window, image=location_image, variable=position, value="right down")
position_radio3_3.grid(row=5, column=2)
label_slider_alpha = Label(window, text="Transparency slider", fg="black")
label_slider_alpha.grid(row=6, column=0, columnspan=3)
slider_alpha = Scale(window, from_=0, to=100, orient='horizontal')
slider_alpha.grid(row=7, column=0, columnspan=3)
label_slider_size = Label(window, text="Size slider", fg="black")
label_slider_size.grid(row=6, column=3, columnspan=2)
slider_size = Scale(window, from_=0, to=200, orient='horizontal')
slider_size.grid(row=7, column=3, columnspan=2)
render_button = Button(window, text="Render image", command=add_image_watermark)
render_button.grid(row=8, column=0)

window.mainloop()

import cv2
from tkinter.ttk import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
from PIL import Image, ImageTk

def button_clicked():
    file_path = askopenfilename(title="Select an image file")
    if file_path:
        image = cv2.imread(file_path)
        if image is not None:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray_image_path = file_path.rsplit('.', 1)[0] + '_gray.png'
            cv2.imwrite(gray_image_path, gray_image)
            messagebox.showinfo(title="Success!", message=f"Grayscale image saved at: {gray_image_path}")
            os.startfile(os.path.dirname(file_path))
        else:
            messagebox.showinfo(title="Error", message="Failed to load the image.")
    else:
        messagebox.showinfo(title="Error", message="No file selected.")

def camera_opener():
    cam = cv2.VideoCapture(0)
    result, frame = cam.read()
    messagebox.showinfo(title="Info", message="Press 'q' to capture your pic")
    while True:
        result, frame = cam.read()
        if result:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Failed to capture image")
            break
    cam.release()
    cv2.destroyAllWindows()
    if frame is not None:
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(os.path.join(os.getcwd(), f"output_gray.png"), gray_image)
        folder_path = os.getcwd()
        os.startfile(folder_path)
    else:
        messagebox.showinfo(title="Error", message="Failed to load the image.")

root = Tk(screenName="Gray Scale Image Converter")
root.title("Grayman")
root.minsize(width=1050, height=500)
root.configure(bg='#ACC7B4')

w = Label(root, text="Gray Scale Image Converter", font=("Century Gothic", 28))
w.config(bg="#ACC7B4", fg="#331B3F")
w.grid(row=0, column=0, columnspan=3, padx=20, pady=30, sticky="nsew")

photo = PhotoImage(file=r"C:\Users\Kishan\OneDrive\Desktop\Prospace_Project\image.png" )
button_photo = photo  # Keep a reference to the PhotoImage object

button = Button(root, command=button_clicked, text="Click me!", image=button_photo, bg="#ACC7B4" , height=15)
button.grid(row=1, column=1, pady=10, sticky="nsew")

photo2 = PhotoImage(file=r"C:\Users\Kishan\OneDrive\Desktop\Prospace_Project\image2.png")
button_photo2 = photo2  # Keep a reference to the PhotoImage object

button2 = Button(root, command=camera_opener, text="Click me!", image=button_photo2, bg="#ACC7B4" , height= 15)
button2.grid(row=2, column=1, pady=10, sticky="nsew")

image_paths = [
    r"C:\Users\Kishan\OneDrive\Desktop\Prospace_Project\colorful.jpg",
    r"C:\Users\Kishan\OneDrive\Desktop\Prospace_Project\arrow.jpg",
    r"C:\Users\Kishan\OneDrive\Desktop\Prospace_Project\bandw.png"
]

labels = []
for i, path in enumerate(image_paths):
    image = Image.open(path)
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo, bg="#ACC7B4")
    label.image = photo  # Keep a reference to avoid garbage collection
    label.grid(row=3, column=i, padx=20, pady=10, sticky="nsew")
    labels.append(label)  # Keep references to avoid garbage collection

# Configure grid weights for responsiveness
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

root.mainloop()

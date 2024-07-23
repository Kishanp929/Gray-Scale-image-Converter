# Gray-Scale-image-Converter

<h1> You can Download the exe file from <a href="https://drive.google.com/file/d/1alJUk85YjM7bs0QpO_iMxiXXN1wHgunI/view?usp=sharing" >HERE</a></h1>

<h3> The .exe file converts the Colorful image to Black and white image. </h3>

<h3> The code uses the camera on port 0 , so it may be possible that you are using an external camera device , if this happens then just download the project zip file open the <code>main.py</code>
and change the 0 in <code>cv2.VideoCapture(0)</code> to whatever port your camera is connected. Then use command prompt install pyinstaller using <code>pip install pyinstaller</code> then in the project directory use the command <code> pyinstaller --onefile --noconsole main.py</code> this will generate a .exe file in the <code>dist</code> folder </h3>

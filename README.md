
 Image Filters Web Application

This project is an interactive Image Filter Application built using Streamlit and OpenCV (cv2). It allows users to upload an image and apply various image processing filters like black & white, pencil sketch, HDR, brightness adjustment, and artistic stylization — all in real-time through a web interface.  

 Features

* Upload `.png`, `.jpg`, or `.jpeg` images.
* Apply a range of filters:

  *  Black & White
  *  Pencil Sketch
  *  HDR (High Dynamic Range)
  *  Brightness Adjustment
  *  Stylized Effect
* Adjustable filter parameters using sliders.
* Live preview of original and filtered images side by side.



 Technologies Used

Python
* Streamlit – for building the web interface
* OpenCV – for applying image filters and transformations
* NumPy – for handling image arrays
* Pillow (PIL) – for image I/O

 Installation & Setup

 1. Clone the Repository

bash
git clone https://github.com/yourusername/image-filters-app.git
cd image-filters-app


 2. Create a Virtual Environment (Optional)

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

 3. Install Dependencies

bash
pip install -r requirements.txt


Sample `requirements.txt`:

txt
streamlit
opencv-python
numpy
pillow


 4. Run the App
bash
streamlit run Filters_APP.py








 Project Structure


image-filters-app/
│
├── Filters_APP.py           Main Streamlit application
├── requirements.txt          Dependencies
├── README.md                This file
└── sample_images/           (Optional) Add sample test images here













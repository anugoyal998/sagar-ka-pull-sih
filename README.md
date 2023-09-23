## PROJECT REPORT
1. **Introduction** - The scope of existing CCTV technology is narrow due to the absence of advanced algorithms. The widespread deployment of CCTV cameras offers an opportunity to automate crowd management, identify potential criminal activities, and enhance disaster management techniques through the application of AI/ML techniques. This project seeks to address these challenges by developing a comprehensive solution.

2. **Problem Statement** - This project aims to tackle the problems of:
    - Implementing crowd counting mechanisms for public safety.
    - Detecting firearms, fire, and smoke.
    - Identifying acts of assault.
    - Garbage detection on railway tracks.
    - Notifying authorities in the event of disruptions.

3. **Technology Stack** - The project leverages the following technology stack:
    - Front End
        - HTML5
        - CSS
        - JavaScript
        - React.js
        - TypeScript
        - Bootstrap
        - TailwindCSS
    - Backend
        - Python
        - FastAPI
    - AI/CV/DL Framework - Tensorflow,Pytorch, Opencv, Sklearn, Numpy, Pandas, Seaborn, Matplotlib
    - Devops - Docker, Microsoft Azure, Heroku, AWS Lambda, SageMaker

4. **Methodology** -

    1.  **Data Collection and Management** - The primary step is accessing the datasources available including cctv footages and other relevant data. A database management system capable of handling large datasets is then deviced.

    2. **Technology Evaluation** - The next step is to train the models for fire and smoke detection, weapon detection, crowd counting and garbage detection on given datasets using Yolov8 and RCNN algorithms.

    3.  **Infrastructure Planning** - A robust backend infrastructure was designed and developed using Python and FastAPI to process data, trigger alerts, and manage user requests.

    4. **Testing and Validation** - Rigorous testing was conducted to ensure system accuracy and reliability, including real-world scenarios.

    5. **Regulatory Compliance** - The system was designed to comply with relevant regulatory and compliance standards to ensure responsible usage and privacy protection by avoiding identity collection using face blurring and mosaic effect algorithms.

5. **Results** - 
    - The web application provided real-time monitoring capabilities for crowd management, crime prevention, and work monitoring.
    - RCNN and YOLO algorithms successfully detected guns, fire, smoke, acts of assault, garbage and gave a crowd count.
    - Authorities received immediate alerts, ensuring swift response to disruptions.

6. **Discussion** - 
    - The chosen technology stack facilitated the development of a user-friendly and responsive web application.
    - The integration of RCNN and YOLO algorithms significantly improved the accuracy of object detection.
    - Regulatory compliance was maintained to ensure ethical and legal use of the system.

7. **Conclusion** - This project successfully demonstrated the capability of utilizing existing CCTV networks in enhancing public safety and work monitoring. 
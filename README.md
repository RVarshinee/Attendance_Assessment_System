# Attendance_Assessment_System
Face Recognition based Attendance Assessment System to ensure proper identity of student and staff

Steps to run the project:
1. Install the following python modules:
     tkinter, 
     numpy, 
     opencv, 
     pandas, 
     arrow,
     matplotlib
    
2. Copy the code from Face_Recognition.py and paste it in your Python IDE

3. Download the background image (i.e, the file named as face1.jpg) that is provided in the repository and in Face_Recognition.py in line number 28 update the absolute    path of the downloaded image.

4. Download the Students image (i.e, the file named as student.jpeg) that is provided in the repository and in Face_Recognition.py in line number 48 update the            absolute path of the downloaded image.

5. Download the Staff image (i.e, the file named as teacher.jpg) that is provided in the repository and in Face_Recognition.py in line number 357 update the absolute      path of the downloaded image.

6. Download the haarcascade_frontalface_default.xml file and make sure to download it in the directory in which python is present

7. Create a folder named Staff and within the folder create the subfolders Attendance , StaffDetails , TrainingImageLabel , TrainingImages on your computer and in        Face_Recognition.py in line number 464 and 508 update the absolute path of the TrainingImages folder. Create a folder named Students and and within the folder          create the subfolders Attendance , StaffDetails , TrainingImageLabel , TrainingImages on your computer and in Face_Recognition.py in line number 155 and 200 update    the absolute path of the TrainingImages folder.

8. In StaffDetails folder create an excel file and save it as staffDetails.csv and in StudentDetails folder create an excel file and save it as studentDetails.csv and    in both the csv files name the cell in first row and first column as 'Id' and name the cell in first row and second column as 'Name'. In staffDetails.csv name the      cell in first row and third column as 'Designation'. In studentDetails.csv name the cell in the first row and third column as 'Subject'  

9. In Face_Recognition.py in line number 166 and line number 244 update the absolute path of studentDetails.csv and in line number 475 and line number 554 update the      absolute path of staffDetails.csv

10. In Staff folder in TrainingImageLabel folder create a .yml file and name it as Trainer.yml (Simply create a notepad file and save it with the extension .yml) and       In Face_Recognition.py in line number 202 and 240 update the absolute path of Trainer.yml and similarly in Students folder in TrainingImageLabel folder create a       .yml file and name it as Trainer.yml and in Face_Recognition.py in line number 510 and 550 update the absolute path of Trainer.yml

11. In Face_Recognition.py in line number 279 update the absolute path of Attendance folder present in Students folder and in line number 589 update the absolute path     of Attendance folder present in the Staff folder




















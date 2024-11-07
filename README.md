![image](https://github.com/user-attachments/assets/ac9e321f-6ab5-41d4-9585-8dcc729461ab)Create a note book instance.![image](https://github.com/user-attachments/assets/fab35fe4-ca71-4d30-8af9-6de423f40566)
Ensure the IAM role assigned during notebook creation as necesarry permissions for performing processing jobs. ![image](https://github.com/user-attachments/assets/3be49ae5-3fe7-4dfb-8d77-1b9f841a5cbc)
You can create a new poilcy - customer inline. ![image](https://github.com/user-attachments/assets/ef84008e-8129-46a0-ad17-5321dc7d0c75)
![image](https://github.com/user-attachments/assets/2fcb2123-9c70-4583-bbd0-fbd9be47b30b)
Create a bucker to store input and output data. Creating separate folders for input and output data is suggested.![image](https://github.com/user-attachments/assets/5f919849-35a2-45a9-a333-2a52fb38432e)
![image](https://github.com/user-attachments/assets/2543a1e3-1d21-4e26-82da-425cd7c1812c)
Create a ECR private registory(or public based on your requirement) to store the image. ![image](https://github.com/user-attachments/assets/d46b384f-d1c7-4e64-bf00-49d9c6668e06)
Using the terminal in the notebook instance. Bulid the docker image. login to ecr, tag and push the image.
you can use following commands for reference:
First you need to compile the c++ code to and store the file in the same directory
>g++ main.cpp -o a.out
Now build docker image:
>docker build -t cpp_processing_1 .
Now login to ecr:
>aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 665764469544.dkr.ecr.eu-north-1.amazonaws.com
Now tag the image:
>docker tag cpp_processing_1:latest 665764469544.dkr.ecr.eu-north-1.amazonaws.com/cpp_processing_1:latest
Now push  the image:
> docker push 665764469544.dkr.ecr.eu-north-1.amazonaws.com/cpp_processing_1:latest

Now excete the file that contains code to execute a processing job.
sample out: this code prints input and output and notifies when processing job is initiated.
![image](https://github.com/user-attachments/assets/4f0047b8-6161-4eb0-8855-7b91960a6a08)

You can look under processing section
![image](https://github.com/user-attachments/assets/cf729842-3e21-4cd7-b011-4b76eb3ac46b)

# FaceSafe
A program that uses face recognition to decrypt a file.

## Files
There are seven main files in this repository:
- setup_directories.py: used to create directories which are used to store model data and user files.
- data.py: gathers pictures of a person's face to then train the model (used as a library).
- trainer.py: trains the model based on the data.py's gathered images (used as a library).
- recognizer.py: used to recognize faces based on the trained model (used as a library).
- setup_new_user.py: uses data.py and trainer.py to create a new face model.
- main.py: the main file in the repository, uses the recognizer.py file to recognize faces, then opens the users encrypted file.
- Cascades/cascade.xml: the file used to define what a face is.

## Usage
1. Unzip the repository.
2. Run the "setup_directories.py" file to create the needed folders.
3. Run the "setup_new_user.py" file. The following will happen:
   - The program will ask you for a "User ID". This is just a number to identify a user.
   - The program will take 30 pictures of your face.
   - The program will take the pictures of your face and train a model using those pictures.
   - The program will create two files. One called "UserID.bin" and the other called "UserId.key. One is your encrypted file and the other is the encryption key.
4. Run the main.py file. The following will happen:
   - A window will pop up showing the camera view and looking for any faces that it recognizes from the trained model.
   - Once the program finds a familiar face, it will assosciate it with a UserID and decrypt the user's file. Another window will pop up showing the contents of the file.
   - You can edit the contents and click the "Save" button to save the file changes and the "Exit" button to quit.

**Note: You can have more than one face added in the program. To add a new user, just run the "setup_new_user.py" file again.**

## Video
## Credits
By Matteo Giovanni

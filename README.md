# Project-Nanite

### What is Nanite?

Nanite is a writing productivity app focused on helping you visualize progress towards writing goals. It does so by helping to visualize your history and progress of words written in a manuscript. 


### How is it used?

Nanite is a desktop application that acts independently from your word processor of choice. It reads in a file (or folder) containing the contents of your writing. From there, it scans your current wordcounts and adds a record for the given day. It saves these records to help visualize your progress.


### How Do I install it?

There isn’t technically an installation process, but rather just downloading directly and running it. 
First off, make sure you are on the current URL for where Nanite is hosted. Right now that is https://github.com/ericoulster/Project-Nanite. Chances are, you are viewing this readme on that particular web-page.
Next, navigate to the ‘releases’ section. It’s findable on the sidebar.

![Releases](/documentation_pictures/Releases.PNG)

Within the ‘releases’ sidebar on github, click on the tags button. There are 3 releases files: for Windows, OSX, and Linux Distributions. Choose the one which corresponds to your Operating system, then click the ‘Downloads’ button.
Choose the first option, which should be a .zip file, and choose a place on your local hard-drive to put the zipped file.

Within the zip file (which you can open with 7-zip or another decompression program), there should be the ‘binary’ file. This should be Nanite.exe (Windows/Linux) or Nanite.app (OS X). Double-clicking this will open the program.
If you’d like to have a browser icon, make sure to make a shortcut using your OS file explorer menu.
We have had experiences where anti-virus software has flagged Nanite with a false positive. If this concerns you, all code used in Nanite is easily and publicly viewable within the github repo, and you or someone you trust is welcome to look through the project files.

### How do I uninstall it?
There is no uninstallation process required for Nanite. You just need to delete the parent folder, and Nanite will be gone!


## App Tour
When we boot up Nanite, we begin our journey on the Welcome Screen. 

![Welcome Screen](/documentation_pictures/Welcome_Screen.PNG)

This screen serves no purpose other than to welcome you back to Nanite. It’s nice to be greeted!

Once you’re checked in (by clicking the button), you gain access to the ‘Home Screen’. On your first time booting up, this will be blank.

![Home Image](/documentation_pictures/Home_Screen.PNG)

While clicking the Home Button, Nanite Button, or Author Icon routes you back to the Welcome Screen, the other two buttons have special functions.
To get your first project started and tracked, click on the + icon.
A window will open up asking you what your writing goals are.

![Project Window Empty Image](/documentation_pictures/Word_Screen.PNG)

First off, name your project. Don’t worry if it’s just a working title- you can change it later!

Next, you select where your project is located.
Your ‘project’ is your writing documents. As in, the .txt, .rtf, or .docx file (or a collection of them) which are somewhere on your computer.
If your project is entirely contained within a single file, you can choose ‘select file’. If you work across multiple files (i.e., one document per chapter), then you can choose ‘select folder’, and choose the folder where all the files are housed.

![Project Window Full Image](/documentation_pictures/Add_Project.PNG)

Add in all of the details for your project. There are three types of word goals you can see- variable daily, where you can set different goals throughout the week (i.e. 500 words on Mondays and Wednesdays, 1000 on Tuesdays, Thursdays and Fridays, and 2000 on Saturdays and Sundays), or you can choose consistent daily (i.e. 800 words a day).

On top of all of that, you can also just set an overall target goal (i.e. write an 80000 word manuscript). Consistent daily goals are calculated based on the length of time between your start and end date, along with the world goal itself to make consistent daily goals.
After setting these parameters, hit project and your project will be created.
The home screen will now house a project.

![Home Screen With Project](/documentation_pictures/Home_Screen_Project.PNG)

You can edit the name and word goals of the project with the pencil icon. You can download a .csv file of your project records with the download icon (in case you wanted that data elsewhere). You can delete the project with the garbage can.

Each time you hit ‘refresh project’, your daily progress towards your wordcount goals will be updated. You may need to hit refresh projects initially for any words to show up at all. Nanite 'saves' your wordcounts each time you hit the refresh button, so you don't need to worry about closing the application so long as a refresh has already completed.
Project stats shows you a historical overview of the total number of words you have written.

![Historical Window Image](/documentation_pictures/Project_Screen.PNG)

Currently, there are only a couple of days worth of writing, but you will be able to see a wide range of dates- as well as see them summarized into totally weekly or monthly words by changing the ‘Daily’ tab to another setting.

If we were to exit out of our project window, there is one last window just to be aware of: the credit’s screen.

![Credit Window Image](/documentation_pictures/Credit_Screen.PNG)

This screen simply tells you the names of the hardworking people who created Nanite.

That is all for this high-level overview of the product. We hope you enjoy the product and if you encounter any issues, please be sure to post them in our issues tab of github.

Thank you,
Team Nanite

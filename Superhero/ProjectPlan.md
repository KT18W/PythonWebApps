# Week 2
 - # Past Work
    - Requirements, Design, Code, Test
        - The requirements were to create a very basic static website with a profile on it, there was very little design to it, it just used headers and paragraphs and a single image. The code just involved one html page.

    - New Skills learned
        - We had to learn how to hook up gitHub to be the repository and connect it to our visual studio code. Then we had to set up our dev environments and python and create the first app.

    - Design patterns used
        - The only design pattern that was the generic pattern you showed us.

    - loose ends to resolve
        - There are no loose ends to resolve.

 - # Future Work
    - Requirements, Design, Code, Test to do
        - The main requirement at this stage is to get the application hosted on a hosting service. This does not require any new design other than just including the yaml file.

    - New skills needed
        - The ability to get a website on a hosting service.

    - Challenges to resolve
        - The main challenge was to get the github connected to the digital ocean profile and then set it to look for changes on the right project and get all of the environmental variables set up correctly.

# Week 4
 - # Past Work
    - Requirements, Design, Code, Test
        - The requirements here are to get a django application up and running and have a few heros with some attributes on each and create a page different page for each hero

    - New Skills learned
        - Creating data and then using the data in the app instead of just hard coding everything in the regular page.

    - Design patterns used
        - Each hero had to have an image and certain attributes displayed along with it on seperate pages.

    - loose ends to resolve
        - There are no loose ends to resolve.
    
 - # Future Work
    - Requirements, Design, Code, Test to do
        - Here we need to make it to where the pages can be generated off of the data using views and have each of the pages inherate the main page theme using inheritance.

    - New skills needed
        - We needed to figure out how to get the code to where we did not need to create each page individually but rather have each page create itself using a view based off of the data that is in a table.

    - Challenges to resolve
        - We needed to get the pages to generate themselvs.

# Week 6
 - # Past Work
    - Requirements, Design, Code, Test
        - Here we learned how to get a database up and running in django so that way the data would be flexible and the pages could look up the records. We had to build a table that contained columns with specific attributes that related a hero to strengths, weaknesses, etc.

    - New Skills learned
        - The main new skill that we learned here was how to create a database and build the models in your code that allow the database and your application to talk to each other.

    - Design patterns used
        - We used an index page that allows you to click on a hero and see them on a completely different page.

    - loose ends to resolve
        - There are no loose ends to resolve.
    
 - # Future Work
    - Requirements, Design, Code, Test to do
        - The requirements for this week were to create CRUD views so that the database would be able to be modified from the website itself instead of just the command line or going to the admin page in django.

    - New skills needed
        - The new skills needed were to figure out how to allow the front end to talk to the backend directly.

    - Challenges to resolve
        - One of the main challengs that needed to be resolved was not just setting up the view but actually getting it to communicate properly.


# Week 8
 - # Past Work
    - Requirements, Design, Code, Test
        - We were required to implement the functionality of having users in our database and have the front end allow them to sign up or log in and log out. We also had to make it to where some of the functions like creating, updating, and deleting heros required the user to be logged in, while allowing everyone including non-logged in people to be able to view the existing heros. This included updating the database with a new table and updating the views that allow you to change items in the database to require logging in before viewing.

    - New Skills learned
        - I learned how to create a user database and hide specific views behind the log in interface so that only people who have accounts can see them.

    - Design patterns used
        - I used the main theme that was used in all of the other views as the basis for the log in page on top of which I just put a log in form.

    - loose ends to resolve
        - There are no loose ends to resolve.
    
 - # Future Work
    - Requirements, Design, Code, Test to do
        - In order to speed up the design process I need to implement some automatic testing that will test all of the aspects when I need it too so that I don't have to manually go back in and do it myself. This mainly includes creating a testing file with all of the test cases for all of the views.

    - New skills needed
        - Basically I need to learn how automated testing works as a whole.

    - Challenges to resolve
        - One of the biggest challenges is getting the tests to actually work with the database and run properly.


# Week 10
 - # Past Work
    - Requirements, Design, Code, Test
        - This week I will need to produce a production database so that way everytime an update is commited and pushed, the data will not clear itself. This mainly included changing the yaml file and going through and changing digital ocean.

    - New Skills learned
        - I learned how to publish a website that will keep it's data even when it is being updated.

    - Design patterns used
        - There were no design patterns used as this was more of a functionality thing than a design thing.

    - loose ends to resolve
        - There are no loose ends to resolve.
    
 - # Future Work
    - Requirements, Design, Code, Test to do
        This week I will be updating the views so that way they are split up into more components so that way the elements can stay designed better even when other parts of the page need to be changed. This will mean changing the code from being one big page to having a nav bar, a header, a body, and a footer.

    - New skills needed
        - The new skill needed is that of being able to use the correct syntax to seperate out each of the elements listed above, and how to make the items in the navbar functional.

    - Challenges to resolve
        - The main challenge to resolve this week is getting the footer bar to stick to the bottom of the page at all times.


# Week 12
 # Past Work
   - Requirements, Design, Code, Test
       - This week I had to create the functionality of 4 management commands so that I could create and destroy files containing the database, 2 of which delt with JSON files and the other 2 delt with CSV files.

    - New Skills learned
        - The new skills that I learned was how to create management commands and download data in two different ways and then delete them.

    - Design patterns used
        - There were no real patterns used as this was also more dealing with functionality than design work.

    - loose ends to resolve
        - There are no loose ends to resolve.

 # Future Work
   - Requirements, Design, Code, Test to do
    - I will be implementing the code in my forms that allow the user to be able to upload their own images when they are either creating a new hero or updating an existing hero.

    - New skills needed
        - The new skill that is needed is how to get it to where the database can point to images and how to store those images. Also how to get the upload button to have a file explorer with all of the images that the person has on there local storage to pop up and let them pick an image.

    - Challenges to resolve
        - The main challenge to solve was updating the places where the code pointed to the images themselves, the models were also a bit of a challenge to update properly because I had to implement a photo table and that involved a foreign key.


# Week 14
- Requirements, Design, Code, Test
    - The requirements this week involved using code that you developed in order to automatically create code with giving it a specific name.

- New Skills learned
    - I learned that it is possible to create code with a code generator.

- Design patterns used
    - I did not use any design patterns as this is building code, not designing the actual webpage.

- loose ends to resolve
    - generating code into the superhero app.
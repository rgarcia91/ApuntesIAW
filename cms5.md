# Introduction
In this guided trial, you will see an example of how easy it is to build a solution using and extending Liferay DXP’s low-code and no-code capabilities. Follow the guide to leverage Objects, Client Extensions, Fragments, and Segmentation to build a Customer Portal.

Clarity, a fictional eyewear manufacturer, needs a self-service customer portal. Clarity could buy a subscription to a point solution like a specialized ticketing system, but the CTO has a better idea: to leverage a pre-existing investment in Liferay DXP to create a solution using Liferay's extension capabilities.
In this guide we will cover:

You acting as a Clarity Customer
Viewing & creating tickets
You acting as a Clarity Customer Support Representative
Moving tickets through the workflow
You acting as a Clarity Admin
Understanding Objects
Working with Objects and default Liferay Frameworks
Using Objects through Client Extensions to implement advanced requirements
Look and feel main considerations
Structured content
One more tip: In this Trial Guide you can mark each step as complete once you follow all the instructions by pressing the Mark as Complete button. This way you can keep track of your progress even if you log out and return later.

## Activating Users

We’ve already created some users for you, but you have to activate them:

You should be logged in with the super user credentials for your Pre-Built Trial, found in your welcome email. If not, open a new tab and log in using these credentials. Remember: you should have this Trial Guide opened in a separate tab at all times while following along.
Click the grid icon at the top right of the page.
In the Control Panel tab, find Users and Organizations and click the link.
Press the Filter icon and select Inactive to see a list of all inactive users.
Select the three users we will be using in this Trial: M2H8 Admin Adam, M2H8 Customer Carl, and M2H8 Support Sam, by pressing the checkbox to the left of each user.
Activate these users by pressing Activate above the list on the right.
Remove the status Inactive filter to double-check that the three users are now active.
Each user has the default password test. When you log in for the first time as each of these users, you’ll be prompted to change the password. Make sure to write down the new passwords you choose.

## You as a Customer

For this portion of the Pre-Built Trial, you will log in as Customer Carl.
### View Tickets
Log in to Clarity as Customer Carl.
From the Home Page, click View My Tickets.
You should see an empty list of tickets.

Customer Carl
Carl is a customer of Clarity. He can create tickets to explain what problems or questions he has.
Email

m2h8.customer.carl@liferay.com

Password

[Your chosen password]

### Adding a Ticket
Click the New Ticket button at the top right of the page to create a ticket.
A new form will appear where you can add the following info:
Subject: Add a subject. E.g., “Requesting help with my glasses order.”.
Description: Add a description. E.g., “I can’t find the tracking information for my order.“.
Related Ticket: Leave this empty.
Attachment: You can leave this empty or add an example of an attachment. For an example attachment, go to Learning > Attachments in the top menu, and click the folder named Attachments, then download one of the files. You will need to click on the icon with an i to toggle the Info Panel where the Download button is. Upload this file to the ticket.
Don’t upload anything new or person from your own device.
After adding any desired info, click Submit.
### Viewing One Ticket
Click the top menu in View Tickets to see the list again.
Click either the Number or the Title of your new ticket to view its details. This is a Display Page Template that maps to and displays each ticket's specific data. You’ll learn more about this later as the Clarity Admin.
As a Clarity Customer, you can see the ticket’s: 
Subject and status (Open, In Progress, Blocked, Closed)
Full description
Assignee and any related tickets
Downloadable attachments
You can use the “back” button at the left to return to the complete ticket list.



## You as a Customer Support Representative

Log out of Carl’s account, then sign in as Support Sam. Because Support Sam has the Customer Support Representative role, you now have access to additional ticket management functionality.
Check that View Tickets in the top navigation now has two additional sub-options: Admin View and Tickets Dashboard.

### Admin View

The Admin View page includes the default View that gets generated when a New Object is created, you’ll learn more about this later as the Clarity Admin. As a Customer Support Rep., here you can: Create, Read, Update, and Delete Tickets.

Click on any Ticket ID to see its details.
Next, return to the Admin View and click the three vertical dots besides one of the existing tickets.
Click Assign Ticket to Me to assign the ticket to yourself.
Make sure the list refreshes. You should see M2H8 Support in the User to J3Y7 Ticket column. Leave at least one ticket unassigned.

Support Sam
Sam works in Clarity's Support department as a Customer Support Representative.
Email

m2h8.support.sam@liferay.com

Password

[Your chosen password]

### Tickets Dashboard

Click the Tickets Dashboard link under View Tickets. This page includes more advanced ticket management options. For instance, here you can change the status of tickets using similar functionality as a standard ticketing tool. You’ll learn more about this later as the Clarity Admin.
Click and drag a ticket from the Open column to In-Progress.
Try to move the ticket from In-Progress back to Open. You will see a red message that prevents you from doing this. That’s because we’ve restricted certain status movements in the Ticket Object. We’ll discuss this more later.
You can also assign the ticket to yourself by expanding one of the unassigned tickets and clicking the Assign to Me button.
If you've created a ticket with the Customer role previously, there will be a notification in your profile image at the top of the page. You can press the icon and then Notifications to see that you as the Customer Support Rep. are receiving a new notification when a ticket is created.
Now that you understand how to use the Clarity portal as both Customer Carl and Support Sam, we'll shift our focus to an under-the-hood look at how the portal is built from the vantage point of the Clarity Admin role.

## You As a Clarity Admin, Part I: Understanding Objects

Log out of Support Sam's account, then sign in as Admin Adam to gain access to all the power of Liferay SaaS.
We'll start by explaining our Ticket object, which was built with Liferay Objects. Liferay Objects provide easily configurable development capabilities in the Liferay UI.

### Main Information
Click the grid icon in the top right of the page.
Use the Control Panel tab, find Objects and click the link. Here you should see our Ticket Object.
Take a look at the Fields that represent the Object: there are default System Fields (such as Modified Date, Status, etc.) as well as the specific fields we've created for this demo: Subject, Description, Ticket Status, Attachment, User To Ticket relation, etc.
Confirm that Ticket Status is a PickList that is defined in [Control Panel > Objects > PickLists]. This is a list of different statuses.
Click on the field itself in the object to check the Mandatory and Marked as State: this field describes the ticket's status.
Confirm that User to J3Y7 Ticket is a Relationship field with User (to assign tickets to users).
Go back to [Control Panel > Object > Objects] and choose the User System Object. In the Relationships tab the User object has a oneToMany relationship to the Ticket Object.
Return to our Ticket Object, and confirm that J3Y7 Ticket to J3Y7 Tickets is a Relationship field with the Ticket itself. Go to the Relationships tab here in the Ticket Object to confirm that there's a oneToMany relationship to the Ticket Object.
Confirm the rest of the fields as simple fields of different types
Familiarize yourself with the Relationships tab to understand the different relationships this object has, as we’ve already mentioned.
You can also have a look at the different relationships by pressing the View in Model Builder button back in [Control Panel > Object > Objects].
As an optional exercise, you can create a new Folder and assign our Ticket Object to that Folder to get a simpler view when clicking the View in Model Builder button.
Check that Layouts, Views, and Validations are all empty right now.
As an exercise you can try creating a default Layout, which will alter the default Form to Insert and Edit new instances of the object.
You can also add a default View, which will change the default list of tickets.
If you do this, check in [Control Panel > Applications > Content > J3Y7 Tickets] for both the list and the insert/update form.
Check Actions to understand the different actions defined.
Assign Ticket to Me will allow you to assign a ticket to the user performing the action. (Check that this is a standalone action in the Action Builder subtab. Its corresponding low-code represents what the action will do).
Ticket Creation Notification will trigger a Notification template named New Ticket was Created on each ticket creation (On After Add)
You can find the Notification template itself by going to [Control Panel > Notifications > Templates].
Check State Manager to see that we have limited the transitions from one state to another.
​​​​​​​This explains why, earlier, you couldn't transition the ticket from In Progress to Open.

Admin Adam
Adam is the Admin User and has access to all the settings and customizations on the platform.
Email

m2h8.admin.adam@liferay.com

Password

[Your chosen password]

### Additional Information

Let’s dig a little deeper into how this Object works as well as how you can see Liferay’s out-of-the-box features on display here.

Permissions: Go to [Control Panel > Roles] and make sure you see two roles: M2H8 Petitionaries and M2H8 Ticket Solvers
M2H8 Petitionaries is a role describing users that can create tickets (like Customer Carl, in our example).
Check that the role is defining Add and Update permissions on the ticket object. View permissions are not granted because in Liferay DXP a user can already view the objects they create (as the Owner), and we don't want the user to see tickets belonging to other users.
Check that the role can also interact with Documents and Media, as users belonging to this role will need to upload documents as attachments to the ticket itself.
M2H8 Ticket Solvers is a role describing users that can solve tickets (in our example, the Customer Support Representative, Support Sam).
Check that the role has different permissions defined that relate to the Ticket object including View and the AssignToMe standalone action. (Liferay DXP created this permission for us automatically when we created the standalone action in the previous step.)
Check that the role can also interact with Documents and Media, as users belonging to this role will need to view/upload documents as attachments to the ticket itself.
Default Widgets 
Look under the first tab in the Ticket object to see that the information is stored at the Company Level. There should be a switch already enabled to Show Widget in Page Builder. In the list above, Panel Link, we've chosen to show the widget under [Control Panel > Object].
Headless: Liferay provides a suite of APIs that perform the same kinds of actions available in the web interface. In the case of Objects, same, there's a set of headless end-points that have been generated automatically, both GraphQL and Rest.
You can check this by opening a new tab in your browser and typing your Pre-Built Trial base URL and then adding /o/api. Now click on Rest Applications in the top right menu and select c/J3Y7tickets end-point.
You will see that there are Get, Put, Delete, etc. actions generated. These end-points will be used later in this demo through different Fragments and Client Extensions.
We have completed the overview of our base Ticket Object. Now let's see how the Ticket Object can be used.

## You as a Clarity Admin, Part II: Building Pages with No-Code

Let's take a look at how the different main pages are created.

### Ticket List
Make sure you are on the View Tickets page. Click on the Edit Page icon (represented by a Pencil icon) at the top right icons' menu.
Check the top right buttons, New Ticket and View Dashboard. The New Ticket button only appears for certain users. We are using Liferay DXP Personalization out of the box.
Check the Default experience and the Admin View experience at the top. The Admin View is an experience for users who meet certain conditions. You can check out the segment definition in [People > Segments] at site level. In this case, we've used the email of each person, but you could also change it to be role-based.
Note: There are several ways to implement this with Liferay DXP out of the box; this is just one way.
The list of tickets simulates a Table View by using different out-of-the-box fragments included in Liferay DXP like Containers and Grids.
A Collection Display Fragment has been configured to show the Collection called J3Y7 Tickets. Objects provide this out of the box. Check that you can configure different aspects such as pagination, number of elements per page, etc.
Inside this fragment, there’s a grid with text fragments (Dialect text) mapped to specific columns of our Ticket Object (Subject, Date, etc.).
Check that the Date is mapped with a Date fragment, where we can define a specific format (e.g., dd MMM, yyyy hh:mm a). Liferay DXP provides direct configuration for different date types by default.
Check that we are using an Info Template for the Ticket Description to do some custom formatting: as the Description is a WYSIWYG field, we decided to remove all HTML formatting and show only the 50 first characters for this list.
Check this Info Template in [Design > Templates > Information Templates], and then the M2H8 Attachment Description Summarized template.
Double-click either the Id or Title columns to check they are mapped to the Display Page URL that belongs to each object, in the Link tab at your right.
This is just a way of listing all the tickets using out-of-the-box elements in Liferay DXP. You can also use a Widget that is autogenerated for each Object you create, but the formatting won't be as flexible as the one you can configure with the Collection Display Fragment.


Admin Adam
Adam is the Admin User and has access to all the settings and customizations on the platform.
Email

m2h8.admin.adam@liferay.com

Password

[Your chosen password]

### Viewing a Ticket
Back on the Ticket List page, click on a ticket, then click the Edit Page icon (represented by a Pencil icon) at the top right icons' menu, then click Edit Display Page Template to see how this Display Page Template was created. (Note: You can also edit this page by going to [Design > Page Templates > Display Page Templates] and selecting Ticket DPT.).
Check how the different fragments have been dragged, dropped, and mapped to the main fields of the Ticket Object (Subject, Date, Status, etc.).
Check specific configurations for certain fields:
For the Attachment, find one Info Template, mapped to an HTML fragment where we show the attachment information by calling the Headless layer of our Ticket object through the restClient object, an easy way of injecting headless resources into templates.
For the Related ticket, we're using a Collection Display Fragment, which is mapped to an auto-generated collection called J3Y7 Ticket to J3Y7 Tickets (Parent). Thanks to this collection, it's very easy to list all the information of a related object that has a relationship with our main object.
Remember, always create a Display Page Template for each of your objects and mark it as the default one, so Liferay DXP can show it when showing the details of an Object in its Display Page URL
### Adding a Ticket

Next, we’ll talk about how to create the Form to add a ticket. Liferay does provide an out-of-the-box form for ticket creation, which you saw when we talked about the Object in-depth. For this example, however, we’re going to look at the custom Form we’ve created, which is another option if you want more flexibility.

Go to the New Ticket Page and press the Edit Page icon (represented by a Pencil icon) at the top right icons' menu.
The main component we’re using is a Form Container, which allows you to create Forms that are connected to Objects directly in the page editor. Liferay DXP also provides Forms to create full Forms that can be integrated with Objects as well. What you should choose will depend on the circumstances, but by default, a Form Container is the preferred way to integrate gathering data for Objects. Here are the main components of the Form:
Containers and Grids connected to each Object’s field have some of Liferay’s out-of-the-box field types, 
As an example, you can click on the Subject field and check that it is mapped to the Subject field of the Ticket Object
You can do the same for the rest of the fields.
There's a Submit button to send the information
That’s it! The default form has really only been customized in terms of its look and feel. But you can customize the default form in many other ways, as well. 
For example, if you need to add validations, you can control the Submit button enablement depending on whether or not the validations have been completed. All of this happens in two layers: on the client side, where you will need to add JavaScript, etc. to manage this through fragments (from our documentation, see Creating Form Fragments); and on the server side, where you can either use the default object validations or create custom validations.
### Exercise (Optional)
Here’s an optional exercise to see what we mean. Let's add a validation for both the Client and the Server Side. 

Go to the Ticket Object and modify the Subject Field by activating the switch Limit Characters. Limit the number of characters to 100, as an example. Save the changes.
Now you can check that if you add a new Ticket and put a Subject with more than 100 characters, you’ll receive a message first on the Client Side (JavaScript), and if you still try to Submit, then you won't be able to save and you’ll receive another message on the Server Side.
You can also edit the Add New Ticket Form and click on the Subject field to activate a character count for the user while writing. 
Look in [Design > Fragments] at the site level, and then at Form Components in the Default Collection to see how the Text Input form field is created to manage all of this. Don't forget to check our documentation around Form Fragment Components if you want to learn more.
This is just one example using out-of-the-box validations. There are other validations you can check, both at the Object's field level and in the Validation tab of an object. Read Validations for Objects in our documentation to understand how they can be added.

## You as a Clarity Admin, Part III: Client Extensions

### Dashboard Page

Go to the Dashboard View and click on the Edit Page icon (represented by a Pencil icon) at the top right icons' menu
You’ll notice that this page only has a single Widget called Liferay Ticket Custom Element. This is a Front End Client Extension that we implemented in React, then declared in Liferay DXP through our SaaS orchestrator, and now we can drag and drop it into pages. Let's explain it step by step:
In the [Control Panel > Applications > Custom Apps > Client Extensions], you can see that we have one Client Extension, the Liferay Ticket Custom Element.
Click on this Client Extension and check that there are URLs pointing to the code the Client Extension needs to run.
Once the Client Extension is available in Liferay DXP, you can drag and drop it on any page, like any other normal widget or fragment.
When it comes to extending Liferay DXP with JavaScript Advanced Frameworks, such as Angular, React, Vue, etc. everything is easy if you follow the Client Extensions path.

Admin Adam
Adam is the Admin User and has access to all the settings and customizations on the platform.
Email

m2h8.admin.adam@liferay.com

Password

[Your chosen password]
### Client Extensions
In this Pre-Buil Trial Liferay SaaS installation you are provided with a Front End Client Extension that is installed and already configured. In a real Liferay SaaS installation, you will deal with different Client Extensions to extend Liferay DXP when needed and can manage them through the Liferay Cloud Console.
Note: In order to deploy a Client Extension in Liferay SaaS, you’ll need to meet some pre-requisites. In this Pre-Built Trial you can't access the Extensions environment that Liferay SaaS provides, but you will have access to it if you have a real Liferay SaaS subscription.
There's a specific Command Line Tool (CLI tooling) to be installed locally to deploy in Liferay SaaS.


## You as a Clarity Admin, Part IV: Additional information
### Structured Content

This Trial also includes an FAQ page with an example of Structured Content so you can see a typical way of creating content in Liferay DXP through Structured Content that can then be displayed in pages with out-of-the-box capabilities. A couple of things to highlight:

Structure: the FAQ structure is defined in the site. Just open the menu on the left side and locate [Content & Data > Web Content], then the Structures tab.
You will find a simple structure with two fields, Question and Answer. 
In the other tab, Templates, you can create templates using FreeMarker to control how to display a given Web Content.
In this Trial, however, we are using a Collection Display Fragment to display the content on the page. This way, we are maximizing the use of low-code and no code capabilities by just dragging, dropping and mapping fragments to our FAQ’s structure fields.
Take a look at the FAQ page to understand how this was built.
Back in [Content & Data > Web Content], you should find a folder with all the FAQs. Feel free to look at one as an example to see all the different things you can define on a single piece of web content in the right panel when in Edit mode, like: metadata, templates, categorization, schedule, search settings, and related assets. 
You can find related information in our documentation for Web Content.

### Look and Feel

On all the pages you’ve seen, including these tutorial pages, you’ve looked at different examples of how Pages in Liferay DXP can easily be created with out-of-the-box fragments. You’ve also seen additional example fragments that have been developed.
Don't forget to open the menu on the left side and check out.

Style Books: This is the base configuration for colors, fonts, spaces, etc. in defining our base look and feel.
Fragments: Here, you can find the default fragments plus the additional examples we’ve developed for this demo.
Templates: This includes the Information Templates and Widget Templates used.
Page Templates: Here you can find the Master Pages and Display Page Templates used.
Navigation Menus: The top menu we have defined is created here.
Collections: This includes some collections we have defined for certain pages.
Liferay DXP is a Digital Experience Platform that empowers you to create personalized digital experiences your way that go beyond the limitations of point solutions and connect with your audience. Keep on learning with us!

Not ready for your Pre-Built Trial to end? Contact sales@liferay.com to extend the trial or for more information on getting started with Liferay SaaS.
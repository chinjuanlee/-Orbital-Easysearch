# -Orbital-Easysearch
Orbital Project 2021
<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 15.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>
<a href="#gdcalert10">alert10</a>
<a href="#gdcalert11">alert11</a>
<a href="#gdcalert12">alert12</a>
<a href="#gdcalert13">alert13</a>
<a href="#gdcalert14">alert14</a>
<a href="#gdcalert15">alert15</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


**Milestone 3 Submission**

 

**Team Name:**

 

Team CheapSkate

 

 

**Proposed Level of Achievement:**

 

Apollo 11

 

**Poster**

**<span style="text-decoration:underline;">Motivation</span>**

 

Do you feel like there are too many e-commerce websites/online stores, but it is too troublesome to find the best deals out there? Do you always regret buying things and realise that there are cheaper deals elsewhere? Are the prices not shown in SGD S$? Is it too frustrating for you and why can’t there be apps which show the BEST DEALS and the next “MEGA” sale and compare retail store prices versus e-commerce website prices?

 

**<span style="text-decoration:underline;">Aim</span>**

 

We hope to make to make a web-based platform which **shows the best deals and sale on the most popular online websites/stores** (Amazon, Lazada, Shopee, Qoo10) and **convert the prices all to Singapore dollars** for easy comparison

 

**<span style="text-decoration:underline;">User Stories</span>**

 



1. As a consumer, I can search across multiple e-commerce and retail sites, so I can find the best deals.
2. As a consumer, I can bookmark certain items so that I can easily refer back to them to check for price changes or if I have not made up my mind.
3. As a consumer, I can create my own personal account so that my items and search history are for personal viewing only.

 

**<span style="text-decoration:underline;">Deployment</span>**

**Front-end (web-app): **

[https://easysearch.vercel.app/](https://easysearch.vercel.app/)

**Back-end: **

(API call - Amazon Web Service)

[http://easysearchserver-env-3.eba-3pjbymty.ap-southeast-1.elasticbeanstalk.com/](http://easysearchserver-env-3.eba-3pjbymty.ap-southeast-1.elasticbeanstalk.com/)

(Scheduled scripts)

**Heroku**

**Note: We have shifted our backend server on AWS Elastic Beanstalk to provide faster search results and improve User Experience. However, computationally intensive tasks like our scheduled scripts (trending products, wishlist emailing) are left on Heroku since we are using AWS Free Tier and have limited resources per month.**

**<span style="text-decoration:underline;">Tech Stack</span>**



1. ReactJS + MaterialUI (Front-end)
2. Python Flask + Selenium + BeautifulSoup (Back-end)
3. Google Firebase (Database, User Authentication)
4. Git, Github (For repository control and source-code control)

**<span style="text-decoration:underline;">Project Scope</span>**

Our project consists of 3 sprints: **Initialisation** (Sprint 1), **Functionality **(Sprint 2), **Extension **(Sprint 3)

**Initialisation: **User Registration and Login, Web scraping scripts, Displaying database items

**Functionality: **Trending products, Real-time search, Wishlist, History page

**Extension: **Scheduled email notifications of wishlist products, Mobile Friendly Application, Product Recommendation (Stretch goal if time permits and if database has sufficient queries for supervised ML model)

**<span style="text-decoration:underline;">Sprint One (Milestone 1)</span>**

**Features**: 



1. **User Account Registration and Login**

    - Setting up Firebase Authentication and Front-end Web Routing


**					Figure: **User Registration Page

**					Figure: **User Login Page

**Description**: Introduce user registration and login required by all users. After users register, they will then gain access to the web application.



2. **Web scraping for Shopee and EzBuy (API call)**

    - Request product API from Shopee and Ezbuy servers to retrieve product information and provide recommendation


    	   **Figure: **Sample code fragment of product API call to Ezbuy server


**Description:** Implementation of e-commerce web scraping via web API call which retrieves information from Shopee and EzBuy servers and performs CRUD operations to write data into Google Firebase

**Note**: Search results were not optimised yet, however we managed to retrieve product information from API calls



3. **Establishing front-end/back-end link**

    - Creating search bar function and displaying results stored in Firebase database




<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


**Description:** Displaying product information of scraped data (Item name, price, store, rating, image, link to page)

**Note**: Search-function not in real time yet, web page only displays products in database that is manually scraped

**These features are implemented for submission at Milestone 1**

**<span style="text-decoration:underline;">Sprint Two (Milestone 2)</span>**

**Features**: 



1. **Web scraping for Amazon and Qoo10 (Using Selenium ChromeDriver)**

    - Extending scraping capabilities to e-commerce websites (without API access) using Selenium to allow cross-product comparison across more e-commerce sites


    **  Figure: **Sample code fragment of web scraping of Qoo10 


**Description:** Using headless Chrome browser to conduct web scraping of HTML web elements to retrieve product details

**Note**: Time taken to retrieve product information for sites like Amazon and Qoo10 is considerably longer due the inability of accessing APIs, therefore search results may take up to 30-40 seconds.

**Constraints: **1) Not all websites allow web scraping (e.g. Lazada) due to explicit instructions on Robots.txt file, 2) Web pages of Amazon and Qoo10 were lazily loaded, which meant that not all web elements were displayed.

**Fix**: 1) Updated script to simulate intermittent scrolling from what a real user would perform, which allowed lazily loaded elements to appear during headless browsing.



2. **Deploying Realtime search capabilities**

    - Hosting backend Flask server on Heroku and implementing GET requests from front-end interface to the backend server to run searches


    **Figure: **Successful GET requests &lt;Response 200> to backend server


**Description:** When a user searches for an item in the search bar, the front-end interface will asynchronously send GET requests to the backend server which will run multiple tasks to scrape e-commerce websites. Backend python scripts will perform CRUD operations and update product information in Google Firebase which will be displayed on the front-end interface.

**Constraints: **1) GET requests may take longer than 30s resulting in &lt;Response 503> timeout due to Heroku’s timeout limit, 2) Search results 

**Fix: **We realised that long-polling methods (which sends a single-byte response after 30 seconds) extends the timeout by another 55 seconds. Though not optimal, this provides a workaround to the timeout limit imposed by Heroku. Alternative options were considered like deploying the backend server on AWS Lambda or Microsoft Azure with Singapore/Asia-Pacific servers for faster response, however this required monthly billing and also Heroku was more tailored for our scripts due to pre-written buildpacks that supported the running of Selenium ChromeDriver.



3. **Wishlist for individual users**

    - Allow users to bookmark items which they may want to track




<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


**Description: **Users can opt to add/remove items to the wishlist when they search for products. The wish list helps users to bookmark the prospective product and keep track of any price fluctuations by sending out email notifications to inform users if price drop.



4. **User Search History **

    - Storage of users past search history unique to the individual user




<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


**Description: **Users can retrieve past search history under the “History” tab of the web-application. Front-end interface caches search history into Google Firestore. Users can click the “Results” button under the search history which redirects them to the specific search results for ease of use.



5. **Sorting search results **

    - Allow users to sort their search results based on price and store




<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")


**Description: **Deployed interactive buttons which allows user to sort products based on overall ascending/descending price across all sites or within individual e-commerce sites



6. **Refining search algorithm and optimising code**

    - Reducing search time and improving relevance of recommendation


    	**Figure:** Example of backend response before optimisation (Time ≈ 49s)


    **Figure:** Example of backend response after optimisation (Time ≈ 27s)


**Description (Part 1): **We refined our backend web scraping scripts to reduce scraping time for web elements for Amazon and Qoo10 sites. By importing the Python asyncio library, we managed to use asynchronous programming to perform extraction of multiple web elements concurrently (e.g. title, price, url, image). On average, we managed to cut down GET requests time from 45s to 30s which allowed faster display time of products on our website.

**Constraints:** We note that 30s is still far from optimal but due to Amazon and Qoo10 not having open product APIs, we are limited by the scraping duration of Selenium ChromeDriver. 

**Description (Part 2): **During milestone evaluation, one of the teams mentioned that we should consider Bayesian Average to aggregate product ratings. We adjusted our backend scripts to assign Bayesian Average to the products listed on the e-commerce websites and provided our recommendations based on the top 3 scores.

**Note:** We are still working on this and are hoping to work on feedback given for search recommendation based on the User Acceptance Test after Milestone 2 submission. 



7. **Trending products**

    - Cross platform monitoring of trending items across popular product categories 


    **  Figure: **Front-end display of carousel containing trending products




<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")



        **    	 Figure: **Trending products from Home and Health products

**Description: **Deployed additional backend Python scripts hosted on Heroku to scrape trending products daily at UTC 0900H across popular categories (Technology, Beauty, Fashion, Food and Home & Health Products). Product details of top 5 trending products are extracted and displayed on the web application.

**Note: **We hoped to track the hourly price changes and trending products from each site, however in order not to overload the e-commerce sites we decided to conduct daily scraping instead.

**These features are implemented for submission at Milestone 2 and are currently deployed on the web-application**

**<span style="text-decoration:underline;">Sprint Three (Milestone 3)</span>**

**Features:**



1. **Mobile Responsive Application**

    - Create mobile friendly webpage to allow easy access on mobile phones


                **Figure: **Webpage viewed on IOS


**Description: **Applying mobile responsiveness so that the app still looks good on mobile viewports and user experience is not hindered by a smaller screen. Text elements that are too long are changed into icons that are intuitive in nature and less important details of the product are removed when on the mobile viewport while still maintaining the full feature set available to desktop users. 



2. **Scheduled email notifications for products on wishlist**

    - Automated emailing function to notify customers on price drop


        ** 		Figure: **Sample email notification for price drop


**Description: **Deployed scheduled backend scripts to run and track wishlist items for all users. If any products have price changes, scripts will automatically update prices in the database. In the event of a price drop, email will be sent to the specific user to inform them on the changes which allows them to consider if they would want to make the purchase.

**Note: **Email notification will be sent to the corresponding email that the user has provided when signing up.



3. **Forgot password/Reset function**

    - Allow users to reset password using Google Firebase


                **Figure: **Page to reset password 


                **Figure: **Email link to reset password


**Description: **Allow users to reset their password to their account using Google Firebase. Reset password link will be generated and sent to the email address of the user.



4. **Extension of web scraping to food deals**

    - Extending capabilities of web scraping to retrieving food deals 


** 				Figure: **List of food deals for bubble tea (Sample)

**Description: **Widened web scraping capabilities to retrieve food deals from websites like Chope and Fave. Successfully deployed backend scripts for Chope but not Fave (able to do it on localhost), however access to websites was denied when we shifted the script to AWS Elastic Beanstalk.

**Constraints:** We realised that the AWS Load Balance which handled the instance was default set to IPV4 and not IPV6. This was likely the reason which prevented us from accessing the Zalora webpage when we deployed to AWS Elastic Beanstalk as CloudFront was throwing an Error 403 message. However, to use the IPV6 configuration, we had to set up a VPC which was extremely costly and not budget friendly for this project (**$0.045 per hour**). Therefore, we are unable to deploy Fave web scraping scripts.



5. **Redeployment of web scraping scripts to AWS Elastic Beanstalk**

    - Drastically decreasing search times for results by deploying on AWS




<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")



        **         Figure: **Deployment status of backend search server on AWS

**Description: **Shifted backend web scraping scripts to AWS Elastic Beanstalk to optimise search times. Compared to Heroku, we reduced average search times from 30s to 10s per search. Search results for Amazon, Ezbuy and Shopee are almost instantaneous while Qoo10 takes longer due to usage of Selenium ChromeDriver.

**Note: **Due to the dynamic elements on Qoo10 webpage, we are restricted to using Selenium ChromeDriver in order to extract the images. While this is not ideal, we believe that the benefits of extracting the images is important because this helps the user make informed choices when purchasing items.



6. **Delete search History function**

    - Allowing users to select which search history they would like to erase


**Description: **Deployed a delete history function which allows users to delete selected search history. When users delete selected history, search history will be removed from the user’s History collection in Google Firebase

**Constraints: **Unfortunately, Google Firebase restricts us from purging the entire History collection and therefore we are unable to successfully deploy a **Delete Everything function**, instead users can select multiple/individual search history for deletion.

**These features are implemented for submission at Milestone 3 and are currently deployed on the web-application**

**<span style="text-decoration:underline;">Features Limitations/Constraints</span>**

Apart from our features, our team would like to discuss the limitations of our web application.



1. **<span style="text-decoration:underline;">Extension difficulties to other popular websites (e.g, Fave, Zalora, Lazada)</span>**

    For popular websites like Lazada, web-scraping is difficult due to Robots.txt restrictions which prevents us from scraping their product catalogue. Furthermore, Lazada has bot detection algorithms that prevent Selenium webdriver from accessing its sites frequently. **We have also attempted to expand our scraping to **Zalora and Fave and while we managed to get our scripts working on the localhost, we were unable to access the webpage when deployed on the Cloud, AWS Elastic Beanstalk. In order to circumvent this, we are required to have a VPC that allows IPV6 network configuration for our Elastic Load Balancer so that websites do not block our access when on the Cloud. However, this is very expensive and unfeasible especially for the scale of our project. In an ideal situation, we hope to have open access to the product API for Lazada and necessary VPC set up for our AWS backend server but given the scale of Orbital, **our project is currently limited to the current features.**

2. **<span style="text-decoration:underline;">Query limitations (AWS Free Tier, Google Firebase)</span>**

    Given the **free-to-use services** that we are currently running on, our backend servers are not able to handle excessive queries. As such, it is currently difficult for us to scale up and handle commercial-level queries (AWS EC2 - 750 free hours per month, Google Firebase 50K read/day). However, our web application is still functional and able to work efficiently for the current Orbital level for our project.

3. **<span style="text-decoration:underline;">Dynamic Loaded webpage (Qoo10, Chope)</span>**

    Due to the private product API key of websites like Qoo10 and Chope, we shifted to using either requests/Selenium ChromeDriver. However, the requests library does not support the scraping of dynamic loaded web pages via JavaScript, therefore only Selenium ChromeDriver supports the functionality. However, scraping using selenium is much slower as it uses a headless browser which takes some time to load and is not ideal. To further optimise searches, we have used asynchronous methods to speed up browsing. However, we do hope to get access to the official product API key for scaling up the webpage.

4. **<span style="text-decoration:underline;">ML Product Recommendation Model</span>**

    Typical product recommendation systems are trained on a user’s shopping habits and search history among other parameters and for our app this is a stretch goal **(beyond Milestone 3)** since we do not really have enough data to ensure that our model is not overfitted. To put into perspective Google Recommendations AI requires a minimum of 1 week of data with an average of 10 add-to-cart events per catalog item. 


**<span style="text-decoration:underline;">Program Flow</span>**

(Click for a clearer view)

**<span style="text-decoration:underline;">Software engineering practices</span>**



1. **<span style="text-decoration:underline;">Iterative development</span>**

    Pushing updates to Git regularly after features are implemented or improved upon allows for careful control of the app at all points of development, allowing for rollback of code if features are to be scrapped or postponed without affecting the rest of the codebase. 




<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")




<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image8.png "image_tooltip")




2. **<span style="text-decoration:underline;">Code reusability</span>**

    Using the principle of abstraction and the power of React we are able to extract and reuse certain UI components in the various pages we have on our webapp. This allows for faster development since lesser code is written and a lesser chance of repeating ourselves. It is also easier for debugging purposes since the code is shorter and the aptly named components can point to the problem when a bug is discovered in the UI.




<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.png "image_tooltip")




3. **<span style="text-decoration:underline;">Communications</span>**

    We did not make use of Kanban boards to document our development progress. Rather we came together on an app called Notion which allowed us to make use of checklists to keep track of our features to be implemented as well as to include images to document bugs found and our meeting minutes in case ideas during our meeting discussions could be used. The flexibility of Notion meant anything from text to files to images could be added and we could easily stay in sync while developing our project while communicating our ideas across well.




<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image10.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image10.png "image_tooltip")




4. **<span style="text-decoration:underline;">Continuous testing</span>**

    As of date most of the software testing is done by us developers manually with the occasional input from random users but done on a small scale. We have implemented snapshot tests and functional tests to ensure the features of our web app are working as intended before pushing it out to potential users to conduct our User Acceptance Testing to obtain feedback to improve on the UI/UX of our app. More details can be found below.


**<span style="text-decoration:underline;">Diagrams</span>**

**Activity Diagram**

The diagram below is an activity diagram of a user interacting with the features on our platform. A more detailed explanation of the features presented can be found above in the project scope section. 



<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image11.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image11.jpg "image_tooltip")


**Visual Sitemap**

Our webapp’s sitemap. A clearer image can be seen by clicking on the image below for a link to the original image.



<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image12.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image12.jpg "image_tooltip")


**<span style="text-decoration:underline;">Quality Assurance</span>**

Our app is front-end heavy since most of the backend is handled by firebase so most of our tests are focused on providing sufficient coverage for our UI and UX. Snapshot testing allows us to make sure that our UI does not break whenever new code is being written before it is pushed to deployment while functional tests ensure that our features are working as intended. All these tests allow us to push new features to our app while ensuring that existing features and UI can continue to work as per normal. User Acceptance testing ties everything together by ensuring that the app is satisfactory to any user that is using it.

**<span style="text-decoration:underline;">Snapshot Testing</span>**



<p id="gdcalert13" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image13.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert14">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image13.png "image_tooltip")


 In general, this test covers all our navigation pages except for 2 which contains dynamic elements that the snapshots are unable to capture (Home and Trending page, which both use carousels)

We make use of snapshot testing to drastically improve test coverage of our code while not needing to write a lot of code for it given the short amount of time we have. This method of testing allows us to know if any code changes resulted in a drastic modification in the UI displayed to our user so that we are able to fix it. Before we push our code to github we always ensure that the snapshot tests pass and if they fail we identify whether it was expected or unexpected and if necessary update the snapshots.

**<span style="text-decoration:underline;">Functional testing</span>**

We make use of the automated testing platform TestProject to run our functional tests to ensure that our various components as well as front-end and back-end are working in tandem whenever we write new code to make sure that nothing is broken before we push the code to development. As we are able to visually observe the code as it is being run, if a test fails we can immediately identify where the bug may have occurred instead of looking all over the place. The Nature of our functional tests are in line with our UATs so you can also refer to the pdf below to get a rough understanding of how our functional tests are structured.



<p id="gdcalert14" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image14.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert15">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image14.png "image_tooltip")


Figure: An example of a functional test

**<span style="text-decoration:underline;">User Acceptance Testing (UAT)</span>**

Our app focuses heavily on the user experience so the tests in this category are very comprehensive, covering every feature available to the user, with detailed instructions on how to carry out the tests and what to expect from the features when testing. The tests are categorized into their features for easier additions of tests in the future if need be and anyone taking over the project is also able to understand in a short amount of time. Users can also give responses or feedback if they find bugs specific to the features and on how to replicate it so it is easier for us to fix the bugs. The process is carried out using Google Forms and the responses are recorded for us to view

User Acceptance Tests can be found in this link below:





<p id="gdcalert15" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image15.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert16">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image15.png "image_tooltip")


Fig. 1 Responses to some tests

The full responses can be found in this link below:



**<span style="text-decoration:underline;">Project Log</span>**

**Milestone 1**


<table>
  <tr>
   <td>Task
   </td>
   <td>Date
   </td>
   <td>Orbitee 1
   </td>
   <td>Orbitee 2
   </td>
   <td>Remarks
   </td>
  </tr>
  <tr>
   <td>Team meeting and initial planning
   </td>
   <td>10/05/2021
   </td>
   <td>8
   </td>
   <td>8
   </td>
   <td>
<ul>

<li>Online zoom call to sketch out product design and structure
<ul>

<li>Delegated roles
</li>
</ul>
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Team meeting:
<p>
implementation details and meeting with advisor
   </td>
   <td>13/05/2021
   </td>
   <td>10
   </td>
   <td>10
   </td>
   <td>
<ul>

<li>Q&A with advisor on project direction and feasibility
<ul>

<li>Decided on technology to use for creation of webapp
</li>
</ul>
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Working on submission for liftoff 
   </td>
   <td>15/05/2021
   </td>
   <td>3
   </td>
   <td>3
   </td>
   <td>
<ul>

<li>Poster and video do-up
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>17/05/2021
   </td>
   <td>3
   </td>
   <td>3
   </td>
   <td>
<ul>

<li>Created frontend skeleton of webapp with necessary pages

<li>Working on web crawler script
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>18/05/2021
   </td>
   <td>2
   </td>
   <td>2
   </td>
   <td>
<ul>

<li>Created routing for login and signup pages

<li>Working on web crawler script
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>22/05/2021
   </td>
   <td>4
   </td>
   <td>4
   </td>
   <td>
<ul>

<li>Beautifying webapp pages and further work on routing

<li>Web crawler script successful and able to store data into firebase
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>23/05/2021
   </td>
   <td>4
   </td>
   <td>4
   </td>
   <td>
<ul>

<li>Adding firebase authentication to web app for users

<li>Realised some pages don’t like web scrapers, experimenting on request APIs instead
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>25/05/2021
   </td>
   <td>3
   </td>
   <td>3
   </td>
   <td>
<ul>

<li>Error handling for invalid user credentials

<li>Successful retrieval of data from script
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>28/05/2021
   </td>
   <td>4
   </td>
   <td>4
   </td>
   <td>
<ul>

<li>Added display of search results retrieved from firebase

<li>Working on web scraper via API
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Working on Submission for Milestone 1
   </td>
   <td>29/05/2021
   </td>
   <td>4
   </td>
   <td>4
   </td>
   <td>
<ul>

<li>Technical proof of concept video recording

<li>Milestone 1 report do-up
</li>
</ul>
   </td>
  </tr>
</table>



<table>
  <tr>
   <td>Total Hours
   </td>
   <td>Orbitee 1
   </td>
   <td>Orbitee 2
   </td>
  </tr>
  <tr>
   <td>90
   </td>
   <td>45
   </td>
   <td>45
   </td>
  </tr>
</table>


**Milestone 2**


<table>
  <tr>
   <td>Task
   </td>
   <td>Date
   </td>
   <td>Orbitee 1
   </td>
   <td>Orbitee 2
   </td>
   <td>Remarks
   </td>
  </tr>
  <tr>
   <td>Write Milestone 1 Peer Review for other teams
   </td>
   <td>01/06/2021
   </td>
   <td>5
   </td>
   <td>5
   </td>
   <td>
<ul>

<li>Online zoom call to discuss and evaluate other teams

<li>Split workload for each group
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Review and Reflect on Milestone 1 Evaluation from Peer Review
   </td>
   <td>05/06/2021
   </td>
   <td>5
   </td>
   <td>5
   </td>
   <td>
<ul>

<li>Review feedback given by other teams and discussed how to improve webapp
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>07/06/2021
   </td>
   <td>5
   </td>
   <td>5
   </td>
   <td>
<ul>

<li>Incorporated request APIs into search engine for products not in database

<li>Implemented request API for Shopee and Ezbuy successfully
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>08/06/2021
   </td>
   <td>4
   </td>
   <td>4
   </td>
   <td>
<ul>

<li>Refactoring code logic for login, signup and search, beautified login and signup pages

<li>Testing on API scripts using multiple searches to determine relevance of search results

<li>Refined searches based on Bayesian average
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>10/06/2021
   </td>
   <td>6
   </td>
   <td>6
   </td>
   <td>
<ul>

<li>Added history functionality via firestore

<li>Work on web scraping script for Qoo10 and Amazon using selenium 
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>12/06/2021
   </td>
   <td>4
   </td>
   <td>4
   </td>
   <td>
<ul>

<li>Implemented sortable results display and streamlined display logic

<li>Debugging web scraping for Qoo10 and Amazon and implemented pause time within searches to prevent overloading webpage
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>14/06/2021
   </td>
   <td>4
   </td>
   <td>4
   </td>
   <td>
<ul>

<li>Added wishlist UI to results and a ratings column, wishlist WIP

<li>Implemented Qoo10 and Amazon script to retrieve products and refined search results
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>16/06/2021
   </td>
   <td>5
   </td>
   <td>5
   </td>
   <td>
<ul>

<li>Fixing issue where multiple API calls to the same API were made when searching for a product

<li>Worked on deploying web scraping script to Heroku for deployment of backend server
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>18/06/2021
   </td>
   <td>6
   </td>
   <td>6
   </td>
   <td>
<ul>

<li>Wishlist logic implemented, history and wishlist features functional

<li>Working on deploying script to track trending searches by category via selenium chromedriver
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>20/06/2021
   </td>
   <td>5
   </td>
   <td>5
   </td>
   <td>
<ul>

<li>Implemented carousel display for trending products on the Web, cleaning up code and bug fixes before milestone 2

<li>Deploy script for trending products on Heroku and implemented scheduler to schedule daily scraping at UTC 0900H
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Working on Submission for Milestone 2
   </td>
   <td>26/06/2021
   </td>
   <td>6
   </td>
   <td>6
   </td>
   <td>
<ul>

<li>Video recording

<li>Redoing of poster

<li>Milestone 2 report do-up
</li>
</ul>
   </td>
  </tr>
</table>


*All work is done from the safety of our homes


<table>
  <tr>
   <td>Total Hours (as of Milestone 2)
   </td>
   <td>Orbitee 1
   </td>
   <td>Orbitee 2
   </td>
  </tr>
  <tr>
   <td>200
   </td>
   <td>100
   </td>
   <td>100
   </td>
  </tr>
</table>


**Milestone 3**


<table>
  <tr>
   <td>Task
   </td>
   <td>Date
   </td>
   <td>Orbitee 1
   </td>
   <td>Orbitee 2
   </td>
   <td>Remarks
   </td>
  </tr>
  <tr>
   <td>Write Milestone 2 Peer Review for other teams
   </td>
   <td>01/07/2021
   </td>
   <td>8
   </td>
   <td>8
   </td>
   <td>
<ul>

<li>Online zoom call to discuss and evaluate other teams

<li>Split workload for each group

<li>Test app functionality for each group
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Review and Reflect on Milestone 2 Evaluation from Peer Review
   </td>
   <td>06/07/2021
   </td>
   <td>6
   </td>
   <td>6
   </td>
   <td>
<ul>

<li>Review feedback given by other teams and discussed how to improve webapp

<li>Note down areas of improvement
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>07/06/2021
   </td>
   <td>5
   </td>
   <td>5
   </td>
   <td>
<ul>

<li>Working on feature to disable searches while scraper is running

<li>Generated snapshots for testing

<li>Working on extending web scraping scripts to get food deals mainly on websites like Fave and Chope
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>09/07/2021
   </td>
   <td>4
   </td>
   <td>4
   </td>
   <td>
<ul>

<li>Working on feature to disable searches while scraper is running

<li>Successfully wrote scripts to extract deals from both websites, Fave and Chope on localhost
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>11/07/2021
   </td>
   <td>6
   </td>
   <td>6
   </td>
   <td>
<ul>

<li>Working on food page for users to search for food discounts

<li>Attempted to deploy scripts on Heroku, however only web scraping scripts for Chope managed to work

<li>Debugging script for web scraping of Fave
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>13/07/2021
   </td>
   <td>8
   </td>
   <td>8
   </td>
   <td>
<ul>

<li>Updating UI to include food searches for history

<li>Attempt to deploy Fave script on Heroku failed, explored alternatives to deployment

<li>Optimising web scraping for existing scripts using selenium, e.g. Amazon and Qoo10
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>14/07/2021
   </td>
   <td>6
   </td>
   <td>6
   </td>
   <td>
<ul>

<li>Working on delete history function

<li>Writing integration tests using react-testing-library and jest

<li>Successfully shifted web scraping of Amazon from selenium to requests by wrapping User-Agent header upon request

<li>Debugged Qoo10 error of not loading images by simulating mouse-scroll movements which helped load images
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>15/07/2021
   </td>
   <td>7
   </td>
   <td>7
   </td>
   <td>
<ul>

<li>Resolving issues with asynchronous callbacks affecting UI changes on history page when deleting items

<li>Shifted backend searching scripts to AWS Elastic Beanstalk for faster search time
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>18/07/2021
   </td>
   <td>6
   </td>
   <td>6
   </td>
   <td>
<ul>

<li>Fixing existing UI bugs

<li>Writing integration tests using react-testing-library and jest

<li>Configuring Dockerfile for Qoo10 script to allow selenium to run on AWS Elastic Beanstalk

<li>Debugging error prompts on AWS due to selenium
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>20/07/2021
   </td>
   <td>6
   </td>
   <td>6
   </td>
   <td>
<ul>

<li>Fixing existing UI bugs

<li>Writing integration tests using react-testing-library and jest

<li>Working on scripts to allow automated emailing and checking of prices

<li>Refining search results of Amazon scripts to improve relevancy
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Frontend & Backend
   </td>
   <td>22/07/2021
   </td>
   <td>8
   </td>
   <td>8
   </td>
   <td>
<ul>

<li>Writing integration tests

<li>Successfully implemented scheduled email scripts to send out email when wishlist price drops
</li>
</ul>
   </td>
  </tr>
  <tr>
   <td>Working on Submission for Milestone 3
   </td>
   <td>25/07/2021
   </td>
   <td>7
   </td>
   <td>7
   </td>
   <td>
<ul>

<li>Video recording

<li>Milestone 3 report do-up
</li>
</ul>
   </td>
  </tr>
</table>


*All work is done from the safety of our homes


<table>
  <tr>
   <td>Total Hours (as of Milestone 3)
   </td>
   <td>Orbitee 1
   </td>
   <td>Orbitee 2
   </td>
  </tr>
  <tr>
   <td>354
   </td>
   <td>177
   </td>
   <td>177
   </td>
  </tr>
</table>


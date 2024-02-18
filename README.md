## Snow Angels 
While winter is often associated with festivity and love, it also brings about challenges, particularly for senior citizens who are disproportionately affected. Physical obstacles such as slippery ice, cold-related health issues, and limited access to healthcare pose significant threats to elderly wellbring. Additionally, mental health hurdles, including seasonal depression, isolation, and loneliness, further amplify the difficulties faced by seniors. These harsh winter effects also extend to the younger demographic, evident in the rising cases of Seasonal Affective Disorder (SAD).

Introducing SnowAngels, our innovative solution designed to alleviate the winter blues. This app serves as a bridge connecting young adults with senior citizens. By allowing seniors to upload events they need assistance with, SnowAngels not only facilitates the safe completion of tasks but also reduces their isolation levels. Simultaneously, it provides an opportunity for the younger generation to make a positive impact in their community. We know there are many seniors who fear for their health and safety when leaving their homes, and we aim to put an end to their struggles. SnowAngels strives to create a supportive network that transcends generational boundaries, fostering a sense of community and mutual care during the challenging winter months.

## What It Does
Snow Angels uses the powerful MongoDB database to manage the extensive user base, comprising both senior citizens and young adults seeking connections through the app. Tailoring the interface to cater specifically to each demographic, Snow Angels ensures a user-friendly experience.

For senior citizens, we've prioritized accessibility by incorporating large fonts and easily distinguishable text. This design choice facilitates the seamless input of crucial information, including medical conditions, ensuring that users face no challenges in providing vital details. On the volunteer side, vibrant and saturated colors, together with diverse text displays, create an engaging interface that appeals to the intended audience. Volunteers are required to input various qualifications, such as first aid certifications, ensuring their preparedness to assist senior citizens in any situation.

In terms of functionality, senior citizens initiate the process by booking assistance through a form. This form allows them to specify the details of their needs, including the location, date, and additional information about the event. On the volunteer side, a comprehensive list of senior citizens seeking assistance is available, affording volunteers the flexibility to choose when they are available to lend a helping hand. Both users can easily track their scheduled events, fostering transparency and coordination between the two groups. Snow Angels strives to create a streamlined and user-centric platform that facilitates meaningful connections and assistance.


## How We Built It
We built the frontend with HTML/CSS, JavaScript, and Bootstrap, and the backend with Python and Django. To improve user experience, we integrated Google Maps API to convert location text (e.g., "NYC, USA") into coordinates. These coordinates helped us plot paths on the map, prioritizing sidewalks, pedestrian crossings, and safe traffic routes, particularly beneficial for the elderly. Furthermore, our focus was on safety rather than just finding the shortest path, an algorithm often employed by popular navigation apps like Waze.

For real-time traffic data and road geometries, we utilized OpenStreetMap and processed it with MapBox GL. This allowed us to calculate optimal paths that consider traffic, incidents, sidewalks, and pedestrian crossings.

In managing volunteer and senior data, we employed MongoDB Atlas. Volunteer information included certifications like First Aid, while for seniors, we stored age and any existing health conditions.

## Challenges
Some challenges we ran into were decoding polylines into a list of coordinates that could be plotted using MapBoxGL. Additionally, we also had trouble deciding which parameters and data from OpenStreetMap were pertinent, and configuring parameters such that it would always prioritize pedestrian crossings and safety over shortest path. To tackle this, each time we made a request to MapBoxGL for routing information, we adjusted the routing parameters to assign higher weights to pedestrian-friendly features such as sidewalks and designated crossings. This ensured that pedestrian safety was consistently prioritized in our route calculations and path plotting.

## Accomplishments That We Are Proud Of 
We are proud of having been able to quickly learn new tools and integrate them into a fully-functional app within tight time constraints. This experience also taught us a lot about working in a smaller team and the best way to divide and conquer while playing to each others strengths. We are also proud that though we were intimidated by this daunting topic, as solving a major world problem doesn't come easily, we learned how to effectively brainstorm and bounce ideas of the other. Rather than dismissing ideas outright, we learned the power of constructive dialogue and how it contributes to innovative problem-solving.

## What We Learned
This was our first time working with various tools; namely, OpenStreetMap and MongoDB. One of the teammates also learned Bootstrap for responsive web development. Apart from the new databases and frameworks we learned in less than 36 hours, we also learned about optimizing workflow and the importance of organization when working on a project in a team. Another important skill we acquired is knowing when it's time to pivot and tackle a problem from another approach, as a significant aspect of working under time constraints is understanding what lies beyond your limitations.

#What's next for Snow Angels
As mentioned earlier, our main inspiration for Snow Angels was being able to connect people to help them overcome their own difficulties and bring a little light into a gloomy time of year. We can continue bringing this inspiration to life by implementing features such as live chat and adding more filters so that volunteers and senior citizens can accept/request people based on mutual interests and similar lifestyles. On the user experience side of things, we look forward to adding features such as live navigation and weather forecasts built into the app so that Snow Angels provides everything that users need to enjoy their journey together.



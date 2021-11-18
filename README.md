# Inrix-Hack

**Inspiration**
- As we are going back to our normal ways of living post-pandemic, San Francisco has witnessed a 753% rise in vehicle thefts and break-ins from May 2020 to May 2021. We decided that it is time that we solve this compelling issue that many San Franciscans and visitors face daily.

**What it does**
- ParkSafe API is a custom developed API that provides available parking spots with the most safety factor within one mile. By safety factor, it means how likely is your car vulnerable to vehicle related crimes(such as Larceny, arson, etc.). More the safety factor, safer is it to park your car at that particular spot.

- ParkSafe is a web application that implements the Parksafe API which helps vehicle owners stay worry-free by identifying parking spots that are safe from theft and break-ins by mapping out crimes through historical data.

Currently, ParkSafe provides crime-mapped parking data to San Francisco Area.

**How we built it**
- We collected and processed crime statistics (time, location, description, etc.) we used the San Francisco crime data and Arrest information provided by Civic Hub. - We had to do some hacking and front-end processing magic in order to use their data.
- We developed an algorithm to find the safety score for each parking location
- Designed a custom ParkSafe API that provides available parking spots with the least crime rate within one mile.
- Developed a web app that helps vehicle owners stay worry-free by identifying parking spots that are safe from theft and break-ins by mapping out crimes through ParkSafe API.

**Challenges we ran into**
- Due to all of the different policing agencies at play and the lack of publicly available datasets, we initially had trouble finding data to work with
Fortunately, we were able to stumble upon the San Francisco crime data and Arrest information provided by Civic Hub, which sources directly from the SF Police Department. Although this limited the scope of our project to just San Francisco County, the high quality of the data and ease of use (after jumping over some hurdles) made it a no-brainer to use in our hack
- Front and Back end integration
- Learning new frameworks
- Creation of an algorithm to assess the risk of a particular parking spot

**Accomplishments that we're proud of**
- We’re very proud of the quality of our app and our own risk factor scoring algorithm, given how quickly we had to build it out. We were able to build an almost full-featured app with a fleshed-out design that not only has a great UI/UX but also is very useful for the general public, all in less than a day.

**What we learned**
- Outstanding Inrix API capabilities
- Front and Back end communication
- Interactive OpenStreetMaps integration
- Data cleansing, transformation, and representation
- Time Utilization and Team Collaboration

**What's next for Parksafe**
- API can be extended from parking to streets
- Expansion into other cities in California, and beyond
- Normalize data from all different databases, so we can offer this product/service to every user
- Collaboration with San Francisco Police Department

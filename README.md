# project-4-group-14
Project 4: Olympics

Introduction
The Summer 2024 Olympic Games were celebrated with great enthusiasm, featuring popular events like track and field, basketball, soccer, gymnastics, and volleyball that attracted global spectators. While hard work and dedication are crucial for winning medals, our project explores the potential of predictive technology, specifically machine learning, to gain an advantage. Using a comprehensive dataset from both the Summer and Winter Olympics up to 2016, we aim to create insightful visuals with Tableau, develop a predictive model to assess an individual's likelihood of medaling based on physical attributes, and present our findings in an engaging web application.


Data Cleaning & Engineering
We utilized pandas, numpy, scikit-learn, matplotlib, and seaborn for our analysis of 120 years of Olympic data, from Athens 1896 to Rio 2016. Each row represents an athlete and includes their name, sex, age, height, weight, country, medal status, event name, sport, games, year, and city.

During data exploration, we found null values for Age, Height, Weight, and Medal. We filled "No Medal" for null Medal values and used the median by Sex and Sport for the other attributes. To focus on essential features for predicting medal outcomes, we dropped the ID, Name, Team, Games, City, and Event columns, retaining Sex, Age, Height, Weight, NOC, Year, Season, and Sport.

We narrowed our focus to the 2014 and 2016 Olympic Games to improve model efficiency and manage output size. Our dataset was imbalanced, with medal winners comprising only 15%, so we employed SMOTE for oversampling.

We chose the Random Forest Classifier for multi-class predictions (gold, silver, bronze, or no medal) and tested n-estimators from 1 to 50 to optimize accuracy. The best performance was achieved with 48 n-estimators.

After running the model, we generated a classification report and confusion matrix, and calculated feature importance. The analysis revealed that the country name is the most significant predictor of medal outcomes, followed by Sport, Height, Weight, and Age.


Color Design Considerations
Our main color palette for the project was the color of the Olympic rings, as shown below. The Olympic rings signifies the unity of the five continents and the Olympic athletes of various countries coming together. These bright, distinct colors are displayed throughout our web page and Tableau visualizations. We also used gold, silver, and bronze colors to represent the different medal types in certain visualizations. 


Web App Development
Our web application features six pages: a home page, medal predictor, Olympic medal breakdown, basketball analysis, and about us and work cited pages. All pages utilize Lux Bootswatch and custom inline CSS.

The home page introduces the website and project premise. The medal predictor includes an interactive inference maker, allowing users to customize predictions, which are processed by our back-end model to predict podium placements. It also displays feature importance for user-selected categories, making it the most interactive page for engaging with our machine learning model.

The 'Medal Breakdown' page embeds a Tableau dashboard for detailed analysis of Olympic competitiveness by country and sport. Similarly, the 'Olympic Basketball' page features another embedded Tableau dashboard.

The 'About Us' page lists team members with links to their GitHub profiles, while the 'Work Cited' page provides interactive links to all project sources.

The most challenging aspect was integrating our model using the modelHelper, which contained the prediction function from our Machine Learning algorithm. Additionally, learning to process user inputs in the back-end for meaningful results was complex.


Dashboard Design Concepts - Part 1
Our first Tableau dashboard focuses on medal breakdown, featuring a world map that displays each country's medal count. The size and color of the circles indicate the count, with larger circles representing more medals. The Olympic ring color palette is used, where blue signifies lower counts and red indicates higher counts. Users can filter by sport and medal type (gold, silver, bronze, no medal).

The United States leads in total gold, silver, and bronze medals, but specific sports reveal interesting trends, such as Japan and Cuba tying for the most baseball medals (112 each), compared to the U.S. with 88. In cycling, Great Britain and France have high medal counts (582 and 679, respectively), while the U.S. has 523.

The second visualization is a bubble chart showing athlete counts per sport, using the same color palette. Red indicates higher athlete counts, while blue signifies lower counts. This chart can be filtered by sex (M/F) and season (winter/summer). Athletics has the highest athlete count overall, with 11,666 female athletes and 26,598 male athletes, followed by swimming (9,850 females) and gymnastics (17,578 males).

The final visualization is a stacked horizontal bar chart displaying medal counts per country, with sections representing gold, silver, and bronze. Hovering over the bars reveals the athlete count for each medal type. The United States has the highest counts: gold (2,474), silver (1,512), and bronze (1,233).


Dashboard Design Concepts - Part 2
The Olympic Basketball Tableau dashboard analyzes the average physical attributes of Olympic basketball teams and their correlation with medal success. Key attributes include average height, weight, and age, with filters available for the year of the games and team sex.

The first visualization is a bubble chart that shows a team's average height and weight during a tournament. The bubble size represents average height, while the darkness indicates average weight, with larger, darker bubbles reflecting greater height and weight. Hovering over a bubble reveals the country name and medal results.

The second visualization is an interactive table displaying the average age of basketball teams. It highlights the balance between physical ability and basketball IQ, noting that younger players often have high athletic potential but lower game knowledge, while older players may experience physical decline but possess extensive experience. The table allows users to see how age influenced medal outcomes compared to other teams, displaying countries, medal results, and average ages.


Bias/Limitations
The Olympic dataset used did have its fair share of bias and limitations. The first being its size. As many can imagine, using a dataset with data dating back to 1896 to 2016 can make for a very large file. Especially when you can draw down to the individual athlete with their various data points. This in turn made the diversification of the model more limited. There were also a lot more summer sports than winter sports in the data set, which can also skew how the model was trained.


Future Work
In the future, adding features such as an athlete’s years of experience, previous Olympic participation, and injury history could enhance the model's predictability for medal attainment. Incorporating data on coaches' experience would also be valuable, as coaching significantly impacts team success. For outdoor events, including climate data from the host country could provide insights into performance, especially for athletes from regions with different climates. Finally, cross-referencing Olympic data with census data from various countries could reveal how population size influences Olympic success.


Conclusions/Reflection
There were many takeaways that came from the data and the predictive model. Within the predictive model the athlete’s country proved to be the most important feature. Especially when pulling from countries with great Olympic success. In the Tableau visuals we can see that the United States had the highest amount of total medals over the course of all Olympic games and is historically dominant in the sport of basketball. The most athlete-dense sports are track & field, gymnastics, and swimming. Both the model and the visuals are very feature heavy and can make a lot of interesting predictions and showcases that are all cohesively packaged in the web application.

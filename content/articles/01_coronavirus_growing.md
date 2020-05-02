Title: Coronavirus spreads globally
Date: 2020-04-25 11:20
Author: Ryan Benkeser
Tags: coronavirus, visualizations
## The Spread of Coronavirus
In this post we'll see how coronavirus is spreading around the world over time.  The first visualization is a racing bar chart by country.  The second visualization is an international geographical mapping.  Which visualization do you like better? Comment below!

It has been widely reported that some countries do not have access to tests so they will not appear on the visualizations below.  In addition, a recent <a href="https://www.paloaltoonline.com/news/2020/04/17/stanford-study-more-than-48000-santa-clara-county-residents-have-likely-been-infected-by-coronavirus">prevalence study</a> suggests that case counts are vastly under-represented in many San Francisco communities.  Assuming this is true, we can assume that the case counts are significantly higher around the world as well (and that perhaps Coronavirus is less deadly than current knowledge).  Therefore, please take these facts into account as we reflect on CoV-2 spread in the visualizations below.   


<html>
<body>

<h1>Racing Bar Chart (Flourish Studio)</h1>
Creating racing bar charts on Flourish Studio is remarkably easy.  After going through the exercise of creating one, I realize now why they have grown so popular on Youtube.  The main input is a simple CSV upload and the output, after moving a few columns around, is the attached visualization.  Please feel free to explore <a href="https://app.flourish.studio/visualisation/1907728/">the visualization</a> to get ideas for creating your own visualizations on Flourish Studio.   

<iframe width="1120" height="630" src="https://www.youtube.com/embed/lGYYWhRI2HU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


<h1>World Map (Jupyter Notebooks)</h1>
The next video is a geographical mapping of the spread.  I built it in Jupyter Notebooks with the Plotly package.  If you know Python and are willing to read through some Plotly and/or Matplotlib documentation, much of this visualization is also abstracted for you to construct yourself.  Free free to visit my <a href="https://github.com/RyanBenkeser/COVID-19/blob/master/COVID19_World_Growth.ipynb">COVID19 Repo</a> to explore the visualization on your own! 


<iframe src="https://ryanbenkeser.github.io/COVID-19/covid19.html" scrolling="no" frameborder="0"
style="position: relative; top: 0; right: 0; left: 100; bottom: 0; height: 600px; width: 1200px" allowfullscreen></iframe>

</body>
</html>

##

Good luck and hopefully you can start rending your own data visualizations.  

Signing off on Sunday, April 25th 2020.

-- Ryan Benkeser








